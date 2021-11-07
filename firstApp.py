
import streamlit as st 
import pandas as pd

import numpy as np



#load daatset

def load_data(dataset):
    df = pd.read_csv(dataset)
    return df

st.title("Data Analysis using app")
st.subheader("Load Dataset and start Analysing and Visualizing")

menu = ['House Price Dataset','Netflix Dataset']
choice = st.sidebar.selectbox("Select Activity",options=menu)

#lets Start the coding area

if choice=='House Price Dataset':
        st.subheader("House Price Dataset")
        data = load_data("D:/Data Analsis/houseprices.csv")
        st.dataframe(data.head(5))


        # show summary
        if st.checkbox("Show Summary"):
            st.write(data.describe())
#show Shape
            if st.checkbox("Show Shape"):
                st.write(data.shape)
#check null values
                if st.checkbox("Check Null Values"):
                    st.write(data.isnull().sum())
#filling Null Values
                    if st.checkbox("Filling Null Values with Previous Value"):
                        st.write(data.fillna(0,inplace=True))
#again checking Nan values
                        if st.checkbox("Again Checking NaN Values"):
                            st.write(data.isnull().sum())

                            if st.button("1st 5 data"):
                                    st.write(data.head(5))
                                    

if choice=='Netflix Dataset':
        st.subheader("Netflix Dataset")
        data = load_data("C:/Users/Admin/Desktop/ML al l Pojects/Netflix Dataset.csv")
        st.dataframe(data.head(5))


        if st.checkbox("Show Shape"):
                st.write(data.shape)
#check null values
                if st.checkbox("Check Null Values"):
                    st.write(data.isnull().sum())
#filling Null Values
                    if st.checkbox("Filling Null Values with Previous Value"):
                        st.write(data.fillna(0,inplace=True))
#again checking Nan values
                        if st.checkbox("Again Checking NaN Values"):
                            st.write(data.isnull().sum())

                            if st.button("1st 5 data"):
                                    st.write(data.head(5))

            







            






  
        


                       
