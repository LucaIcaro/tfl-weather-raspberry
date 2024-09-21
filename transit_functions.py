import requests
import time
import state
from config import API_KEY, BUS_URL, OVERGROUND_URL, UNDERGROUND_URL

def get_arrivals(url):
    params = {'app_key': API_KEY}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def get_underground_status():
    params = {'app_key': API_KEY}
    try:
        response = requests.get(UNDERGROUND_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching underground status: {e}")
        return None

def truncate_text(text, max_length):
    if len(text) <= max_length:
        return text
    return text[:max_length-3] + '...'

def format_bus_arrivals(data, limit=8, max_dest_length=15):
    sorted_arrivals = sorted(data, key=lambda x: x['timeToStation'])[:limit]
    return [
        f"{arrival['lineName']} to {truncate_text(arrival['destinationName'], max_dest_length)}: {arrival['timeToStation'] // 60} min"
        for arrival in sorted_arrivals
    ]

def format_overground_arrivals(data, limit=8, max_dest_length=20):
    sorted_arrivals = sorted(data, key=lambda x: x['timeToStation'])[:limit]
    return [
        f"To {truncate_text(arrival['destinationName'], max_dest_length)}: {arrival['timeToStation'] // 60} min"
        for arrival in sorted_arrivals
    ]

def format_underground_status(data):
    disrupted_lines = [
        f"{line['name']}: {line['lineStatuses'][0]['statusSeverityDescription']}"
        for line in data
        if line['lineStatuses'][0]['statusSeverityDescription'] != "Good Service"
    ]

    if not disrupted_lines:
        return ["Good service on all lines"]
    else:
        return disrupted_lines

def update_main_data():
    while True:
        bus_arrivals = get_arrivals(BUS_URL)
        overground_arrivals = get_arrivals(OVERGROUND_URL)
        underground_status = get_underground_status()

        new_bus_data = format_bus_arrivals(bus_arrivals) if bus_arrivals else ["No bus data available"]
        new_overground_data = format_overground_arrivals(overground_arrivals) if overground_arrivals else ["No overground data available"]
        new_underground_data = format_underground_status(underground_status) if underground_status else ["No underground data available"]

        if (new_bus_data != state.bus_data or 
            new_overground_data != state.overground_data or 
            new_underground_data != state.underground_data):
            state.bus_data = new_bus_data
            state.overground_data = new_overground_data
            state.underground_data = new_underground_data
            state.main_last_update_time = time.time()
            state.main_need_redraw = True

        time.sleep(30)  # Update every 30 seconds

def toggle_main_display():
    state.main_display_mode = (state.main_display_mode + 1) % 3  # Cycle through 0, 1, 2
    state.main_need_redraw = True