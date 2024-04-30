import io
import re
import requests
import urllib.request
from datetime import datetime
from pathlib import Path

source = io.open("source.txt", 'r', encoding="UTF-8").read()
source = source[source.find('data-swiper-slide-index="0"')+1:]
source = source[source.find('data-swiper-slide-index="0"')+1:]
source = source[:source.find('data-swiper-slide-index="0"')]
img_links = re.findall(r'(?<=<img src=")[^"]+', source)
folder_name = str(datetime.now()).replace(":", "-")
folder_name = folder_name[:folder_name.find(".")]
Path(folder_name).mkdir(parents=True, exist_ok=True)
for img_link, img_index in zip(img_links, range(len(img_links))):
	img_data = requests.get(img_link).content
	
	with io.open(f"{folder_name}/{img_index}.png", 'wb') as handler:
		handler.write(img_data)

print(f"{len(img_links)} images found and downloaded.\nPress any key to exit")
input()