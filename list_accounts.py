from modules import list_created_account

accounts = list_created_account.list_created_account()

for a in accounts:
    print("username {}\tpassword {}".format(a['username'],a['password']))
