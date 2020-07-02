import requests

# 
class RequestException(Exception):
    pass


def get_metadata(imdb_id: str, api_key: str, plot_type: str = "full") -> dict:
    response = requests.get(f"http://www.omdbapi.com/?apikey={api_key}&i={imdb_id}&plot={plot_type}")
    if response.status_code != 200:
        raise RequestException(f"Last reponse status code was {response.status_code}\n{response.content}")
    try:
        data = response.json()
        return data
    except Exception:
        return


if __name__ == '__main__':

    import pandas as pd
    from pathlib import Path
    from tqdm import tqdm

    api_key = input("Enter APi-Key: ")
    movies = pd.read_csv('../dataset/movies.csv')
    if not Path('../dataset/openIMDB.csv').exists():
        openimdb = pd.DataFrame()
        openimdb['imdbID'] = []
        openimdb.to_csv('../dataset/openIMDB.csv')

    openimdb = pd.read_csv('../dataset/openIMDB.csv')
    entries = []
    pbar = tqdm(movies['IMDB_ID'])
    for imdb_id in pbar:
        if imdb_id in openimdb['imdbID'].to_list():
            pbar.set_description(f'Already got data for {imdb_id}')
            continue
        else:
            pbar.set_description(f'Load data for {imdb_id}')
            try:
                data = get_metadata(imdb_id, api_key)
                if data:
                    entries.append(data)
            except RequestException as e:
                pbar.set_description(f'Error: {e}')
                break

    new_df = pd.DataFrame.from_records(entries)
    openimdb = openimdb.append(new_df)
    openimdb.to_csv('../dataset/openIMDB.csv')
