# Waerungsumrechner_ILA3_0110

## 1. Informieren

### 1.1 Anforderungen

| An-№ | Typ           | Beschreibung                                                                      |
| ---- | ------------- | ---------------------------------------------------------------------------------- |
| 1    | Funktional    | Die Applikation soll verschiedene Währungen umrechnen können.                      |
| 2    | Funktional    | Die Applikation soll Eingaben von Währung nehmen können.                          |
| 3    | Funktional    | Die Applikation soll die gewollte Ausgabe geben.                                  |
| 4    | Funktional    | Die Applikation soll Eingaben von der gewollten Menge der Währung nehmen können.  |
| 5    | Funktional    | Die Applikation soll aktuelle Wechselkurse von einer externen API abrufen.         |
| 6    | Funktional    | Die Applikation soll eine Benutzeroberfläche bieten, um Währungen auszuwählen.     |
| 7    | Funktional    | Die Applikation soll mehrere Umrechnungen in einer Sitzung durchführen können.     |
| 8    | Funktional    | Die Applikation soll eine Fehlermeldung anzeigen, wenn ungültige Eingaben gemacht werden. |
| 9    | Qualitativ    | Die Applikation soll eine hohe Verfügbarkeit haben, mit minimalen Ausfallzeiten.  |
| 10   | Qualitativ    | Die Benutzeroberfläche soll intuitiv und benutzerfreundlich gestaltet sein.       |
| 11   | Qualitativ    | Die Applikation soll mit verschiedenen Bildschirmgrößen und Auflösungen kompatibel sein. |
| 12   | Qualitativ    | Die Anwendung soll schnelle Reaktionszeiten bei der Umrechnung bieten.            |
| 13   | Randbedingung | Die Applikation muss in Python 3.8 oder höher lauffähig sein.                     |

### 1.2 User-Storys

| US-№ | An-№ | Verbindlichkeit | Beschreibung                                                                 |
| ---- | ---- | ---------------- | ---------------------------------------------------------------------------- |
| 1.1  | 1    | muss             | Als User möchte ich irgendeine Währung eingeben, damit ich den Wechselkurs zu einer anderen Währung sehen kann. |
| 2.1  | 2    | muss             | Als User möchte ich meine ausgewählte Währung eingeben, damit sie danach umrechnen kann. |
| 3.1  | 3    | muss             | Als User möchte ich die gewollte Ausgabe erhalten, damit ich sie für meine Zwecke benutzen kann. |
| 4.1  | 4    | muss             | Als User möchte ich meine gewollte Menge der Währung eingeben, damit ich dann die Ausgabe der gewollte Menge der Währung habe. |
| 5.1  | 5    | muss             | Als User möchte ich, dass die Applikation mit einer Währungsaktualliserungs-API läuft , damit die Währungen immer aktualisiert sind |
| 6.1  | 6    | muss             | Als User möchte ich, dass die Applikation eine Benutzeroberfläche hat, damit ich Währungen auswählen kann. |
| 7.1  | 7    | muss             | Als User möchte ich, dass die Applikation nicht neu starten muss um eine neu rechnung durchzuführen, damit ich keine Zeit verschwende. |
| 8.1  | 8    | muss             | Als User möchte ich, dass die Applikation Fehlermeldungen anzeigt, damit ich meine Fehler korrigieren kann. |

## 2. Planen

### 2.1 Arbeitspakete

| AP-№  | Zuständig  | Frist       | Beschreibung                                                                | Geplante Zeit |
| ----- | ---------- | ----------- | --------------------------------------------------------------------------- | ------------- |
| 1     | Jeanneret  | 23.8.24     | Erstellung des Projektantrag und Festlegung der Meilensteine/Ziele.         | 90 min        |
| 2     | Jeanneret  | 23.8.24     | Anforderungen und User-storeis schreiben.                                   | 60 min        |
| 3     | Jeanneret  | 23.8.24     | Arbeitspakete und Testfälle schreiben.                                      | 60 min        |
| 4     | Jeanneret  | 30.8.24     | Design der Benutzeroberfläche und der Systemarchitektur erstellen.          | 180 min        |
| 5     | Jeanneret  | 6.9.24      | Implementierung des Frontends.                                              | 180 min        |
| 6     | Jeanneret  | 13.9.24     | Entwicklung und Integration des Backends und der API.                       | 180 min        |
| 7     | Jeanneret  | 20.9.24     | Datenbankintegration durchführen (falls notwendig).                         | 180 min        |
| 8     | Jeanneret  | 27.9.24     | Durchführung von Tests und Behebung von Fehlern.                            | 180 min        |
| 9     | Jeanneret  | 1.11.24     | Fertigstellung der Dokumentation und Auswertung.                            | 180 min        |

### 2.3 Testfälle

| TC-№ | Ausgangslage                      | Eingabe                                               | Erwartete Ausgabe                                                |
| ---- | --------------------------------- | ----------------------------------------------------- | ---------------------------------------------------------------- |
| 1.1  | Applikation ist geöffnet          | Keine Eingabe                                        | Startbildschirm wird angezeigt.                                   |
| 1.2  | Applikation ist geöffnet          | Währung auswählen und Betrag eingeben                | Die eingegebene Währung und Betrag werden korrekt angezeigt.      |
| 1.3  | Applikation ist geöffnet          | Eine ungültige Währung eingeben                       | Fehlermeldung: „Ungültige Währung“                               |
| 2.1  | Applikation ist geöffnet          | Wechselkurs-API ist aktiv                            | Aktuelle Wechselkurse werden angezeigt.                           |
| 2.2  | Applikation ist geöffnet          | Eine gültige Währung eingeben, die nicht in der API enthalten ist | Fehlermeldung: „Daten nicht verfügbar“               |
| 3.1  | Applikation ist geöffnet          | Betrag für eine Währung eingeben und auf „Berechnen“ klicken | Umgerechneter Betrag wird korrekt angezeigt.              |
| 3.2  | Applikation ist geöffnet          | Einen sehr großen Betrag eingeben                    | Die Umrechnung erfolgt korrekt, keine Überlauf-Fehler.            |
| 4.1  | Applikation ist geöffnet          | Eingabe von 0 als Betrag                             | Die Umrechnung zeigt „0“ als Ergebnis.                            |
| 4.2  | Applikation ist geöffnet          | Mehrere Währungen nacheinander eingeben               | Jeder Wechselkurs wird korrekt umgerechnet und angezeigt.        |
| 5.1  | Applikation ist geöffnet          | Eingaben in der UI ändern                             | UI aktualisiert sich entsprechend der neuen Eingaben.            |
| 5.2  | Applikation ist geöffnet          | Falsche Eingaben machen und dann korrigieren         | Die Fehler werden behoben und die korrekte Ausgabe angezeigt.     |
| 6.1  | Applikation ist geöffnet          | Applikation während einer Umrechnung schließen        | Die Umrechnung wird abgebrochen und es wird keine fehlerhafte Ausgabe angezeigt. |
| 6.2  | Applikation ist geöffnet          | Neue Umrechnung nach einem API-Ausfall durchführen    | Die Umrechnung erfolgt nach der Wiederherstellung der API korrekt.|


## 3 Entscheiden


### 3.1

Ich habe mich entschieden das ich kein UI-Prototyp machen werde und mit dem Backend beginnen werde, weil der Code wird wahrscheinlich schwiriger sein als meine andere Projekte und ich muss Python dazu lernen.


## 4 Realisieren

### 4.1 
| AP-№ | Datum     | Zuständig        | geplante Zeit | tatsächliche Zeit |
| ---- | --------- | ---------------- | ------------- | ----------------- |
| 1    | 23.8.24   | Jeanneret| 90 min        |      90 min               |
| 2    | 23.8.24   | Jeanneret| 60 min        |      60 min               |
| 3    | 23.8.24   | Jeanneret| 60 min        |      60 min               |
| 4    | n/a       | Jeanneret| 180 min       |      n/a              |
| 5    | 20.9.24    | Jeanneret| 180 min       |      180 min              |
| 6    | 30.8.24/6.9.24   | Jeanneret| 180 min       |      180 min              |
| 7    | 13.9.24   | Jeanneret| 180 min       |      180 min              | 
| 8    | 27.9.24    | Jeanneret| 180 min       |      180 min              |
| 9    | 1.11.24   | Jeanneret| 180 min       |      180 min              |




