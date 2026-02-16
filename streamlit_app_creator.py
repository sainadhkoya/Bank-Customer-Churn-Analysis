import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Bank Churn Dashboard", layout="wide")

st.title("European Bank Customer Churn Dashboard")

@st.cache_data
def load_data():
    return pd.read_csv("European_Bank.csv")

df = load_data()

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Churn by Geography")
fig, ax = plt.subplots()
sns.countplot(x='Geography', hue='Exited', data=df, ax=ax)
st.pyplot(fig)

st.subheader("Churn by Age")
fig, ax = plt.subplots()
sns.histplot(data=df, x="Age", hue="Exited", bins=20, ax=ax)
st.pyplot(fig)

st.subheader("Active Members vs Churn")
fig, ax = plt.subplots()
sns.countplot(x='IsActiveMember', hue='Exited', data=df, ax=ax)
st.pyplot(fig)
