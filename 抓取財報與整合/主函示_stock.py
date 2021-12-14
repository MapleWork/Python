import get_data as gd
import time
path = 'D:\\資料庫\\台股\\'
group_name = '資訊服務業'


slist = gd.get_stocknumber()
cnt = len(slist)
for i in range(cnt):
    number,name,group = slist[i]
    if group == group_name:
        gd.get_data(path,number,group)
        gd.combine_all_data(path,number,name,group)
        print(number + "\t Success")
gd.csv_db(group_name,path)
