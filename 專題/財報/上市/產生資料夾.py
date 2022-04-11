import os
import csv

def get_stocknumber():
    res = []
    try:
        with open('stock_number.csv', encoding="utf-8") as f:
            slist = f.readlines()
            print('讀入：',slist)
            for lst in slist:
                s = lst.split(',')
                res.append([s[0].strip(),str(s[1].strip()),str(s[2].strip())])
    except:
        print('讀不到')
    return res

#個股
def merge(group,number,rows):
    folder = "D:/資料庫/台股/個股/"+group+"/"+s+""
    if not os.path.isdir(folder):
        os.makedirs(folder)

    f = open("D:/資料庫/台股/個股/"+group+"/"+s+"/"+number+".csv",mode='w', newline="")
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
    f.close()

rows = []
season = ['2019Q4','2020Q1','2020Q2','2020Q3','2020Q4']

for s in range(len(season)):
    
    s = season[s]
    slist = get_stocknumber()
    cnt = len(slist)
    for i in range(cnt):
        number,name,group = slist[i]
        try:
            merge(group,number,rows)
            print(number + "\t Success")
        except:
            pass
