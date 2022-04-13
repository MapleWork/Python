import sqlite3
from turtle import pen

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

from Stock_Widget.models import User, Post


@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        languages = []

        with open('stock_number.csv', encoding="utf-8") as f: 
            slist = f.readlines() 

            for lst in slist: 
                s = lst.split(',') 
                # print(s[0] + "\t").strip()
                languages.append("{}".format(s[0].strip()))
                # languages.append("{} {} {}".format(s[0].strip(), s[1].strip(), s[2].strip()))

        keyword = request.args.get('ID')
        
        print(keyword)
        try:
            conn = sqlite3.connect('Stock.db')
            sql = "SELECT 股票代碼, 股票名稱, 股票類別, 季, ROE FROM Stock WHERE 股票代碼=" + str(keyword)
            cursor = conn.cursor()
            cursor.execute(sql)
            content = cursor.fetchall()
            field_name = [i[0] for i in cursor.description]

            cursor.execute(sql)
            sql = cursor.fetchall()
            
            stock_name = "SELECT 股票名稱 FROM Stock WHERE 股票代碼 = " + str(keyword)
            cursor.execute(stock_name)
            stock_name = cursor.fetchall()
            for i in range(1):
                name = stock_name[i][0]
            
            roe_res = []
            for i in range(11):
                roe = sql[i][4]
                roe_res.append(roe)
                
            season_res = []
            for i in range(11):
                season = sql[i][3]
                season_res.append(season)
                
            c = (
                Line(init_opts=opts.InitOpts(width="800px",height='300px'))
                # https://tw511.com/a/01/32805.html 設定版面大小
                .add_xaxis(season_res)
                .add_yaxis("ROE", roe_res, areastyle_opts=opts.AreaStyleOpts(opacity=0.3),color = "#FFA500",symbol_size=10)
                # https://www.796t.com/article.php?id=411538 圓心設定
                .set_series_opts(label_opts = opts.LabelOpts(color="#000000",font_size="15"))
                .set_global_opts(title_opts=opts.TitleOpts(title=keyword+" "+name+"  報酬率與季收盤價比較圖"),
                xaxis_opts = opts.AxisOpts(name="Season"),
                yaxis_opts = opts.AxisOpts(name="ROE"),
                )
                )
            data_plot = c.render_embed()
            
            conn = sqlite3.connect('Stock.db')
            sql2 = "SELECT 股票代碼, 股票名稱, 股票類別, 季, ROE_近四季 FROM Stock WHERE 股票代碼=" + str(keyword)
            cursor = conn.cursor()
            cursor.execute(sql2)
            content2 = cursor.fetchall()
            field_name2 = [i[0] for i in cursor.description]

            cursor.execute(sql2)
            sql2 = cursor.fetchall()

            roe_res_four = []
            for i in range(11):
                roe = sql2[i][4]
                roe_res_four.append(roe)
            
                
            # for i in range(11):
            #     if i == 0:
            #         roe = round(sql[i][4],2)
            #         roe_res_four.append(roe)

            #     elif i ==1:
            #         roe = round(sql[i][4]+sql[i-1][4],2)
            #         roe_res_four.append(roe)

            #     elif i ==2:
            #         roe = round(sql[i][4]+sql[i-1][4]+sql[i-2][4],2)
            #         roe_res_four.append(roe)

            #     else:
            #         roe = round(sql[i][4]+sql[i-1][4]+sql[i-2][4]+sql[i-3][4],2)
            #         roe_res_four.append(roe)

            d = (
                Line(init_opts=opts.InitOpts(width="800px",height='300px'))
                # https://tw511.com/a/01/32805.html 設定版面大小
                .add_xaxis(season_res)
                .add_yaxis("ROE", roe_res_four, areastyle_opts=opts.AreaStyleOpts(opacity=0.3),color = "#FFA500",symbol_size=10)
                # https://www.796t.com/article.php?id=411538 圓心設定
                .set_series_opts(label_opts = opts.LabelOpts(color="#000000",font_size="15"))
                .set_global_opts(title_opts=opts.TitleOpts(title=keyword+" "+name+"  報酬率與季收盤價比較圖"),
                xaxis_opts = opts.AxisOpts(name="Season"),
                yaxis_opts = opts.AxisOpts(name="ROE"),
                )
            )

            data_plot_d = d.render_embed()

            roe_res_year = []
            for i in range(11):
                if i == 4 or i == 8 or i == 12:
                    roe = round(sql[i][4]+sql[i-1][4]+sql[i-2][4]+sql[i-3][4],2)
                    roe_res_year.append(roe)
                    
            year = ['2019','2020','2021']

            y = (
                Line(init_opts=opts.InitOpts(width="800px",height='300px'))
                # https://tw511.com/a/01/32805.html 設定版面大小
                .add_xaxis(year)
                .add_yaxis("ROE", roe_res_year, areastyle_opts=opts.AreaStyleOpts(opacity=0.3),color = "#FFA500",symbol_size=10)
                # https://www.796t.com/article.php?id=411538 圓心設定
                .set_series_opts(label_opts = opts.LabelOpts(color="#000000",font_size="15"))
                .set_global_opts(title_opts=opts.TitleOpts(title=keyword+" "+name+"  報酬率與季收盤價比較圖"),
                xaxis_opts = opts.AxisOpts(name="Season"),
                yaxis_opts = opts.AxisOpts(name="ROE"),
                )
            )
            data_plot_y = y.render_embed()
            
            # return render_template('home.html', languages=languages, labels=field_name, content=content)
            return render_template('home.html',languages=languages, labels2 = field_name2, content2 = content2, labels=field_name, content=content, stock = keyword, data_plot = data_plot, data_plot_d = data_plot_d, roe_res_four = roe_res_four, data_plot_y=data_plot_y)
        except:
            return render_template('home.html', languages=languages)


@app.route("/calculate", methods=['GET','POST'])
def calculate():
    if request.method == "GET":
        languages = []

        with open('stock_number.csv', encoding="utf-8") as f: 
            slist = f.readlines() 

            for lst in slist: 
                s = lst.split(',') 
                languages.append("{}".format(s[2].strip()))

        ID = request.args.get('ID')
        
        print(ID)

        conn = sqlite3.connect('Stock.db')
        cur = conn.cursor()

        if ID == None:
            sql = "SELECT 股票類別, 股票代碼, 股票名稱, ROE, 流動比率, 速動比率, 利息保障倍數, 現金流量比率, 應收款項週轉率, 固定資產週轉率, 存貨週轉率, 總資產週轉率, 負債佔資產比率, 純益率 FROM Stock WHERE 季 = '2021Q3' ORDER BY ROE DESC"
            cur.execute(sql)
            content = cur.fetchall()
            field_name = [i[0] for i in cur.description]

        else:
            sql = "SELECT 股票類別, 股票代碼, 股票名稱, ROE, 流動比率, 速動比率, 利息保障倍數, 現金流量比率, 應收款項週轉率, 固定資產週轉率, 存貨週轉率, 總資產週轉率, 負債佔資產比率, 純益率  FROM Stock WHERE 季 = '2021Q3' AND 股票類別='{}' ORDER BY ROE DESC".format(ID)
            cur.execute(sql)
            content = cur.fetchall()
            field_name = [i[0] for i in cur.description]

        if ID == None:
            sql = "SELECT 季, 股票類別, 股票代碼, 股票名稱, ROE_近四季 FROM Stock"
            cur.execute(sql)
            content1 = cur.fetchall()
            field_name1 = [i[0] for i in cur.description]
        
        else:
            sql = "SELECT 季, 股票類別, 股票代碼, 股票名稱, ROE_近四季 FROM Stock WHERE 股票類別='{}'".format(ID)
            cur.execute(sql)
            content1 = cur.fetchall()
            field_name1 = [i[0] for i in cur.description]

        return render_template('calculate.html', content=content, labels=field_name, content1=content1, labels1=field_name1, languages=languages)

    return render_template('calculate.html')

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


