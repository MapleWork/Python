from asyncio.windows_events import NULL
import os
import sqlite3
import pandas as pd

from glob import glob
from numpy import int64

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

def read_folder_saveCSV(path,html_path,number,group):
    for i in range(0,len(os.listdir(html_path))):
        folder = (os.listdir(html_path)[i]) #取得陣列中的資料夾名稱
        df = pd.read_html(html_path+"\\"+folder+"\\"+number+".html") #讀取資料夾內的檔案

        for index_num in range(0,3): #取得陣列中的資料
            file_num = str(index_num+1) #資料儲存檔名
            Path_CSV = path+"\\"+group+"\\"+folder+"\\"+number #設定資料存放路徑
            if not os.path.isdir(Path_CSV): #判斷資料夾是否存在
                os.makedirs(Path_CSV) #新增資料夾

            df[index_num].to_csv(Path_CSV+"\\"+number+"_"+file_num+".csv", index = False, encoding='utf_8-sig')

def combine_all_data(path,html_path,number,name,group):
    Path = path+"\\"+group #設定資料存放路徑
    for i in range(0,len(os.listdir(html_path))):
        folder = (os.listdir(html_path)[i]) #取得陣列中的資料夾名稱
        Path_CSV = Path+"\\"+folder+"\\"+number #設定個股資料存放路徑

        for x in range(1,4):
            file_num = str(x) #轉換資料型別
            df = pd.read_csv(Path_CSV+"\\"+number+"_"+file_num+".csv", encoding= "utf_8_sig") #取得csv檔案位置
            num = (len(df.columns))+1 #取得csv表格列數
            df = df.values.tolist() #整個轉為list
            num_list = [] #設定一個空陣列，放置列數

            for i in range(1, num):
                num_list += [i]
            num_list = [str(i) for i in num_list] #將陣列從int轉str
            df = pd.DataFrame(columns = num_list, data = df)

            #刪除num_list陣列的3、4
            del num_list[1] #刪除num_list陣列的3
            del num_list[1] #刪除num_list陣列的4

            df = df.drop(num_list,axis=1) #刪除不需要的資料
            data = df.values #把 Dataframe 轉成 2D numpy array
            index1 = list(df.keys()) #找到數據的 key
            data = list(map(list, zip(*data))) #行列互換，再利用map函數將zip內的元組轉列表
            data = pd.DataFrame(data, index=index1)
            data.to_csv(Path_CSV+"\\"+number+"_getfile_"+file_num+".csv",header=0, encoding= "utf_8_sig") #存檔

        files = glob(Path_CSV+"\\"+number+"_getfile_1.csv") #取得檔案
        df = pd.concat(
                    (pd.read_csv(file,header=0, usecols=['2','流動資產合計 Total current assets','流動負債合計 Total current liabilities',
                                                        '存貨 Current inventories','不動產、廠房及設備 Property, plant and equipment',
                                                        '資產總計　Total assets','負債總計 Total liabilities',
                                                        '歸屬於母公司業主之權益合計 Total equity attributable to owners of parent',
                                                        '非控制權益 Non-controlling interests','應收帳款淨額 Accounts receivable, net'] #抓取需要的資料
                                                        ,dtype={'name': str, 'tweet':str}) for file in files), sort=False, ignore_index=True)
        df.to_csv(Path_CSV+"\\"+number+"_getfile_1.csv", encoding= "utf_8_sig", index = False) #存檔
        
        files = glob(Path_CSV+"\\"+number+"_getfile_2.csv") #取得檔案
        df = pd.concat(
                    (pd.read_csv(file,header=0, usecols=['2','本期淨利（淨損）Profit (loss)','營業收入合計　Total operating revenue',
                                                        '營業成本合計　Total operating costs'] #抓取需要的資料
                                                        ,dtype={'name': str, 'tweet':str}) for file in files), sort=False, ignore_index=True)
        df.to_csv(Path_CSV+"\\"+number+"_getfile_2.csv", encoding= "utf_8_sig", index = False) #存檔
        
        files = glob(Path_CSV+"\\"+number+"_getfile_3.csv") #取得檔案
        df = pd.concat(
                    (pd.read_csv(file,header=0, usecols=['2','本期稅前淨利（淨損）　Profit (loss) before tax',
                                                         '營業活動之淨現金流入（流出）Net cash flows from (used in) operating activities',
                                                         '利息費用 Interest expense'] #抓取需要的資料
                                    ,dtype={'name': str, 'tweet':str}) for file in files), sort=False, ignore_index=True)
        df.to_csv(Path_CSV+"\\"+number+"_getfile_3.csv", encoding= "utf_8_sig", index = False) #存檔
        
        files = glob(Path_CSV+"\\"+number+"_getfile_*"+".csv") #取得資料夾內需要的資料
        df_list = [pd.read_csv(file) for file in files] #串列中包含兩個Pandas DataFrame
        result = pd.merge(df_list[0],df_list[1], on='2') #進行資料合併
        result = pd.merge(result,df_list[2],on='2') #進行資料合併
        result["股票代碼"] = number #新增股票代碼
        result["股票名稱"] = name #新增股票名稱
        result["股票類別"] = group #新增股票名稱
        result["季"] = folder #新增季別
        folder_save = Path_CSV+"\\計算"
        if not os.path.isdir(folder_save): #判斷資料夾是否存在
            os.makedirs(folder_save) #新增資料夾
        result.to_csv(folder_save+"\\stock_"+number+".csv", encoding='utf_8-sig', index = False) #存檔

def csv_data(path,number,html_path,group):
    Path = path+"\\"+group
    for i in range(0,len(os.listdir(html_path))):
        folder = (os.listdir(html_path)[i])
        Path_CSV = Path+"\\"+folder+"\\"+number

        files = glob(Path_CSV+"\\計算\\stock_"+number+".csv")
        df = pd.concat(
                (pd.read_csv(file,header=0, usecols=['應收帳款淨額 Accounts receivable, net',
                                                    '流動資產合計 Total current assets',
                                                    '流動負債合計 Total current liabilities',
                                                    '存貨 Current inventories',
                                                    '不動產、廠房及設備 Property, plant and equipment',
                                                    '資產總計　Total assets',
                                                    '負債總計 Total liabilities',
                                                    '歸屬於母公司業主之權益合計 Total equity attributable to owners of parent',
                                                    '非控制權益 Non-controlling interests',
                                                    '本期淨利（淨損）Profit (loss)',
                                                    '營業收入合計　Total operating revenue',
                                                    '營業成本合計　Total operating costs',
                                                    '本期稅前淨利（淨損）　Profit (loss) before tax',
                                                    '營業活動之淨現金流入（流出）Net cash flows from (used in) operating activities',
                                                    '利息費用 Interest expense',
                                                    '股票代碼','股票名稱','股票類別','季']
                                ,dtype={'name': str, 'tweet':str}) for file in files),
                sort=False, ignore_index=True).replace( '[(]','-',  regex=True).replace( '[,]','',  regex=True).replace( '[)]','',  regex=True)
        df.columns = ['應收帳款淨額',
                    '存貨',
                    '流動資產合計',
                    '不動產廠房及設備',
                    '資產總計',
                    '流動負債合計',
                    '負債總計',
                    '歸屬於母公司業主之權益合計',
                    '非控制權益',
                    '營業收入合計',
                    '營業成本合計',
                    '本期淨利',
                    '本期稅前淨利',
                    '利息費用',
                    '營業活動之淨現金流入',
                    '股票代碼','股票名稱','股票類別','季']

        df["流動比率"] = df.流動資產合計.astype(int64) / df.流動負債合計.astype(int64)
        df["流動比率"] = round(df["流動比率"]*100,2) 


        df["速動比率"] = (df.流動資產合計.astype(int64) - df.存貨.astype(int64)) / df.流動負債合計.astype(int64)
        df["速動比率"] = round(df["速動比率"]*100,2) 


        df["利息保障倍數"] = (df.本期稅前淨利.astype(int64) + df.利息費用.astype(int64)) / df.利息費用.astype(int64)
        df["利息保障倍數"] = round(df["利息保障倍數"],2)  


        df["現金流量比率"] = (df.營業活動之淨現金流入.astype(int64)) / df.流動負債合計.astype(int64)
        df["現金流量比率"] = round(df["利息保障倍數"]*100,2)  


        df["總資產週轉率"] = (df.營業收入合計.astype(int64)) / df.資產總計.astype(int64)
        df["總資產週轉率"] = round(df["總資產週轉率"],2)  
        

        df["負債佔資產比率"] = (df.負債總計.astype(int64)) / df.資產總計.astype(int64)
        df["負債佔資產比率"] = round(df["負債佔資產比率"]*100,2)  


        df["純益率"] = (df.本期淨利.astype(int64)) / df.營業收入合計.astype(int64)
        df["純益率"] = round(df["負債佔資產比率"]*100,2)

        if folder == '2019Q4' or folder == '2020Q4':
            folder1 = (os.listdir(html_path)[i-3])
            Path_CSV1 = Path+"\\"+folder1+"\\"+number
            df1 = pd.read_csv(Path_CSV1+"\\計算\\stock_"+number+".csv")
            a1 = (df1.本期淨利.astype(int64))

            folder2 = (os.listdir(html_path)[i-2])
            Path_CSV2 = Path+"\\"+folder2+"\\"+number
            df2 = pd.read_csv(Path_CSV2+"\\計算\\stock_"+number+".csv")
            a2 = (df2.本期淨利.astype(int64))

            folder3 = (os.listdir(html_path)[i-1])
            Path_CSV3 = Path+"\\"+folder3+"\\"+number
            df3 = pd.read_csv(Path_CSV3+"\\計算\\stock_"+number+".csv")
            a3 = (df3.本期淨利.astype(int64))

            a = (df.本期淨利.astype(int64))
            a = (a-a1-a2-a3)
            df["ROE"] = a / (df.歸屬於母公司業主之權益合計.astype(int64)-df.非控制權益.astype(int64))
            df["ROE"] = round(df["ROE"]*100,2) 
        else:
            df["ROE"] = df.本期淨利.astype(int64) / (df.歸屬於母公司業主之權益合計.astype(int64)-df.非控制權益.astype(int64))
            df["ROE"] = round(df["ROE"]*100,2) 
        df.to_csv(Path_CSV+"\\計算\\stock_"+number+".csv", encoding="utf_8-sig", index = False)

def calculate(path,number,html_path,group):
    Path = path+"\\"+group
    for i in range(0,len(os.listdir(html_path))):
        folder = (os.listdir(html_path)[i])
        Path_CSV = Path+"\\"+folder+"\\"+number
        df = pd.read_csv(Path_CSV+"\\計算\\stock_"+number+".csv")

        if folder == '2019Q1':#df['應收款項週轉率'] = d
            a = 0
            b = 0
        elif folder == '2019Q4' or folder == '2020Q4':
            folder1 = (os.listdir(html_path)[i-3])
            Path_CSV1 = Path+"\\"+folder1+"\\"+number
            df1 = pd.read_csv(Path_CSV1+"\\計算\\stock_"+number+".csv")
            a1 = (df1.營業收入合計.astype(int64))

            folder2 = (os.listdir(html_path)[i-2])
            Path_CSV2 = Path+"\\"+folder2+"\\"+number
            df2 = pd.read_csv(Path_CSV2+"\\計算\\stock_"+number+".csv")
            a2 = (df2.營業收入合計.astype(int64))

            folder3 = (os.listdir(html_path)[i-1])
            Path_CSV3 = Path+"\\"+folder3+"\\"+number
            df3 = pd.read_csv(Path_CSV3+"\\計算\\stock_"+number+".csv")
            a3 = (df3.營業收入合計.astype(int64))

            a = (df.營業收入合計.astype(int64))
            b = (df.應收帳款淨額.astype(int64))
            a = (a-a1-a2-a3)
        else:
            a = (df.營業收入合計.astype(int64))
            b = (df.應收帳款淨額.astype(int64))
        folder_before = (os.listdir(html_path)[i-1])
        Path_CSV_before = Path+"\\"+folder_before+"\\"+number
        df_before = pd.read_csv(Path_CSV_before+"\\計算\\stock_"+number+".csv")

        c = (df_before.應收帳款淨額.astype(int64))
        d = a/((b+c)/2)
        d = round(d,2)

        if folder == '2019Q1':#df['固定資產週轉率'] = e
            a = 0
            b = 0
        elif folder == '2019Q4' or folder == '2020Q4':
            folder1 = (os.listdir(html_path)[i-3])
            Path_CSV1 = Path+"\\"+folder1+"\\"+number
            df1 = pd.read_csv(Path_CSV1+"\\計算\\stock_"+number+".csv")
            a1 = (df1.營業收入合計.astype(int64))

            folder2 = (os.listdir(html_path)[i-2])
            Path_CSV2 = Path+"\\"+folder2+"\\"+number
            df2 = pd.read_csv(Path_CSV2+"\\計算\\stock_"+number+".csv")
            a2 = (df2.營業收入合計.astype(int64))

            folder3 = (os.listdir(html_path)[i-1])
            Path_CSV3 = Path+"\\"+folder3+"\\"+number
            df3 = pd.read_csv(Path_CSV3+"\\計算\\stock_"+number+".csv")
            a3 = (df3.營業收入合計.astype(int64))

            a = (df.營業收入合計.astype(int64))
            b = (df.不動產廠房及設備.astype(int64))
            a = (a-a1-a2-a3)
        else:
            a = (df.營業收入合計.astype(int64))
            b = (df.不動產廠房及設備.astype(int64))
        
        folder_before = (os.listdir(html_path)[i-1])
        Path_CSV_before = Path+"\\"+folder_before+"\\"+number
        df_before = pd.read_csv(Path_CSV_before+"\\計算\\stock_"+number+".csv")
        c = (df_before.不動產廠房及設備.astype(int64))
        e = a/((b+c)/2)
        e = round(e,2)
        if folder == '2019Q1':#df['存貨週轉率'] = f
            a = 0
            b = 0
        elif folder == '2019Q4' or folder == '2020Q4':
            folder1 = (os.listdir(html_path)[i-3])
            Path_CSV1 = Path+"\\"+folder1+"\\"+number
            df1 = pd.read_csv(Path_CSV1+"\\計算\\stock_"+number+".csv")
            a1 = (df1.營業成本合計.astype(int64))

            folder2 = (os.listdir(html_path)[i-2])
            Path_CSV2 = Path+"\\"+folder2+"\\"+number
            df2 = pd.read_csv(Path_CSV2+"\\計算\\stock_"+number+".csv")
            a2 = (df2.營業成本合計.astype(int64))

            folder3 = (os.listdir(html_path)[i-1])
            Path_CSV3 = Path+"\\"+folder3+"\\"+number
            df3 = pd.read_csv(Path_CSV3+"\\計算\\stock_"+number+".csv")
            a3 = (df3.營業成本合計.astype(int64))
            
            a = (df.營業成本合計.astype(int64))
            b = (df.存貨.astype(int64))
            a = (a-a1-a2-a3)
        else:
            a = (df.營業成本合計.astype(int64))
            b = (df.存貨.astype(int64))
            
        folder_before = (os.listdir(html_path)[i-1])
        Path_CSV_before = Path+"\\"+folder_before+"\\"+number
        df_before = pd.read_csv(Path_CSV_before+"\\計算\\stock_"+number+".csv")

        c = (df_before.存貨.astype(int64))
        f = a/((b+c)/2)
        f = round(f,2)

        files = glob(Path_CSV+"\\計算\\stock_"+number+".csv") #取得資料夾內需要的資料
        
        df = pd.concat(
                (pd.read_csv(file,header=0, usecols=['應收帳款淨額',
                    '存貨',
                    '流動資產合計',
                    '不動產廠房及設備',
                    '資產總計',
                    '流動負債合計',
                    '負債總計',
                    '歸屬於母公司業主之權益合計',
                    '非控制權益',
                    '營業收入合計',
                    '營業成本合計',
                    '本期淨利',
                    '本期稅前淨利',
                    '利息費用',
                    '營業活動之淨現金流入',
                    '股票代碼','股票名稱','股票類別','季','流動比率','速動比率','利息保障倍數','現金流量比率','總資產週轉率','負債佔資產比率','純益率','ROE']
                                ,dtype={'name': str, 'tweet':str}) for file in files),
                sort=False, ignore_index=True).replace( '[(]','-',  regex=True).replace( '[,]','',  regex=True).replace( '[)]','',  regex=True)
        df.columns = ['應收帳款淨額',
                    '存貨',
                    '流動資產合計',
                    '不動產廠房及設備',
                    '資產總計',
                    '流動負債合計',
                    '負債總計',
                    '歸屬於母公司業主之權益合計',
                    '非控制權益',
                    '營業收入合計',
                    '營業成本合計',
                    '本期淨利',
                    '本期稅前淨利',
                    '利息費用',
                    '營業活動之淨現金流入',
                    '股票代碼','股票名稱','股票類別','季','流動比率','速動比率','利息保障倍數','現金流量比率','總資產週轉率','負債佔資產比率','純益率','ROE']
        df['應收款項週轉率'] = d
        df['固定資產週轉率'] = e
        df['存貨週轉率'] = f
        
        df.to_csv(Path_CSV+"\\計算\\stock_"+number+".csv", encoding="utf_8-sig", index = False)

def calculate_4(path,number,html_path,group):
    Path = path+"\\"+group
    for i in range(0,len(os.listdir(html_path))):
        folder = (os.listdir(html_path)[i])
        Path_CSV = Path+"\\"+folder+"\\"+number
        df = pd.read_csv(Path_CSV+"\\計算\\stock_"+number+".csv")

        if folder == '2019Q1' or folder == '2019Q2' or folder == '2019Q3' or folder == '2019Q4' or folder == '2020Q1' or folder == '2020Q2' or folder == '2020Q3' or folder == '2020Q4' or folder == '2021Q1' or folder == '2021Q2' or folder == '2021Q3':
            folder1 = (os.listdir(html_path)[i-1])
            Path_CSV1 = Path+"\\"+folder1+"\\"+number
            df1 = pd.read_csv(Path_CSV1+"\\計算\\stock_"+number+".csv")
            g1 = (df1.ROE.astype(int64))

            folder2 = (os.listdir(html_path)[i-2])
            Path_CSV2 = Path+"\\"+folder2+"\\"+number
            df2 = pd.read_csv(Path_CSV2+"\\計算\\stock_"+number+".csv")
            g2 = (df2.ROE.astype(int64))

            folder3 = (os.listdir(html_path)[i-3])
            Path_CSV3 = Path+"\\"+folder3+"\\"+number
            df3 = pd.read_csv(Path_CSV3+"\\計算\\stock_"+number+".csv")
            g3 = (df3.ROE.astype(int64))

            g = (df.ROE.astype(int64))
            g = (g+g1+g2+g3)

            df['ROE_近四季'] = g

        df.to_csv(Path_CSV+"\\計算\\stock_"+number+".csv", encoding="utf_8-sig", index = False)

def csv_db(path,html_path,number,group):
    Path = path+"\\"+group
    for i in range(0,len(os.listdir(html_path))):
        folder = (os.listdir(html_path)[i])
        Path_CSV = Path+"\\"+folder+"\\"+number
        sql_data = path+"\\DB\\"

        if not os.path.isdir(sql_data):
            os.makedirs(sql_data)

        conn = sqlite3.connect(path+"\\DB\\Stock.db")
        df = pd.read_csv(Path_CSV+"\\計算\\stock_"+number+".csv", encoding="utf_8-sig")
        df.to_sql("Stock", conn, if_exists="append", index=False)
        