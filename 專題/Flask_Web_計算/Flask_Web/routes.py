import os
import sqlite3
import psycopg2

from flask import jsonify

from flask import flash
from flask import request
from flask import url_for
from flask import redirect
from flask import render_template
from soupsieve import escape

from Flask_Web.forms import LoginForm
from Flask_Web.forms import RegistrationForm

from Flask_Web import db
from Flask_Web import app
from Flask_Web import bcrypt

from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user
from flask_login import login_required

from Flask_Web.models import User, Post

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

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

    return render_template('home.html')
