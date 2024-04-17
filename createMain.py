import ingameMovements
import time
import pyautogui
import accCreatorTool
import keyboard
import capSolver
import browserAutomation

key = 'b'
while True:
    if keyboard.is_pressed(key):
        with open('bot.txt') as f:
            lines = [line.rstrip('\n') for line in f]
        for i in lines:

            log, pas = i.split()
            ingameMovements.enterLogPass(log, pas)
            time.sleep(0.1)

            capSolver.solveCap()
            capSolver.emailCap()
            code = browserAutomation.getCode(log, pas)
            ingameMovements.enterCode(code)
            capSolver.checkForFresh()


            pyautogui.moveTo(955, 720)

            ingameMovements.enterGame()

            accCreatorTool.enterGameAndFinishTutorial()

            accCreatorTool.fromFirstStatueToDungsQuests()

            accCreatorTool.threeDungeons()

            accCreatorTool.teleports()

            accCreatorTool.anemoculuses()

            accCreatorTool.chests()

            accCreatorTool.finish10LV()

            time.sleep(2)

            pyautogui.press('f6')
            time.sleep(1)
            pyautogui.press('f7')
            time.sleep(1)




