import os
from twilio.rest import Client

# Retrieve the values from environment variables
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

# Create a Twilio client
client = Client(account_sid, auth_token)

# List of phone numbers to call
phone_numbers = ['+12403059007', '+14044446018']

for to_number in phone_numbers:
    call = client.calls  \
        .create(
            machine_detection='Enable',
            url='https://handler.twilio.com/twiml/EH8ccdbd7f0b8fe34357da8ce87ebe5a16',
            to='+12403059007',
            from_='+18339854826'
        )

print(call.sid)
