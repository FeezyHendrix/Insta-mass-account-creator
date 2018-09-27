from firebase import firebase
from .config import Config

firebase = firebase.FirebaseApplication(str(Config['firebase_url']), None)
def storeinfirebase(name):
    print('preparing to store username')
    print('storing.....')
    post = firebase.post('/usernames', {'username' : name})
    print('stored')
    return post