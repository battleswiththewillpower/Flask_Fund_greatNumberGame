from flask import Flask, render_template, request, redirect, session # added request
import random  # import the random module

app = Flask(__name__)
app.secret_key = 'stop forgetting to put a secret key' # set a secret key for security purposes

@app.route('/')                           
def index():
#In the root route, save a random number between 1 and 100 and 
# display a form for the user to guess the number
    if "num" not in session:
        session["num"] = random.randint(1, 100) 		# random number between 1-100
    
    return render_template('index.html') 

@app.route('/guessnumber', methods=['POST'])
def guess_number():
    print(request.form)
    session['guessnumber'] = int(request.form['guessnumber'])
    

    return redirect('/')