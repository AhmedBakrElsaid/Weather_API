from django.shortcuts import render
import requests
# Create your views here.

def index (request):
    
    api_url = "http //api.openweathermap.org/data/2.5/weather q="
    city_name = "Egypt"
    
    url = api_url + city_name
    response = requests.get(url)
    content = response.json()
    city_weather = {
        'city' : city_name,
        'temperature': content['main']['temp'],
        'description': content ['weather'][0]['temperature'],
        'icon': content['weather'][0]['icon'],
    }
    
return render(request,'weather.html',{'city_weather': city_weather})
    