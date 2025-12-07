import pyautogui
import time
import pyperclip
import os

pyautogui.moveTo(1243, 234, 0.2)
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("서울 날씨")
pyautogui.hotkey("command", "v") # 윈도우는 ctrl
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)

start_x = 855
start_y = 325
end_x = 1566
end_y = 863

file_path = os.path.join(os.path.dirname(__file__), '서울날씨.png')
screenshot = pyautogui.screenshot(file_path, region=(start_x, start_y, end_x - start_x, end_y - start_y))
screenshot.save(file_path)
