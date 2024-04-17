import pygsheets

def getLogin(logIndex):
    auth = pygsheets.authorize('client_secret.json')
    db = auth.open("Genshin Impact")
    tempsheet = db.worksheet_by_title('Temporary')
    login = tempsheet.get_value(logIndex)

    return login

def getPass(passIndex):
    auth = pygsheets.authorize('client_secret.json')
    db = auth.open("Genshin Impact")
    tempsheet = db.worksheet_by_title('Temporary')
    passw = tempsheet.get_value(passIndex)

    return passw

def writeCheck(accNum):
    auth = pygsheets.authorize('client_secret.json')
    db = auth.open("Genshin Impact")
    tempsheet = db.worksheet_by_title('Temporary')
    tempsheet.update_value('O' + str(accNum), 'CHECK')
