# SubtitleClustering

Metadaten: https://www.imdb.com/interfaces/

# Datasets

Neues komplettes Dataset mit (fast allen IMDB-Metadaten) ```dataset/complete_dataset.csv```
Am besten alle Daten hier runterladen: https://drive.google.com/file/d/1xykqbrzUNKVBUEHAbuBDSIbhqIbeoHM2/view?usp=sharing und dann in den ```datatset```-Ordner entpacken. 

### Achtung

Nur bei 92 Enträgen sind alle Metadaten vorhanden, d.h. ```df.dropna()``` führt dazu, dass fast alle Daten verworfen werden.
Also lieber mit ```df.dropa(subset=['spalte_zum_filtern'])``` spezifische Spalten filtern.

## Ideen:

1. Nach Genres clustern (Evelin)
2. Hollowood vs. Nicht-Hollywood (Diana)
3. Zeitperioden (Jan) 
4. Drehbuchautorenvergleich (Lennart)

## Plan fürs nächste Treffen:

* Repräsentativen Sampledatensatz