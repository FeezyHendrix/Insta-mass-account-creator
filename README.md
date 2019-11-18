# Insta Mass Account creator
![Version](https://img.shields.io/badge/version-1.1.0-brightgreen.svg?style=flat-square)
![Version](https://img.shields.io/badge/release-beta-green.svg?style=flat-square)

#### Actively not being maintained, due to different challenges. if you would like to maintain this project contact me!

Create a new virtualenv

- Requirements:<br>
  - run `pip install -r requirements.txt`
<br>
Download chrome driver<br>
configure it to path<br>



## Configuration
open config.py in modules

| Config               | Usage                                                                                                |
| :------------------- | :--------------------------------------------------------------------------------------------------- |
| chromedriver_path    | Path to chromedriver                                                                                 |
| bot_type             | Default is 1 to use selenium to create accounts or use 2 to use python requests                      |
| password             | General password for Each account generated to be able to login                                      |
| use_local_ip_address | using local Ip to create account, default is False                                                   |
| use_custom_proxy     | use your own custom proxy, Default is False change to True add list of proxies to Assets/proxies.txt |
| amount_of_account    | amount of account to create                                                                          |
| proxy_file_path      | Path to the proxy file .txt format                                                                   |
| amount_per_proxy     | for custom proxy, amount of account to create for each proxy                                         |
| email_domain         | for custom domain name, is useful for use own email_domain                                           |
| country              | the country of account                                                                               |
| identity             | the complete name of created accounts                                                                |

run <strong>`python creator.py`</strong>
<br>
All username are stored in Assets/usernames.txt

### Features
this script create account with random name get by the web and doesn't use random name or random usernames. All user created are older 18 years

### Important
-  The new fake Instagram account with an unverified phone number after ~ 1-24 hours could not do any requests. All requests will be redirected to the page           
<a href="https://instagram.com/challenge">https://instagram.com/challenge</a>

### contribution
- Fork this repo.
- Add new features.
- Create a new pull request for this branch.


### Credits
[Matteo Gaito](https://github.com/matteogaito)
