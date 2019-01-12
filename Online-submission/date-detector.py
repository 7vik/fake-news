#Pravega IBM Hackathon Submission

import re
import datetime
from datetime import date


def load_article(file):
    f = open(file)
    return f.read()

def find_dates(text_str):
    dates = []
    #all = re.findall(r"(\d{1,2} (?:January|February|March|April|May|June|July|August|September|October|November|December) \d{4})", text_str)
    try:
        for m in re.findall(r'\d{1}-\d{1}-\d{4}', text_str):
            date = datetime.datetime.strptime(m, '%d-%m-%Y').date()
            dates.append(date)
        for m in re.findall(r'(\d{1,2} (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{4})', text_str):
            date= datetime.datetime.strptime(m, '%d %b %Y').date()
            dates.append(date)
        for m in re.findall(r"((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) the \d{1}th)", text_str):
            date = datetime.datetime.strptime(m, '%B'+' the '+'%d'+'th').date()
            dates.append(date)
        for m in re.findall(r"((?:January|February|March|April|May|June|July|August|September|October|November|December) \d{2}, \d{4})", text_str):
            date = datetime.datetime.strptime(m, '%B %d, %Y' ).date()
            dates.append(date)
    except AttributeError:
    #no dates in article
        pass 
    return dates


def main():
    art = load_article('sample-article.txt')
    dates = find_dates(art)
    print("All the dates in this article are:")
    for each_date in dates:
        print(each_date)


if __name__ == "__main__":
    main()