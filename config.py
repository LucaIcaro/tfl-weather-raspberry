# Existing TfL API details
API_KEY = 'XXXXXXXXXX'
BUS_STOP_ID = 'XXXXXXXXXX'
OVERGROUND_STATION_ID = 'XXXXXXXXXX'
BUS_URL = f'https://api.tfl.gov.uk/StopPoint/{BUS_STOP_ID}/Arrivals'
OVERGROUND_URL = f'https://api.tfl.gov.uk/StopPoint/{OVERGROUND_STATION_ID}/Arrivals'
UNDERGROUND_URL = 'https://api.tfl.gov.uk/line/mode/tube/status'

# Weather API details
WEATHER_URL = "https://data.hub.api.metoffice.gov.uk/sitespecific/v0/point/hourly"
WEATHER_PARAMS = {
    "latitude": 50,
    "longitude": 0
}
WEATHER_HEADERS = {
    "accept": "application/json",
    "apikey": "XXXXXXXXXX"  # Replace with your actual API key
}

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (228, 88, 50)

# Pygame settings
FULLSCREEN = True

# Weather code definitions
WEATHER_CODES = {
    "NA": "Not available",
    -1: "Trace rain",
    0: "Clear night",
    1: "Sunny day",
    2: "Partly cloudy (night)",
    3: "Partly cloudy (day)",
    4: "Not used",
    5: "Mist",
    6: "Fog",
    7: "Cloudy",
    8: "Overcast",
    9: "Light rain shower (night)",
    10: "Light rain shower (day)",
    11: "Drizzle",
    12: "Light rain",
    13: "Heavy rain shower (night)",
    14: "Heavy rain shower (day)",
    15: "Heavy rain",
    16: "Sleet shower (night)",
    17: "Sleet shower (day)",
    18: "Sleet",
    19: "Hail shower (night)",
    20: "Hail shower (day)",
    21: "Hail",
    22: "Light snow shower (night)",
    23: "Light snow shower (day)",
    24: "Light snow",
    25: "Heavy snow shower (night)",
    26: "Heavy snow shower (day)",
    27: "Heavy snow",
    28: "Thunder shower (night)",
    29: "Thunder shower (day)",
    30: "Thunder"
}