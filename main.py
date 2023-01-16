import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
import sklearn
import matplotlib
st.set_page_config('Logistic Model Deployment',page_icon='🤗')
st.write(st.__version__)
st.write(pd.__version__)
st.write(sklearn.__version__)
st.write(matplotlib.__version__)


st.markdown(f"<h1 style='text-align:center;background-color:green;font-color: #a4c639;border-style:dotted;padding:15px;border-width:15px'>{'Logistic Model'}</h1>",unsafe_allow_html=True)
# load dataset

data=pd.read_csv('claimants data.csv')
data
col1,col2,col3=st.columns(3)
# missing Values
col1.markdown('Missing values')
col1.write(data.isnull().sum())

# Head
col2.markdown(f"<h1 style='text-align:center;background-color:green;font-color: #a4c639;border-style:dotted;padding:15px;")