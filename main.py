import streamlit as st
import plotly.express as px
from backendfile import get_data
st.title("Weather Forecast for the Next Days")
place=st.text_input("Place:") #input
days=st.slider("Forecast Days",min_value=1,max_value=5,help="Select the number of forecasted days ")
option=st.selectbox("Select data to view",("Temperature","Sky")) #options come in tuple as strings
st.subheader(f"{option} for the next {days} days in {place}")
d,t=get_data(place,days,option)
if option=="Temperature":
    figure=px.line(x=d,y=t,labels={"x":"Date","y":"Temperature(C)"})
    st.plotly_chart(figure)