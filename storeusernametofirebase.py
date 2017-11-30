from firebase import firebase
firebase = firebase.FirebaseApplication('https://instausergenerator.firebaseio.com', None)
def storeinfirebase(name):
    print('preparing to store username')
    print('storing.....')
    post = firebase.post('/usernames', {'username' : name})
    print('stored')
    return post