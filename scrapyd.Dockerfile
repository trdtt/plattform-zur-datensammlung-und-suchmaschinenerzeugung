FROM python as builder

RUN pip install scrapyd-client

WORKDIR /build

COPY urlcrawler .

RUN scrapyd-deploy --build-egg=urlcrawler.egg

FROM python:alpine as scrapyd

RUN apk add --update --no-cache --virtual .build-deps \
      gcc \
      libffi-dev \
      libressl-dev \
      libxml2 \
      libxml2-dev \
      libxslt-dev \
      musl-dev \
    && pip install --no-cache-dir \
      scrapyd \
      extruct requests rdflib w3lib \
    && apk del .build-deps \
    && apk add \
      libressl \
      libxslt

VOLUME /etc/scrapyd/ /var/lib/scrapyd/

COPY urlcrawler/scrapyd.conf /etc/scrapyd/

RUN mkdir -p /var/lib/scrapyd/eggs/urlcrawler
COPY --from=builder /build/urlcrawler.egg /var/lib/scrapyd/eggs/urlcrawler/urlcrawler.egg

ENTRYPOINT ["scrapyd", "--pidfile="]