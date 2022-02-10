import streamlit as st 
import pandas as pd 
import numpy as np 
import joblib 

model = open("finall.pkl","rb")
loaded_model = joblib.load(model)

def lr_prediction(var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13):
    num_arr = np.array([var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13])
    pred = num_arr.reshape(1,-1)
    preds = pred.astype(float)
    modelprediction = loaded_model.predict(preds)
    return modelprediction

def run():
    st.title("House Price prediction")
												
    var1 = st.text_input('enter CRIM')
    var2 = st.text_input('enter ZN')
    var3 = st.text_input('enter INDUS')
    var4 = st.text_input('enter CHAS')
    var5 = st.text_input('enter NOX')
    var6 = st.text_input('enter RM')
    var7 = st.text_input('enter AGE')
    var8 = st.text_input('enter DIS')
    var9 = st.text_input('enter RAD')
    var10 = st.text_input('enter TAX')
    var11 = st.text_input('enter PTRATIO')
    var12 = st.text_input('enter B')
    var13 = st.text_input('enter LSTAT')

    loan = ""
    if st.button("predict"):
        loan = lr_prediction(var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13)
    st.success("House price is  model:{}".format(loan))

if __name__ == '__main__':
    run()
            
