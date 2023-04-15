# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Cq2MVS1NqjJ1EIW_wS9x3Qs-2uZ59kUH
"""

import streamlit as st
import numpy as np
import pickle
import pandas as pd
from house_price_prediction_file import predict_house_price


df = pd.read_csv('./train_new.csv')

with open('./my_model.pickle', 'rb') as f:
    model = pickle.load(f)




primaryColor="#6eb52f"
backgroundColor="#f0f0f5"
secondaryBackgroundColor="#e0e0ef"
textColor="#262730"
font="sans serif"
st.write('div.row-widget.stRadio > div{flex-direction:row;}', unsafe_allow_html=True)
#OverallCond = st.text_input("Enter Overall condition rating (between 1-5)")
# print the user's name
#st.write("OverallCond :", OverallCond)

#TotalBsmtSF = st.text_input("Enter Total Basement Surface Area")
# print the user's name
#st.write("TotalBsmtSF :", TotalBsmtSF)

#FirstFlrSF = st.text_input("Enter  First Floor Surface Area")
# print the user's name
#st.write("FirstFlrSF :", FirstFlrSF)

#SecondFlrSF = st.text_input("Enter Second Floor Surface Area")
# print the user's name
#st.write("SecondFlrSF :", SecondFlrSF)

#GrLivArea = st.text_input("Enter Living Room Surface Area")
# print the user's name
#st.write("GrLivArea :", GrLivArea)

#FullBath = st.text_input("Enter number of Full Baths")
# print the user's name
#st.write("FullBath :", FullBath)

#BedroomAbvGr = st.text_input("Enter number of Bedrooms")
# print the user's name
#st.write("BedroomAbvGr :", BedroomAbvGr)

st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>', unsafe_allow_html=True)

st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;}</style>', unsafe_allow_html=True)

#user_inputs_app = [OverallCond, TotalBsmtSF, FirstFlrSF, SecondFlrSF, GrLivArea, FullBath, BedroomAbvGr]

#if st.button('Predict House Price'):
#    predict_house_price(user_inputs_app, model, df)
st.title('Home price prediction')
 
st.write('---')

OverallCond = st.radio("Enter Overall condition rating (between 1-5)",( 1, 2 , 3,4,5))
# print the user's name
#st.write("OverallCond :", OverallCond)

TotalBsmtSF = st.slider("Enter Total Basement Surface Area", 800, 900, 1000)
# print the user's name
#st.write("TotalBsmtSF :", TotalBsmtSF)

FirstFlrSF = st.slider("Enter  First Floor Surface Area",800, 900, 1000)
# print the user's name
#st.write("FirstFlrSF :", FirstFlrSF)

SecondFlrSF = st.slider("Enter Second Floor Surface Area",800, 900, 1000)
# print the user's name
#st.write("SecondFlrSF :", SecondFlrSF)

GrLivArea = st.slider("Enter Living Room Surface Area",1000, 1500,2000)
# print the user's name
#st.write("GrLivArea :", GrLivArea)

FullBath = st.radio("Enter number of Full Baths",(1, 2 , 3,4,5))
# print the user's name
#st.write("FullBath :", FullBath)

BedroomAbvGr = st.radio("Enter number of Bedrooms",(1, 2 , 3,4,5))
# print the user's name
#st.write("BedroomAbvGr :", BedroomAbvGr)


user_inputs_app = [OverallCond, TotalBsmtSF, FirstFlrSF, SecondFlrSF, GrLivArea, FullBath, BedroomAbvGr]

if st.button('Predict House Price'):
    predict_house_price(user_inputs_app, model, df)

