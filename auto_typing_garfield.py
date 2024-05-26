import time
import random
import pyautogui

time.sleep(5)

def type_text(text):
    for char in text:
        if char == '\n':
            pyautogui.press('enter')
            time.sleep(random.uniform(1, 5))  # Pause between paragraphs
        else:
            pyautogui.typewrite(char)
            time.sleep(random.uniform(0.001, 0.001))  # Simulate human typing speed

# Read the text from the "Garfield.txt" file
with open("Garfield.txt", "r") as file:
    sample_text = file.read()

# Start typing the text
type_text(sample_text)
