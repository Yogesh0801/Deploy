import pandas as pd
import streamlit as st
import numpy as np
import matplotlib


data=pd.read_csv('claimants data.csv')
data
st.markdown (f"<h1 style=text-align:center;color:blue;background-color:red;> Logistics Regression</h1>",unsafe_allow_html=True)
