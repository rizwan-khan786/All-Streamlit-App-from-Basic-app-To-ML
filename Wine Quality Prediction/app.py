import streamlit as st 
import numpy as np 
import pickle 

loaded_model = pickle.load(open('model.sav','rb'))


def wine_prediction(input):
    
    inputdata = np.asarray(input)

    inputdata_reshaped = inputdata.reshape(1,-1)

    prediction = loaded_model.predict(inputdata_reshaped)

    print(prediction)

    if(prediction[0]==1):
        return 'Good Quality Wine have a Drink'
    else:
        return 'Dont Buy Bad Quality Wine'  

def main():
    										
    st.title('WinenPrediction Web App') 
        
    fixedacidity = st.text_input('Number of fixed acidity')
    volatileacidity = st.text_input('volatile acidity')
    citricacid = st.text_input('citric acid')
    residualsugar= st.text_input('residual sugar')
    chlorides= st.text_input('chlorides')
    freesulfurdioxide= st.text_input('free sulfur dioxide')
    totalsulfurdioxide = st.text_input('total sulfur dioxide')
    density = st.text_input('Age of the Person')
    pH = st.text_input('Enter PH value')
    sulphates = st.text_input('Enter Sulphate value')
    alcohol = st.text_input('alcohol')
        

    wine = ''

        # create abuttonfor predict

    if st.button("Wine Quality prediction"):
       wine = wine_prediction([fixedacidity,volatileacidity,citricacid,residualsugar,chlorides,freesulfurdioxide,totalsulfurdioxide,density,pH,sulphates,alcohol])

    st.success(wine)



if __name__=='__main__':
    main()
