"""

"""
import requests
from modules.config import Config
from modules.generateaccountinformation import new_account
import json
import re
from modules.storeusername import store


#custom class for creating accounts
class CreateAccount:
    def __init__(self, email, username, password, name, numberofaccounts, use_custom_proxy, use_local_ip_address, proxy=None):
        self.sockets = []
        self.email = email
        self.username = username
        self.password = password
        self.name = name
        self.numberofaccounts = numberofaccounts
        self.use_custom_proxy = use_custom_proxy
        self.use_local_ip_address = use_local_ip_address
        self.url = "https://www.instagram.com/accounts/web_create_ajax/"
        self.referer_url = "https://www.instagram.com/"
        self.proxy = proxy
       
        self.__collect_sockets()

    # A function to fetch custom proxies
    def __collect_sockets(self):
        r = requests.get("https://www.sslproxies.org/")
        matches = re.findall(r"<td>\d+.\d+.\d+.\d+</td><td>\d+</td>", r.text)
        revised_list = [m1.replace("<td>", "") for m1 in matches]
        for socket_str in revised_list:
            self.sockets.append(socket_str[:-5].replace("</td>", ":"))

    # def __collectcrsf(self):
    #     r = requests.get('https://instagram.com/accounts/emailsignup/')
    #     print(r)

    # Account creation function
    def createaccount(self):
        # Account creation payload
        payload = {
            'email': self.email,
            'password': self.password,
            'username': self.username,
            'first_name': self.name,
           'seamless_login_enabled' : '1',
            'tos_version' : 'row',
            'opt_into_one_tap' : 'false'
        }

        """
            Check if to use local ip address to create account, then create account based on the amount set in the config.py
        """
        if self.use_local_ip_address is True:
            session = requests.Session()
            try: 
                session_start = session.get(self.url);
                session.headers.update({'referer' : self.referer_url,'x-csrftoken' : session_start.cookies['csrftoken']})

                create_request = session.post(self.url, data=payload, allow_redirects=True)
                session.headers.update({'x-csrftoken' : session_start.cookies['csrftoken']})
                response_text = create_request.text
                response = json.loads(create_request.text)
                print(response)
            except Exception as e:
                print(e)
                print("---Request Bot --- An error occured while creating account with local ip address")

        elif self.use_custom_proxy is True:
            try: 
                session = requests.Session()
                if(self.proxy is not None):
                    try: 
                        session_start = session.get(self.url,   proxies={'http' : self.proxy, 'https' : self.proxy})
                        session.headers.update({'referer' : self.referer_url,'x-csrftoken' : session_start.cookies['csrftoken']})

                        create_request = session.post(self.url, data=payload, allow_redirects=True)
                        session.headers.update({'x-csrftoken' : session_start.cookies['csrftoken']})
                        response_text = create_request.text
                        response = json.loads(create_request.text)
                        print(response)
                    except Exception as e:
                        print(e)
                        print("---Request Bot --- An error occured while creating account with custom proxy")
                else: 
                    raise Exception('---Request Bot --- Proxy must to added to proxies.txt list')

                session.get(self.url)
            except Exception as e:
                 print(e)
                 print("---Request Bot --- An error occured while creating account with custom proxy")
        else:
            if len(self.sockets) > 0:
                current_socket = self.sockets.pop(0)
                proxies = {"http": "http://" + current_socket, "https": "https://" + current_socket}
                session = requests.Session()
                try:
                    session_start = session.get(self.url,   proxies=proxies);
                    session.headers.update({'referer' : self.referer_url,'x-csrftoken' : session_start.cookies['csrftoken']})

                    create_request = session.post(self.url, data=payload, allow_redirects=True)
                    session.headers.update({'x-csrftoken' : session_start.cookies['csrftoken']})
                    response_text = create_request.text
                    response = json.loads(create_request.text)
                    print(response)
                except Exception as e:
                    print(e)
                    print("---Request Bot --- An error occured while creating account with fetched proxy")
        





def runBot():
    for i in range(Config['amount_of_account']):
       
        if(Config['use_custom_proxy'] == True):
             with open(Config['proxy_file_path'], 'r') as file:
                content = file.read().splitlines()
                for proxy in content:
                    account_info = new_account()
                    account = CreateAccount(
                        account_info['email'],
                        account_info['username'],
                        account_info['password'],
                        account_info['name'],
                        Config['amount_of_account'], 
                        Config['use_custom_proxy'], 
                        Config['use_local_ip_address'],proxy=proxy)
                    account.createaccount()
        else :
            account_info = new_account()
            account = CreateAccount(
                account_info['email'],
                account_info['username'],
                account_info['password'],
                account_info['name'],
                Config['amount_of_account'], 
                Config['use_custom_proxy'], 
                Config['use_local_ip_address'])
            account.createaccount()
