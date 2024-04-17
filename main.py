import capSolver
import sheetsOperations
import ingameMovements
import time
import pyautogui

accNum = int(input('Enter start acc number: ')) + 1
totalAccs = int(input('Enter total amount of accs: ')) + 1

capSolver.openGenshin()

while accNum <= totalAccs:
    log = sheetsOperations.getLogin("M" + str(accNum))
    pas = sheetsOperations.getPass("N" + str(accNum))

    ingameMovements.enterLogPass(log, pas)
    time.sleep(0.1)

    capSolver.solveCap()

    capSolver.checkForFresh()

    ingameMovements.enterGame()

    ingameMovements.openMailandCollect()

    time.sleep(2)
    pyautogui.press("f3")
    time.sleep(2.5)
    ingameMovements.roll(accNum)

    ingameMovements.exitAcc()

    print('Acc ', accNum, ' has been rolled smooth')

    accNum += 1








