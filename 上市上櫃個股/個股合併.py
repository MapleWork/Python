import sqlite3
import pandas as pd

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

def merge(number):
    import glob
    season = ["2019Q4","2020Q1","2020Q2","2020Q3","2020Q4"]

    for s in range(len(season)):
        s = season[s]
        
        data = glob.glob("D:\\資料庫\\台股\\上市\\Change csv title\\"+s+"\\"+number+".csv")
        for i in data:
            fr = open(i, 'rb').read()
            with open("D:\\資料庫\\台股\\個股\\"+number+".csv",'ab') as f:
                f.write(fr)
                
def drop(number):
    df = pd.read_csv("D:\\資料庫\\台股\\個股\\"+number+".csv")
    data = df.drop_duplicates(subset = None, keep=False)
    
    data.to_csv("D:\\資料庫\\台股\\個股\\"+number+".csv", encoding="utf_8-sig")

def csv(number):
    from glob import glob
    files = glob("D:\\資料庫\\台股\\個股\\"+number+".csv")
    df = pd.concat(
            (pd.read_csv(file,header=0, usecols=['存貨','流動資產合計','不動產、廠房及設備','資產總計','流動負債合計','負債總計','營業收入合計',
                  '本期淨利（淨損）','本期稅前淨利（淨損）','利息費用','營業活動之淨現金流入（流出）','股票代碼','股票名稱','季']
                            ,dtype={'name': str, 'tweet': str}) for file in files), sort=False, ignore_index=True)
    df.columns = ['存貨','流動資產合計','不動產、廠房及設備','資產總計','流動負債合計','負債總計','營業收入合計',
                  '本期淨利（淨損）','本期稅前淨利（淨損）','利息費用','營業活動之淨現金流入（流出）','股票代碼','股票名稱','季']
    df.to_csv("D:\\資料庫\\台股\\個股\\"+number+".csv", encoding="utf_8-sig", index = False)

    conn = sqlite3.connect("D:\\資料庫\\台股\\個股\\DB\\"+number+".db")
    df = pd.read_csv("D:\\資料庫\\台股\\個股\\"+number+".csv", encoding="utf_8-sig")
    df.to_sql("sort_All", conn, if_exists="append", index=False, dtype={ "本期淨利（淨損）": "float64", "本期稅前淨利（淨損）": "float64", "營業活動之淨現金流入（流出）": "float64"})

slist = get_stocknumber()
cnt = len(slist)
for i in range(cnt):
    try:
        number,name,group = slist[i]
        merge(number)
        drop(number)
        csv(number)
        print(number)
    except:
        pass
