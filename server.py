from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)
app.secret_key = 'you will never guess this lol.'

@app.route('/')
def random_num():
    if 'random_num' not in session:
        session['random_num'] = random.randint(1, 100)
    return render_template('index.html')

@app.route('/guess',methods=['POST'])
def guessing():
    if request.form['guess'] == '':
        redirect('/')
    else:
        session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/restart')
def play_again():
    session.clear()
    return redirect('/')

if __name__==('__main__'):
    app.run(debug=True)