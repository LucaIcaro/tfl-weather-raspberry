import pygame
import threading
from gpiozero import Button
import state
from transit_functions import update_main_data, toggle_main_display
from weather_functions import update_weather_data
from display_functions import draw_main_screen, draw_weather_screen
from config import FULLSCREEN
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import ImageFont

def main():
    # Pygame setup
    pygame.init()
    pygame.mouse.set_visible(False)
    main_screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN if FULLSCREEN else 0)
    
    # Font setup for main screen
    main_font = pygame.font.Font(None, 72)
    main_small_font = pygame.font.Font(None, 60)
    
    # OLED setup
    serial = i2c(port=1, address=0x3C)
    oled_device = ssd1306(serial, width=128, height=64)
    
    # Font setup for OLED screen
    oled_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
    oled_small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
    
    # Initialize state
    state.init(main_screen, main_font, main_small_font, oled_device, oled_font, oled_small_font)

    # Button setup
    key1 = Button(4)  # Assuming KEY1 is connected to GPIO 4
    key1.when_pressed = toggle_main_display

    # Start the data update threads
    threading.Thread(target=update_main_data, daemon=True).start()
    threading.Thread(target=update_weather_data, daemon=True).start()

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        draw_main_screen()
        draw_weather_screen()
        clock.tick(1)  # 1 FPS

    pygame.quit()

if __name__ == "__main__":
    main()