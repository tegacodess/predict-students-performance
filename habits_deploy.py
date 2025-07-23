import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load('Logistic Regression_students.pkl')


st.title('Students Performance Predictor')

st.markdown('Fill in the students lifestyle and study habits to make a prediction on their performance')

with st.form("Student Form"):
  age = st.number_input('Age', 10, 25, 15)
  study_hours = st.number_input('Daily Study Hours', 0.0, 24.0, 5.0)
  social_media_hours = st.number_input('Daily Social Media Hours', 0.0, 24.0, 2.0)
  netflix_hours = st.number_input('Time Spent on Netflix Daily', 0.0, 24.0, 3.0)
  attendance_percentage =st.number_input('Attendance Percentage %',0.0, 100.0, 75.0)
  sleep_hours = st.number_input('Sleep Hours', 0.0, 24.0, 7.0)
  exercise_frequency = st.slider('Weekly Exercise Frequency', 0, 10, 4)
  mental_health_rating = st.number_input('Students Mental Health Rating', 0, 10, 7 )
  gender = st.selectbox("Students Gender", ("Male", "Female"))
  part_time_job = st.selectbox("Does the Student Work Part-time?", ("Yes", "No"))
  diet_quality = st.selectbox('Students Diet Quality', ('Fair', 'Good', 'Poor'))
  internet_quality = st.select_slider("Internet Quality", ('Average', 'Poor', 'Good'))
  extracurricular = st.selectbox("Does the Student Participate in Extra-curriculars?" ('No', "Yes"))
  parents = st.select_slider("Parents Education Level",('Master', 'High School', 'Bachelor', 'None'))



  submitted = st.form_submit_button('Predict')
  
  if submitted:
    input_data = pd.DataFrame({
        'age': [age],
        'gender':[gender],
        'study_hours_per_day': [study_hours],
        'social_media_hours':[social_media_hours],
        'netflix_hours':[netflix_hours],
        'part_time_job':[part_time_job],
        'attendance_percentage':[attendance_percentage],
        'sleep_hours':[sleep_hours],
        'diet_quality':[diet_quality],
        'exercise_frequency':[exercise_frequency],
        'parental_education_level':[parents],
        'internet_quality':[internet_quality],
        'mental_health_rating':[mental_health_rating],
        'extracurricular_participation':[extracurricular]
    })

    prediction = model.predict(input_data)

    print(f'Student Performance is {prediction}')
