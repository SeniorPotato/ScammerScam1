import requests
import os
import random
import string
import json

# Use this script to flood the scammer server with fake login credentials.
# You will need the URL, from 'network' tab, in the dev chrome tool, where the email and password is being sent

chars = string.ascii_letters + string.digits + '!£$%^&*()'
random.seed = (os.urandom(1024))

# Paste the url between the ''
url = 'https://feature-testing.quantum-pfe.com/Account/Login'

# Read in the json files
names = json.loads(open('names.json').read())
surnames = json.loads(open('surnames.json').read())
emails = json.loads(open('email.json').read())
password_list = json.loads(open('password_list.json').read())

# join names and surnames (Where to add the '.' to split the surname and the name
for name in names:
    full_name = ''.join(random.choice(surnames))

    # Generate random emails and passwords
    username = random.choice(names) + random.choice(surnames) + random.choice(emails)
    password = random.choice(password_list)

    # Get the location where the data is sent from the Chrome network tab
    requests.post(url, allow_redirects=False, data={
        # paste the location of the login credentials here
        'UserName': username,
        'Password': password
    })

    print('sending username %s and password %s' % (username, password))
