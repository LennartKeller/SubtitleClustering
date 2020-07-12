import glob
import pandas as pd
from xml.etree import ElementTree

### Wenn ihr die dataset_create nutzen wollt müsst ihr die Pfade anpassen in line 8 und 49
### dir_year und dir_movie enthalten jeweils die Pfade allen Ordner in den Directories, path_year und path_movie entsprechend die Pfade zu den einzelnen Ordnern
data=[]
dir_year = glob.glob('tokenizedCorpusFilesXMLleftmostcolumn_de/OpenSubtitles/xml/de/*')
#print(dir_year)
for path_year in dir_year:
    print(path_year)
    dir_movie = glob.glob(path_year + '/*')
    #print(dir_movie)
    for path_movie in dir_movie:
        #print(path_movie)
        file_movie = glob.glob(path_movie + '/*.xml')
        #print(file_movie)
        for subtitle_version in file_movie:
            #print(subtitle_version.replace('\\','/'))
            movie_xml = ElementTree.parse(subtitle_version.replace('\\','/'))
            subtitles = movie_xml.findall('.//w')
            #print(subtitles)
            concat_text = ''
            for sentence in subtitles:
                line = sentence.text
                concat_text = concat_text + line + ' '
            genre = movie_xml.find('.//meta/source/genre')
            region = movie_xml.find('.//meta/source/original')
            duration = movie_xml.find('.//meta/source/duration')
            ### If's zur Abfrage ob die jeweiligen Daten im meta-Block in den xml vorhanden sind
            if region != None:
                label_region = region.text
            else:
                label_region = ''  
            if duration != None:
                label_duration = duration.text
            else:
                label_duration = ''  
            if genre != None:
                label_genre = genre.text
            else:
                label_genre = ''
            ### Zusammenfassen der Daten in Dictionary für jede einzelne Datei und ab in die Liste Data
            data.append({
                'filename': subtitle_version.replace(path_movie + '\\', ''),
                'text': concat_text,
                'IMDB_ID': path_movie.replace(path_year + '\\', ''),
                'genre': label_genre,
                'year': path_year.replace('tokenizedCorpusFilesXMLleftmostcolumn_de/OpenSubtitles/xml/de\\', ''),
                'production_region': label_region,
                'corpus': 'tokenisiert',
                'duration' : label_duration                            
            })

df = pd.DataFrame.from_dict(data)
print(df.shape)
print(df.head())
df.to_csv('subtitles_dataset_tokenized.csv', encoding='UTF-8')