import pandas as pd
import numpy as np
import seaborn as sns
import itertools
import streamlit as st

import plotly.express as px
from plotly import graph_objs as go



from plotly import subplots

st.markdown(f"<h1 style=color:green;text-align:center;background-color:red;>PLOTLY</h1>",unsafe_allow_html=True)
data=sns.load_dataset("flights")
st.write(sns.get_dataset_names())
st.write(data)
# ============================\
st.markdown(f"<h1 style=color:blue;><p>We'll be taking our data visualization skills to the next level with plotly.plotly is a great package that allows you to create dynamic data visualizations in Python.Here's an example of what we'll be able to create by the end of this tutorial.</p></h1>",unsafe_allow_html=True)

df_flights = sns.load_dataset("flights")
df_flights['passengers'] = df_flights['passengers'].map(lambda x: [i for i in range(x)])
df_flights = df_flights.explode('passengers')
df_flights['passenger_id'] = df_flights['year'].astype(str) + '-' + df_flights['month'].astype(str) + '-' + df_flights['passengers'].astype(str)
df_flights = df_flights.drop(columns=['passengers'], axis=1)

df_growth = df_flights['passenger_id'].groupby(df_flights['year']).count().to_frame()
df_growth = df_growth.reset_index(level=0)
df_growth = df_growth.rename(columns={"passenger_id": "passengers"})
df_growth['prev_passengers'] = df_growth['passengers'].shift(1)
df_growth['passenger_growth_yoy'] = (df_growth['passengers'] - df_growth['prev_passengers']) / df_growth['prev_passengers']

fig = subplots.make_subplots(
    rows=2, cols=1, row_heights=[0.3, 0.7],
    subplot_titles=['YoY Growth', 'Monthly and Yearly Distribution']
)

fig.add_trace(
    go.Bar(
        x=df_growth['year'], y=df_growth['passenger_growth_yoy'], name='YoY Growth',
        marker_color='green'
    ),
    row=1, col=1
)

fig.add_trace(
    go.Histogram2d(
        x=df_flights['year'], y=df_flights['month'], z=df_flights['passenger_id'],
        name='Distribution',
        histfunc='count', texttemplate="%{z}"
    ),
    row=2, col=1
)

fig.update_layout(
    title='Flight Passengers Evolution 1949-1960',
    height=800,
    yaxis1_tickformat='.2%',
    xaxis2_title='Year', yaxis2_title='Month',
    plot_bgcolor='white'
)

# fig.show()

st.plotly_chart(fig)

st.markdown(f"<h1 style=color:blue;><p>During the course of this tutorial we'll be exploring 2 plotly modules: plotly.express and plotly.graph_objects.plotly.express (px) is a fast and easy way to create dynamic data visualizations.plotly.graph_objects (go) is the lower level API that grants more control over your visualizations, but is more code intensive.<p></h1>",unsafe_allow_html=True)
st.markdown(f"<h1 style=color:Red;>🚚 Import</h1>",unsafe_allow_html=True)
st.markdown(f"<h1><p>   import numpy as np  # linear algebra <br>import pandas as pd  # data processing<br>import seaborn as sns  # datasets<br>import itertools  # iteration utils<br>from scipy.interpolate import griddata  # for 3d surface plot<br>import plotly.express as px<br>import plotly.graph_objects as go<br>from plotly import subplots)<br></p></h1>",unsafe_allow_html=True)
import numpy as np  # linear algebra
import pandas as pd  # data processing
import seaborn as sns  # datasets
import itertools  # iteration utils
from scipy.interpolate import griddata  # for 3d surface plot

import plotly.express as px
import plotly.graph_objects as go
from plotly import subplots

st.markdown(f"<h1 style=color:Red;># 📊 Bar Chart</h1>",unsafe_allow_html=True)

st.markdown(f"<h2 style=color:blue;><p>Let's start by creating a few bar charts.We'll be analizing the builtin plotly.express <h2>gapminder dataset</h2>, which contains a few metrics for each country of the world.</p></h2>",unsafe_allow_html=True)
df_world = px.data.gapminder()
st.write(df_world.head())
st.plotly_chart(px.bar(df_world, x='year', y='pop', color='continent', hover_name='country', title='World Population Growth'))
st.markdown(f"<h1 style=color:blue;><p>Next let's take a more detailed look at Europe's population distribution by country in 2007.We can query the dataset by using the query() method and by passing in a Python logic statement as a string parameter.</p></h1>",unsafe_allow_html=True)
df_europe = px.data.gapminder().query("continent == 'Europe' and year == 2007 ")
st.write(df_europe.head())
st.markdown(f"<h2 style=color:blue;>We can instantiate any chart/plot as an object and access its methods for more granular control over our data</h2>", unsafe_allow_html=True)

fig = px.bar(df_europe, x='country', y='pop', text='pop', color='country')
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
st.plotly_chart(fig.show())