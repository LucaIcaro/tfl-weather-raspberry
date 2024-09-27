# tfl-weather-raspberry
This is a simple project to display MET weather forecast and TFL bus and overground stations on the OLED LCD display by waveshare

This project uses a Raspberry Pi with an OLED LCD HAT to display real-time transit information and weather forecasts. It shows bus, overground, and underground transit data on the main screen, while displaying weather information on a separate OLED screen.

## Hardware Requirements

- Raspberry Pi 3B+ (or newer)
- OLED LCD HAT peripheral with 3 screens

## Software Requirements

- Python 3.7+
- Pygame
- luma.oled
- Pillow
- requests
- python-dateutil
- gpiozero
- python-dotenv

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/LucaIcaro/tfl-weather-raspberry.git
   cd tfl-weather-raspberry
   ```

2. Install required Python packages:
   ```
   pip install pygame luma.oled pillow requests python-dateutil gpiozero python-dotenv
   ```

3. Set up your environment variables:
   - Create a `.env` file in the project root
   - Add the following lines, replacing the values with your actual API keys and location:
   ```
   TFL_API_KEY=your_tfl_api_key
   BUS_STOP_ID=your_bus_stop_id
   OVERGROUND_STATION_ID=your_overground_station_id
   WEATHER_LATITUDE=your_latitude
   WEATHER_LONGITUDE=your_longitude
   WEATHER_API_KEY=your_met_office_api_key
   ```

## File Structure

- `main.py`: Main program file, initializes displays and runs the main loop
- `state.py`: Manages shared state across the application
- `config.py`: Loads configuration from environment variables
- `transit_functions.py`: Handles transit data fetching and processing
- `weather_functions.py`: Handles weather data fetching and processing
- `display_functions.py`: Manages display logic for both main and OLED screens
- `.env`: Contains sensitive configuration data (not tracked by git)

## Usage

Run the program by executing:

```
python main.py
```

- The main screen will display transit information (bus, overground, underground)
- The OLED screens will show weather information
- Press KEY1 (GPIO 4) to cycle through different transit information on the main screen
- Press KEY2 (GPIO 17) to toggle between today's and tomorrow's weather forecast on the OLED screens

## Features

- Real-time bus arrival times
- Overground train schedules
- Underground service status
- Weather forecast for today and tomorrow, including temperature range and precipitation predictions
- Automatic updates (transit: every 30 seconds, weather: every 30 minutes)

## Customization

- To modify display layouts, edit `display_functions.py`
- To change update frequencies, modify the sleep times in `transit_functions.py` and `weather_functions.py`
- To add new data sources or modify existing ones, update the respective function files

## Troubleshooting

TBD

## Contributing

Contributions to improve the project are welcome. Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is licensed under the MIT License.
