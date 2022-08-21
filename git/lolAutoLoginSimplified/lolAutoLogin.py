import pyautogui, mouse, time


filename = 'login.txt'


def arraymaking(filename):
    '''takes txt file with logins and passwords and puts them in the array'''
    allLoginArray = []
    with open(filename, 'r') as logintxt:
        for line in logintxt:
            allLoginArray.append(line.strip().split(' '))
    return allLoginArray


def menu(allLoginArray):
    '''makes a menu using an array from arraymaking function'''
    menuNumber = 1
    print('Which account do you want to log into?')
    for i in range(len(allLoginArray)):
        print(str(menuNumber) + ': '+ allLoginArray[i][0])
        menuNumber += 1
    accountChoice = input('Select the coresponding number: ')

    return [int(accountChoice)]


def whatToDoWithAccountChoice(allLoginArray, choice):
    '''puts in login and password, takes login array and your choice as parameters'''
    for i in range(len(allLoginArray)+1):
        if i == choice:
            time.sleep(1)
            mouse.move(330, 370, absolute=True, duration=0)
            mouse.click('left')
            pyautogui.write(allLoginArray[i-1][0])
            time.sleep(0.3)
            mouse.move(330, 430, absolute=True, duration=0)
            mouse.click('left')
            pyautogui.write(allLoginArray[i-1][1])
            break


def altTab():
    '''alt tab'''
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')


def pressLogin():
    '''presses login button'''
    mouse.move(390, 800, absolute=True, duration=0)
    mouse.click('left')


def allFunctionsCombined():
    allLoginArray = arraymaking(filename)
    choices = menu(allLoginArray)
    altTab()
    whatToDoWithAccountChoice(allLoginArray,choices[0])
    pressLogin()

allFunctionsCombined()

