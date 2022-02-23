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

def get_data(path,number,group,s):
    df = pd.read_html("D:\\資料庫\\台股\\html\\上市\\"+s+"\\"+number+".html")

    folder = ""+path+group+"\\"+s+"\\"+number+"\\"
    if not os.path.isdir(folder):
        os.makedirs(folder)

    df[0].to_csv(path+group+"\\"+s+"\\"+number+"\\"+number+"_1.csv",header=0, encoding= "utf_8_sig")
    df[1].to_csv(path+group+"\\"+s+"\\"+number+"\\"+number+"_2.csv",header=0, encoding= "utf_8_sig")
    df[2].to_csv(path+group+"\\"+s+"\\"+number+"\\"+number+"_3.csv",header=0, encoding= "utf_8_sig")

def combine_all_data(path,number,name,group,s):

    for i in range(1,4):
        #取得csv檔案位置
        a = str(i)
        df = pd.read_csv(path+group+"\\"+s+"\\"+number+"\\"+number+"_"+a+".csv", encoding= "utf_8_sig")
        #取得csv表格列數
        num = (len(df.columns))+1
        #整個轉為list
        df = df.values.tolist()
        #設定一個空陣列，放置列數
        num_list = []
        for i in range(1, num):
            num_list += [i]
        #將陣列從int轉str
        num_list = [str(i) for i in num_list]
        df = pd.DataFrame(columns = num_list, data = df)
        #刪除num_list陣列的3、4
        del num_list[2]
        del num_list[2]
        #刪除不需要的資料
        df = df.drop(num_list,axis=1)
        #把 Dataframe 轉成 2D numpy array
        data = df.values
        #找到數據的 key
        index1 = list(df.keys())
        #行列互換，再利用map函數將zip內的元組轉列表
        data = list(map(list, zip(*data)))
        data = pd.DataFrame(data, index=index1)
        #存檔
        data.to_csv(path+group+"\\"+s+"\\"+number+"\\"+number+"_new_"+a+".csv",header=0, encoding= "utf_8_sig")

    files = glob(path+group+"\\"+s+"\\"+number+"\\"+number+"_new_1.csv")
    df = pd.concat(
            (pd.read_csv(file,header=0, usecols=['3','流動資產合計 Total current assets','流動負債合計 Total current liabilities',
                                                 '存貨 Current inventories','不動產、廠房及設備 Property, plant and equipment',
                                                 '資產總計　Total assets','負債總計 Total liabilities']
                                                 ,dtype={'name': str, 'tweet':str}) for file in files), sort=False, ignore_index=True)
    #存檔
    df.to_csv(path+group+"\\"+s+"\\"+number+"\\"+number+"_getnum_1.csv", encoding= "utf_8_sig", index = False)

    files = glob(path+group+"\\"+s+"\\"+number+"\\"+number+"_new_2.csv")
    df = pd.concat(
            (pd.read_csv(file,header=0, usecols=['3','本期淨利（淨損）Profit (loss)','營業收入合計　Total operating revenue']
                            ,dtype={'name': str, 'tweet':str}) for file in files), sort=False, ignore_index=True).replace( '[(]','-',  regex=True).replace( '[,]','',  regex=True).replace( '[)]','',  regex=True)
    #存檔
    df.to_csv(path+group+"\\"+s+"\\"+number+"\\"+number+"_getnum_2.csv", encoding= "utf-8-sig", index = False)
    

    files = glob(path+group+"\\"+s+"\\"+number+"\\"+number+"_new_3.csv")
    df = pd.concat(
            (pd.read_csv(file,header=0, usecols=['3','本期稅前淨利（淨損）　Profit (loss) before tax','利息費用 Interest expense','營業活動之淨現金流入（流出）Net cash flows from (used in) operating activities']
                            ,dtype={'name': str, 'tweet':str}) for file in files), sort=False, ignore_index=True).replace( '[(]','-',  regex=True).replace( '[,]','',  regex=True).replace( '[)]','',  regex=True)
    
    #存檔
    df.to_csv(path+group+"\\"+s+"\\"+number+"\\"+number+"_getnum_3.csv", encoding= "utf-8-sig", index = False)
    
    #取得資料夾內所有資料
    files = glob(path+group+"\\"+s+"\\"+number+"\\"+number+"_getnum_*.csv")
    #串列中包含兩個Pandas DataFrame
    df_list = [pd.read_csv(file) for file in files]
    result = pd.merge(df_list[0],df_list[1], on='3')
    result = pd.merge(result,df_list[2],on='3')
    #新增股票代碼
    result["股票代碼"] = number 
    #新增股票名稱
    result["股票名稱"] = name
    #新增季
    result["季"] = s
    # 查詢是否已有資料夾，無資料夾則新增一個
    folder = ""+path+group+"\\"+s+"\\計算"
    if not os.path.isdir(folder):
        os.makedirs(folder)
    #存檔
    
    result.to_csv(path+group+"\\"+s+"\\計算\\stock_"+number+".csv", encoding='utf-8-sig', index = False)

def csv_db(group_name,path,s):
    files = glob(path+group_name+"\\"+s+"\\計算\\stock_*.csv")
    df = pd.concat(
            (pd.read_csv(file,header=0, usecols=['流動資產合計 Total current assets','流動負債合計 Total current liabilities',
                                                 '存貨 Current inventories','本期稅前淨利（淨損）　Profit (loss) before tax',
                                                 '營業活動之淨現金流入（流出）Net cash flows from (used in) operating activities',
                                                 '不動產、廠房及設備 Property, plant and equipment',
                                                 '資產總計　Total assets','負債總計 Total liabilities','本期淨利（淨損）Profit (loss)',
                                                 '營業收入合計　Total operating revenue','利息費用 Interest expense','股票代碼', '股票名稱','季']
                            ,dtype={'name': str, 'tweet': str}) for file in files), sort=False, ignore_index=True).replace( '[(]','-',  regex=True).replace( '[,]','',  regex=True).replace( '[)]','',  regex=True)
                           
    df.columns = ['存貨','流動資產合計','不動產、廠房及設備','資產總計','流動負債合計','負債總計','營業收入合計',
                  '本期淨利（淨損）','本期稅前淨利（淨損）','利息費用','營業活動之淨現金流入（流出）','股票代碼','股票名稱','季']
    df.to_csv(path+"Sort_All\\"+s+"\\"+group_name+".csv", encoding="utf_8-sig", index = False)
    
    conn = sqlite3.connect(path+"DB\\"+s+"\\"+group_name+".db")
    df = pd.read_csv(path+"Sort_All\\"+s+"\\"+group_name+".csv", encoding="utf_8-sig")
    df.to_sql("sort_All", conn, if_exists="append", index=False, dtype={ "本期淨利（淨損）": "float64", "本期稅前淨利（淨損）": "float64", "營業活動之淨現金流入（流出）": "float64"
    })
