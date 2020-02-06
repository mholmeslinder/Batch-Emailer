# ks_script.py
from sys import argv
import csv
import mailer

# since these are a little more private we pull them in from argv, 
# though if message body was sensitive enough that we didn't want to check in on github \
# then you might not want to include that in the file as well
# import codes_file
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
        subject='cool subject',
        from_address='no-reply@thing.com',
        to=recipient,
        body=f'Here is your damn {code}',)
    )

for message in messages:
    sender.send(message)

print(f'Script completed! Logs written to {log_file_path}')
