import pickle
from .config import Config, ASSET_DIR

def list_created_account():
    f = open( ASSET_DIR + '/usernames.pkl', 'rb' )
    accounts = []
    try:
        while True:
            accounts.append(pickle.load(f))
    except EOFError:
        pass
    return(accounts)
