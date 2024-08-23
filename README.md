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
