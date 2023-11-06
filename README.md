# QEnable

## Usage

Das Projekt lässt sich am einfachsten über Docker Compose ausführen: 

```shell
docker-compose up -d
```

QEnable ist nun unter [http://localhost:8080](http://localhost:8080) erreichbar.


### Bedienung der Webseite

![image](doc/assets/sprint2/step0.png)

> Nachdem Sie sich auf unserer Webseite befinden, müssen Sie sich rechts in ihrer Instanz von QAnswer einloggen (Nutzername Passwort)
> Falls Account nicht vorhanden, schlägt der Login fehl.

![image](doc/assets/sprint2/step1.png)

![image](doc/assets/sprint2/step2.png)

> Nach dem erfolgreichen Login, verschwindet das „login-Panel“ .
> Nun können Sie einen Link im Rechten Fenster „Quelle“ eingeben und mit einem Namen für das Dataset in QAnswer versehen.
> Durch anschließendes Betätigen des „start process!“ Buttons wird der Crawl Vorgang gestartet und die gecrawlten rdf files direkt an die eingeloggte Instanz von QAnswer übergeben.

![image](doc/assets/sprint2/step3.png)

> QA-Instanz aufrufbar unter https://app.qanswer.ai/

![image](doc/assets/sprint2/step4.png)
![image](doc/assets/sprint2/step5.png)
![image](doc/assets/sprint2/step6.png)

> Nun können (abhängig von der Strukturierung des RDF) in der QA Instanz fragen auf die Webseiten beantwortet werden.


## Entwicklungssetup

Diese Anleitung sollte für Linux und MacOS funktionieren. Getestet wurde sie für Debian 11.

Für Windows sind leichte Anpassungen insb. bei Dateipfaden notwendig, grundsätzlich können aber die gleichen Tools genutzt werden.

### Voraussetzungen

- Python >= 3.8.1
- Pip
- Docker

### qaclient

Um das Projekt ohne Docker lokal auszuführen, musst du dir zunächst das Python-Modul _QAnswer Client_ aus der Swagger-Dokumentation der QAnswer API generieren. 
Das funktioniert am leichtesten über den folgenden Docker-Befehl: 

```shell
docker run --user "$(id -u):$(id -g)" --rm -v "${PWD}:/local" openapitools/openapi-generator-cli:v6.1.0 generate \
  -i https://app.qanswer.ai/v2/api-docs \
  -g python \
  --package-name qaclient \
  -o /local/qaclient \
  --skip-validate-spec
```

### poetry

Poetry ist eine Python Tool, das u. A. das Verpacken von Projekten und das Händeln von virtuellen Umgebungen vereinfacht. 
Poetry greift dafür auf pip zurück. 

Zuerst die Installation von poetry: `pip install poetry`

Nun kannst du poetry nutzen um das Python-Projekt lokal zu installieren: `poetry install`

Falls du dich zum Zeitpunkt der Installation **nicht** in einer virtuellen Umgebung (venv) befindest erstellt poetry für dich eine neue und installiert das Projekt dort. 
Du kannst in diesem Fall über `poetry run` bzw. `poetry shell` auf diese Umgebung zugreifen.
Falls du poetry bereits in einer venv ausführst, nutzt poetry diese und alle folgenden Kommandos können ohne `poetry run` ausgeführt werden. 

Das Starten des Servers erfolgt über 

```shell
export FLASK_ENV=dev ; poetry run flask --app qenable --debug run
```

QEnable sollte nun unter [http://localhost:5000](http://localhost:5000) erreichbar sein. 

Linting kann ausgeführt werden über 
`poetry run pylint src` 
bzw. 
`poetry run flake8`

Neue Python-Abhängigkeiten können über `poetry add <Paketname>` hinzugefügt werden.
Zum updaten der bestehend Abhängigkeiten nutze `poetry update`.

### React

React ist etwas anderes als was wir benutzt haben. Dafür musste man entweder `yarn` oder `npm` nutzen, also einen Package-Manager.

`yarn` installiert die Packages parallel und ist dafür schneller als  `npm` aber die beiden machen genauso die selbe Aufgabe.

Falls man eine neue Library braucht, kann man die mit `yarn add <Library-name>` hinzufügen, dafür wird `package.json` und `package-lock.json` geändert (es ist nicht schlimm).

Zuerst soll man ins frontend-Verzeichnis gehen und `yarn install` eingeben. Das kann ein paar Minuten dauern bis alles heruntergeladen wird oder einfach gesagt bis `node_modules` heruntergeladen wird.

node_modules hat viele Packages und wir brauchen nicht alle aber für die Entwicklung ist das ganz praktisch, damit man nicht jedes mal irgendwas installieren muss, da dieser Ordner fast alles, was der Entwickler braucht, beeinhaltet.

Es soll bei euch im frontend-Verzeichnis nichts geändert werden, falls in der Datei `package-lock.json` nach dem `yarn install` was neues oder eine Änderung kommt, bitte diese Änderung löschen und den alten Zustand der Datei behalten.

`yarn start` im frontend-Verzeichnis eingeben und kurz warten bis das ganze gebildet wird (der frontend-Server), danach wird ein Fenster im Browser automatisch geöffnet und zack ist das frontend da zu sehen.

Nun möchten wir von unserer Arbeit das Produkt bilden, da wir unsere Arbeit in der Development-Umgebung gebaut haben. Das kann man einfach mit `yarn build` im frontend-Verzeichnis machen und wieder kurz warten bis das fertig wird. Den build-Ordner kann man dann in `src/qenable` schieben und `flask` kümmert sich um den Rest.
