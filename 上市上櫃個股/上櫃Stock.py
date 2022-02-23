import get_data as gd

group_name = '橡膠工業'
path = 'D:\\資料庫\\台股\\上櫃\\'
season = ['2019Q4','2020Q1','2020Q2','2020Q3','2020Q4']

for s in range(len(season)):
    
    s = season[s]
    slist = gd.get_stocknumber()
    cnt = len(slist)
    for i in range(cnt):
        number,name,group = slist[i]
        if group == group_name:
            try:
                gd.get_data(path,number,group,s)
                gd.combine_all_data(path,number,name,group,s)
                print(number + "\t Success")
            except:
                pass
            
    gd.csv_db(group_name,path,s)
