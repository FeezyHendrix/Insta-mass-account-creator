""" author: feezyhendrix

    main function borcore
 """

from time import sleep
from random import randint

import modules.config as config
# importing generated info
import modules.generateaccountinformation as accnt
from modules.storeusername import store
from activate_account import get_activation_url
# library import
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys  # and Krates
import requests
import re
import logging

from pymailutils import Imap

class AccountCreator():
    def __init__(self, use_custom_proxy, use_local_ip_address):
        self.sockets = []
        self.use_custom_proxy = use_custom_proxy
        self.use_local_ip_address = use_local_ip_address
        self.url = 'https://www.instagram.com/'
        self.__collect_sockets()

    def __collect_sockets(self):
        r = requests.get("https://www.sslproxies.org/")
        matches = re.findall(r"<td>\d+.\d+.\d+.\d+</td><td>\d+</td>", r.text)
        revised_list = [m1.replace("<td>", "") for m1 in matches]
        for socket_str in revised_list:
            self.sockets.append(socket_str[:-5].replace("</td>", ":"))

    def createaccount(self, proxy=None):
        chrome_options = webdriver.ChromeOptions()
        if proxy != None:
            chrome_options.add_argument('--proxy-server=%s' % proxy)

        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get(self.url)
        action_chains = ActionChains(driver)
        sleep(5)
        # username
        account_info = accnt.new_account()

        # fill the email value
        email_field = driver.find_element_by_name('emailOrPhone')
        action_chains.move_to_element(email_field)
        email_field.send_keys(account_info["email"])

        sleep(2)

        # fill the fullname value
        fullname_field = driver.find_element_by_name('fullName')
        action_chains.move_to_element(fullname_field)
        fullname_field.send_keys(account_info["name"])

        sleep(2)

        # fill username value
        username_field = driver.find_element_by_name('username')
        action_chains.move_to_element(username_field)
        username_field.send_keys(account_info["username"])

        sleep(2)

        # fill password value
        password_field = driver.find_element_by_name('password')
        action_chains.move_to_element(password_field)
        passW = account_info["password"]
        password_field.send_keys(passW)

        sleep(2)

        submit = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[7]/div/button')

        action_chains.move_to_element(submit)

        sleep(2)
        submit.click()

        sleep(3)

        age_button = driver.find_element_by_xpath( "//input[@name='ageRadio' and @value='above_18']")
        age_button.click()

        sleep(2)
        next_button = driver.find_elements_by_xpath('//button[text()="Next"]')[1]
        next_button.click()

        sleep(4)
        # After the first fill save the account account_info
        store(account_info)

        # Activate the account
        confirm_url = get_activation_url(account_info['email'])
        logging.info("The confirm url is {}".format(confirm_url))
        driver.get(confirm_url)

        driver.close()

    def creation_config(self):
        try:
            if self.use_local_ip_address == False:
                if self.use_custom_proxy == False:
                    for i in range(0, config.Config['amount_of_account']):
                        if len(self.sockets) > 0:
                            current_socket = self.sockets.pop(0)
                            try:
                                self.createaccount(current_socket)
                            except Exception as e:
                                print('Error!, Trying another Proxy {}'.format(current_socket))
                                self.createaccount(current_socket)

                else:
                    with open(config.Config['proxy_file_path'], 'r') as file:
                        content = file.read().splitlines()
                        for proxy in content:
                            amount_per_proxy = config.Config['amount_per_proxy']

                            if amount_per_proxy != 0:
                                print("Creating {} amount of users for this proxy".format(amount_per_proxy))
                                for i in range(0, amount_per_proxy):
                                    try:
                                        self.createaccount(proxy)

                                    except Exception as e:
                                        print("An error has occured" + e)

                            else:
                                random_number = randint(1, 20)
                                print("Creating {} amount of users for this proxy".format(random_number))
                                for i in range(0, random_number):
                                    try:
                                        self.createaccount(proxy)
                                    except Exception as e:
                                        print(e)
            else:
                for i in range(0, config.Config['amount_of_account']):
                            try:
                                self.createaccount()
                            except Exception as e:
                                print('Error!, Check its possible your ip might be banned')
                                self.createaccount()


        except Exception as e:
            print(e)


def runbot():
    account = AccountCreator(config.Config['use_custom_proxy'], config.Config['use_local_ip_address'])
    account.creation_config()
