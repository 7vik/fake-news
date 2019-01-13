import json
import csv

file_base = input('Base:  ')
start = int(input())
rng = int(input())
with open(file_base+'.csv', 'w+') as outFile:
    outs = csv.writer(outFile)
    for i in range(start, rng):
        file_ = file_base + str(i)
        with open(file_+'.json', 'r+') as inFile:
            ins = json.load(inFile)
            for x in ins:
                outs.writerow([
                    x["title"],
                    x["content"],
                    x["image"],
                    x["time"]
                ])
        print(file_, 'done')
