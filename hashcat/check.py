#!/usr/bin/python

from twilio.rest import Client
from datetime import datetime
import subprocess

auth_token = ''
account_sid = ''
client = Client(account_sid, auth_token)
numbers = []

def sendText(message):
    client.messages.create(
        to = '',
        from_ = '',
        body = '{:%B %d, %Y}\n{}'.format(datetime.now(), message)
    )

output = subprocess.check_output(['apt', 'update'], stderr=subprocess.PIPE)
if 'packages can be upgraded' in output:
    output = output.strip().split('\n')[-1]
    output = output.split('.')[0].replace('can be', 'were')
    message = 'Hashcat is now up to date. {}\n'.format(output)
    sendText(message)
else:
    message = 'Your system is up to date!\n'
    sendText(message)
