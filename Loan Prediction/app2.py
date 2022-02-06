import streamlit as st 
import numpy as np
import pickle 

loaded_model = pickle.load(open('trained_model.pkl','rb'))

# creating a function for prediction

def loan_prediction(input_data):
    input_np =np.asarray(input_data) 

    input_reshape = input_np.reshape(1,-1)

    prediction = loaded_model.predict(input_reshape)
    print(prediction)

    if(prediction[0]==0):
        return 'Your Loan is passed'
    else:
        return 'Your Loan is Rejecteds'



def main():
    st.title('Diabetes pediction web App') 
        


    Gender = st.text_input('Enter Gender ')
    Married = st.text_input('Enter Martial Status')
    Dependents    = st.text_input('Enter Dependents')
    Education = st.text_input('enter Education')
    Self_Employed= st.text_input('Self_Employed')
    ApplicantIncome= st.text_input('Application Income')
    CoapplicantIncome = st.text_input('CoapplicantIncome')
    LoanAmount = st.text_input('LoanAmount')
    Loan_Amount_Term= st.text_input('Loan_Amount_Term')
    Credit_History = st.text_input('Credit_History')
    Property_Area= st.text_input('Property_Area')
    
        

    loan = ''

        # create abuttonfor predict

    if st.button("Your Loan Status"):
        loan = loan_prediction([Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area])

    st.success(loan)


if __name__=='__main__':
    main()