import os
import csv
import pandas as pd
from glob import glob
from pathlib import Path

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

def merge(path,group,number,s):
    files = glob(path+group+"\\"+s+"\\計算\\stock_"+number+".csv")
    
    df = pd.concat(
            (pd.read_csv(file,header=0, usecols=['流動資產合計 Total current assets','流動負債合計 Total current liabilities',
                                                 '存貨 Current inventories','本期稅前淨利（淨損）　Profit (loss) before tax',
                                                 '營業活動之淨現金流入（流出）Net cash flows from (used in) operating activities',
                                                 '不動產、廠房及設備 Property, plant and equipment',
                                                 '資產總計　Total assets','負債總計 Total liabilities','本期淨利（淨損）Profit (loss)',
                                                 '營業收入合計　Total operating revenue','利息費用 Interest expense','股票代碼', '股票名稱','季']
                            ,dtype={'name': str, 'tweet': str}) for file in files), sort=False, ignore_index=True)
                           
    df.columns = ['存貨','流動資產合計','不動產、廠房及設備','資產總計','流動負債合計','負債總計','營業收入合計',
                  '本期淨利（淨損）','本期稅前淨利（淨損）','利息費用','營業活動之淨現金流入（流出）','股票代碼','股票名稱','季']

    folder = "D:\\資料庫\\台股\\上市\\Change csv title\\"+s+""
    if not os.path.isdir(folder):
        os.makedirs(folder)

    df.to_csv("D:\\資料庫\\台股\\上市\\Change csv title\\"+s+"\\"+number+".csv", encoding="utf_8-sig", index = False)

path = "D:\\資料庫\\台股\\上市\\"
season = ["2019Q4","2020Q1","2020Q2","2020Q3","2020Q4"]

for s in range(len(season)):
    s = season[s]
    slist = get_stocknumber()
    cnt = len(slist)
    for i in range(cnt):
        try:
            number,name,group = slist[i]
            merge(path,group,number,s)
            print(number)
        except:
            pass
