import time

import pandas as pd
from flair.data import Sentence
from flair.embeddings import TransformerDocumentEmbeddings
from torch.cuda import is_available
from tqdm import tqdm

if __name__ == '__main__':

    print("Checking if CUDA is available...")
    print("CUDA is enabled" if is_available() else "CUDA is not enabled")
    print("Reading dataset...")
    df = pd.read_csv('../dataset/movies_complete.csv')
    df.drop_duplicates(subset=['IMDB_ID'], inplace=True)
    df.dropna(subset=['filename'], inplace=True)
    df.dropna(subset=['Plot'], inplace=True)

    doc_embeddings = TransformerDocumentEmbeddings('bert-base-nli-stsb-mean-tokens')

    embeddings = []

    print("Start computing embeddings..")
    for index, row in tqdm(df.iterrows()):
        if not row.Plot:
            continue

        # heat and tail method (https://arxiv.org/pdf/1905.05583.pdf)
        token = row.Plot.split()
        if len(token) > 96:
            text = " ".join(token[:96])
        else:
            text = " ".join(token)

        doc = Sentence(text)

        doc_embeddings.embed(doc)
        sequence_embedding = doc.embedding.cpu().detach().numpy()
        #time.sleep(0.1)

        with open('embeddings_bert_summaries.txt', 'a') as f:
            f.write(f"{row.filename} {' '.join(map(str, sequence_embedding))}\n")

