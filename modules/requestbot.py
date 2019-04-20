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
    def __init__(self, email, username, password, name, numberofaccounts, use_custom_proxy, use_local_ip_address):
        self.sockets = []
        self.email = email
        self.username = username
        self.password = password
        self.name = name
        self.numberofaccounts = numberofaccounts
        self.use_custom_proxy = use_custom_proxy
        self.use_local_ip_address = use_local_ip_address
        self.url = "https://www.instagram.com/accounts/web_create_ajax/"
        self.headers = {
            'accept': "*/*",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "en-US,en;q=0.8",
            'content-length': "241",
            'content-type': 'application/x-www-form-urlencoded',
            'origin': "https://www.instagram.com",
            'referer': "https://www.instagram.com/",
            'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36",
            'x-csrftoken': "95RtiLDyX9J6AcVz9jtUIySbwf75WhvG",
            'x-instagram-ajax': "c7e210fa2eb7",
            'x-requested-with': "XMLHttpRequest",
            'Cache-Control': "no-cache",
        }
        self.__collectcrsf()
        self.__collect_sockets()

    # A function to fetch custom proxies
    def __collect_sockets(self):
        r = requests.get("https://www.sslproxies.org/")
        matches = re.findall(r"<td>\d+.\d+.\d+.\d+</td><td>\d+</td>", r.text)
        revised_list = [m1.replace("<td>", "") for m1 in matches]
        for socket_str in revised_list:
            self.sockets.append(socket_str[:-5].replace("</td>", ":"))

    def __collectcrsf(self):
        r = requests.get('https://instagram.com/accounts/emailsignup/')
        print(r)

    # Account creation function
    def createaccount(self):
        # Account creation payload
        payload = {
            'email': self.email,
            'password': self.password,
            'username': self.username,
            'first_name': self.name,
            'client_id': 'W6mHTAAEAAHsVu2N0wGEChTQpTfn',
            'seamless_login_enabled': '1',
            'gdpr_s': '%5B0%2C2%2C0%2Cnull%5D',
            'tos_version': 'eu',
            'opt_into_one_tap': 'false'
        }
        if self.use_local_ip_address is True:
            request = requests.post(self.url, data=payload, headers=self.headers)
            response = json.loads(request.text)
            print(response)
        else :
            if len(self.sockets) > 0:
                current_socket = self.sockets.pop(0)
                proxies = {"http": "http://" + current_socket, "https": "https://" + current_socket}
                try:
                    if(response["account_created"] is False):
                        if(response["errors"]["password"]):
                            print(response["errors"]["password"]["message"])
                            quit()
                        elif(response["errors"]["ip"]):
                            print(response["errors"]["ip"]["message"])
                        else:
                            pass
                        self.createaccount()
                    else:
                        pass
                except:
                    pass
            except:
                print('Error!, Trying another Proxy {}'.format(current_socket))
                self.createaccount()






def runBot():
    for i in range(Config['amount_of_account']):
        account_info = new_account(country=Config['country'])
        account = CreateAccount(
            account_info['email'],
            account_info['username'],
            account_info['password'],
            account_info['name'],
            Config['amount_of_account'])
        account.createaccount()
