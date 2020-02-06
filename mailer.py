# mailer module for ks_script
import requests


class Message(object):

    def __init__(self, subject, from_address, to, body):
        self.subject = subject 
        self.from_address = from_address
        self.to = to
        self.body = body


class Sender(object):

    def __init__(self, api_key, domain, log_file_path):
        self.api_key = api_key
        self.domain = domain
        self.log_file_path = log_file_path
        
    def send(self, Message):
        # open file for recording recipients, codes, status, and msg body.
        # File is created if it doesn't exist. Append only.
        log = open(self.log_file_path, "a+")
        try:
            requests.post(
            f"https://api.mailgun.net/v3/{self.domain}/messages",
            auth=("api", self.api_key),
            data={"from": Message.from_address,
                "to": Message.to,
                "subject": Message.subject,
                "text": Message.body})
            # write recipient, code, status, and msg body to file
            log.write(f"Recipient: {Message.to} \n\n")
        except requests.exceptions.RequestException as e:
            # write exception to same file as everything else
            log.write(f"Had error: {e} when emailing {Message.to}")

        # close log
        log.close()
        