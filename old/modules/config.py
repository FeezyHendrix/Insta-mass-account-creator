""" author: feezyhendrix

    this is for configuration files
    notes: make sure you configure the rules in firebase
"""

""" 
    profile_per_proxy : 0 #Creates random number between 1 - 10, to create per proxy
"""

Config = {
    "password" : "generalpassword for each account created ",
    "firebase_url" : "database url",
    "proxy_server" : "proxy server", #213.168.210.76 sample proxy server to not let instagram block your ip
    "has_proxy_file" : False, #change to True to use proxy list file 
    "proxy_file" : {
        "proxy_server_txt_file_path" : "Assets/proxies.txt", # input file path
        "profile_per_proxy" : 0 , # 0 creates random of number of account per proxy found, set in between 1 - 10
    },
    "amount_of_run" : 100 #amount of time to run code
}
