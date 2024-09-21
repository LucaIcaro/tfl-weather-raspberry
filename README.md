# tfl-weather-raspberry
This is a simple project to display MET weather forecast and TFL bus and overground stations on the OLED LCD display by waveshare

This project uses a Raspberry Pi with an OLED LCD HAT to display real-time transit information and weather forecasts. It shows bus, overground, and underground transit data on the main screen, while displaying weather information on a separate OLED screen.

## Hardware Requirements

- Raspberry Pi 3B+ (or newer)
- OLED LCD HAT peripheral with 3 screens
- Button connected to GPIO 4

## Software Requirements

- Python 3.7+
- Pygame
- luma.oled
- Pillow
- requests
- python-dateutil
- gpiozero

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/rpi-transit-weather-display.git
   cd rpi-transit-weather-display
   ```

2. Install required Python packages:
   ```
   pip install pygame luma.oled pillow requests python-dateutil gpiozero
   ```

3. Set up your API keys:
   - Open `config.py`
   - Replace `'xxxxxx'` with your actual Met Office API key
   - Ensure your TfL API key is correct

## File Structure

- `main.py`: Main program file, initializes displays and runs the main loop
- `state.py`: Manages shared state across the application
- `config.py`: Contains configuration constants and API keys
- `transit_functions.py`: Handles transit data fetching and processing
- `weather_functions.py`: Handles weather data fetching and processing
- `display_functions.py`: Manages display logic for both main and OLED screens

## Usage

Run the program by executing:

```
python main.py
```

- The main screen will display transit information (bus, overground, underground)
- The OLED screen will show weather information
- Press the button connected to GPIO 4 to cycle through different transit information on the main screen

## Features

- Real-time bus arrival times
- Overground train schedules
- Underground service status
- Daily weather forecast including temperature range and rain predictions
- Automatic updates (transit: every 30 seconds, weather: every 30 minutes)

## Customization

- To modify display layouts, edit `display_functions.py`
- To change update frequencies, modify the sleep times in `transit_functions.py` and `weather_functions.py`
- To add new data sources or modify existing ones, update the respective function files

## Troubleshooting

If you encounter any issues:
1. Ensure all required libraries are installed
2. Check that your API keys are correct and have the necessary permissions
3. Verify that the OLED LCD HAT is properly connected and configured

## Contributing

Contributions to improve the project are welcome. Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.