
import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.3

# abrir o navegador (chrome)

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link 
pyautogui.write("https://meurh.bomfuturo.com.br/rm/web/app/RH/PortalMeuRH/#/login")
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=522, y=782)
time.sleep(5)

pyautogui.click(x=69, y=339)
time.sleep(1)
pyautogui.click(x=59, y=430)
time.sleep(2)

# pyautogui.doubleClick(x=1098, y=574) 
# time.sleep(7)

for i in range(4):
    pyautogui.hotkey("ctrl", "f4")
    time.sleep(1)

pyautogui.hotkey("ctrl","f4")
pyautogui.press("enter")







