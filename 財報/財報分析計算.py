import os
import pandas as pd
import glob

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

def calculate(path,html_path,number,name,group):
    for i in range(0,len(os.listdir(html_path))):
        folder1 = (os.listdir(html_path)[i])
        folder2 = (os.listdir(html_path)[i-1])

        df1 = pd.read_csv(path+"\\"+group+"\\"+folder1+"\\"+number+"\\計算\\stock_"+number+".csv", encoding="utf_8-sig")
        df2 = pd.read_csv(path+"\\"+group+"\\"+folder2+"\\"+number+"\\計算\\stock_"+number+".csv", encoding="utf_8-sig")

        result1 = df1.營業收入合計 / df1.資產總計
        result2 = df1.負債總計/df1.資產總計
        result3 = df1.流動資產合計/df1.流動負債合計
        result4 = (df1.流動資產合計-df1.存貨)/df1.流動負債合計
        result5 = (df1.本期稅前淨利+df1.利息費用)/df1.利息費用
        result6 = df1.營業活動之淨現金流入/df1.流動負債合計
        result7 = df1.本期稅前淨利/df1.營業收入合計

        df = pd.DataFrame(columns = ["總資產周轉率","負債佔資產比率","流動比率",
                                     "速動比率","利息保障倍數","現金流量比率","純益率",
                                     "股票代碼","股票名稱","股票類別","季"])

        df['總資產周轉率']=result1
        df['負債佔資產比率']=result2
        df['流動比率']=result3
        df['速動比率']=result4
        df['利息保障倍數']=result5
        df['現金流量比率']=result6
        df['純益率']=result7
        df['股票代碼']=number
        df['股票名稱']=name
        df['股票類別']=group
        df['季']=folder1

        Path_CSV = path+"\\calculate\\"+folder1

        if not os.path.isdir(Path_CSV):
            os.makedirs(Path_CSV)

        df.to_csv(Path_CSV+"\\Stock_"+number+".csv", encoding="utf_8-sig", index = False)

path = 'D:\\資料庫\\台股\\上市'
html_path = 'D:\\資料庫\\台股\\html\\上市'

slist = get_stocknumber()
cnt = len(slist)
for i in range(cnt):
    number,name,group = slist[i]
    try:
        calculate(path,html_path,number,name,group)
        print(number + "\t Success")
    except:
        pass
    
