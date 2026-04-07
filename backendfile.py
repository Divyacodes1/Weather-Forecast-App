import requests
API_KEY="12a03cbdd8371730530254bfd56a2f59"
def get_data(place,forecast_days=None):
    url=f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response=requests.get(url)
    data=response.json()
    filtered_data=data["list"]
    nr_values=8*forecast_days #because each day's weather is noted 8 times in the data
    filtered_data=filtered_data[:nr_values]
    return filtered_data

if __name__=="__main__":
  print(get_data(place="Tokyo",forecast_days=3))

