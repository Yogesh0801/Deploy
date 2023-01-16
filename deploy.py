import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets  
import numpy as np
import streamlit as st


from sklearn.model_selection import train_test_split
from sklearn.tree import  DecisionTreeClassifier,plot_tree
from sklearn.metrics import classification_report
from sklearn import preprocessing


st.markdown (f"<h1 style=text-align:center;color:blue;background-color:red;> Data Deployment</h1>",unsafe_allow_html=True)
st.markdown(f"<h2 style=text-align:left;color:green;background-color:yello;>In Churn_Modeling</h2>",unsafe_allow_html=True)

data=pd.read_csv('hyd/Churn_Modelling.csv')
data
st.markdown(f"<h2 style=color:green;>Head</h2>",unsafe_allow_html=True)
st.write(data.head())
st.write("<h2 style=color:green;>Tail 😅</h2>",unsafe_allow_html=True)
st.write(data.tail())

pd.plotting.scatter_matrix(data)
st.markdown(f"<h2 style=color:yellow;text-align:center;background-color:maroon;> data deployment start</h2>",unsafe_allow_html=True)
st.write(data.info)
st.markdown(f"<h2 style=color:purple;background-color:white;text-align:center;>Describe</h2>",unsafe_allow_html=True)
st.write(data.describe)




