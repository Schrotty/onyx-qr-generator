# Onyx - QR-Generator
Onyx ist ein QR-Code Generator bestehend aus einer REST-Schnittstelle und einem dazugehörigen Web-Frontend. Die REST-Komponente ist dabei eigenständig und kann auch ohne das mitgeliferte Frontend betrieben werden. Eine Übersicht über Architektur und Funktionsumfang der jeweiligen Komponent findet sich in Backend und Frontend.

## Kubernetes
Die folgenden Diagramme bieten eine schnelle Übersicht über den Aufbau der Anwendung in einem Kubernetes Cluster. Kommunikation zwischen einzelnen Services, wie Backend -> Redis oder Frontend -> Backend, sind hier nicht abgebildet, sondern lediglich welche Kubernetes Komponenten in Beziehung zueinander stehen.

Das Projekt wurde in zwei separate Services aufgetrennt um Backend und Frontend sauber von einander zu trennen. 

![Kubernetes Übersicht](/docs/kube-overview.png)

## Onyx-Backend
Übersicht über die Architektur, Konfiguration und den Einsatz des Onyx Backends.

### Funktionsumfang
Neben der Möglichkeit reguläre/ statische QR-Codes zu erzeugen gibt es noch persistente QR-Codes. Dabei wird der eigentliche Inhalt des Codes in eine Redis-Datenbank geschrieben. Als Key dient der gehashte Inhalt. Die REST-Schnittstelle liefert statt des Inhaltes nun einen Link mit dem der gespeicherte Inhalt abgerufen werden kann.

Grundsätzlich besteht die Möglichkeit jede Art von Information/ Datei zu hinterlegen, solange diese als Zeichenkette vorhanden ist. Als Beispiel seien Bilder genannt die als base64 String vorliegen.

#### Konkrete Möglichkeiten
* Codieren von Zeichenketten in statische QR-Codes.
* Codieren von Zeichenketten in dynamische QR-Codes.
  * Aktuell werden nur Fließtext und base64 enkodierte PNGs und JPGs unterstüzt.
* Abrufen, verändern und löschen von dynamischen QR-Codes.

### Architektur
Das Onyx Backend setzt sich aus den folgenden Komponenten zusammen:

**flask**

Ein minimalistisches Framework für Web-Services. Als Basis für das Backend vorgegeben.

**flask-RESTful**

Eine Erweiterung für *flask*, für die Entwicklung von leichtgewichtigen RESTful Services. Ermöglicht mit *flak-apispec* und *marshmallow* den komfortablen und schnellen Entwurf von REST-Schnittstellen inkl. Dokumentation.

**flask-apispec**

Eine Erweiterung für *flask* die neben automatischem Request-Parsing auch die Dokumentation mit *apispec* ermöglicht. Das Request-Parsing vereinfacht die Entwicklung dahingehend dass kein eigener Code für das Abrufen und Validieren von Parametern geschrieben werden muss. Komplexe Requests können so in wenigen Zeilen Code abgebildet werden.

**marshmallow**

Wird für die Definition von Request und Response Schemata verwendet mittels derer Requests von *flask-apispec* geparst und validiert werden.

**qrcode**

Wird für das Generieren von QR-Codes verwendet. Bietet im Vergleich zu anderen Bibliotheken wie etwa *Segno* mehr Freiheit im stylen von Codes. Ist dafür von *Pillow* abhängig, einer schwergewichtigen Bildverarbeitungs Bibliothek.

### Konfiguration
Die Konfiguration des Backends erfolgt über verschiedene Umgebungsvariablen, die während des Deployments gesetzt werden. Adresse und Port des Redis-Dienstes werden beim Einsatz in Kubernetes mittels Umgebungsvariablen ausgelesen. Entsprechend muss Redis noch vor dem Backend gestartet werden.

**ONYX_HOSTNAME**=https://onyx.local

Der Hostname unter dem der Service verfügbar ist. Wird für persistente QR-Codes benötigt um den den Link zum Abrufen zu erzeugen.

**ONYX_LOG_LEVEL**=[INFO, WARNING, DEBUG, CRITICAL, FATAL, ERROR]

Setzt dass Log-Level für die Log-Ausgabe fest. Standardmäßig ist WARNING eingestellt.

**ONYX_ENABLE_REDIS**=[true, false]

Bestimmt ob persistente QR-Codes erstellt werden können.

**ONYX_REDIS_HOST**=127.0.0.1

Adresse der zu verwendenden Redis-Datenbank.

**ONYX_REDIS_PORT**=6379

Port der zu verwendeten Redis-Datenbank.

### API-Endpoints

Die vollständige Dokumentation der REST-Schnittstelle ist unter https://onyx.local/api/spec/ui/ einzusehen.

## Onyx-Frontend
Übersicht über die Architektur, Konfiguration und den Einsatz des Onyx Frontends. Das Design des Frontends ist neben dem Einsatz auf großen Bildschirmen auch für den Gebrauch auf Mobilgeräten geeignet.

### Funktionsumfang
Der Funktionsumfang des Frontends gleicht in großen Teilen dem des Backends bzw. nutzt eben dessen Möglichkeiten. Konkret bedeutet dies:
* Erzeugen von statischen QR-Codes
  * Verlinken auf Webseiten
  * E-Mail Vorlagen erstellen
  * Zugangsdaten für WIFIs bereitstellen
  * Auf einen Twitter Account verlinken
* Erzeugen von dynamischen QR-Codes
  * Fließtexte werden als dynamischer QR-Code angelegt um den Code selbst klein zu halten, aber trotzdem größere Mengen an Text hinterlegen zu können.
  * Eine Möglichkeit für den Upload von Bildern gibt es nicht.
* Festlegen von einigen Design Parametern
  * Die farbliche Gestaltung des QR-Codes
  * Das generelle Aussehen des QR-Codes
  * Rand und Komplexität des QR-Codes.

### Architektur
Umgesetzt wurde das Frontend mittels *Vue.js*, einem JavaScript Framework und *Tailwind.css* einem CSS-Framework. Beim Build-Vorgang wird daraus eine statische Seite generiert welche mittels *nginx* ausgelifert wird. *Node.js* wird entsprechend nur für die Entwicklung benötigt.

### Konfiguration
Die Konfiguration des Frontends beschränkt sich auf die Anbindung an die REST-Schnittstelle des Backends und erfolgt über die *config/onyx.json* in der die Endpoints für das Generieren von statischen und dynamischen QR-Codes hinterlegt werden. Für den flexiblen Einsatz in Kubernetes wird auf eine *ConfigMap* zurückgegriffen. Diese wird am Ort der *onyx.json* eingebunden und ermöglicht es so auch zur Laufzeit noch die Endpoints zu ändern ohne den Service neu bauen oder deployen zu müssen.

## Impression
![Kubernetes Übersicht](/docs/onyx.jpeg)

## License
MIT