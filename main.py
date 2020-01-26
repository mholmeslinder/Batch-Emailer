# Mobius Trio Kickstarter 2019 Bandcamp code sender
import requests
import csv
# # TODO Take API key and csv file as environment variables

# open csv and put recipients and codes into lists
recipients = []
codes = []

with open('mailgun.csv') as csvfile:
    read_csv = csv.reader(csvfile, delimiter=',')
    for row in read_csv:
        recipients.append(row[1])
        codes.append(row[0])

# zip those into a dict
pairs = dict(zip(recipients, codes))
print(pairs)
''' use for loop to iterate through dict, 
making request for each recipient/code pair and inserting them into 
{recipient} and {code} '''

# request_url = f'https://api.mailgun.net/v2/{domain}/messages'

# for recipient, code in pairs.items():
#     request = requests.post(request_url, auth=('api', key), data={
#         'from': 'KickstarterFulfillment@mobiustrio.org',
#         'to': {recipient},
#         'subject': 'A digital download of Bon Voyage, for you!' ,
#         'text': f"Hello, wonderful Kickstarter backer! \
#             You wanted a digital download of our new album Bon Voyage,\
#             so here is a code to download it from Bandcamp: {code}\n\n\
#             The way it works is: you navigate to \
#             http://mobiustrio.bandcamp.com/yum , and then you enter \
#             the code! It's as simple as that. We hope you love it.\n\
#             Love,\n The Guys at Mobius Trio"
#     })

# print(f'Status: {request.status_code}')
# print(f'Body:   {request.text}')