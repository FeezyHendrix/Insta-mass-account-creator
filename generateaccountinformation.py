
""" author: feezyhendrix

    this module contains followers generation
 """

import random
import string 




def sample(items):
    
    randomIndex = random.randrange(len(items))
    return items[randomIndex]

def genName():
    boyNames = ["Jack", "Andrew", "Mike", "Terry", "Torvald", "Gatsby"]
    girlNames = ["Alice", "Hana", "Clare", "Janet", "Daisy"]
    return ''.join(sample(boyNames) + ' '  + sample(girlNames))    


def username(size = 6, chars  = string.ascii_lowercase + random.choice(['.', '_'])):
    return ''.join(random.choice(chars) for _ in range(size))



def generatePassword():
    password = 'work@1960'
    return password


def genEmail() :
    return ''.join(username() + '@mail.com')

