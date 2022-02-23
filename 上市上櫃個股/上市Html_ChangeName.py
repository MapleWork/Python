import os

def get_stocknumber():
    res = [] # 存放切割文字結果
    try:
        with open('stock_number.csv', encoding="utf-8") as f: # 開啟csv檔案
            slist = f.readlines() # 以行為單位讀取所有資料
            print('讀入：',slist) # 列印讀取資料
            for lst in slist: # 走訪每一個股票組合
                s = lst.split(',') # 以逗點切割為陣列
                # s = lst.splitlines(',') # 以逗點切割為陣列
                res.append([s[0].strip(),str(s[1].strip()),str(s[2].strip())]) # .strip去除空白，存到res陣列
    except:
        print('讀不到')
    return res

def change_er(path, number):
    for root, dirs, files in os.walk(path):
        for i in files:
            fullpath = os.path.join(root, i)
            filename = os.path.join(i)
            filenumber = '-er-'+number+'-'
            if filenumber in fullpath:
                    if not os.path.isfile(number+".html"):
                        os.rename(filename, number+".html")

def change_cr(path, number):
    for root, dirs, files in os.walk(path):
        for i in files:
            fullpath = os.path.join(root, i)
            filename = os.path.join(i)
            filenumber = '-cr-'+number+'-'
            if filenumber in fullpath:
                    if not os.path.isfile(number+".html"):
                        os.rename(filename, number+".html")

def change_ir(path, number):
    for root, dirs, files in os.walk(path):
        for i in files:
            fullpath = os.path.join(root, i)
            filename = os.path.join(i)
            filenumber = '-ir-'+number+'-'
            if filenumber in fullpath:
                    if not os.path.isfile(number+".html"):
                        os.rename(filename, number+".html")

path = "D:\\資料庫\\台股\\html\\上櫃\\2020Q4"
slist = get_stocknumber()
cnt = len(slist)
for i in range(cnt):
    number,name,group = slist[i]
    change_er(path,number)
    change_cr(path,number)  
    change_ir(path,number)
    print(number)
