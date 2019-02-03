import mechanicalsoup
import random
import logging

def getRandomIdentity(country):
    gender = random.choice(["male", "female"])
    logging.info("Gender: {}".format(gender))
    URL = "https://it.fakenamegenerator.com/gen-{}-{}-{}.php".format(gender,country,country)
    logging.info("Url generated: {}".format(URL))
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

    extra_div = page.soup.find(
        "div",
        { "class": "extra" }
    )

    all_dl = page.soup.find_all(
        "dl",
        {'class':'dl-horizontal'}
    )

    birthday = all_dl[5].find("dd").contents[0]
    logging.info("Birthday: {}".format(birthday))

    return(completename.contents[0],gender, birthday)
