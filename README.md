# SubtitleClustering

### Daten

* Link zum Github-Repository unseres Projekts: [https://github.com/LennartKeller/SubtitleClustering/](https://github.com/LennartKeller/SubtitleClustering/)

* Downloadlink movies_complete.csv, endgültiger, bereinigter Datensatz erweitert mit IMDB Metadaten: [https://drive.google.com/file/d/1Lzs40ugz4mwCWyxhU5JRdJYJX4m-xYhi/view](https://drive.google.com/file/d/1Lzs40ugz4mwCWyxhU5JRdJYJX4m-xYhi/view)


* (Downloadlink Ursprünglicher Datensatz aus den reinen Daten des Opensubtitles.org Datensatz: [https://drive.google.com/file/d/1icM6DojsKWTfL1-nthTMEvEezvLtepo1/view?usp=sharing](https://drive.google.com/file/d/1icM6DojsKWTfL1-nthTMEvEezvLtepo1/view?usp=sharing))

* Außerdem haben wir im Laufe des Projekts mit einer ganzen Reihe von zu Document-Embeddings experimentiert. Diese sind unter [https://drive.google.com/file/d/11LUdfpFhzLgZ9jQI4QgnD6eZauaBBCED/view?usp=sharing](https://drive.google.com/file/d/11LUdfpFhzLgZ9jQI4QgnD6eZauaBBCED/view?usp=sharing) abrufbar.

### Struktur des Repositorys

* Die Finalen Notebooks, deren Inhalte in der Präsentation zusammengefasst wurden befinden sich im Ordner: ```notebooks/final```

* Die Präsentation befindet sich im Ordner: ```presentation```
  * Die Ergebnisse unseres Topic Modellings befinden sich in ```notebooks/final/TopicModelling.ipynb``` (Diese konnten aufgrund der Interaktivität nicht sinnvoll in die Präsentation integriert werden)

* Alle weiteren Notebooks befinden sich im Ordner: ```notebooks```
  * Diese Notebooks enthalten sämtliche Clusterings und Versuche, die über das Semester durchgeführt wurden.

* Die Datensätze sowohl, die von uns bearbeiteten, als auch die Rohdaten von IMBD befinden sich im Ordner: ```datasets```
Die Datensätze sind teilweise zu groß für GIT, weshalb diese über die oben bereitgestellen Links runtergeladen werden müssen.

* Des weiteren enthält der Ordner das Python-Skript (dataset_create_tokenized.py), mit dem die ursprünglichen XML Daten in eine für Pandas einlesbare .csv gespeichert wurden
