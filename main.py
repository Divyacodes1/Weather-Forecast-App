import streamlit as st
import plotly.express as px
from backendfile import get_data
#Add title,text input,slider,selectbox and subheader
st.title("Weather Forecast for the Next Days")
place=st.text_input("Place:") #input
days=st.slider("Forecast Days",min_value=1,max_value=5,help="Select the number of forecasted days ")
option=st.selectbox("Select data to view",("Temperature","Sky")) #options come in tuple as strings
st.subheader(f"{option} for the next {days} days in {place}")
if place:
#Get the temperature/sky data
    try:
        filtered_data=get_data(place, days)
    #Create temperature plot
        if option=="Temperature":
            temperatures= [di["main"]["temp"] /10 for di in filtered_data]
            dates=[di["dt_txt"] for di in filtered_data]
            figure=px.line(x=dates,y=temperatures,labels={"x":"Date","y":"Temperature(C)"})
            st.plotly_chart(figure)

        if option=="Sky":
            sky_conditions= [di["weather"][0]["main"] for di in filtered_data]
            images={"Clear":"clear.png","Clouds":"cloud.png","Rain":"rain.png","Snow":"snow.png"}
            images_path=[images[condition] for condition in sky_conditions]
            st.image(images_path,width=100)
    except KeyError:
        st.write("This place is not available")