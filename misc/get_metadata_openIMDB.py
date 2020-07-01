import requests


def get_metadata(imdb_id: str, api_key: str, plot_type: str = "full") -> dict:
    response = requests.get(f"http://www.omdbapi.com/?apikey={api_key}&i={imdb_id}&plot={plot_type}")
    if response.status_code != 200:
        raise Exception(f"Last reponse status code was {response.status_code}\n{response.content}")
    return response.content


if __name__ == '__main__':

    import pandas as pd
    from pathlib import Path
    from tqdm import tqdm

    api_key = input("Enter APi-Key")
    movies = pd.read_csv('../dataset/movies.csv')
    if Path('../dataset/openIMDB.csv').exists():
        openimdb = pd.read_csv('../dataset/openIMDB.csv')
        prexeisting_data = True
    else:
        openimdb = pd.DataFrame()
        prexeisting_data = False

    data = []
    for imdb_id in tqdm(movies['IMDB_ID']):
        try:
            if prexeisting_data:
                if imdb_id not in openimdb['imdbID']:
                    data.append(get_metadata(imdb_id, api_key))
            else:
                data.append(get_metadata(imdb_id, api_key))
        except Exception as e:
            print(e)

    new_df = pd.DataFrame.from_records(data)

    openimdb.append(new_df)
    openimdb.to_csv('../dataset/openIMDB.csv')


