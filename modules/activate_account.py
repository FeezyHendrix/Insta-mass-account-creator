# import re
# import time
# import logging
# #import sys
# #sys.path.insert(0, "/Users/matte/Projects/My/pymailutils")
# from pymailutils import Imap, Email
# from bs4 import BeautifulSoup

# from .config import Config


# imaphost = Config['activation_email_serv']
# imapport = Config['activation_email_spor']
# watchedemail_add = Config['activation_email_addr']
# watchedemail_pwd = Config['activation_email_pass']

# def get_activation_url(email):
#     pattern = '(TO ' + email + ' )'
#     attempt = 0
#     with Imap( imaphost, port=imapport, username=watchedemail_add, password=watchedemail_pwd ) as imap:
#         for x in range(0, 3):
#             mails = imap.search( pattern )
#             for uid in mails:
#                 logging.info("fetching id {}".format(uid))
#                 msg = imap.fetch_with_uid(uid, mailbox="INBOX")
#                 with Email() as e:
#                     email_body = e.get_body(msg[0][1])

#                     page = BeautifulSoup(email_body, "html.parser")
#                     links = page.find_all("a", href=re.compile("https://instagram.com/accounts/confirm_email"))
#                     confirmurl = re.search("https://(.*)", links[0]['href']).group()
#                     return(confirmurl)
#                     break
#             logging.info("No emails found, sleeping 3 seconds")
#             time.sleep(5)
#         raise Exception('Confirm Url doesn\'t find in mailbox')
