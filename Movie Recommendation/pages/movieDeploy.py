# -*- coding: utf-8 -*-
"""
Created on jan15 19:39:11 2023

@author: Yogesh bandewar
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import streamlit as st
import sklearn
import joblib

import warnings
warnings.filterwarnings('ignore')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(page_title="Model training", page_icon="📈")


def header(url):
     st.markdown(f'<p style="background-color:#f2f3f4;color:#4b5320;font-size:24px;border-radius:2%;text-align:center">{url}</p>',unsafe_allow_html=True)
  
header("TMDB_5000 DataSet")
data=pd.read_excel("https://github.com/Yogesh0801/Machine-Learning-project/blob/main/Movie_recommendation%20system%20dataset/tmdb_5000_movies.xlsb", engine='pyxlsb')








