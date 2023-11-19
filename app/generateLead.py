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
    # Make a Twilio call for each phone number
    call = client.calls.create(
        twiml='<Response><Say>Ahoy, World!</Say></Response>',
        to=to_number,
        from_='+18339854826'  # Replace with your Twilio phone number
    )

    print(f"Call SID for {to_number}: {call.sid}")
