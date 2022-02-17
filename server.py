from turtle import clear
from flask import Flask, render_template, request, redirect, session # don't forget to import redirect!
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'




@app.route('/')
def index():

    return render_template('index.html')

@app.route('/result')
def show_result():
    name = session['name']
    comment = session['comment']
    language = session['language']
    location = session['dojo_location']
    return render_template('result.html', name= name, comment = comment, language = language, location = location)

@app.route('/count', methods= ['POST'])
def addCount():
    print(request.form)
    session['name'] = request.form['name']
    session['comment'] = request.form['comment']
    session['dojo_location'] = request.form['dojo_location']
    session['language'] = request.form['language']
    return redirect('/result')	 
    
# adding this method
@app.route('/destroy_session')
def show_user():
    session.clear() 
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)