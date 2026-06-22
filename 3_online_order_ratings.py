import streamlit as st
import pandas as pd

st.title("Online Order vs Ratings")

data = {
"Online Order": ["No", "Yes"],
"Average Rating": [3.93, 3.89],
"Restaurants": [6749, 16297]
}

df = pd.DataFrame(data)

st.dataframe(df)

st.bar_chart(df.set_index("Online Order")["Average Rating"])