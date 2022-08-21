import pyautogui

def autoAccept():
    '''auto accepts a game found pop up'''
    acceptButton = 'autoAccept.png'
    searching = True
    while searching:
        coords = pyautogui.locateCenterOnScreen(acceptButton)
        if coords:
            pyautogui.click(coords)
            break


autoAccept()