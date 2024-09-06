import pygetwindow as gw
import pyautogui
import time
from PIL import Image

def screenshot_window(window_title, output_filename):
    # Get Mabinogi window
    window = gw.getWindowsWithTitle(window_title)

    if not window:
        print(f"'{window_title}' not found.")
        return
    
    # Get first matching window
    window = window[0]

    # Activate the window to bring it to the foreground
    window.activate()

    # Delay to get Mabinogi window
    time.sleep(1)

    # Get the window's bounding box
    left, top, right, bottom = window.left, window.top, window.right, window.bottom

    # Take screenshot
    screenshot = pyautogui.screenshot(region=(left, top, right-left, bottom-top))

    # Save screenshot
    screenshot.save(output_filename)
    print(f"Screenshot saved as '{output_filename}'")

window_title = "Mabinogi"
output_filename = "mabi_screenshot.png"
screenshot_window(window_title, output_filename)