# Mobius Trio Kickstarter 2019 Bandcamp code sender
import requests
import pandas as pd
# keeping API key and domain secret and safe in their own lil modules
from keys import key, domain

# open backers csv and use for loop to turn emails into recipients
df1 = pd.read_csv('backers.csv', usecols=[3])
recipients = list(df1)

# open bandcamp codes csv and and use for loop to turn codes into codes
df2 = pd.read_csv('codes.csv', usecols=[0])
codes =  list(df2)

# zip those into a dict
pairs = dict(zip(recipients, codes))

''' TODO use for loop to iterate through dict, 
making request for each recipient/code pair and inserting them into 
{recipient} and {code} '''

request_url = f'https://api.mailgun.net/v2/{domain}/messages'

for recipient, code in pairs:
    request = requests.post(request_url, auth=('api', key), data={
        'from': 'KickstarterFulfillment@mobiustrio.org',
        'to': {recipient},
        'subject': 'A digital download of Bon Voyage, for you!' ,
        'text': f"Hello, wonderful Kickstarter backer! \
            You wanted a digital download of our new album Bon Voyage,\
            so here is a code to download it from Bandcamp: {code}\n\n\
            The way it works is: you navigate to \
            http://mobiustrio.bandcamp.com/yum , and then you enter \
            the code! It's as simple as that. We hope you love it.\n\
            Love,\n The Guys at Mobius Trio"
    })

print(f'Status: {request.status_code}')
print(f'Body:   {request.text}')