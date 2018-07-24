""" author: feezyhendrix

    main function borcore
 """

#importing generated info
import modules.generateaccountinformation as accnt
import modules.config as config
#library import 
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % config.Config['proxy_server'])
from selenium.webdriver.common.keys import Keys
from modules.storeusernametofirebase import storeinfirebase
from time import sleep

#creating a chrome object instance to open browser
driver = webdriver.Chrome(chrome_options)

def create_account():
    try:

        driver.get('https://www.instagram.com/')

        #username 
        name = accnt.username()
        
    
        #fill the email value
        email_field = driver.find_element_by_name('emailOrPhone')
        email_field.send_keys(accnt.genEmail())

        #fill the fullname value
        fullname_field = driver.find_element_by_name('fullName')
        fullname_field.send_keys(accnt.genName())

        #fill username value
        username_field = driver.find_element_by_name('username')
        username_field.send_keys(name)

        #fill password value
        password_field  = driver.find_element_by_name('password')
        passW = accnt.generatePassword() 
        password_field.send_keys(passW)

        submit = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[6]/span/button')
        submit.click()

        print('Registering....')

        storeinfirebase(name)


        sleep(1)
        driver.close()
    except Exception as e:
       print(e);


while True:
    create_account()
