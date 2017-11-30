#importing generated info
import generateaccountinformation as accnt

#library import 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from storeusernametofirebase import storeinfirebase
from time import sleep


def create_account():

    

    try:
        #creating a chrome object instance to open browser
        driver = webdriver.Chrome()

        driver.get('https://www.instagram.com/')

        #username 
        name = accnt.username()
        
        #id
        count = 0
    
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


        #skip image 
        driver.get('https://www.instagram.com/accounts/registered/')
        skip = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/button')
        skip.click()
        print('skipping...')

        #skip facebook connect
        driver.get('https://www.instagram.com/accounts/registered/1')
        skip_one = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/button')
        skip_one.click()
        print('skipping...')

        storeinfirebase(name)


        sleep(1)
        driver.close()
    except Exception as e:
        print('bot has encountered an unexpected problem')


while True:
    count = 0 
    count = count + 1
    if count is 100:
        break
    else:
        create_account()