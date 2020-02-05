# Mobius Trio Kickstarter 2019 Bandcamp code sender
import requests
import csv
from sys import argv

class Message(object):

    def __init__(self):
        # Take API key and csv file as arguments
        self._, self.domain, self.codes_file, self.key = argv
        # open csv and put recipients and codes into lists
        self.pairs = {}
        with open(self.codes_file) as csvfile:
            read_csv = csv.reader(csvfile, delimiter=',')
            for row in read_csv:
                self.pairs[row[1]] = row[0]
        self.subject = "A Bandcamp download code for Bon Voyage"


class Sender(object):

    def __init__(self):
        pass
        
    def send_batch_message(self, Message):
        # open file for recording recipients, codes, status, and msg body.
        # File is created if it doesn't exist. Append only.
        log = open("./ignore/log_file.txt", "a+")
        # Take pairs dict and send email to recipient with code in body
        for recipient, code in Message.pairs.items():
            body = f"""
Hello, wonderful Kickstarter backer! You wanted a digital download of our new album Bon Voyage,
so here is a code to download it from Bandcamp: {code}\n\n
The way it works is: you navigate to http://mobiustrio.bandcamp.com/yum, and then you enter the code!
It's as simple as that. We hope you love it.

Love,
The Guys at Mobius Trio
""" 
            try:
                requests.post(
                f"https://api.mailgun.net/v3/{Message.domain}/messages",
                auth=("api", Message.key),
                data={"from": f"mail@{Message.domain}",
                    "to": recipient,
                    "subject": Message.subject,
                    "text": body})
                # write recipient, code, status, and msg body to file
                log.write(f"Recipient: {recipient} \n\n")
            except requests.exceptions.RequestException as e:
                # write exception to same file as everything else
                log.write(f"Had error: {e} when emailing {recipient}")
                continue
        # close log
        log.close()

msg_data = Message()
msg_send = Sender()
msg_send.send_batch_message(msg_data)
