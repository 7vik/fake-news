print('hey!')

#Satvik Golechha

import requests
from bs4 import BeautifulSoup
import re
import os

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)

url = 'https://worldnewsdailyreport.com/canadians-face-major-donut-shortage-after-first-day-of-cannabis-legalization/'

url = input()

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

title = soup.find("h1", {"class":"entry-title"}).prettify().split('\n')[1].strip("'")
print(title)


all_paras_with_tags = ""

for para in soup.find_all('p'):
    all_paras_with_tags += para.prettify()


all_paras_without_tags = remove_tags(all_paras_with_tags)
#print(all_paras_with_tags)
#print(all_paras_without_tags)

all_paras_without_tags = os.linesep.join([s for s in all_paras_without_tags.splitlines() if s.strip()])

print(all_paras_without_tags)

quotes = ""

for head in soup.find_all('em'):
    quotes += remove_tags(head.prettify())

print(quotes)

#images 
image_links = ""
for image in soup.find_all("meta", {"property":"og:image"}):
    image_links += image.prettify()

print("")

print(image_links.split('"')[1])
