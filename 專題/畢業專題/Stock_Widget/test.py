import pandas as pd

list=[[1,2,3],[4,5,6],[7,9,9]]
# 下面這行代碼運行報錯
# list.to_csv('e:/testcsv.csv',encoding='utf-8')
name=['one','two','three']
test=pd.DataFrame(columns=name,data=list)#數據有三列，列名分別爲one,two,three
print(test)
test.to_csv('testcsv.csv',encoding='gbk')