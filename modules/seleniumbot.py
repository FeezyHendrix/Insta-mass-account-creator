""" author: feezyhendrix

    main function borcore
 """

from time import sleep
from random import randint

import modules.config as config
# importing generated info
import modules.generateaccountinformation as accnt
from modules.storeusername import store
# library import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # and Krates
import requests
import re

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
        sleep(5)
        name = accnt.username()
        # username

        # fill the email value
        email_field = driver.find_element_by_name('emailOrPhone')
        email_field.send_keys(accnt.genEmail())

        # fill the fullname value
        fullname_field = driver.find_element_by_name('fullName')
        fullname_field.send_keys(accnt.genName())

        # fill username value
        username_field = driver.find_element_by_name('username')
        username_field.send_keys(name)

        # fill password value
        password_field = driver.find_element_by_name('password')
        passW = accnt.generatePassword()
        password_field.send_keys(passW)

        submit = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[7]/div/button')
        submit.click()

        print('Registering....')
        store(name)

        sleep(4)
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


