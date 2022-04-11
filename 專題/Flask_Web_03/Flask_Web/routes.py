from flask import flash
from flask import request
from flask import url_for
from flask import redirect
from flask import render_template
from flask_wtf import form

from Flask_Web.forms import LoginForm
from Flask_Web.forms import RegistrationForm
from Flask_Web.forms import UpdateAccountForm

from Flask_Web import db
from Flask_Web import app
from Flask_Web import bcrypt

from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user
from flask_login import login_required

import os
import secrets
import sqlite3

from PIL import Image
from Flask_Web.models import User


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    
    output_size = (125,125)
    I = Image.open(form_picture)
    I.thumbnail(output_size)
    I.save(picture_path)

    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been update!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)


@app.route("/fs_rank", methods=['GET', 'POST'])
def fs_rank():
    if request.method == 'GET':
        conn = sqlite3.connect("fs_rank.db")
        cursor = conn.cursor()
        sql="SELECT 股票代碼, 股票名稱, 資產總額, 權益總額, 本期淨利（淨損）, 營業外收入及支出合計, 營業毛利（毛損）, 稅前淨利（淨損）, 營業收入合計 FROM sort_All"
        cursor.execute(sql)
        content = cursor.fetchall()

        field_name = [i[0] for i in cursor.description]
        return render_template('fs_rank.html', labels=field_name, content=content)
    return render_template('home.html')


@app.route("/cement_industry", methods=['GET', 'POST'])
def cement_industry():
    if request.method == 'GET':
        conn = sqlite3.connect("水泥工業財報排行.db")
        cursor = conn.cursor()
        sql="SELECT 股票代碼, 股票名稱, 資產總額, 權益總額, 本期淨利（淨損）, 營業外收入及支出合計, 營業毛利（毛損）, 稅前淨利（淨損）, 營業收入合計 FROM sort_All"
        cursor.execute(sql)
        content = cursor.fetchall()

        field_name = [i[0] for i in cursor.description]
        return render_template('cement_industry.html', labels=field_name, content=content)
    return render_template('home.html')


@app.route("/Semiconductor_industry", methods=['GET', 'POST'])
def Semiconductor_industry():
    if request.method == 'GET':
        conn = sqlite3.connect("DataBase半導體業財務分析資料.db")

        cursor = conn.cursor()
        
        sql="SELECT A1.股票代碼, A1.股票名稱,"\
            "ROUND((A1.流動資產合計/A1.流動負債合計)*100,2) as 流動比率,"\
            "ROUND(((A1.流動資產合計-A1.存貨)/A1.流動負債合計)*100,2) as 速動比率,"\
            "ROUND(((A1.本期稅前淨利（淨損） + A1.利息費用) / A1.利息費用),2) as 利息保障倍數,"\
            "ROUND((A1.營業活動之淨現金流入（流出）/ A1.流動負債合計)*100,2) as 現金流量比率,"\
            "ROUND( A1.營業收入合計/((A1.應收帳款淨額+A2.應收帳款淨額)/2),2) as 應收款項周轉率,"\
            "ROUND((A1.營業收入合計/((A1.存貨+A2.存貨)/2)),2) as 存貨週轉率,"\
            "ROUND( A1.營業收入合計/((A1.不動產、廠房及設備+A2.不動產、廠房及設備)/2),2) as 固定資產周轉率,"\
            "ROUND((A1.營業收入合計/A1.資產總計),2) as 總資產周轉率,"\
            "ROUND((A1.本期淨利（淨損）/(A1.資產總計-A1.負債總計))*100,2) as 股東權益報酬率,"\
            "ROUND((A1.負債總計/A1.資產總計)*100,2) as 負債佔資產比率,"\
            "ROUND((A1.本期淨利（淨損）/A1.營業收入合計)*100,2) as 純益率 FROM sort_2020Q1 A1, sort_2019Q4 A2 WHERE A1.股票代碼 = A2.股票代碼 GROUP BY A1.股票代碼, A1.股票名稱"
 

        cursor.execute(sql)

        content = cursor.fetchall()

        field_name = [i[0] for i in cursor.description]
        return render_template('Semiconductor_industry.html', labels=field_name, content=content)
    return render_template('home.html')