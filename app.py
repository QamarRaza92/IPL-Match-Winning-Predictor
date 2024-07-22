from flask import Flask,render_template,url_for,redirect,flash
import pandas as pd 
import numpy as np
import pickle
from form import InputForm


# Pandas version :  2.1.1
# Numpy version :  1.26.0
# Sklearn version :  1.3.2

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
pipe = pickle.load(open('ipl.pkl', 'rb'))


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title='Home')      


@app.route('/predict', methods = ['GET','POST'])
def predict():
    message1 = ''
    message2 = ''
    message3 = ''
    form = InputForm()
    if form.validate_on_submit():
        batting_team = form.batting_team.data
        bowling_team = form.bowling_team.data
        city = form.city.data
        target_score = form.target_score.data
        Current_Runs = form.Current_Runs.data
        wickets_down = form.wickets_down.data
        over = form.over.data
        ball = form.ball.data
        Required_Runs = target_score - Current_Runs
        current_balls_bowled = (over*6) + ball
        balls_left = 120 - current_balls_bowled
        current_run_rate = Current_Runs/(((over*6)+ball)/6)
        required_run_rate = Required_Runs/(balls_left/6)

        df = pd.DataFrame({'wickets_down':[wickets_down],
                           'target_score':[target_score],
                           'city':[city],
                           'batting_team':[batting_team],
                           'bowling_team':[bowling_team],
                           'over':[over+1],
                           'ball':[ball],
                           'Current_Runs':[Current_Runs],
                           'Required_Runs':[Required_Runs],
                           'current_balls_bowled':[current_balls_bowled],
                           'balls_left':[balls_left],
                           'current_run_rate':[current_run_rate],
                           'required_run_rate':[required_run_rate],})
        
        result = pipe.predict_proba(df)
        bowling_team_chances = int((np.round(result[0][0],3))*100)
        batting_team_chances = int((np.round(result[0][1],3))*100)
        message1 =  f"{batting_team} : {batting_team_chances} %"
        message2 =  f"{bowling_team} : {bowling_team_chances} %"

    else:
        flash("Input Data Not Satisfied")
    return render_template('predict.html',title='Prediction',form=form,output1=message1, output2=message2, output3 = message3)


if __name__ == '__main__':
    app.run(debug=True)