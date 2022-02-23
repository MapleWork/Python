import get_data as gd

path = 'D:\\資料庫\\台股\\個股\\'
season = ['2019Q4','2020Q1','2020Q2','2020Q3','2020Q4']

for s in range(len(season)):
    
    s = season[s]
    slist = gd.get_stocknumber()
    cnt = len(slist)
    for i in range(cnt):
        number,name,group = slist[i]
        try:
            gd.get_data(path,number,group,s)
            gd.combine_all_data(path,number,name,group,s)
            gd.csv_db(group,path,s)
            print(number + "\t Success")
        except:
            pass
            
        
