import pyautogui
import time
from datetime import datetime

def close_popup(window_title):
    # Espera hasta que la ventana emergente aparezca
    window = pyautogui.getWindowsWithTitle(window_title)
    if window:
        window = window[0]
        if window.isActive:
            pyautogui.press('esc')  
            print(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}: Popup '{window_title}' cerrado.")

        else:
            try:
                window.activate()
                pyautogui.press('esc')  
                print(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}: Popup '{window_title}' cerrado.")
            except Exception:
                time.sleep(1)

# Ejecución continua en segundo plano
while True:
    close_popup("About C1TrueDBGrid")
    close_popup("About C1FlexGrid")
    close_popup("About Input")
    close_popup("About Command")
    close_popup("About C1Excel")
    close_popup("About C1InputPanel")
    close_popup("About C1.Win.FlexViewer")
    close_popup("About C1.Win.C1Document")
    close_popup("About C1.C1Pdf")