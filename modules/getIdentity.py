import mechanicalsoup

def getRandomIdentity(country):
    URL = "https://it.fakenamegenerator.com/gen-random-{}-{}.php".format(country,country)
    browser = mechanicalsoup.StatefulBrowser(
        raise_on_404=True,
        user_agent='MyBot/0.1'
    )
    page = browser.get(URL)
    address_div = page.soup.find(
        "div",
        { "class": "address" }
    )
    completename = address_div.find(
        "h3"
    )

    return(completename.contents[0])
