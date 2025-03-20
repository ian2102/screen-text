import subprocess
import pytesseract
from PIL import ImageGrab
import pyperclip
import keyboard
import time
import winsound

# Set as needed.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def take_screenshot():
    subprocess.Popen('%windir%\explorer.exe ms-screenclip:', shell=True)
    
    screenshot = None
    print("Waiting for screenshot to be available in clipboard...")

    while screenshot is None:
        try:
            screenshot = ImageGrab.grabclipboard()
            if screenshot is not None:
                break
        except OSError:
            pass
        time.sleep(0.2)

    return screenshot

def run():
    pyperclip.copy("")  # Empty the clipboard to ensure the correct image is parsed.

    screenshot = take_screenshot()
    if screenshot:
        text = pytesseract.image_to_string(screenshot)
        pyperclip.copy(text)
        print("Text copied to clipboard.")
        winsound.Beep(1000, 200)  # Beep at 1000 Hz for 200 milliseconds.
    else:
        print("No screenshot found in the clipboard or failed to capture.")

if __name__ == '__main__':
    print("Press 'Windows + Shift + C' to take a screenshot and extract text.")
    keyboard.add_hotkey('shift+windows+c', run)
    keyboard.wait('esc')
