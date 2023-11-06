# Prepare static file for flask-server.
# This build might take a while
FROM node:latest AS react-builder
WORKDIR /app
COPY frontend/package.json /app/
RUN yarn install
COPY frontend /app/
RUN yarn build

# Builds the QAnswer client python module
FROM openapitools/openapi-generator-cli:v6.1.0 AS client-builder
RUN java -jar /opt/openapi-generator/modules/openapi-generator-cli/target/openapi-generator-cli.jar generate \
  -i https://app.qanswer.ai/v2/api-docs \
  -g python \
  --package-name qaclient \
  -o /local/qaclient \
  --skip-validate-spec

FROM python:3.10.4 AS app

# Add user to run the server
RUN useradd -ms /bin/bash qauser
USER qauser
WORKDIR /home/qauser
ENV PATH="/home/qauser/.local/bin:${PATH}"

# Installs all python requirements, including the qaclient package built by the client-builder stage
COPY --chown=qauser:qauser . .
COPY --from=client-builder --chown=qauser:qauser /local/qaclient ./qaclient/
RUN pip install --user .

# Copy static files from react-builder into the target image
COPY --from=react-builder --chown=qauser:qauser /app/build ./src/qenable/build

RUN pip install --user .

ENV FLASK_ENV=prod

# Copy source files and start flask server
CMD ["flask", "--app", "qenable","run", "--host", "0.0.0.0", "--port", "80"]

EXPOSE 80
