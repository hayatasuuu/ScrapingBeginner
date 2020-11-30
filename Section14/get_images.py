import os
from time import sleep

import pandas as pd
import requests

IMAGE_DIR = './images/'


df = pd.read_csv('image_urls.csv')
# print(df.columns)
# print(df.yahoo_image_url[:5])

if not os.path.isdir(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)
    print(f'created {IMAGE_DIR}.')
else:
    print(f'{IMAGE_DIR} already exists.')

for file_name, image_url in zip(df.filename[:20], df.yahoo_image_url[:20]):
    image = requests.get(image_url)
    with open(IMAGE_DIR + file_name + '.jpg', 'wb') as f:
        f.write(image.content)
    sleep(2)
