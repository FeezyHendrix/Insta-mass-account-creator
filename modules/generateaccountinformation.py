
""" author: feezyhendrix

    this module contains followers generation
 """

import random
import mechanicalsoup
import string
import logging

from .config import Config
from .getIdentity import getRandomIdentity


#generating a username
def username(identity):
    n = str(random.randint(1,99))
    name = str(identity).lower().replace(" ","")
    username = name + n
    logging.info("Username: {}".format(username))
    return(username)


#generate password
def generatePassword():
    password_characters = string.ascii_letters + string.digits
    return ''.join(random.choice(password_characters) for i in range(12))


def genEmail(username) :
    return ''.join(username + "@" + str(Config["email_domain"]))

def new_account():
    account_info = {}
    identity, gender, birthday = getRandomIdentity(country=Config["country"])
    account_info["name"] = identity
    account_info["username"] = username(account_info["name"])
    account_info["password"] = generatePassword()
    account_info["email"] = genEmail(account_info["username"])
    account_info["gender"] = gender
    account_info["birthday"] = birthday
    return(account_info)
