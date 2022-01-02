import streamlit as st 
import numpy as np
import pickle 

loaded_model = pickle.load(open('C:/Users/Admin/Streamlit app/Diabetes Prediction with web App/trained_model.sav','rb'))

# creating a function for prediction

def diabetes_prediction(input_data):
    input_np =np.asarray(input_data) 

    input_reshape = input_np.reshape(1,-1)

    prediction = loaded_model.predict(input_reshape)
    print(prediction)

    if(prediction[0]==0):
        return 'The person is Non Diabetes'
    else:
        return 'The person is Diabetes'



def main():
    st.title('Diabetes pediction web App') 
        
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')
        

    diagnosis = ''

        # create abuttonfor predict

    if st.button("Diabetes Test prediction"):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])

    st.success(diagnosis)


if __name__=='__main__':
    main()