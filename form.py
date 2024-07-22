from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,FloatField,SelectField,SubmitField
from wtforms.validators import DataRequired


teams = ['Royal Challengers Bangalore', 'Kings XI Punjab',
       'Delhi Daredevils', 'Kolkata Knight Riders', 'Rajasthan Royals',
       'Mumbai Indians', 'Chennai Super Kings', 'Deccan Chargers',
       'Pune Warriors', 'Kochi Tuskers Kerala', 'Sunrisers Hyderabad',
       'Rising Pune Supergiants', 'Gujarat Lions']


cities = ['Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur',
       'Hyderabad', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban',
       'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Kochi', 'Indore', 'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi',
       'Abu Dhabi', 'Sharjah', 'Rajkot', 'Kanpur']


#wickets_down	target_score	city	batting_team	bowling_team	over	ball	Current_Runs	Required_Runs	current_balls_bowled	balls_left	current_run_rate	required_run_rate	


class InputForm(FlaskForm):
       batting_team = SelectField(label="Batting Team",choices=teams,validators=[DataRequired()])
       bowling_team = SelectField(label="Bowling Team",choices=teams,validators=[DataRequired()])
       city =         SelectField(label="Match City",choices=cities,validators=[DataRequired()])
       target_score = IntegerField(label="Target Score",validators=[DataRequired()])
       Current_Runs = IntegerField(label="Current Runs",validators=[DataRequired()])
       wickets_down = IntegerField(label="Wickets Fallen",validators=[DataRequired()])
       over =         IntegerField(label="Overs",validators=[DataRequired()])
       ball =         IntegerField(label="Balls",validators=[DataRequired()])
       submit =       SubmitField('Predict Winning Probability')

