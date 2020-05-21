# SubtitleClustering

Metadaten: https://www.imdb.com/interfaces/
# Datasets

Neues komplettes Dataset mit (fast allen IMDB-Metadaten) dataset_complete.csv
Am besten alle Daten hier runterladen: https://drive.google.com/file/d/1xykqbrzUNKVBUEHAbuBDSIbhqIbeoHM2/view?usp=sharing
Und dann in den "datatset"-Ordner entpacken. 

### Achtung

Nur bei 92 Enträgen sind alle Metadaten vorhanden, d.h. ```df.dropna()``` führt dazu, dass fast alle Daten verworfen werden.
Also lieber mit ```df.dropa(subset=['spalte_zum_filtern'])``` spezifische Spalten filtern.

## Ideen:

1. Nach Genres clustern (Evelin)
2. Hollowood vs. Nicht-Hollywood (Diana)
3. Zeitperioden (Jan) 
4. Drehbuchautorenvergleich (Lennart)

## Plan fürs nächste Treffen:

* Jeder arbeitet an seiner Fragestellung
* Wenn nötig zusätzliche Metadaten einarbeiten => Metadaten von IMDB anschauen 
* Artefakte ins Artefakte.txt eintragen