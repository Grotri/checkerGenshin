from PIL import Image
import imageTools
import pyautogui
import time
from pyclick import HumanClicker

def getFinalPixels():
    finaldir = imageTools.finalDirFinder()

    image_1 = Image.open(finaldir + 'capcrop.jpg')
    image_2 = Image.open('genshin script/process/cap.jpg')

    origx, origy = imageTools.pixelSearch(image_1, image_2)
    finalMovPixels = origx + 54

    return finalMovPixels

def openGenshin():
    pyautogui.hotkey('alt', 'tab')

def checkForFresh():
    time.sleep(3)
    if pyautogui.pixelMatchesColor(750, 700, (57, 59, 64)):
        pyautogui.moveTo(1264, 308)
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(1.5)
        pyautogui.moveTo(580, 490)
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.3)
        pyautogui.moveTo(1160, 790)
        time.sleep(0.1)
        pyautogui.click()

def screenProccesing():
    dir2 = 'genshin script/process/'
    screen = pyautogui.screenshot(region=(829, 420, 260, 120))
    checker = screen.crop((55, 0, 75, 120))
    checker.save(dir2 + 'check.jpg')
    cap = screen.crop((55, 0, 260, 120))
    cap.save(dir2 + 'cap.jpg')

def solveCap():
    pyautogui.moveTo(950, 685)
    time.sleep(0.2)
    pyautogui.leftClick()

    errorCheck = True
    while errorCheck:
        time.sleep(2.8)
        while pyautogui.pixelMatchesColor(840, 430, (255, 255, 255)):
            time.sleep(0.2)
        time.sleep(0.5)
        screenProccesing()

        movePixels = getFinalPixels()

        hc = HumanClicker()
        hc.move((856, 614), 0.75)
        time.sleep(0.2)
        pyautogui.mouseDown()
        time.sleep(0.1)
        moveProcess1 = int(856 + (movePixels / 2))
        moveProcess2 = 856 + movePixels
        hc.move((moveProcess1, 614), 0.85)
        hc.move((moveProcess2, 623), 1.35)
        time.sleep(0.1)
        pyautogui.mouseUp()

        hc.move((1770, 370), 0.7)
        time.sleep(2)
        errorCheck = pyautogui.pixelMatchesColor(900, 600, (138, 157, 202))
        if errorCheck:
            hc.move((965, 600), 0.5)
            time.sleep(0.1)
            pyautogui.click()
        time.sleep(3)
        stuckCheck = pyautogui.pixelMatchesColor(758, 735, (255, 255, 255))
        if not stuckCheck:
            hc.move((1115, 330), 0.3)
            time.sleep(0.1)
            pyautogui.click()
            time.sleep(0.3)
            hc.move((955, 680), 0.3)
            time.sleep(0.1)
            pyautogui.click()
            time.sleep(2)
            errorCheck = True

        hc.move((950, 800), 0.5)

def emailCap():
    time.sleep(3)
    mailCheck = pyautogui.pixelMatchesColor(860, 665, (57, 59, 64))
    if mailCheck:
        pyautogui.moveTo(1150, 550)
        time.sleep(0.2)
        pyautogui.leftClick()

        errorCheck = True
        while errorCheck:
            time.sleep(2.8)
            while pyautogui.pixelMatchesColor(840, 430, (255, 255, 255)):
                time.sleep(0.2)
            time.sleep(0.5)
            screenProccesing()

            movePixels = getFinalPixels()

            hc = HumanClicker()
            hc.move((856, 614), 0.75)
            time.sleep(0.2)
            pyautogui.mouseDown()
            time.sleep(0.1)
            moveProcess1 = int(856 + (movePixels / 2))
            moveProcess2 = 856 + movePixels
            hc.move((moveProcess1, 614), 1.5)
            hc.move((moveProcess2, 623), 2)
            time.sleep(0.1)
            pyautogui.mouseUp()

            hc.move((1770, 370), 0.7)
            time.sleep(2)
            errorCheck = pyautogui.pixelMatchesColor(900, 600, (138, 157, 202))
            if errorCheck:
                hc.move((965, 600), 0.5)
                time.sleep(0.1)
                pyautogui.click()

            stuckCheck = pyautogui.pixelMatchesColor(785, 320, (255, 255, 255))
            if stuckCheck:
                hc.move((1115, 330), 0.3)
                time.sleep(0.1)
                pyautogui.click()
                time.sleep(0.3)
                hc.move((1150, 550), 0.3)
                time.sleep(0.1)
                pyautogui.click()
                time.sleep(2)
                errorCheck = True

            hc.move((950, 800), 0.5)
    