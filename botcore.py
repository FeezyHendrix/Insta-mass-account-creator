import requests


########## ACCOUNT CONFIG ##########
ig_email = 'your@email.com'
ig_username = 'username'
ig_password = 'password'
ig_firstname = 'firstname'
########## ACCOUNT CONFIG ##########

url = "https://www.instagram.com/accounts/web_create_ajax/"
headers = {
    'accept': "*/*",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "es-ES,es;q=0.9,en;q=0.8",
    'content-length': "241",
    'origin': "https://www.instagram.com",
    'referer': "https://www.instagram.com/",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36",
    'x-csrftoken': "95RsiHDyX9J6AcVz9jtCIySbwf75QhvG",
    'x-instagram-ajax': "c7e210fa2eb7",
    'x-requested-with': "XMLHttpRequest",
    'Cache-Control': "no-cache"
    }

payload = {
    'email': ig_email,
    'password': ig_password,
    'username': ig_username,
    'first_name': ig_firstname,
    'client_id': 'W6mHTAAEAAHsVu2N0wGEChTQpTfn',
    'seamless_login_enabled': '1',
    'gdpr_s': '%5B0%2C2%2C0%2Cnull%5D',
    'tos_version': 'eu',
    'opt_into_one_tap': 'false'
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
