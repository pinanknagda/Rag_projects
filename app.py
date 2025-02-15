import streamlit as st
from dotenv import load_dotenv
from utils import query_agent

load_dotenv()

st.title("Let's do some data analysis")
st.header("Upload your CSV file")

data = st.file_uploader("Upload a CSV file", type=["csv"])

query = st.text_area("Enter your query")
button = st.button("Generate response")

if button: 
    #Get the response
    answer = query_agent(data,query)
    st.write("Response: ",answer) 
