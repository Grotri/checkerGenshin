import pyautogui
import time
import sheetsOperations

def enterCode(code):
    pyautogui.moveTo(750, 555)
    time.sleep(0.5)
    pyautogui.click()
    pyautogui.write(code)
    time.sleep(1)
    pyautogui.moveTo(955, 675)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(3)

def enterLogPass(log, pas):
    pyautogui.moveTo(730, 390)
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.write(log)
    time.sleep(0.1)
    pyautogui.moveTo(730, 500)
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.write(pas)
    time.sleep(0.1)

def enterGame():
    time.sleep(3)
    while not pyautogui.pixelMatchesColor(701, 507, (255, 255, 255)):
        time.sleep(0.3)
    time.sleep(1)
    pyautogui.click()
    time.sleep(0.5)
    while not pyautogui.pixelMatchesColor(813, 1011, (255, 255, 255)):
        time.sleep(0.3)
    time.sleep(0.3)
    pyautogui.click()
    time.sleep(2)
    while pyautogui.pixelMatchesColor(950, 340, (255, 255, 255)):
        time.sleep(0.3)
    time.sleep(2)

def openMailandCollect():
    pyautogui.press("esc")
    while not pyautogui.pixelMatchesColor(190, 4, (234, 228, 215)):
        time.sleep(0.2)
    time.sleep(0.5)
    pyautogui.moveTo(45, 605, 0.1)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(250, 1010, 0.1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(965, 660, 0.1)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.press("esc")
    time.sleep(1)
    pyautogui.press("esc")
    time.sleep(2)

def exitAcc():
    time.sleep(1)
    pyautogui.press('esc')
    time.sleep(1)
    pyautogui.press('esc')
    time.sleep(2.5)
    pyautogui.moveTo(45, 1025)
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(0.3)
    pyautogui.moveTo(1160, 760)
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(1)
    while not pyautogui.pixelMatchesColor(1823, 883, (34, 34, 34)):
        time.sleep(0.3)
    time.sleep(2)
    pyautogui.moveTo(1820, 980)
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(0.3)
    pyautogui.moveTo(1075, 570)
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press('backspace')
    time.sleep(0.5)

def buyForDust():
    time.sleep(0.5)
    pyautogui.moveTo(150, 1020)  # open shop
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(1.5)
    pyautogui.moveTo(900, 125)  # open dust section
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(600, 315)  # click on banner rolls
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(0.5)
    buyAvail = pyautogui.pixelMatchesColor(828, 643, (255, 95, 64))
    if buyAvail == False:
        pyautogui.moveTo(740, 620)  # buy banner rolls
        time.sleep(0.1)
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.moveTo(1180, 620, 0.1)
        time.sleep(0.1)
        pyautogui.mouseUp()
        time.sleep(0.1)
        pyautogui.moveTo(1160, 760)  # apply purchase
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.3)
        pyautogui.moveTo(955, 750)
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.3)
        pyautogui.moveTo(1840, 45)  # close shop
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(1)
    else:
        pyautogui.press('esc')
        time.sleep(0.5)
        pyautogui.press('esc')
        time.sleep(1)
    return buyAvail

def buyForGoldDust():
    time.sleep(0.5)
    pyautogui.moveTo(150, 1020)  # open shop
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(1.5)
    pyautogui.moveTo(600, 315)  # click on banner rolls
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(0.5)
    buyAvail = pyautogui.pixelMatchesColor(827, 667, (255, 95, 64))
    if buyAvail == False:
        pyautogui.moveTo(740, 620)  # buy banner rolls
        time.sleep(0.1)
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.moveTo(1180, 620, 0.1)
        time.sleep(0.1)
        pyautogui.mouseUp()
        time.sleep(0.1)
        pyautogui.moveTo(1160, 760)  # apply purchase
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.3)
        pyautogui.moveTo(955, 750)
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.3)
        pyautogui.moveTo(1840, 45)  # close shop
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(1)
    else:
        pyautogui.press('esc')
        time.sleep(0.5)
        pyautogui.press('esc')
        time.sleep(1)
    return buyAvail

def doRoll(fromGems, accNum):
    while True:
        pyautogui.moveTo(1320, 1000)
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(0.2)
        if fromGems == True:
            pyautogui.moveTo(1160, 760)
            time.sleep(0.2)
            pyautogui.click()
            time.sleep(0.3)
        gemCheck = pyautogui.pixelMatchesColor(1050, 750, (74, 83, 102))
        if gemCheck:
            pyautogui.press("esc")
            time.sleep(0.3)
            break
        time.sleep(2)
        pyautogui.moveTo(1790, 40)
        time.sleep(0.3)
        pyautogui.click()
        time.sleep(0.3)
        pyautogui.click()
        global findy
        findy = 575
        while not pyautogui.pixelMatchesColor(200, findy, (255, 204, 50)):
            findy = 575
            for y in range(1, 60):
                findy += 4
                if pyautogui.pixel(200, findy) == (255, 204, 50):
                    break
        time.sleep(1)

        if pyautogui.pixelMatchesColor(360, findy, (255, 204, 50)):
            sheetsOperations.writeCheck(accNum)

        time.sleep(1)
        pyautogui.moveTo(1840, 45)
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.75)

def roll(accNum):
    accNum = accNum

    fromGems = True
    doRoll(fromGems, accNum)

    fromGems = False
    dustCheck = buyForDust()
    if not dustCheck:
        doRoll(fromGems, accNum)

    dustCheck = buyForDust()
    if not dustCheck:
        doRoll(fromGems, accNum)

    gDustCheck = buyForGoldDust()
    if not gDustCheck:
        doRoll(fromGems, accNum)

    dustCheck = buyForDust()
    if not dustCheck:
        doRoll(fromGems, accNum)

