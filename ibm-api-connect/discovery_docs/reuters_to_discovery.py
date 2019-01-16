from pprint import pprint
import json
import os
import csv


title = ""
content = ""
title2 = ""
content2 = ""
with open('../datasets/real8000.csv', 'r+', encoding='ISO-8859-1') as f:
    reader = csv.reader(f)
    count = 0
    for row in reader:
        if count > 3999:
            title2 = title2+'\n'+row[0]
            content2 = content2+'\n'+row[1]
        title = title + row[0]
        content = content+'\n'+row[1]
        count += 1

res = {"title": title, "content": content}
pprint(res)
with open('real3999.json', 'w+') as f:
    f.write(json.dumps(res))


res = {"title": title2, "content": content2}
pprint(res)
with open('real4000.json', 'w+') as f:
    f.write(json.dumps(res))
