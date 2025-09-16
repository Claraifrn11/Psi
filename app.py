from flask import Flask, render_template

@app.route('/')
def index():
    return 'Olá Mundo'

@app.route('/contato')
def.contato():
    return "<h1> alba...</h1>"
@app.route(/exemplo)
def exemplo ():
    return render_template('exemplo.html')
@app.route('exemplo2')
def exemplo2():
     return render_template('exemplo2.html')
