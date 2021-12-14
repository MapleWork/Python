import shutil
import os
from os import walk
from os.path import join
def get_stocknumber():
    res = []
    try:
        with open('stock_number.csv', encoding="utf-8") as f:
            slist = f.readlines()
            print('讀入：',slist)
            for lst in slist:
                s = lst.split(',')
                res.append([s[0].strip(),str(s[1].strip()),str(s[2].strip())]) # .strip去除空白，存到res陣列
    except:
        print('讀不到')
    return res
def change_filename_cr(path,number):
    for root, dirs, files in walk(path):
        for i in files:
            FullPath = join(root, i)
            FileName = join(i)
            filenumber = '-cr-'+number+'-'
            if filenumber in FullPath:
                if not os.path.isfile(number+".html"):
                    os.rename(FileName, number+".html")

def change_filename_ir(path,number):
    for root, dirs, files in walk(path):
        for i in files:
            FullPath = join(root, i)
            FileName = join(i)
            filenumber = '-ir-'+number+'-'
            if filenumber in FullPath:
                if not os.path.isfile(number+".html"):
                    os.rename(FileName, number+".html")

path = "D:\\資料庫\\台股\\html"
slist = get_stocknumber()
cnt = len(slist)
for i in range(cnt):
    number,name,group = slist[i]
    change_filename_cr(path,number)
    change_filename_ir(path,number)
    print(number)
