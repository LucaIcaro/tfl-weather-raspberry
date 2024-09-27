import time

# Main display variables
main_display_mode = 0  # 0: Bus, 1: Overground, 2: Underground
bus_data = []
overground_data = []
underground_data = []
main_last_update_time = time.time()
main_need_redraw = True

# Weather display variables
weather_last_update_time = time.time()
weather_need_redraw = True
weather_data_today = []
weather_data_tomorrow = []
weather_display_day = 0  # 0 for today, 1 for tomorrow

# These will be set in main.py
main_screen = None
MAIN_FONT = None
MAIN_SMALL_FONT = None
MAIN_WIDTH = 0
MAIN_HEIGHT = 0

oled_device_3c = None
oled_device_3d = None
OLED_FONT = None
OLED_SMALL_FONT = None

def init(pygame_screen, main_font, main_small_font, oled_dev_3c, oled_dev_3d, oled_font, oled_small_font):
    global main_screen, MAIN_FONT, MAIN_SMALL_FONT, MAIN_WIDTH, MAIN_HEIGHT
    global oled_device_3c, oled_device_3d, OLED_FONT, OLED_SMALL_FONT

    main_screen = pygame_screen
    MAIN_FONT = main_font
    MAIN_SMALL_FONT = main_small_font
    MAIN_WIDTH, MAIN_HEIGHT = main_screen.get_size()

    oled_device_3c = oled_dev_3c
    oled_device_3d = oled_dev_3d
    OLED_FONT = oled_font
    OLED_SMALL_FONT = oled_small_font