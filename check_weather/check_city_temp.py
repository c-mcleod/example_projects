import requests

def my_weather_forcast(location):
    """Returns for a city the min and max temps for the day after tomorrow"""
    l_url = f"https://geocoding-api.open-meteo.com/v1/search?name={location}&language=de"
    r_l = requests.get(l_url)
    r_l_dict = r_l.json()
    print(f"The latitude and longitude for {location} is {r_l_dict['results'][0]['latitude']}, {r_l_dict['results'][0]['longitude']}.")
    
    url = f"https://api.open-meteo.com/v1/forecast?latitude={r_l_dict['results'][0]['latitude']}&longitude={r_l_dict['results'][0]['longitude']}&models=best_match&daily=weathercode,temperature_2m_max,temperature_2m_min,precipitation_sum,rain_sum,snowfall_sum,precipitation_hours,precipitation_probability_max&current_weather=true&timezone=Europe%2FBerlin"
    r = requests.get(url)
    r_dict = r.json()
    print(f"In {location} for the day after tomorrow, we have a temperature range of {r_dict['daily']['temperature_2m_min'][2]}°C to {r_dict['daily']['temperature_2m_max'][2]}°C.")
    
location = input('Please enter your city:\n')
my_weather_forcast(location)