# Mobius Trio Kickstarter 2019 Bandcamp code sender
import requests
import csv
from sys import argv

# Take API key and csv file as arguments
# _, domain, codes_file, key = argv
# domain = 'mail.mobiustrio.org'

# TODO create Loader
class Loader(object):

    def __init__(self):
        # Take API key and csv file as arguments
        self._, self.domain, self.codes_file, self.key = argv
        # open csv and put recipients and codes into lists
        self.pairs = {}
        with open(self.codes_file) as csvfile:
            read_csv = csv.reader(csvfile, delimiter=',')
            for row in read_csv:
                self.pairs[row[1]] = row[0]



# TODO create Sender
class Sender(object):

    def __init__(self):
    # open file for recording recipients, codes, status, and msg body.
    # File is created if it doesn't exist. Append only.
        self.log = open("./ignore/log_file.txt", "a+")
        self.subject = "A Bandcamp download code for Bon Voyage"
        
    def send_batch_message(self, Loader):
        # Take pairs dict and send email to recipient with code in body
        for recipient, code in Loader.pairs.items():
            try:
                return requests.post(
                f"https://api.mailgun.net/v3/{Loader.domain}/messages",
                auth=("api", Loader.key),
                data={"from": f"mail@{Loader.domain}>",
                    "to": [recipient],
                    "subject": self.subject,
                    "text": f"""
Hello, wonderful Kickstarter backer! You wanted a digital download of our new album Bon Voyage,
so here is a code to download it from Bandcamp: {code}\n\n
The way it works is: you navigate to http://mobiustrio.bandcamp.com/yum , and then you enter the code! 
It's as simple as that. We hope you love it.

Love,
The Guys at Mobius Trio
"""})
                # write recipient, code, status, and msg body to file
                self.log.write(f"Recipient: {recipient} {requests.status}\n\n")
            except requests.exceptions.RequestException as e:
                # print exception to same file as everything else
                self.log.write(f"Had error: {e} when emailing {recipient}")
                continue
        # close log
        self.log.close()

msg_data = Loader()
msg_send = Sender()
msg_send.send_batch_message(msg_data)