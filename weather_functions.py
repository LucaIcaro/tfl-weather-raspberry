import requests
import time
import state
from config import WEATHER_URL, WEATHER_PARAMS, WEATHER_HEADERS, WEATHER_CODES
from datetime import datetime, timedelta, timezone
from dateutil import parser

def get_weather_data():
    try:
        response = requests.get(WEATHER_URL, params=WEATHER_PARAMS, headers=WEATHER_HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def parse_weather_data(data):
    if not data or 'features' not in data or not data['features']:
        return ["No weather data available."]

    time_series = data['features'][0]['properties']['timeSeries']
    
    now = datetime.now(timezone.utc)
    end_of_day = now.replace(hour=23, minute=59, second=59, microsecond=999999)
    
    temperatures = []
    rain_times = []
    
    for entry in time_series:
        entry_time = parser.isoparse(entry['time'])
        
        if now <= entry_time <= end_of_day:
            temp = entry['screenTemperature']
            temperatures.append(temp)
            
            if entry['precipitationRate'] > 0:
                rain_times.append(entry_time.strftime("%H:%M"))
    
    if not temperatures:
        return ["No weather data available."]
    
    min_temp = min(temperatures)
    max_temp = max(temperatures)
    
    weather_info = [f"Today: {int(min_temp)}°C - {int(max_temp)}°C"]
    
    if rain_times:
        weather_info.append(f"Rain at: {', '.join(rain_times)}")
    else:
        weather_info.append("Sunny day expected")
    
    return weather_info

def update_weather_data():
    while True:
        weather_data = get_weather_data()
        new_weather_data = parse_weather_data(weather_data) if weather_data else ["No weather data available"]

        if new_weather_data != state.weather_data:
            state.weather_data = new_weather_data
            state.weather_last_update_time = time.time()
            state.weather_need_redraw = True

        time.sleep(1800)  # Update every 30 minutes