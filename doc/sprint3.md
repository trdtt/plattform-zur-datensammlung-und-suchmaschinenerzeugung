# Sprint 3 - Abgabe

## 1. Name des Projektes

QEnable

## 2. Aktive Teammitglieder 

   - [Abdullah Al-hoty](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/users/aalhoty/activity) [Frontend, verbinden mit Backend ]
   - [Abdul Rahman Alkedda](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/users/aalkedda/activity) [Backend, Frontend, Docker]
   - [David Deutschmann](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/users/users/ddeutsch/activity)
   - [Johannes Kindler](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/users/jkindler/activity) [CI/CD Pipeline, Docker, production deployment server support]
   - [Tony Lenz](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/users/tlenz1/activity)[Ausarbeitung Projektposter, Ausarbeitung Projektpräsentation]
   - [Lukas Marche](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/users/lmarche/activity)[Ausarbeitung Projektposter, Ausarbeitung Projektpräsentation, Vortrag]
   - [Moritz Meister](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/users/mmeister/activity)[Ausarbeitung Projektposter, Ausarbeitung Projektpräsentation, Domain Crawler, Reviewing]
   - [Finn Mergenthal](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/users/users/fmergent/activity) [Restrukturierung des Clients, Code reviews]
   - [Lukas Ponicke](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/users/lponicke/activity) [Scrum master, Ausarbeitung und Vortragen der Praesentation, Protokollieren der Meetings, Crawler, Reviewing]
   - [Laurin Remane](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/users/users/mremane/activity) [Austausch Client]
   - [Philipp Semlinger](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/users/users/psemling/activity) [Scrum Master, Organisation, Kommunikation Projektsponsor]

## 3.1 Link zum Piloten & "Tutorial"

[QEnable-Pilot](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/pdus/plattform-zur-datensammlung-und-suchmaschinenerzeugung/-/tree/developement)

[Tutorial](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/pdus/plattform-zur-datensammlung-und-suchmaschinenerzeugung/-/blob/developement/README.md)

## 3.2 Docker

[Dockerfile](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/pdus/plattform-zur-datensammlung-und-suchmaschinenerzeugung/-/blob/developement/Dockerfile)

Nutzung: siehe [README](README.md)

## 3.3 Gitlab Action

[.gitlab-ci.yml](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/pdus/plattform-zur-datensammlung-und-suchmaschinenerzeugung/-/blob/developement/.gitlab-ci.yml)

## 4.1 Problemdefinition & Produktvison

Problemdefinition:
> Es soll eine einfache Möglichkeit geschaffen werden, RDA-Daten aus schema.org-Webseiten zu ertrahieren, zu mappen und auf QAnswer hochgeladen werden

Produktvision: 
> Die Anwendung soll ein Web-Interface darstellen, in dem es zunächst möglich ist, sich auf QAnswer anzumelden. Der Erfolg soll mit einer Meldung bestätigt werden. Nun soll in einem Textfeld eine URL eingegeben werden und in einem zweiten Textfeld ein Name. Nun soll es zum einen einen Crawl-Button geben, welcher aus der URL die RDA-Daten entsprechend der schema.org-Darstellung extrahiert und als nt-File zum Download bereitstellt. Der Download soll erst mit einem erneuten Klick auf den entsprechenden Button starten. Gleichzeitig sollen die gecrawlten Daten automtisch auf QAnswer hochgeladen werden und dort mit dem Namen aus dem zweiten Textfeld benannt werden.
Nun können die Daten auf qanswer.fr entsprechend verwaltet und durchsucht werden.

  
## 4.2 Design-Thinking-Prototyp

Webapplikation - GUI

![image](https://www.imn.htwk-leipzig.de/~jkindler/PDuS/img-2.png)


## 4.3 Erfüllte funktionale und nicht funktionale Anforderungen

- Interface mit Anmeldeprozess
- Reaktion bei Anmeldung (Erfolgs- oder Misserfolgsmeldung)
- Möglichkeit URLs und Bezeichnungen in 2 Textfeldern einzugeben
- Crawl-Button, der die URL nach RDA-Daten durchsucht
- Reaktion bei Crawling (Erfolgs- oder Misserfolgsmeldung)
- Download-Button
- Korrektes Mapping der Daten entsprechend schema.org-Syntax
- Upload an QAnswer

## 5. Beiträge der Teammitglieder


Viele Tätigkeiten wie beispielsweise 
- Führen von Protokollen
- interne und externe Kommunikation
- Erstellen von Issues
- Code Reviewing
- Leiten der Meetings
- Organisation des Gits
- Erstellen der formalen Anforderungen 
sind Tätigkeiten, die nicht nicht in Commits und LoC messbar sind. 
Wir haben uns Mühe gegeben, unsere Arbeit, wo immer sinnvoll, über GitLab zu dokumentieren und bitten darum, die einzelnen [Activity-Feeds](#2. Aktive Teammitglieder) zur Bewertung der Individualleistung heranzuziehen.

## 6. Intendierte Softwarearchitektur(UML-Diagramm)

![UML Diagramm](doc/assets/sprint3/UML_Sprint_3.jpg)
