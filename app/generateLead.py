import os
from twilio.rest import Client

# Retrieve the values from environment variables
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

# Create a Twilio client
client = Client(account_sid, auth_token)

# Make a Twilio call
call = client.calls.create(
    twiml='<Response><Say>Ahoy, World!</Say></Response>',
    to='+12403059007',  # Replace with the recipient's phone number
    from_='+18339854826'  # Replace with your Twilio phone number
)

print(call.sid)