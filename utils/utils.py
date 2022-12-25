import pandas as pd

def read_csv_from_google_drive(url):
    if not isinstance(url, str):
        raise ValueError('Url should be string!')
    if not url:
        return None
    parsed_url = 'https://drive.google.com/uc?id=' + url.split('/')[-2]
    return pd.read_csv(parsed_url)    