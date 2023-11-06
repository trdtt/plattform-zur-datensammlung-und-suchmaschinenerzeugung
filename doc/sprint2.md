# Sprint 2 - Abgabe

## 1. Name des Projektes

QEnable

## 2. Aktive Teammitglieder 

- [Johannes Kindler](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/jkindler)
- [Philipp Semlinger](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/psemling)
- [Finn Mergenthal](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/fmergent)
- [David Deutschmann](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/ddeutsch)
- [Laurin Remane](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/mremane)
- [Abdul Rahman Alkedda](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/aalkedda)
- [Abdullah Al-hoty](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/aalhoty)
- [Moritz Meister](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/mmeister)
- [Lukas Ponicke](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/lponicke)
- [Tony Lenz](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/tlenz1)
- [Lukas Marche](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/lmarche)

## 3.1 Link zum Piloten & "Tutorial"

[QEnable-Pilot](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/pdus/plattform-zur-datensammlung-und-suchmaschinenerzeugung/-/tree/developement)

[Tutorial](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/pdus/plattform-zur-datensammlung-und-suchmaschinenerzeugung/-/blob/developement/README.md)

## 3.2 Docker

[Dockerfile](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/pdus/plattform-zur-datensammlung-und-suchmaschinenerzeugung/-/blob/developement/Dockerfile)

### 3.3.1 Quick-Start-Guide

    sudo docker build -t flask-image .
    sudo docker run --rm -p 5000:5000 flask-image

Weiter geht´s [hier](#ip).

### 3.3.2 Ausführliches Tutorial

Überprüfe, ob die Gruppe "docker" bereits existiert.

    groups 
    
Sollte die Gruppe nicht exitieren, muss diese erstellt werden.

    sudo groupadd docker


Der Nutzer muss der Gruppe "docker" hinzugefügt werden.

    usermod -aG docker $USER

Dockerstart:

    systemctl start docker

Es muss nun zu dem Verzeichnis des Dockerfiles navigiert und das Docker-Image gebaut werden.

    docker build -t <docker image name> .

Dabei muss `<docker image name>` mit einem Namen für das Docker-Image ersetzt werden. 

Der nächste Schritt ist die Ausführung des Docker-Images.

    docker run --rm -p 5000:5000 <docker image name>


`--rm`: Der Docker-Container wird nach dem Verlassen gelöscht, um Platz zu sparen.

`-p`: Gibt die Spezifikation des Ports an.

<a name="ip" ></a>Die Webseite ist nun unter `http://172.17.0.2:5000` erreichbar.


Optional, wenn man einen Container bauen möchte: 

    docker container create flask-image
    docker container list -a 
    docker start <docker container id>
    docker exec -it <docker container id> /bin/bash

Dabei muss `<docker container id>` mit der ID des Docker-Containers ersetzt werden. 

## 3.3 Gitlab Action

[.gitlab-ci.yml](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/pdus/plattform-zur-datensammlung-und-suchmaschinenerzeugung/-/blob/developement/.gitlab-ci.yml)

## 4.1 Problemdefinition & Produktvison

Problemdefinition:

> Unser Kunde hat zu wenig eingebettete Webseiten aus denen QA Daten bezieht, keine Automatisierter Ablauf zur Indexierung.

Produktvision: 
> Es soll eine Anwendung für Webseitenbetreiber und Privatpersonen, die RDF Daten in Webseiten bereitstellen oder verarbeiten wollen, erstellt werden. In dieser Anwendung soll durch Eingabe einer URL diese Webseite nach RDF Daten gecrawlt, validiert, zwischengespeichert, analysiert und an QAnswer.eu übergeben werden.
Darauf folgend ist eine Suchanfrage auf den Daten über QAnswer möglich und die heraushezogenen RDF-, sowie die Analysedaten stehen dem Nutzer zur Verfügung.

## 4.2 Design-Thinking-Prototyp

Webapplikation - GUI

![image](assets/sprint1/img-2.png)


## 4.3 Erfüllte funktionale und nicht funktionale Anforderungen

> Als IT-Mitarbeiter eines Unternehmens kann ich RDF-Daten aus beliebigen Websiten crawlen und diese an eine konkrete QAnswer instanz hochladen, damit ich auf diesen Daten natürlichsprachliche Fragen auf QAnswer stellen kann. (Die RDF-Daten der gecrawlten Website müssen das Alphabet von Schema.org verwenden, damit Fragen gestellt werden können)

## 5. Beiträge der Teammitglieder

Alle haben sich gleichermaßen an den Projektmeetings beteiligt.
