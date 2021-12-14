import pandas as pd
import os
from glob import glob
import sqlite3
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
def get_data(path,number,group):
    df = pd.read_html(path+"\\html\\"+number+".html")

    folder = ""+path+group+"\\"+number+"\\"
    if not os.path.isdir(folder):
        os.makedirs(folder)

    df[0].to_csv(path+group+"\\"+number+"\\"+number+"_1.csv",header=0, encoding= "utf_8_sig")
    df[1].to_csv(path+group+"\\"+number+"\\"+number+"_2.csv",header=0, encoding= "utf_8_sig")
def combine_all_data(path,number,name,group):

    df = pd.read_csv(path+group+"\\"+number+"\\"+number+"_1.csv", encoding= "utf_8_sig")

    num = (len(df.columns))+1

    df = df.values.tolist()

    num_list = []
    for i in range(1, num):
        num_list += [i]

    num_list = [str(i) for i in num_list]
    df = pd.DataFrame(columns = num_list, data = df)

    del num_list[2]
    del num_list[2]

    df = df.drop(num_list,axis=1)

    data = df.values

    index1 = list(df.keys())
    data = list(map(list, zip(*data)))
    data = pd.DataFrame(data, index=index1)

    data.to_csv(path+group+"\\"+number+"\\"+number+"_new_1.csv",header=0, encoding= "utf_8_sig")

    df = pd.read_csv(path+group+"\\"+number+"\\"+number+"_2.csv", encoding= "utf_8_sig")

    num = (len(df.columns))+1

    df = df.values.tolist()

    num_list = []
    for i in range(1, num):
        num_list += [i]

    num_list = [str(i) for i in num_list]
    df = pd.DataFrame(columns = num_list, data = df)

    del num_list[2]
    del num_list[2]

    df = df.drop(num_list,axis=1)
    data = df.values 
    index1 = list(df.keys())

    data = list(map(list, zip(*data)))
    data = pd.DataFrame(data, index=index1)

    data.to_csv(path+group+"\\"+number+"\\"+number+"_new_2.csv",header=0, encoding= "utf_8_sig")
    files = glob(path+group+"\\"+number+"\\"+number+"_new_*.csv")

    df_list = [pd.read_csv(file) for file in files]  
    result = pd.merge(df_list[0], df_list[1], on='3')

    result["股票代碼"] = number 
    result["股票名稱"] = name   

    folder = ""+path+group+"\\排序"
    if not os.path.isdir(folder):
        os.makedirs(folder)

    result.to_csv(path+group+"\\排序\\stock_"+number+".csv", encoding='utf_8-sig')

def csv_db(group_name,path):
    files = glob(path+group_name+"\\排序\\stock_*.csv")
    df = pd.concat(
            (pd.read_csv(file,header=0, usecols=['資產總計　Total assets','繼續營業單位稅前淨利（淨損）Profit (loss) from continuing operations before tax',
                                        '營業收入合計　Total operating revenue','營業外收入及支出合計　Total non-operating income and expenses',
                                        '營業毛利（毛損）Gross profit (loss) from operations','負債及權益總計　Total liabilities and equity','本期淨利（淨損）Profit (loss)','股票代碼', '股票名稱']
                            ,dtype={'name': str, 'tweet':str}) for file in files), sort=False, ignore_index=True)
    df.columns = ['資產總額','稅前淨利（淨損）','營業收入合計','營業外收入及支出合計','營業毛利（毛損）','權益總額','本期淨利（淨損）','股票代碼','股票名稱']
    df.to_csv(path+"Sort_All\\"+group_name+".csv", encoding="utf_8-sig", index = False)
    
    conn = sqlite3.connect("D:\\Flask\\"+group_name+"財報排行.db")
    df = pd.read_csv(path+"Sort_All\\"+group_name+".csv", encoding="utf_8-sig")
    df.to_sql("sort_All", conn, if_exists="append", index=False)
