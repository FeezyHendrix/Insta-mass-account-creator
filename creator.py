from modules.config import Config
from modules.seleniumbot import runbot
from modules.requestbot import runBot

def accountCreator():
    if Config['bot_type'] == 1:
        runbot()
    else:
        runBot()


accountCreator()
