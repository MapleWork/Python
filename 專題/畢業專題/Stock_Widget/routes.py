import sqlite3

from flask import flash
from flask import request
from flask import url_for
from flask import redirect
from flask import render_template

from Stock_Widget.forms import LoginForm
from Stock_Widget.forms import RegistrationForm

from Stock_Widget import db
from Stock_Widget import app
from Stock_Widget import bcrypt 

from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user
from flask_login import login_required

from pyecharts.charts import Line
from pyecharts import options as opts

import os
import csv
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from cmath import nan
from Stock_Widget.models import User, Post

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        languages = []

        with open('stock_number.csv', encoding="utf-8") as f: 
            slist = f.readlines() 

            for lst in slist: 
                s = lst.replace("\u3000", ",")
                s = s.split(',')

                languages.append("{}".format(s[0].strip()))

        keyword = request.args.get('ID')
        
        print(keyword)
        try:
            conn = sqlite3.connect('Stock.db')
            sql = "SELECT 股票代碼, 股票名稱, 類股, 季別, ROE, ROA FROM Stock WHERE 季別>='2019Q1' AND 股票代碼="+str(keyword)+" ORDER BY 季別 DESC"
            cursor = conn.cursor()
            cursor.execute(sql)
            content = cursor.fetchall()
            field_name = [i[0] for i in cursor.description]
            content_none = []
            content_data = []
            count = 0
            judge = 0
            for i in content:
                for j in i:
                    if j == None:
                        content_none.append(count)
                        pass
                count=count+1
            for i in content:
                if judge in content_none:
                    break
                else:
                    for j in i :
                        content_data.append(i)
                        break
                judge = judge +1
            content = content_data
            cursor.execute(sql)
            sql = cursor.fetchall()
            
            stock_name = "SELECT 股票名稱 FROM Stock WHERE 季別>='2019Q1' AND 股票代碼 = "+str(keyword)
            cursor.execute(stock_name)
            stock_name = cursor.fetchall()
            for i in range(1):
                name = stock_name[i][0]
            none_data = []
            roa_res = []
            for i in range(len(stock_name)):
                roa = sql[i][5]
                if roa == None:
                    none_data.append(i)
                    break
                else:
                    roa_res.append(roa)

            roa_res = list(reversed(roa_res))

            roe_res = []
            for i in range(len(stock_name)):
                roe = sql[i][4]
                if roe == None:
                    break
                else:
                    roe_res.append(roe)

            roe_res = list(reversed(roe_res))
                
            season_res = []
            for i in range(len(stock_name)):
                if i in none_data:
                    break
                else:
                    season = sql[i][3]
                    season_res.append(season)

            season_res = list(reversed(season_res))
                
            c = (
                Line(init_opts=opts.InitOpts(width="800px",height='300px'))
                # https://tw511.com/a/01/32805.html 設定版面大小
                .add_xaxis(season_res)
                .add_yaxis("ROA", roa_res, areastyle_opts=opts.AreaStyleOpts(opacity=0.3),color = "#FFA500",symbol_size=10)
                .add_yaxis("ROE", roe_res, areastyle_opts=opts.AreaStyleOpts(opacity=0.3),color = "#00FF00",symbol_size=10)
                # https://www.796t.com/article.php?id=411538 圓心設定
                .set_series_opts(label_opts = opts.LabelOpts(color="#000000",font_size="15"))
                .set_global_opts(title_opts=opts.TitleOpts(title=keyword+" "+name),
                xaxis_opts = opts.AxisOpts(name="Season"),
                yaxis_opts = opts.AxisOpts(name="ROE、ROA"),#https://tw511.com/a/01/32805.html
                )
                )
            data_plot = c.render_embed()

            ####################################################
            
            conn = sqlite3.connect('Stock.db')
            sql2 = "SELECT 股票代碼, 股票名稱, 類股, 季別, 近四季ROE, 近四季ROA FROM Stock WHERE 季別>='2019Q1' AND 股票代碼="+str(keyword)+" ORDER BY 季別 DESC"
            cursor = conn.cursor()
            cursor.execute(sql2)
            content2 = cursor.fetchall()
            field_name2 = [i[0] for i in cursor.description]

            cursor.execute(sql2)
            sql2 = cursor.fetchall()

            content_none = [] #存放空值欄位數字
            content_data = [] #存放不為空值的資料
            count = 0
            judge = 0
            for i in content2: #使用for迴圈將資料一筆一筆列出
                for j in i: #使用for迴圈列出每一個資料
                    if j == None: #if資料為空
                        content_none.append(count) #儲存當前資料的位置
                        break
                count=count+1
            for i in content2:
                if judge in content_none: #如果judge在content_none陣列中
                    pass
                else:
                    for j in i :
                        content_data.append(i)
                        break
                judge = judge +1
            content2 = content_data

            none_data = []
            roa_res_four = []
            for i in range(len(stock_name)):
                roa = sql2[i][5]
                if roa == None:
                    none_data.append(i)
                    break
                else:
                    roa_res_four.append(roa)

            roa_res_four = list(reversed(roa_res_four))

            roe_res_four = []
            for i in range(len(stock_name)):
                roe = sql2[i][4]
                if roe == None:
                    break
                else:
                    roe_res_four.append(roe)

            roe_res_four = list(reversed(roe_res_four))

            season_res = []
            for i in range(len(stock_name)):
                if i in none_data:
                    break
                else:
                    season = sql2[i][3]
                    season_res.append(season)

            season_res = list(reversed(season_res))            

            d = (
                Line(init_opts=opts.InitOpts(width="800px",height='300px'))
                # https://tw511.com/a/01/32805.html 設定版面大小
                .add_xaxis(season_res)
                .add_yaxis("ROA", roa_res_four, areastyle_opts=opts.AreaStyleOpts(opacity=0.3),color = "#FFA500",symbol_size=10)
                .add_yaxis("ROE", roe_res_four, areastyle_opts=opts.AreaStyleOpts(opacity=0.3),color = "#00FF00",symbol_size=10)
                # https://www.796t.com/article.php?id=411538 圓心設定
                .set_series_opts(label_opts = opts.LabelOpts(color="#000000",font_size="15"))
                .set_global_opts(title_opts=opts.TitleOpts(title=keyword+" "+name),
                xaxis_opts = opts.AxisOpts(name="Season"),
                yaxis_opts = opts.AxisOpts(name="ROE、ROA"),
                )
            )

            data_plot_d = d.render_embed()

            ####################################################

            conn = sqlite3.connect('Stock.db')
            sql3 = "SELECT 股票代碼, 股票名稱, 季別, 年度, 年度ROE, 年度ROA FROM Stock WHERE 季別>='2019Q1' AND 股票代碼=" + str(keyword) + " ORDER BY 季別 DESC"
            cursor = conn.cursor()
            cursor.execute(sql3)
            content3 = cursor.fetchall()
            field_name3 = [i[0] for i in cursor.description]

            cursor.execute(sql3)
            sql3 = cursor.fetchall()
            content_none = []
            content_data = []
            count = 0
            judge = 0
            for i in content3:
                for j in i:
                    if j == None:
                        content_none.append(count)
                        break
                count=count+1
            for i in content3:
                if judge in content_none:
                    pass
                else:
                    for j in i :
                        content_data.append(i)
                        break
                judge = judge +1
            content3 = content_data


            none_data = []
            roa_res_year = []

            for i in range(len(stock_name)):
                roa = sql3[i][5]
                if roa == None:
                    none_data.append(i)
                else:
                    roa_res_year.append(roa)

            roa_res_year = list(reversed(roa_res_year)) 

            roe_res_year = []
            for i in range(len(stock_name)):
                roe = sql3[i][4]
                if roe == None:
                    none_data.append(i)
                else:
                    roe_res_year.append(roe)
            
            roe_res_year = list(reversed(roe_res_year))    

            season_res = []
            for i in range(len(stock_name)):
                if i in none_data:
                    pass
                else:
                    season = sql3[i][3]
                    season_res.append(str(season))
            
            season_res = list(reversed(season_res))   

            y = (
                Line(init_opts=opts.InitOpts(width="800px",height='300px'))
                .add_xaxis(season_res)
                .add_yaxis("ROA", roa_res_year, areastyle_opts=opts.AreaStyleOpts(opacity=0.3),color = "#FFA500",symbol_size=10)
                .add_yaxis("ROE", roe_res_year, areastyle_opts=opts.AreaStyleOpts(opacity=0.3),color = "#00FF00",symbol_size=10)
                .set_series_opts(label_opts = opts.LabelOpts(color="#000000",font_size="15"))
                .set_global_opts(title_opts = opts.TitleOpts(title=keyword+" "+name),
                xaxis_opts = opts.AxisOpts(name="Season"),
                yaxis_opts = opts.AxisOpts(name="ROE、ROA"),
                )
            )
            data_plot_y = y.render_embed()

            
            # return render_template('home.html', languages=languages, labels=field_name, content=content)
            return render_template('home.html',languages=languages, labels3 = field_name3, content3 = content3, labels2 = field_name2, content2 = content2, labels=field_name, content=content, stock = keyword, data_plot = data_plot, data_plot_d = data_plot_d, roe_res_four = roe_res_four, data_plot_y=data_plot_y)
        except:
            return render_template('home.html', languages=languages)


@app.route("/calculate", methods=['GET','POST'])
def calculate():
    if request.method == "GET":
        languages = []

        with open('stock_number.csv', encoding="utf-8") as f: 
            slist = f.readlines() 
            for lst in slist: 
                s = lst.replace("\u3000", ",")
                s = s.split(',')

                languages.append("{}".format(s[2].strip()))
        ID = request.args.get('ID')
        print(ID)

        conn = sqlite3.connect('Stock.db')
        cur = conn.cursor()

        if ID == None:
            sql = "SELECT 類股, 股票代碼, 股票名稱, ROE, ROA FROM Stock WHERE 季別 = '2021Q4' ORDER BY ROE DESC"
            cur.execute(sql)
            content = cur.fetchall()
            field_name = [i[0] for i in cur.description]
        else:
            sql = "SELECT 類股, 股票代碼, 股票名稱, ROE, ROA FROM Stock WHERE 季別 = '2021Q4' AND 類股='{}' ORDER BY ROE DESC".format(ID)
            cur.execute(sql)
            content = cur.fetchall()
            field_name = [i[0] for i in cur.description]
        if ID == None:
            sql = "SELECT 季別, 類股, 股票代碼, 股票名稱, 近四季ROE FROM Stock WHERE 季別>'2019Q1'"
            cur.execute(sql)
            content1 = cur.fetchall()
            field_name1 = [i[0] for i in cur.description]
        else:
            sql = "SELECT 季別, 類股, 股票代碼, 股票名稱, 近四季ROE FROM Stock WHERE 季別>'2019Q1' AND 類股='{}'".format(ID)
            cur.execute(sql)
            content1 = cur.fetchall()
            field_name1 = [i[0] for i in cur.description]

        return render_template('calculate.html', content=content, labels=field_name, 
                                                content1=content1, labels1=field_name1, languages=languages)

    return render_template('home.html')


@app.route("/ML")
def ML():
    # 取得使用者輸入的資料
    input_roe =  request.args.get('roe')
    input_eps =  request.args.get('eps')
    input_gross_margin =  request.args.get('gross_margin')
    input_dividend_yield =  request.args.get('dividend_yield')
    # 起始畫面
    if input_roe == None :
        input_roe =10
    if input_eps == None:
        input_eps = 0
    if input_gross_margin == None:
        input_gross_margin = 20
    if input_dividend_yield == None:
        input_dividend_yield = 5
    # 轉換資料型別
    input_roe = float(input_roe)
    input_eps = float(input_eps)
    input_gross_margin = float(input_gross_margin)
    input_dividend_yield = float(input_dividend_yield)


    conn = sqlite3.connect("stock_1.db") # 連接資料庫
    sql = "SELECT 代碼,股票,ROE_5Y,EPS_5Y,毛利率_5Y,現金殖利率 FROM  Result"
    #sql = "SELECT 股票代碼,股票名稱,類股,年度,毛利率,年度ROE,每股盈餘 FROM Stock"#毛利率>20%,每股盈餘>0,ROE>10%
    cursor = conn.cursor()
    cursor.execute(sql)
    content = cursor.fetchall()
    field_name = [i[0] for i in cursor.description]
    content_none = [] # 放置空值資料位置
    content_data = [] # 放置刪除空值後的資料
    count = 0
    judge = 0
    # 確認有空值的資料位置
    for i in content:
        for j in i:
            if j == None:
                content_none.append(count)
                break
        count=count+1
    # 跳過具有空值的位置
    for i in content:
        if judge in content_none:
            pass
        else:
            for j in i :
                content_data.append(i)
                break
        judge = judge +1
    data = content_data
    # 判斷指標label
    sort_label=[]
    for i in range(len(field_name)):
        if i < 2:
            pass
        else:
            sort_label.append(field_name[i])
    sort_label.append('符合數量')
    sort_label.append('正負樣本')
    # 判斷數值
    conn = sqlite3.connect("stock_1.db")
    sql = "SELECT ROE_5Y,EPS_5Y,毛利率_5Y,現金殖利率 FROM  Result"
    #sql = "SELECT 股票代碼,股票名稱,類股,年度,毛利率,年度ROE,每股盈餘 FROM Stock"#毛利率>20%,每股盈餘>0,ROE>10%
    cursor = conn.cursor()
    cursor.execute(sql)
    content = cursor.fetchall()
    content_none = []
    content_data = []
    count = 0
    judge = 0
    for i in content:
        for j in i:
            if j == None:
                content_none.append(count)
                break
        count=count+1
    # print(content_none) #確認none資料位置
    for i in content:
        if judge in content_none:
            pass
        else:
            for j in i :
                content_data.append(i)
                break
        judge = judge +1
    content = content_data
    roe = []
    eps = []
    gross_margin=[] #毛利率
    dividend_yield = [] #現金殖利率
    for i in range(len(content)):
        for j in range(len(content[i])):
            if j == 0:
                if content[i][j] >=input_roe:
                    roe.append(1)
                else:
                    roe.append(0)
            if j == 1:
                if content[i][j] >input_eps:
                    eps.append(1)
                else:
                    eps.append(0)
            if j == 2:
                if content[i][j] >input_gross_margin:
                    gross_margin.append(1)
                else:
                    gross_margin.append(0)
            if j == 3:
                if content[i][j] >input_dividend_yield:
                    dividend_yield.append(1)
                else:
                    dividend_yield.append(0)
        
    content_data = []
    content_data_array = []
    num = 0
    count_num = 0
    match=0 #計算符合的公司
    not_match = 0 #計算不符合的公司
    match_plus = 0 #計算正樣本數量
    match_minus  = 0 #計算負樣本數量
    total = 0 #計算樣本總數
    for i in data:
        total +=1
        content_data=[]
        for j in i:
            
            content_data.append(j)
            num+=1
            if num == len(data[1]):
                content_data_match_count = []
                match_count = 0
                content_data.append(roe[count_num])
                content_data.append(eps[count_num])
                content_data.append(gross_margin[count_num])
                content_data.append(dividend_yield[count_num])
                match_count = roe[count_num]+eps[count_num]+gross_margin[count_num]+dividend_yield[count_num]
                content_data_match_count.append(match_count)
                if match_count >=3:
                    content_data_match_count.append(1)
                    match_plus+=1
                elif match_count <=1:
                    content_data_match_count.append(-1)
                    match_minus+=1
                else:
                    content_data_match_count.append(0)
                if roe[count_num]==1 and eps[count_num] ==1 and gross_margin[count_num]==1 and dividend_yield[count_num]==1:
                    # content_data.append(1) #判斷是否皆符合
                    match+=1
                elif roe[count_num]==0 and eps[count_num] ==0 and gross_margin[count_num]==0 and dividend_yield[count_num]==0:
                    # content_data.append(-1)
                    not_match+=1                    
                # else:
                    # content_data.append(0)
                count_num+=1
                num =0
        name = field_name+sort_label
        content_data_array.append(content_data+content_data_match_count)
        test=pd.DataFrame(columns=name,data=content_data_array)#數據有三列，列名分別爲one,two,three
        #test.to_csv('ROE'+input_roe+'_EPS'+input_eps+'_GM'+input_gross_margin+'_DY'+input_dividend_yield+'.csv', encoding= "utf_8_sig", index = False)
        test.to_csv('testcsv.csv', encoding= "utf_8_sig", index = False)
    return render_template("ML.html",labels = field_name,content=content_data_array,sort_label = sort_label,
                                        roe = input_roe,eps = input_eps,gross_margin = input_gross_margin,
                                        dividend_yield = input_dividend_yield,match=match,not_match = not_match,match_plus = match_plus,match_minus = match_minus,total = total)

@app.route("/dataScience")
def dataScience():
    
    df = pd.read_csv('testcsv.csv', index_col=[0, 1], encoding='utf-8')
    df = df[(df.正負樣本 == 1) | (df.正負樣本 == -1)]


    X = df.drop(['ROE_5Y.1','EPS_5Y.1','毛利率_5Y.1','現金殖利率.1','符合數量','正負樣本'], axis=1)
    y = df['正負樣本']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)


    svc=SVC(C=1000.0)
    svc.fit(X_train, y_train)
    y_pred=svc.predict(X_test)
    print('Model accuracy score with rbf kernel and C=1000.0 : {0:0.4f}'. format(accuracy_score(y_test, y_pred)))


    linear_svc100=SVC(kernel='linear', C=100.0) 
    linear_svc100.fit(X_train, y_train)
    y_pred=linear_svc100.predict(X_test)
    print('Model accuracy score with linear kernel and C=100.0 : {0:0.4f}'. format(accuracy_score(y_test, y_pred)))
    print('Training set score: {:.4f}'.format(linear_svc100.score(X_train, y_train)))
    print('Test set score: {:.4f}'.format(linear_svc100.score(X_test, y_test)))
    Data1 = pd.DataFrame(y_pred)
    Data1.columns = ["答案"]
    Data1.to_csv("Answer.csv", index=False, encoding='utf_8_sig')

    Data2 = pd.DataFrame(X_test)
    Data2.to_csv("Answer_Data.csv", encoding='utf_8_sig')

    File1 = pd.read_csv("Answer.csv")
    File2 = pd.read_csv("Answer_Data.csv")
    Result = pd.concat([File2, File1], axis=1, sort=False)
    Result.to_csv("Test.csv", index=False, encoding='utf_8_sig')

    df = pd.read_csv('Test.csv', encoding='utf-8')
    total = len(df)
    Keyword = request.args.get('True_False')
    print(Keyword)

    TData = df[(df.答案 == 1)]
    TData.to_csv("TData.csv", index=False, encoding='utf_8_sig')
    T_total = len(TData)

    FData = df[(df.答案 == -1)]
    FData.to_csv("FData.csv", index=False, encoding='utf_8_sig')
    F_total = len(FData)

    if Keyword == '正' :        
        with open("TData.csv","r",encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader)
            return render_template('dataScience.html', header=header, rows=reader,total = T_total,A_total = total)
    if Keyword == '負' :
        with open("FData.csv","r",encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader)
            return render_template('dataScience.html', header=header, rows=reader,total = F_total,A_total = total)
    else:
        with open("Test.csv","r",encoding="utf-8") as file:
            data_result = []
            result = []
            reader = csv.reader(file)
            header = next(reader)
            for i in csv.reader(file):
                stock_number = i[0]
                price_data = pd.read_csv('股價.csv')
                count = 0
                for x in price_data['代號']:
                    if str(x) == stock_number:
                        stock_price = (price_data['股價'][count])
                    count += 1
                count_index = 0
                for j in i:
                    if count_index == 2:
                        result.append(stock_price)
                    result.append(j)
                    count_index += 1
                data_result.append(result)
                result = []
            header = ['代碼','股票','股價','ROE_5Y','EPS_5Y','毛利率5Y','現金殖利率','答案']
            true_false_data_array=pd.DataFrame(columns=header,data=data_result)#數據有三列，列名分別爲one,two,three
            true_false_data_array.to_csv("true_false.csv", index = False, encoding='utf_8-sig')
    
    return render_template('dataScience.html', header=header, rows=data_result,A_total = T_total+F_total)

@app.route("/decisionTree")
def decisionTree():
    import os
    import numpy as np 
    import pandas as pd 
    import matplotlib.pyplot as plt 
    import warnings
    warnings.filterwarnings('ignore')
    data = 'testcsv.csv'
    df = pd.read_csv(data)
    df['判斷'] = df['代碼']
    df.to_csv('testcsv.csv', index=False, encoding='utf-8-sig')
    df
    data = 'testcsv.csv'
    df = pd.read_csv(data, index_col='判斷')
    df = df.drop_duplicates(keep='first')
    df.to_csv('testcsv.csv', index=False, encoding='utf-8-sig')
    df
    df['正負樣本'].value_counts()


    X = df.drop(['代碼', '股票', 'ROE_5Y.1', 'EPS_5Y.1', '毛利率_5Y.1', '現金殖利率.1', '符合數量', '正負樣本'], axis=1) 

    y = df['正負樣本']


    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)


    from sklearn.tree import DecisionTreeClassifier


    clf_gini = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=0)

    clf_gini.fit(X_train, y_train)

    y_pred_gini = clf_gini.predict(X_test)


    from sklearn.metrics import accuracy_score

    print('Model accuracy score with criterion gini index: {0:0.4f}'. format(accuracy_score(y_test, y_pred_gini)))


    y_pred_train_gini = clf_gini.predict(X_train)

    y_pred_train_gini


    print('Training-set accuracy score: {0:0.4f}'. format(accuracy_score(y_train, y_pred_train_gini)))


    print('Training set score: {:.4f}'.format(clf_gini.score(X_train, y_train)))

    print('Test set score: {:.4f}'.format(clf_gini.score(X_test, y_test)))


    plt.figure(figsize=(12,8))

    from sklearn import tree

    tree.plot_tree(clf_gini.fit(X_train, y_train), feature_names=X_train.columns)

    import graphviz 

    Data = tree.export_graphviz(clf_gini, out_file=None, feature_names=X_train.columns)   
    Output = graphviz.Source(Data.replace('helvetica', "Microsoft YaHei"), encoding='utf-8')
    Output.format = 'png'
    Output.render("testcsv") 
    Output

    df = X_train.merge(y_train, on='判斷')
    df


    # A類：第一種可能

    # 355 rows × 4 columns
    ROE_5Y = df[(df['ROE_5Y'] <= 10.035)]
    ROE_5Y

    # 290 rows × 4 columns
    Dividend_Yield = ROE_5Y[(ROE_5Y['現金殖利率'] <= 5.045)]
    Dividend_Yield

    Dividend_Yield['代碼'] = Dividend_Yield.index
    Dividend_Yield.to_csv('Class_A.csv', encoding='utf-8-sig')

    A = Dividend_Yield
    A


    # B類：第二種可能

    # 355 rows × 4 columns
    ROE_5Y = df[(df['ROE_5Y'] <= 10.035)]
    ROE_5Y

    # 65 rows × 4 columns
    Dividend_Yield = ROE_5Y[(ROE_5Y['現金殖利率'] >= 5.045)]
    Dividend_Yield

    # 37 rows × 4 columns
    Gross_Margin = Dividend_Yield[(Dividend_Yield['毛利率_5Y'] <= 20.335)]
    Gross_Margin
    len(Gross_Margin)

    Gross_Margin['代碼'] = Gross_Margin.index
    Gross_Margin.to_csv('Class_B.csv', encoding='utf-8-sig')

    B = Gross_Margin
    B

    # 355 rows × 4 columns
    ROE_5Y = df[(df['ROE_5Y'] <= 10.035)]
    ROE_5Y

    # 65 rows × 4 columns
    Dividend_Yield = ROE_5Y[(ROE_5Y['現金殖利率'] >= 5.045)]
    Dividend_Yield

    # 37 rows × 4 columns
    Gross_Margin = Dividend_Yield[(Dividend_Yield['毛利率_5Y'] >= 20.335)]
    Gross_Margin
    len(Gross_Margin)

    Gross_Margin['代碼'] = Gross_Margin.index
    Gross_Margin.to_csv('Class_C.csv', encoding='utf-8-sig')

    C = Gross_Margin
    C

    # D類：第四種可能

    # 246 rows × 4 columns
    ROE_5Y = df[(df['ROE_5Y'] >= 10.035)]
    ROE_5Y

    # 85 rows × 4 columns
    Gross_Margin = ROE_5Y[(ROE_5Y['毛利率_5Y'] <= 19.98)]
    Gross_Margin

    # 41 rows × 4 columns
    Dividend_Yield = Gross_Margin[(Gross_Margin['現金殖利率'] <= 4.905)]
    Dividend_Yield
    # len(Dividend_Yield)

    Dividend_Yield['代碼'] = Dividend_Yield.index
    Dividend_Yield.to_csv('Class_D.csv', encoding='utf-8-sig')

    D = Dividend_Yield
    D


    # E類：第五種可能

    # 246 rows × 4 columns
    ROE_5Y = df[(df['ROE_5Y'] >= 10.035)]
    ROE_5Y

    # 85 rows × 4 columns
    Gross_Margin = ROE_5Y[(ROE_5Y['毛利率_5Y'] <= 19.98)]
    Gross_Margin

    # 44 rows × 4 columns
    Dividend_Yield = Gross_Margin[(Gross_Margin['現金殖利率'] >= 4.905)]
    Dividend_Yield
    len(Dividend_Yield)

    Dividend_Yield['代碼'] = Dividend_Yield.index
    Dividend_Yield.to_csv('Class_E.csv', encoding='utf-8-sig')

    E = Dividend_Yield
    E

    # F類：第四種可能

    # 246 rows × 4 columns
    ROE_5Y = df[(df['ROE_5Y'] >= 10.035)]
    ROE_5Y

    # 161 rows × 4 columns
    Gross_Margin = ROE_5Y[(ROE_5Y['毛利率_5Y'] >= 19.98)]
    Gross_Margin

    Gross_Margin['代碼'] = Gross_Margin.index
    Gross_Margin.to_csv('Class_F.csv', encoding='utf-8-sig')

    F = Gross_Margin
    F


    # 正樣本資料

    True_M = pd.concat([C, E, F])
    True_M['代碼'] = True_M.index
    True_M.to_csv('Possitive Sample Data.csv', encoding='utf-8-sig')
    True_M


    # 負樣本資料

    False_M = pd.concat([A, B, D])
    False_M['代碼'] = False_M.index
    False_M.to_csv('Negative Sample Data.csv', encoding='utf-8-sig')
    False_M


    data = 'testcsv.csv'
    File = pd.read_csv(data)
    File['判斷'] = File['代碼']
    File.to_csv('testcsv.csv', index=False, encoding='utf-8-sig')
    File

    data = 'testcsv.csv'
    File = pd.read_csv(data, index_col='判斷')
    File = File.drop_duplicates(keep='first')
    File.to_csv('testcsv.csv', index=False, encoding='utf-8-sig')
    File

    NSD = pd.read_csv('Negative Sample Data.csv', index_col='判斷', encoding='utf-8-sig')
    PSD = pd.read_csv('Possitive Sample Data.csv', index_col='判斷', encoding='utf-8-sig')

    Result = pd.concat([NSD, PSD])
    Result.to_csv('Result.csv', index=False, encoding='utf-8-sig')

    A = Result[Result['ROE_5Y'] <= 10.035] 
    A = A[A['現金殖利率'] <= 5.045]
    A['備註'] = 'ROE_5Y <= 10.035, 現金殖利率 <= 5.045'
    A

    B = Result[Result['ROE_5Y'] <= 10.035] 
    B = B[B['現金殖利率'] >= 5.045]
    B = B[B['毛利率_5Y'] <= 20.335]
    B['備註'] = 'ROE_5Y <= 10.035, 現金殖利率 >= 5.045, 毛利率_5Y <= 20.335'
    B

    C = Result[Result['ROE_5Y'] <= 10.035] 
    C = C[C['現金殖利率'] >= 5.045]
    C = C[C['毛利率_5Y'] >= 20.335]
    C['備註'] = 'ROE_5Y <= 10.035, 現金殖利率 >= 5.045, 毛利率_5Y >= 20.335'
    C

    D = Result[Result['ROE_5Y'] >= 10.035] 
    D = D[D['毛利率_5Y'] <= 19.98]
    D = D[D['現金殖利率'] <= 4.905]
    D['備註'] = 'ROE_5Y >= 10.035, 現金殖利率 <= 4.905, 毛利率_5Y <= 19.98'
    D

    E = Result[Result['ROE_5Y'] >= 10.035] 
    E = E[E['毛利率_5Y'] <= 19.98]
    E = E[E['現金殖利率'] >= 4.905]
    E['備註'] = 'ROE_5Y >= 10.035, 現金殖利率 >= 4.905, 毛利率_5Y <= 19.98'
    E

    F = Result[Result['ROE_5Y'] >= 10.035] 
    F = F[F['毛利率_5Y'] >= 19.98]
    F['備註'] = 'ROE_5Y >= 10.035, 毛利率_5Y >= 19.98'
    F

    Result = pd.concat([C, E, F, A, B, D])
    Result = Result.reindex(columns=['代碼', "ROE_5Y", "EPS_5Y", "毛利率_5Y", "現金殖利率", "正負樣本", "備註"])

    Result.to_csv('Result.csv', index=False, encoding='utf-8-sig')
    df = pd.read_csv('Result.csv', encoding='utf-8')
    total = len(df)
    Keyword = request.args.get('True_False')
    print(Keyword)

    TData = df[(df.正負樣本 == 1)]
    TData.to_csv("DS_TData.csv", index=False, encoding='utf_8_sig')
    T_total = len(TData)

    FData = df[(df.正負樣本 == -1)]
    FData.to_csv("FData.csv", index=False, encoding='utf_8_sig')
    F_total = len(FData)
    if Keyword == '正' :        
        with open("DS_TData.csv","r",encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader)
            return render_template('dataScience.html', header=header, rows=reader,total = T_total,A_total = total)
    if Keyword == '負' :
        with open("DS_FData.csv","r",encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader)
            return render_template('dataScience.html', header=header, rows=reader,total = F_total,A_total = total)
    else:
        with open("Result.csv","r",encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader)
            
            return render_template('decisionTree.html', header=header,reader = reader,A_total = total)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect( url_for('home') )

    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are now able to log in', 'success')
        return redirect( url_for('login') )
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect( url_for('home') )

    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect( url_for('home') )
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user() 
    return redirect( url_for('home') )

    
@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')


