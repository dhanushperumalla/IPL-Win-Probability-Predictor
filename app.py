import streamlit as st
import pickle
import pandas as pd

# Define the teams and cities
teams = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore',
         'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings',
         'Rajasthan Royals', 'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
          'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
          'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
          'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
          'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
          'Sharjah', 'Mohali', 'Bengaluru']

# Load the pre-trained model
pipe = pickle.load(open('pipe.pkl', 'rb'))

# Set the title of the Streamlit app
st.title('IPL Win Predictor Using IPL DATA (2008-2019)')

# Create columns for team selection
col1, col2 = st.columns(2)

# Select the batting team
with col1:
    batting_team = st.selectbox('Select the batting team', sorted(teams))

# Select the bowling team
with col2:
    bowling_team = st.selectbox('Select the bowling team', sorted(teams))

# Select the host city
selected_city = st.selectbox('Select host city', sorted(cities))

# Input the target score
target = st.number_input('Target')

# Create columns for match details
col3, col4, col5 = st.columns(3)

# Input the current score
with col3:
    score = st.number_input('Score')

# Input the overs completed
with col4:
    overs = st.number_input('Overs completed')

# Input the wickets out
with col5:
    wickets = st.number_input('Wickets out')

# Predict the win probability when the button is clicked
if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs * 6)
    wickets = 10 - wickets
    crr = score / overs
    rrr = (runs_left * 6) / balls_left

    # Create a dataframe with the input data
    input_df = pd.DataFrame({'batting_team': [batting_team],
                             'bowling_team': [bowling_team],
                             'city': [selected_city],
                             'runs_left': [runs_left],
                             'balls_left': [balls_left],
                             'wickets': [wickets],
                             'total_runs_x': [target],
                             'crr': [crr],
                             'rrr': [rrr]})

    # Predict the win probability
    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]

    # Display the win probabilities
    st.header(batting_team + "- " + str(round(win * 100)) + "%")
    st.header(bowling_team + "- " + str(round(loss * 100)) + "%")
