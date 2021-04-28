from flask import Flask, session, redirect, url_for, request, render_template
from markupsafe import escape
 
app = Flask(__name__)

 
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/ksu1", methods=['POST']) 
def move_forward1(): 
    forward_message = "Forward to ..." 
    return redirect('https://en.wikipedia.org/wiki/Taiwan_Miracle')
 
@app.route("/ksu2", methods=['POST']) 
def move_forward2():  
    forward_message = "Forward to ..." 
    return redirect('https://www.ecoflex-experience.com/the-right-solution-to-sightsee-in-japan/')
 
@app.route("/ksu3", methods=['POST']) 
def move_forward3(): 
    forward_message = "Forward to ..." 
    return redirect('https://hubpages.com/travel/Exploring-the-City-of-Korean-Drama-A-Travel-in-South-Korea')
