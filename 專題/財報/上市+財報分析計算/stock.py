import get_data as gd

path = 'D:\\資料庫\\台股\\上市'
html_path = 'D:\\資料庫\\台股\\html\\上市'

slist = gd.get_stocknumber()
cnt = len(slist)
for i in range(cnt):
    number,name,group = slist[i]
    try:
        gd.read_folder_saveCSV(path,html_path,number,group)
        gd.combine_all_data(path,html_path,number,name,group)
        gd.csv_data(path,number,html_path,group)
        gd.calculate(path,number,html_path,group)
        gd.calculate_4(path,number,html_path,group)
        gd.csv_db(path,html_path,number,group)
        print(number + "\t Success")
    except:
        pass