import pygame
import time
import state
from config import ORANGE
from luma.core.render import canvas

def draw_main_screen():
    if not state.main_need_redraw:
        return

    state.main_screen.fill((0, 0, 0))  # Black background

    if state.main_display_mode == 0:
        title = "Bus Times"
        data = state.bus_data
    elif state.main_display_mode == 1:
        title = "Overground Times"
        data = state.overground_data
    else:
        title = "Underground Status"
        data = state.underground_data

    title_surface = state.MAIN_FONT.render(title, True, ORANGE)
    state.main_screen.blit(title_surface, (10, 10))

    if state.main_display_mode == 2 and len(data) == 1 and data[0] == "Good service on all lines":
        text_surface = state.MAIN_SMALL_FONT.render(data[0], True, (0, 255, 0))  # Green text for good service
        state.main_screen.blit(text_surface, (10, 50))
    else:
        for i, line in enumerate(data):
            text_surface = state.MAIN_SMALL_FONT.render(line, True, ORANGE)
            state.main_screen.blit(text_surface, (10, 65 + i * 40))  # Adjusted y-coordinate for more lines

    update_time = time.strftime("%H:%M:%S", time.localtime(state.main_last_update_time))
    time_surface = state.MAIN_SMALL_FONT.render(f"Last updated: {update_time}", True, (200, 200, 200))
    state.main_screen.blit(time_surface, (10, state.MAIN_HEIGHT - 30))

    pygame.display.flip()
    state.main_need_redraw = False

def wrap_text(text, font, max_width):
    words = text.split()
    lines = []
    current_line = []
    for word in words:
        test_line = ' '.join(current_line + [word])
        if font.getlength(test_line) <= max_width:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
    if current_line:
        lines.append(' '.join(current_line))
    return lines

def draw_weather_screens():
    if not state.weather_need_redraw:
        return

    weather_data = state.weather_data_today if state.weather_display_day == 0 else state.weather_data_tomorrow
    day_str = "Today" if state.weather_display_day == 0 else "Tomorrow"

    # First OLED screen (0x3C)
    with canvas(state.oled_device_3c) as draw:
        draw.text((0, 0), f"{day_str}'s Weather", font=state.OLED_FONT, fill="white")

        y_offset = 16
        for line in weather_data[:3]:  # Display first 3 lines on this screen
            draw.text((0, y_offset), line, font=state.OLED_SMALL_FONT, fill="white")
            y_offset += 12

        update_time = time.strftime("%H:%M", time.localtime(state.weather_last_update_time))
        draw.text((0, 54), f"Updated: {update_time}", font=state.OLED_SMALL_FONT, fill="white")

    # Second OLED screen (0x3D)
    with canvas(state.oled_device_3d) as draw:
        if len(weather_data) > 3:
            draw.text((0, 0), f"{day_str} (cont.)", font=state.OLED_FONT, fill="white")

            y_offset = 16
            for line in weather_data[3:]:  # Display remaining lines on this screen
                draw.text((0, y_offset), line, font=state.OLED_SMALL_FONT, fill="white")
                y_offset += 12
                if y_offset >= 54:  # Stop if we're about to overlap with the bottom of the screen
                    break
        else:
            draw.text((0, 0), f"{day_str}'s Weather", font=state.OLED_FONT, fill="white")
            draw.text((0, 16), "No precipitation", font=state.OLED_SMALL_FONT, fill="white")
            draw.text((0, 28), "or extreme weather", font=state.OLED_SMALL_FONT, fill="white")
            draw.text((0, 40), "expected", font=state.OLED_SMALL_FONT, fill="white")

    state.weather_need_redraw = False
