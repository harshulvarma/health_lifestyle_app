import streamlit as st
import pandas as pd
import pickle

st.write("""
# Health Lifestyle Prediction App
## This app predicts user's lifestyle based on resting heartrate and BMI.


### Currently the lifestyle available are:

** Sedentary ** - average person with sedentary lifestyle

**Cardio Trainer** - cardio training focused person

**Weight Trainer** - weight training focused person


*This app uses machine learning can be used to tailor workouts by personal trainers for new gym clients.*

*::currently using random forest classifier and achieved 0.96 F1 Score::*

""")




st.header('Input your Resting Heartrate and BMI')


def user_input_features():
    resting_heartrate = st.slider('Average Resting Heartrate', 20, 180, 72)
    BMI = st.slider('BMI', 10, 35, 21)

    data = {'resting_heartrate': resting_heartrate,
            'BMI': BMI
            }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

st.subheader('User Input parameters')
st.write(input_df)


model = pickle.load(open('health_app_rf_weights.pkl','rb'))

prediction = model.predict(input_df)
prediction_proba = model.predict_proba(input_df)

target_names = ['Cardio Trainer','Sedentary','Weight Trainer']
st.subheader('Lifestyle Prediction:')
st.write(target_names[prediction[0]])