import pandas as pd
import csv

with open("true_false.csv","r",encoding="utf-8") as data:
    reader = csv.reader(data)
    header = next(reader)
    for i in reader:
        if i[7] == 1:
            count