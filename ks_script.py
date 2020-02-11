# ks_script.py - 
from sys import argv
import csv
import mailer

# take sensitive info as arguments
# order = api_key, domain, csv with recipients and codes, and filepath to logfile
_, api_key, domain, codes_file, log_file_path = argv
sender = mailer.Sender(api_key=api_key, domain=domain, log_file_path=log_file_path)

# open csv, create download code:recipient mapping inside this script
pairs = {}
with open(codes_file) as csvfile:
    read_csv = csv.reader(csvfile, delimiter=',')
    for row in read_csv:
        pairs[row[1]] = row[0] 

messages = []
for recipient, code in pairs.items():
    messages.append(mailer.Message(
        # Just plug in your subject 
        subject='cool subject',
        # desired from-address (where the email is coming from)
        from_address='no-reply@thing.com',
        to=recipient,
        # Email body - use {code} where you want to put the Bandcamp code
        body=f'Here is your damn {code}',)
    )

for message in messages:
    sender.send(message)

print(f'Script completed! Logs written to {log_file_path}')
