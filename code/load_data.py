import os
import requests
from pathlib import Path

def download_yandex(sharing_link, file_path):
  API_ENDPOINT = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key={}'
  pk_request = requests.get(API_ENDPOINT.format(sharing_link))
  r = requests.get(pk_request.json()['href'])
  open(file_path, 'wb').write(r.content)

data_path = os.path.join(Path(__file__).parent.parent, 'data/bronze/interactions.parquet.gz')
download_yandex('https://disk.yandex.ru/d/QsJkkMN5KDQobA', data_path)