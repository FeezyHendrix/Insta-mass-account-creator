from .config import Config, ASSET_DIR
import logging
import pickle

def store(account):
    with open(ASSET_DIR + '/usernames.pkl', 'a+') as f:
        logging.info("Storing username {}".format(account['username']))
        logging.info(account)
        pickle.dump(account, f, pickle.HIGHEST_PROTOCOL)
