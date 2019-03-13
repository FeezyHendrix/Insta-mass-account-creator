"""
    author: feezyhendrix

    Configuration files
    NOTE: check Assets/proxies.txt to use your custom proxies.
 """
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSET_DIR = os.path.join(BASE_DIR, 'Assets' )

Config = {
    # Default is 1 using the selenium bot, choose 2 to use python requests.
    "bot_type" : 2,
    # General Account password.
    "password" : "work@1960",
    # Default is False, change to True to use a file containing multiple proxies of yours.
    "use_custom_proxy" : False,
    # Default is False, change to True to use your computers ip directly.
    "use_local_ip_address" : True,
    # Amount of account you want to create.
    "amount_of_account": 10,
    # If you are using multiple proxy, amount of account to be created which proxy.
    "amount_per_proxy": 10,
    # Default path to proxy, change to a file path pointing to your proxy.
    "proxy_file_path" : ASSET_DIR + "/proxies.txt"
}
