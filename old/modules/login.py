  #login the created account
    driver.get('https://www.instagram.com/accounts/login/')
    login_username = driver.find_element_by_name('username')
    login_username.send_keys('wsbcwe')
    login_password = driver.find_element_by_name('password')
    login_password.send_keys('work@1960')

    login_btn = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/span/button')
    login_btn.click()
    print('logging in ......im bad like that')
    sleep(2)
    

    #follow user 
    usertofollow = 'feezyhendrix'
    driver.get('https://www.instagram.com/' + usertofollow)
    
