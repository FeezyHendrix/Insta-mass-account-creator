from firebase import firebase
firebase = firebase.FirebaseApplication('https://instausergenerator.firebaseio.com', None)
def store(name):
    print('preparing to store username')
    print('storing.....')
    post = firebase.post('/usernames', {'username' : 'hafeez'})
    print(post)


store('boy')