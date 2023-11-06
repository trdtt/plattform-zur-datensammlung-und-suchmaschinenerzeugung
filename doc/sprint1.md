# Plattform zur Datensammlung und Suchmaschinenerzeugung

## Gitlab

[Group - PDuS](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/pdus)

[Repo - Main](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/pdus/plattform-zur-datensammlung-und-suchmaschinenerzeugung)

## Members

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

## Design-Thinking-Prozess

### Schritt 1: Verstehen

- Was soll neu entwickelt werden?
    - eine Anwendung welches einer Webseite die Anbindung an QAnswer ermöglicht, um die darin enthaltenen Informationen bereitzustellen und über das QA System erreichbar zu machen
- gemeinsames Verständnis in Text ausdrücken
    - bereits existierende Toolchain zum (www -> rdf) einheitlich, dauerhaft und nutzer*innen-freundlich konfigurieren können
- Für wen soll entwickelt werden?
    - User Typ 1 (Edeka): Business Besitzer, der seine Daten auf QA zur Verfügung stellen/verarbeiten möchte
    - User Typ 2 (Theresa): Möchte Informationen aus spezifischen selbst ausgewählten Quellen durchsuchen können (automatisierte Datenbeschaffung)
    - User Typ 3 (Sheldon): Möchte Rdf-Statistiken seiner Webseite bekommen
- Welche Rahmenbedingungen berücksichtigen?
    - robots.txt berücksichtigen
    - Zeitplan und Budget einhalten
- Endzustand der Lösung?
    - User übergibt API Website per URL. Diese wird live gecrawlt an QAnswer übergeben, sodass der User Typ 1 direkt seine Daten zur Verfügung gestellt hat und User Typ 2 direkt seine Anfragen geben kann.

### Schritt 2: Beobachten

- Wie gehen Nutzer aktuell vor (in realer Umgebung)?
    - manuelles hochladen reiner RDF Dateien und dann Auswertung via QAnswe
    - Prozess soll automatisiert werdenr
    - keine Möglichkeit automatisierter Datenbeschaffung in der Form (Typ 2)
- Welche Verbesserungen werden gewünscht?
    - Nutzeroberfläche soll geschaffen werden
    - Eingabe der URL
    - beständiges aktualisieren/updates des Datensatzes
    - persistente Konfiguration des Crawlingprozesses
- <a name="userReq">Welche Wünsche haben die Nutzer?</a>
    - Nicht-funktionale Anforderungen:
        - gute Handhabbarkeit
        - ansprechendes Design
        - URL ähnlich zu QAnswer oder an QAnswer angegliedert
        - Ausführungsqualität\
            Zuverlässiges Arbeiten, Rückmeldungen/ Fehlermeldungen
        - Leistung und Effizienz\
            so schnell wie möglich, Redundanzvermeidung/Update-Verhalten, Verhindern, dass dieselben Seiten mehrmals gleichzeitig gecrawlt werden (Update-Cyclus)
        - Aussehen und Handhabung\
            GUI, UX, Funktionalität vs Intuitivität, technisch versierter User
        - Sicherheitsanforderungen\
            Abgeriegelte Accounts\
        - Korrektheit\
            Prüfen auf Korrektheit, Syntax-Fehler, RDF-Analyse
        Weiterentwicklungsqualität\
        - Wartbarkeit\
        - Portier und Übertragbarkeit\
        - Flexibilität (Einbringen von Standarts)\
            Modularisierung, Orientierung an 'Pipeline'
            Docker
            Sparql
            RDF
        - Skalierbarkeit (später diskussionsrelevent)\
    - Funktionale Anforderungen
        - Webseite auf RDF-Daten überprüfen
        - Webseite auf RDF Daten Crawlen
        - RDF Daten an QAnswer übergeben
        - Nutzer erfolgreiche QA Anfrage ermöglichen
        - Nutzer RDF Daten bereitstellen
        - ggf. Updaten/Synchronisieren von RDF Daten aus anderen Quellen (Triplestores)
- Was würden sich die Nutzer (nicht die Devs!) als einen Idealzustand vorstellen?
    - Öffnen der Applikation, Einfügen des Links der Webseite, Bestätigen, (kurz!  Warten,) (Anfragen eingeben, Antworten erhalten, Fertig) ~> siehe nächster Punkt
    - danach erfolgreiches Nutzen von QAnswer auf den neu gewonnenen Daten
    - Rückgabe von Statistiken (Menge der verwertbaren Daten, Häufigkeit der verwertbaren Daten in Gesamtdatensatz)
    - (Möglichkeit der direkten Nutzung einer QAnswer Suchzeile und Rückgabe der Antworten  innerhalb der Webseite)

### Schritt 3: Synthese

#### User Stories
- Jeder Nutzer ist grundsätzlich auf Korrektheit und Gesamtheit der gecrawlten Daten, möglichst schnelle und effiziente Verarbeitung und möglichst einfache Handhabung angewiesen.

- Ein zuständiger Mitarbeiter von Edeka würde gern seine gesamte Webpräsenz übersichtlich darstellbar aufbereiten, um Sichtbarkeit bei Suchmaschinen und ihm statistische Auswertungen zu ermöglichen.

- Eine recherchierende Schülerin möchte schnell und ohne technisches Verständnis oder eigenen Server Daten von Wikipedia aufbereitet bekommen, um Zeit zu sparen.

- Ein Mitarbeiter eines Bürgerbüros will Dokumente, Formulare, Ansprechpartnerinnen natürlichsprachlich durch eigene QAnswer-Instanz durchsuchbar machen. Dafür konfiguriert sie den Crawler auf Bundes-, Landes- und kommunalen Websites auf strukturierte Daten. Dazu konfiguriert sie zusätzlich Update-Prozess aus eigenem Triplestore auf QAnswer-Instanz.

- Ein Wirtschaftsanalyst möchte präzise Daten von verschiedenen Webseiten auf einmal zusammentragen, um sie anhand von ordinalen Kategorien zu analysieren.

### Schritt 4: Lösungsideen finden

- bereits exisitierendes Programm der Uni Mannheim zum Crawlen für QA
- siehe Schritt 2 unter ["Welche Wünsche haben die Nutzer?"](#userReq)

### Schritt 5 : Prototyping

Technische Möglichkeiten bzw. bereits vorhandene Technologien:
- RDFa 1.1 Distiller (alternativ JCrawler)
- Frameworks für Website (react)
- Komponenten als Docker Images an QAnswer
- Datenbank (u.A. zur Erfassung von Statistiken)
- aufbereitete (alterantive) Lösungsideen (für Personas), welche die besonderen Lösungscharakteristika betonen
- Mockup-GUI: via mokup oder wireframe


#### Prototyp 1: Pipelines

- Unser Produkt dient der Migration und Synchronisation strukturierter Daten aus unterschiedlichen Quellen in Datensenken.

- Dazu wird dem/der Nutzer\*in ermöglicht Pipelines zu definieren. Eine Pipeline besteht aus einer Datenquelle (Website mit strukturierten Informationen, Tripplestore (SPARQL-Query), RDF-Datei), einer Datensenke (Tripplestore, QAnswer-Instanz, RDF-Datei) und ggf. Verarbeitungsschritten (z. B. Mapping von RDF-Vokabular) dazwischen. Jede Komponente der Pipeline und jede Pipeline an sich ist unabhängig voneinander konfigurierbar (Baukastensystem). 

- Einmal erstellt, können die Pipelines auf Knopfdruck oder zyklisch die Datenbasis der Quelle migrieren bzw. die bestehenden Daten der Senke updaten.

- Die Konfiguration des Systems könnte Dateibasiert und/oder eine Website erfolgen.

### Schritt 6: Testen

- Beobachtungen und Fragen von Nutzer erfassen
- Feedback/Bewertung sammeln
- Testfälle definieren, durchführen und auswerten
- Ableitung einer Bewertung der Lösungsideen (beste Lösung finden!)

## Problemdefinition

Unser Kunde hat zu wenig eingebettete Webseiten aus denen QA Daten bezieht, keine Automatisierter Ablauf zur Indexierung.

## Design-Thinking-Prototyp

Was muss der nutzer können?

- Crawlvorgang starten (Linkeingabe)
- Crawl und Mapping Parameter anpassen
- RDF-Daten anzeigen und analysieren

![image](assets/sprint1/img-1.png)

Webapplikation - GUI

![image](assets/sprint1/img-2.png)


Plug-In (optional)

![image](assets/sprint1/img-3.png)

TODO : Download für extrahierte RDF´s einbinden

## User Stories
- Jeder Nutzer ist grundsätzlich auf Korrektheit und Gesamtheit der gecrawlten Daten, möglichst schnelle und effiziente Verarbeitung und möglichst einfache Handhabung angewiesen.

- Ein zuständiger Mitarbeiter von Edeka würde gern seine gesamte Webpräsenz übersichtlich darstellbar aufbereiten, um Sichtbarkeit bei Suchmaschinen und ihm statistische Auswertungen zu ermöglichen.

- Eine recherchierende Schülerin möchte schnell und ohne technisches Verständnis oder eigenen Server Daten von Wikipedia aufbereitet bekommen, um Zeit zu sparen.

- Ein Mitarbeiter eines Bürgerbüros will Dokumente, Formulare, Ansprechpartnerinnen natürlichsprachlich durch eigene QAnswer-Instanz durchsuchbar machen. Dafür konfiguriert sie den Crawler auf Bundes-, Landes- und kommunalen Websites auf strukturierte Daten. Dazu konfiguriert sie zusätzlich Update-Prozess aus eigenem Triplestore auf QAnswer-Instanz.

- Ein Wirtschaftsanalyst möchte präzise Daten von verschiedenen Webseiten auf einmal zusammentragen, um sie anhand von ordinalen Kategorien zu analysieren.

## Produktvision

Es soll eine Anwendung für Webseitenbetreiber und Privatpersonen, die RDF Daten in Webseiten bereitstellen oder verarbeiten wollen, erstellt werden. In dieser Anwendung soll durch Eingabe einer URL diese Webseite nach RDF Daten gecrawlt, validiert, zwischengespeichert, analysiert und an QAnswer.eu übergeben werden.
Darauf folgend ist eine Suchanfrage auf den Daten über QAnswer möglich und die heraushezogenen RDF-, sowie die Analysedaten stehen dem Nutzer zur Verfügung.

## Meetings 

- [Protocols](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/pdus/plattform-zur-datensammlung-und-suchmaschinenerzeugung/-/wikis/Board-Meetings)
