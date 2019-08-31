from .config import Config, ASSET_DIR
import logging
import pickle

def store(account):
    with open(ASSET_DIR + '/usernames.pkl', 'ab') as f:
        logging.info("Storing username {}".format(str(account['username'])))
        logging.info(str(account))
        pickle.dump(str(account), f, pickle.HIGHEST_PROTOCOL)
