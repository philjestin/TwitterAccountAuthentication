#Philip Middleton
#Python script for creating a twitter account, parsing the confirmation email, and authenticating.

import imaplib
import email
import re
from bs4 import BeautifulSoup
import urllib

def extract_body(payload):
    if isinstance(payload,str):
        return payload
    else:
        return '\n'.join([extract_body(part.get_payload()) for part in payload])


def connect_to_gmail()
    conn = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    conn.login("username", "psswd")
    conn.select()
    typ, data = conn.search(None, 'UNSEEN')
    try:
        for num in data[0].split():
            typ, msg_data = conn.fetch(num, '(RFC822)')
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    subject=msg['subject']                   
                    print(subject)
                    payload=msg.get_payload()
                    body=extract_body(payload)
                    body=body.replace("<br>", '\n')
                    body=body.strip("<p>")
                    currentEmails = open('currentEmails.txt', 'w')
                    currentEmails.write(body)
                    print(body)
            typ, response = conn.store(num, '+FLAGS', r'(\Seen)')
    finally:
        try:
            conn.close()
        except:
            pass
        conn.logout()

#This function strips the url from currentEmails.txt and passes it to beautiful soup.
def obtain_url():  
    currentEmails = open('currentEmails.txt', 'r')
    count = 0
    link = ''
    for url in currentEmails:
        count += 1
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url)
        if(count==8):
            theLink = urls
            print(theLink)
            link = theLink[0]
            link = link.replace('[', '')
            link = link.replace(']', '')
            link = link.replace('\'', '')
    return link

#This function takes a string "url" and goes to the page to confirm the accounts creation
def authenticate_with_twitter(url)
    soup = BeautifulSoup(urllib.urlopen(url).read())
