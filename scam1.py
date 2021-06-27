import requests
import os
import random
import string
import json

# You will need the URL, the location from 'network' tab where the email and password is being sent

chars = string.ascii_letters + string.digits + '!£$%^&*()'
random.seed = (os.urandom(1024))

url = ''

# Read in the json files
names = json.loads(open('names.json').read())
surnames = json.loads(open('surnames.json').read())
emails = json.loads(open('email.json').read())

# join names and surnames (Where to add the '.' to split the surname and the name
for name in names:
    full_name = ''.join(random.choice(surnames))

    # Generate random emails and passwords
    username = name.lower() + surnames.lower() + random.choice(emails)
    password = ''.join(random.choice(chars) for i in range(8))

    # Get the location where the data is sent from the Chrome network tab
    requests.post(url, allow_redirects=False, data={
        '': username,
        '': password
    })

    print('sending username %s and password %s' % (username, password))
