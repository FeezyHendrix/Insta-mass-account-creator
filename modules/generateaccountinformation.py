
""" author: feezyhendrix

    this module contains followers generation
 """

import random
import mechanicalsoup
import string

from .config import Config

# generating name functions
def genName():
    return(Config["identity"])


#generating a username
def username():
    n = str(random.randint(1,99))
    name = str(Config["identity"]).lower().replace(" ","")
    username = name + n
    return(username)


#generate password
def generatePassword():
    password = str(Config["password"])
    return password


def genEmail(username) :
    return ''.join(username + "@" + str(Config["email_domain"]))
