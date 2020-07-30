---
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
html: true
---

## Makroperspektive

Können wir Genres und Sprachen auch in ihrer Gesamtheit mit Clustering-Techniken analysieren?

---

## Vorgehen

1. Zusammenfassen aller Texte mit gleichem Label (Sprachen/ Genres)
2. Filtern von zusammengefassten Instanzen die aus nur wenigen Texten bestehen
3. Cluster-Analyse der zusammengefassten Daten
   1. KMeans, BayesianGaussianMixture-Models 
      => Anzahl der Cluster = Anzahl an Einzelsprachen
   1. DBSCAN => "Tuning" der *eps* und *min_samples* Parameter
4. Evaluation: durch subjektive Analyse der Cluster & (Davies Bouldin Score + Calinski Harabasz Score)

---

## Schwachstellen dieses Ansatzes

- Die Anzahl der Texte (sowie die Anzahl der Tokens) sind stark schief verteilt.

- Geeignete Evaluationsmetrik(en)?

---
## Feature-Extraction Pipeline

1. ```TfidfVectorizer(max_features=[100, 150, 250, 500, 1000, 5000]), stop_words=None)```
2. (```UMAP(n_components=[90, 70, 50, 30, 25, 10])``` oder ```PCA(<n_components von UMAP>)```)
   - => Maximale Anzahl der Components durch Anzahl an Instanzen beschränkt

**Besonderheit:** Ebenfalls wurde auch eine gefilterte Version des Textes verwendet bei der alle Wörter bis auf die Stopwörter entfernt wurden.

---

**Visualisierungen**
```UMAP(n_components=2, n_neigbors=[5,..,10])``` auf den Features aus der Pipeline

---

## Genres: Textverteilung

<iframe src="http://localhost:5050/Genre_Distribution.html" style="border:none;height:100%;width:100%;"></iframe>

=> Alle Genres die seltener als viermal vorkommen wurden gefiltert

---

## Genres: Beste Feauture-Kombination

```python
Pipeline(steps=[('tfidfvectorizer', TfidfVectorizer(max_features=1000)),
                ('densetransformer', DenseTransformer(),
                ('umap', UMAP(n_components=10))])
```

---

## Genres: KMeans

<iframe src="http://localhost:5050/GENRE_KMEANS.html" style="border:none;height:100%;width:100%;"></iframe>

---

## Genres: KMeans

<iframe src="http://localhost:5050/kmeans_genre_table.html" style="border:none;height:100%;width:100%;"></iframe>

---
## Genres: DBScan

<iframe src="http://localhost:5050/GENRE_DBSCAN.html" style="border:none;height:100%;width:100%;"></iframe>

---

## Genres: DBScan

<iframe src="http://localhost:5050/dbscan_genre_table.html" style="border:none;height:100%;width:100%;"></iframe>

---
## Genres: Gaussian-Mixture Model

<iframe src="http://localhost:5050/GENRE_GMM.html" style="border:none;height:100%;width:100%;"></iframe>

---

## Genres: Gaussian-Mixture Model

<iframe src="http://localhost:5050/gmm_genre_table.html" style="border:none;height:100%;width:100%;"></iframe>

---

## Languages: Textverteilung

<iframe src="http://localhost:5050/Language_Distribution.html" style="border:none;height:100%;width:100%;"></iframe>


---

## Languages: Beste Feauture-Kombination

```python
Pipeline(steps=[('tfidfvectorizer', TfidfVectorizer(max_features=150)),
                ('densetransformer', DenseTransformer(),
                ('umap', UMAP(n_components=40, random_state=42))])
```

---

## Languages: KMeans

<iframe src="http://localhost:5050/Language_KMEANS.html" style="border:none;height:100%;width:100%;"></iframe>

---

## Languages: KMeans

<iframe src="http://localhost:5050/kmeans_lang_table.html" style="border:none;height:100%;width:100%;"></iframe>

---

## Languages: DBScan

<iframe src="http://localhost:5050/Language_DBSCAN.html" style="border:none;height:100%;width:100%;"></iframe>

---

## Languages: DBScan

<iframe src="http://localhost:5050/dbscan_lang_table.html" style="border:none;height:100%;width:100%;"></iframe>

---


## Languages: Gaussian-Mixture Model

<iframe src="http://localhost:5050/Language_GMM.html" style="border:none;height:100%;width:100%;"></iframe>

---

## Languages: Gaussian-Mixture Model

<iframe src="http://localhost:5050/gmm_lang_table.html" style="border:none;height:100%;width:100%;"></iframe>

---

## Autoencoder
#### Architektur

![bg left 50%](http://localhost:5050/autoencoder_annotated.png)

**Training:**
- num_words:  2500
- Maximale Sequenzlänge: 1000
- Epochen: 40

---

**Trainingsdaten:**
* Maximale Sequenzlänge ist ein Beschränkung bei rekurrenten Netzen
  *  => Bei praktikablen Sequenzlänge würden wir nur den ersten Text betrachten
* Deshalb wurden 250 Sätze pro Instanz zufällig gesampelt und konkanteniert

----

## Autoencoder
#### Ergebnisse

<iframe src="http://localhost:5050/Genre_Autoencoder_KMEANS.html" style="border:none;height:100%;width:100%;"></iframe>


---

## Fazit

1. Inbesondere die Erkennung der Originalsprachen anhand ihrer deutschen Übersetzungen scheint ein _stilometrisches_ Problem zu sein, da der Fokus auf wenige häufige (Stop-)Wörter die Ergebnisse verbessert
2. UMAP und PCA als Techniken zur Dimensionreduktion auf den Tfidf-Feature scheinen ebenfalls einen positiven Einfluss auf die Ergebnisse zu haben
3. DBSCAN ist extrem instabil und funktioniert eher nicht auf Textdaten

