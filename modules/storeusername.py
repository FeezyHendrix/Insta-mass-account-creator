from .config import Config, ASSET_DIR


def store(username): 
    file = open( ASSET_DIR + '/usernames.txt', 'a+')
    print("storing username")
    file.write(username  + ', \n')
    file.close()
    print("stored")

