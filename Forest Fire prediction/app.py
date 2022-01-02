import streamlit as st 
import numpy as np 
import pickle 

loaded_model = pickle.load(open('C:/Users/Admin/Streamlit app/Forest Fire prediction/model.pkl','rb'))


def fire_prediction(input_data):
    input_np =np.asarray(input_data) 

    input_reshape = input_np.reshape(1,-1)

    prediction = loaded_model.predict(input_reshape)
    print(prediction)

    if(prediction[0]==0):
        return 'There is no chance of Fire'
    else:
        return 'There is chance of Fire'



def main():
    st.title('Fire pediction web App') 
        
    Oxygen = st.text_input('Number of Pregnancies')
    Temperature = st.text_input('Glucose Level')
    Humidity = st.text_input('Blood Pressure value')
    
        

    occur = ''

        # create abuttonfor predict

    if st.button("Check Fire prediction"):
        occur = fire_prediction([Oxygen,Temperature,Humidity])

    st.success(occur)


if __name__=='__main__':
    main()