# Mobius Trio Kickstarter 2019 Bandcamp code sender
# TODO Implement OOP version
import requests
import csv
from sys import argv

# Take API key and csv file as arguments
_, domain, codes_file, key = argv

# open csv and put recipients and codes into lists
pairs = {}
with open(codes_file) as csvfile:
    read_csv = csv.reader(csvfile, delimiter=',')
    for row in read_csv:
        pairs[row[1]] = row[0]

request_url = f'https://api.mailgun.net/v2/{domain}/messages'

# open file for recording recipients, codes, status, and msg body. File is created if it doesn't exist. Append only.
log = open("./ignore/log_file.txt", "a+")
# Take pairs dict and send email to recipient with code in body
for recipient, code in pairs.items():
    try:
        # TODO how to not hardcode body?
        body = f"""
Hello, wonderful Kickstarter backer! You wanted a digital download of our new album Bon Voyage,
so here is a code to download it from Bandcamp: {code}\n\n
The way it works is: you navigate to http://mobiustrio.bandcamp.com/yum , and then you enter the code!
It's as simple as that. We hope you love it.

Love,
The Guys at Mobius Trio
"""
        # TODO Make this dict, esp body text, more elegant/customizable
        request = requests.post(request_url, auth=('api', key), data={
            'from': 'KickstarterFulfillment@mobiustrio.org',
            'to': recipient,
            'subject': 'A digital download of Bon Voyage, for you!' ,
            'text': body
})
        # write recipient, code, status, and msg body to file
        log.write(f"Recipient: {recipient} {body} Status code: {request.status_code}\n\n")
    except requests.exceptions.RequestException as e:
        # print exception to same file as everything else
        log.write(f"Had error: {e} when emailing {recipient}")
        continue

log.close()