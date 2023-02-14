from flask import Flask, request
from nutrition import nutrition_driver 
app = Flask(__name__)

@app.route('/nutriition/', methods=['GET','POST'])
def Nutrition():
    if request.form:
        nutrition_driver()

