from .config import Config, ASSET_DIR
import logging
import pickle
import csv

def store(account):
    with open(ASSET_DIR + '/usernames.pkl', 'ab') as f:
        logging.info("Storing username {}".format(str(account['username'])))
        logging.info(str(account))
        pickle.dump(str(account), f, pickle.HIGHEST_PROTOCOL)

    # storing username.csv file
    with open('usernames.csv', 'w', newline='') as file:
        logging.info("Storing username {}".format(str(account['username'])))
        logging.info(str(account))
        writer = csv.writer(file)
        writer.writerow(["Name", "Username", "Password", "Email", "Gender", "Birthday"])
        writer.writerow([
            account["name"], 
            account["username"], 
            account["password"], 
            account["email"],
            account["gender"],
            account["birthday"]
        ])
