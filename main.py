# Mobius Trio Kickstarter 2019 Bandcamp code sender
import requests
# keeping API key and domain secret and safe in their own lil modules
from keys import key, domain

recipients = []
codes =  []
pairs = {}

request_url = f'https://api.mailgun.net/v2/{domain}/messages'
# TODO open recipients csv and use for loop to turn emails into recipients

# TODO open bandcamp codes csv and and use for loop to turn codes into codes

# TODO  zip those into a dict

''' TODO use for loop to iterate through dict, 
making request for each recipient/code pair and inserting them into 
{recipient} and {code} '''

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
            the code! It's as simple as that! We hope you love it.\n\
            Love, The Guys at Mobius Trio"
    })

print(f'Status: {request.status_code}')
print(f'Body:   {request.text}')