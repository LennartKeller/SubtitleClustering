import re

import nltk
import numpy as np
import pandas as pd
from flair.data import Sentence
from flair.embeddings import TransformerDocumentEmbeddings
from torch.cuda import is_available
from tqdm import tqdm
import re

if __name__ == '__main__':

    print("Checking if CUDA is available...")
    print("CUDA is enabled" if is_available() else "CUDA is not enabled")
    print("Reading dataset...")
    df = pd.read_csv('../dataset/complete_dataset.csv')
    df.drop_duplicates(subset=['IMDB_ID'], inplace=True)
    df.dropna(subset=['filename'], inplace=True)
    df.dropna(subset=['text'], inplace=True)

    print("Filtering noise from text data...")
    remove_subcentral_annotation = re.compile(r'übersetzt von.+$', flags=re.I)
    remove_season_episode_annotation = re.compile(r's\d+?e\d+?', flags=re.I)
    remove_remove_season_episode_annotation_german = re.compile(r'staffel.+?episode', flags=re.I)
    remove_remove_season_episode_annotation_german_2 = re.compile(r'staffel.+?folge', flags=re.I)
    remove_subcentral_note = re.compile(r'subcentral.+ präsentiert', flags=re.I)
    remove_subtitle_statement = re.compile(r'Untertitel von.+$', flags=re.I)
    remove_netflix_original_statement = re.compile(r'EINE NETFLIX ORIGINAL SERIE', flags=re.I)
    remove_tvuser = re.compile(r'tv4user.+?präsentiert', flags=re.I)
    remove_tvuser_subcentral = re.compile(r'subcentral.+?tv4user', flags=re.I)
    remove_subcentral_url = re.compile(r'subcentral\.de', flags=re.I)
    remove_tv4user_url = re.compile(r'tv4user\.de', flags=re.I)
    remove_sub_statement = re.compile(r'subbed\w+?by', flags=re.I)
    remove_tiger_statement = re.compile(r'übersetzung filmtiger', flags=re.I)

    for regex in (remove_subcentral_annotation,
                  remove_season_episode_annotation,
                  remove_remove_season_episode_annotation_german,
                  remove_remove_season_episode_annotation_german_2,
                  remove_subcentral_note,
                  remove_subtitle_statement,
                  remove_netflix_original_statement,
                  remove_tvuser,
                  remove_tvuser_subcentral,
                  remove_subcentral_url,
                  remove_tv4user_url,
                  remove_sub_statement,
                  remove_tiger_statement):
        df.text = df.text.str.replace(regex, '')

    doc_embeddings = TransformerDocumentEmbeddings('distilbert-base-german-cased')

    embeddings = []

    print("Start computing embeddings..")
    for index, row in tqdm(df.iterrows()):
        if not row.text:
            continue

        # heat and tail method (https://arxiv.org/pdf/1905.05583.pdf)
        token = re.findall(r'\w+', row.text)
        if len(token) < 512:
            head = token[:128]
            tail = token[382:]
            text = " ".join(head + tail)
        else:
            text = " ".join(token)

        doc = Sentence(text)

        doc_embeddings.embed(doc)
        sequence_embedding = doc.embedding.cpu().detach().numpy()

        with open('embeddings_bert_headtail.txt', 'a') as f:
            f.write(f"{row.filename} {' '.join(map(str, sequence_embedding))}\n")

