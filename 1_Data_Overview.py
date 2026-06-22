import streamlit as st
import pandas as pd

st.title(" Data Overview")

df = pd.read_csv("uber_eats_final_cleaned.csv")

st.subheader("Dataset Shape")

st.write(f"Rows: {df.shape[0]}")
st.write(f"Columns: {df.shape[1]}")

st.subheader("Sample Data")

st.dataframe(df.head())

st.subheader("Missing Values")

st.write(df.isnull().sum())