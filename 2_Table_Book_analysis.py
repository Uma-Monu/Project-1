import streamlit as st
import pandas as pd

st.title("Table Booking vs Ratings")

data = {
"Book Table": ["No", "Yes"],
"Average Rating": [3.81, 4.16],
"Restaurants": [17005, 6041]
}

df = pd.DataFrame(data)

st.dataframe(df)

st.bar_chart(df.set_index("Book Table")["Average Rating"])