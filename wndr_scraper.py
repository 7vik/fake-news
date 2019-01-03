import csv
import requests
from bs4 import BeautifulSoup
import re
import os

# Use sitemap (xml) to get all URLs on a website to text format 
#to load all valid URLs from file to a list
def load_urls():
    URLS = []
    f = open("wndr-URLs.txt")
    u = "asdf"
    while u != "":
        u = f.readline()
        if len(u)>70:
            URLS.append(u)
    return URLS

#to remove all html tags from string
def remove_tags(text):
    TAG_RE = re.compile(r'<[^>]+>')
    return TAG_RE.sub('', text)

# Create a file to write to, add headers row
def initialise_csv():
    f = csv.writer(open('wndr_dataset.csv', 'w'))
    f.writerow(['URL', 'Title', 'Content', 'Image'])
    return f

class WNDR_Article:
    'common class for all world news daily report fake news articles'
    article_count = 0
    
    def __init__(self, url, filename):
        self.ur = url
        self.fil = filename
        WNDR_Article.article_count += 1
        
    def make_soup(self):
        page = requests.get(self.ur)
        soup = BeautifulSoup(page.text, 'html.parser')
        return soup

    def get_title(self, soup):
        t = ""
        try:
            t = soup.find("h1", {"class":"entry-title"}).prettify().split('\n')[1].strip("'")
        except AttributeError:
            pass
        return t

    def get_text(self, soup):
        all_paras_with_tags = ""
        for para in soup.find_all('p'):
            all_paras_with_tags += para.prettify()
        all_paras_without_tags = remove_tags(all_paras_with_tags)
        all_paras_without_tags = os.linesep.join([s for s in all_paras_without_tags.splitlines() if s.strip()])
        for head in soup.find_all('em'):
            all_paras_without_tags += remove_tags(head.prettify())
        return all_paras_without_tags

    def get_image(self, soup):
        image_links = ""
        for image in soup.find_all("meta", {"property":"og:image"}):
            image_links += image.prettify()
        try:    
            img = image_links.split('"')[1]
        except IndexError:
            img = ""
        return img

    def write_to_csv(self, fil):
        s = self.make_soup()
        fil.writerow([self.ur, self.get_title(s), self.get_text(s), self.get_image(s)])
#End of class WNDR_Article

def main():
    URLS = load_urls()
    file = initialise_csv()
    for url in URLS:
        try:
            art = WNDR_Article(url, file)
            art.write_to_csv(file)
            print("......Scraping article #"+str(WNDR_Article.article_count)+"......." )
        except:
            pass
    print("Scraped their whole server!")

if __name__ == "__main__":
    main()
