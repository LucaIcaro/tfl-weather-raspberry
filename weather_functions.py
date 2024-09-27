import requests
import time
import state
from config import WEATHER_URL, WEATHER_PARAMS, WEATHER_HEADERS, WEATHER_CODES
from datetime import datetime, timedelta, timezone
from dateutil import parser
from itertools import groupby
from operator import itemgetter

def get_weather_data():
    try:
        response = requests.get(WEATHER_URL, params=WEATHER_PARAMS, headers=WEATHER_HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def categorize_weather(weather_code, precip_rate):
    if weather_code in [9, 10, 11, 12]:
        if precip_rate < 0.5:
            return "Drizzle"
        elif precip_rate < 4:
            return "Light rain"
        elif precip_rate < 8:
            return "Moderate rain"
        else:
            return "Heavy rain"
    elif weather_code in [13, 14, 15]:
        return "Heavy rain"
    elif weather_code in [16, 17, 18]:
        return "Sleet"
    elif weather_code in [19, 20, 21]:
        return "Hail"
    elif weather_code in [22, 23, 24, 25, 26, 27]:
        return "Snow"
    elif weather_code in [28, 29, 30]:
        return "Thunder"
    else:
        return None

def format_time_range(start, end):
    start_str = start.strftime("%I%p").lstrip('0')
    end_str = end.strftime("%I%p").lstrip('0')
    return f"{start_str}-{end_str}"

def parse_weather_data(data, day_offset=0):
    if not data or 'features' not in data or not data['features']:
        return ["No weather data available."]

    time_series = data['features'][0]['properties']['timeSeries']

    now = datetime.now(timezone.utc)
    target_day = now + timedelta(days=day_offset)
    start_of_day = target_day.replace(hour=0, minute=0, second=0, microsecond=0)
    end_of_day = target_day.replace(hour=23, minute=59, second=59, microsecond=999999)

    temperatures = []
    weather_events = []

    for entry in time_series:
        entry_time = parser.isoparse(entry['time'])

        if start_of_day <= entry_time <= end_of_day:
            temp = entry['screenTemperature']
            temperatures.append(temp)

            weather_type = categorize_weather(entry['significantWeatherCode'], entry['precipitationRate'])
            if weather_type:
                weather_events.append((entry_time, weather_type))

    if not temperatures:
        return ["No weather data available."]

    min_temp = min(temperatures)
    max_temp = max(temperatures)

    day_str = "Today" if day_offset == 0 else "Tomorrow"
    weather_info = [f"{day_str}: {int(min_temp)}°C - {int(max_temp)}°C"]

    if weather_events:
        # Group weather events by type and consecutive time periods
        grouped_events = []
        for k, g in groupby(weather_events, key=itemgetter(1)):
            group = list(g)
            start = group[0][0]
            end = group[-1][0]
            if start != end:
                grouped_events.append((k, start, end))
            else:
                grouped_events.append((k, start, start + timedelta(hours=1)))

        # Format weather information
        weather_info_details = []
        for weather_type, start, end in grouped_events:
            time_range = format_time_range(start, end)
            weather_info_details.append(f"{weather_type} {time_range}")

        weather_info.extend(weather_info_details)
    else:
        weather_info.append("No precipitation expected")

    return weather_info

def update_weather_data():
    while True:
        weather_data = get_weather_data()
        new_weather_data_today = parse_weather_data(weather_data, day_offset=0) if weather_data else ["No weather data available"]
        new_weather_data_tomorrow = parse_weather_data(weather_data, day_offset=1) if weather_data else ["No weather data available"]

        if new_weather_data_today != state.weather_data_today or new_weather_data_tomorrow != state.weather_data_tomorrow:
            state.weather_data_today = new_weather_data_today
            state.weather_data_tomorrow = new_weather_data_tomorrow
            state.weather_last_update_time = time.time()
            state.weather_need_redraw = True

        time.sleep(1800)  # Update every 30 minutes
