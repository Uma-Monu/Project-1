import streamlit as st
import plotly.express as px
import pandas as pd

data = {
    "Online Order": ["Yes", "No"],
    "Restaurants": [16297, 6749]
}

df = pd.DataFrame(data)

fig = px.pie(
    df,
    values="Restaurants",
    names="Online Order",
    hole=0.5
)

st.plotly_chart(fig, use_container_width=True)