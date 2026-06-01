import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Mediscan",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', value='5')

    with col2:
        Glucose = st.text_input('Glucose Level', value='166')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value', value='72')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value', value='19')

    with col2:
        Insulin = st.text_input('Insulin Level', value='175')

    with col3:
        BMI = st.text_input('BMI value', value='25.8')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value', value='0.587')

    with col2:
        Age = st.text_input('Age of the Person', value='51')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) if x != '' else 0.0 for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age', value='62')

    with col2:
        sex = st.text_input('Sex', value='0')

    with col3:
        cp = st.text_input('Chest Pain types', value='0')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure', value='140')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl', value='268')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl', value='0')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results', value='0')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved', value='160')

    with col3:
        exang = st.text_input('Exercise Induced Angina', value='0')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise', value='3.6')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment', value='0')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy', value='2')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', value='2')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) if x != '' else 0.0 for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)', value='119.992')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)', value='157.302')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)', value='74.997')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)', value='0.00784')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)', value='0.00007')

    with col1:
        RAP = st.text_input('MDVP:RAP', value='0.0037')

    with col2:
        PPQ = st.text_input('MDVP:PPQ', value='0.00554')

    with col3:
        DDP = st.text_input('Jitter:DDP', value='0.01109')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer', value='0.04374')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)', value='0.426')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3', value='0.02182')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5', value='0.0313')

    with col3:
        APQ = st.text_input('MDVP:APQ', value='0.02971')

    with col4:
        DDA = st.text_input('Shimmer:DDA', value='0.06545')

    with col5:
        NHR = st.text_input('NHR', value='0.02211')

    with col1:
        HNR = st.text_input('HNR', value='21.033')

    with col2:
        RPDE = st.text_input('RPDE', value='0.414783')

    with col3:
        DFA = st.text_input('DFA', value='0.815285')

    with col4:
        spread1 = st.text_input('spread1', value='-4.813031')

    with col5:
        spread2 = st.text_input('spread2', value='0.266482')

    with col1:
        D2 = st.text_input('D2', value='2.301442')

    with col2:
        PPE = st.text_input('PPE', value='0.284654')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) if x != '' else 0.0 for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
