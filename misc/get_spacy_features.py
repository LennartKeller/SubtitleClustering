import spacy
import pandas as pd
from tqdm import tqdm

df = pd.read_csv('../dataset/movies.csv')

#spacy.prefer_gpu()
nlp = spacy.load("de_core_news_sm")

lemma_result, pos_result, tag_result, dep_result, shape_result, ent_text_result, ent_label_result = [], [], [], [], [], [], []

for text in tqdm(df.text):

    doc = nlp(text)

    lemma, pos, tag, dep, shape, ent_text, ent_label = [], [], [], [], [], [], []

    for token in doc:
        lemma.append(token.lemma_)
        pos.append(token.pos_)
        tag.append(token.tag_)
        dep.append(token.dep_)
        shape.append(token.shape_)

    for ent in doc.ents:
        ent_text.append(ent.text)
        ent_label.append(ent.label_)

    lemma_result.append(" ".join(lemma))
    pos_result.append(" ".join(pos))
    tag_result.append(" ".join(tag))
    dep_result.append(" ".join(dep))
    shape_result.append(" ".join(shape))
    ent_text_result.append("|".join(ent_text))
    ent_label_result.append("|".join(ent_label))


df['lemma'] = lemma_result
df['pos'] = pos_result
df['tag'] = tag_result
df['dep'] = dep_result
df['token_shape'] = shape_result
df['ent_text'] = ent_text_result
df['ent_label'] = ent_label_result


df.to_csv('../dataset/movies.csv')


