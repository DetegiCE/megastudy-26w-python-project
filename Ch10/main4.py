import pyautogui
import time
import pyperclip
import os

weather = ['서울 날씨', '부산 날씨', '대구 날씨', '인천 날씨', '광주 날씨']

addr_x = 1011
addr_y = 101
start_x = 855
start_y = 325
end_x = 1566
end_y = 863

for local in weather:
    pyautogui.moveTo(addr_x, addr_y, 1)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.write("www.naver.com", interval=0.1)
    pyautogui.write(["enter"])
    time.sleep(1)

    pyperclip.copy(local)
    pyautogui.hotkey("command", "v") # 윈도우는 ctrl
    time.sleep(0.5)
    pyautogui.write(["enter"])
    time.sleep(1)

    file_path = os.path.join(os.path.dirname(__file__), local + '.png')
    screenshot = pyautogui.screenshot(file_path, region=(start_x, start_y, end_x - start_x, end_y - start_y))
    screenshot.save(file_path)
