import os
from twilio.rest import Client

# Retrieve the values from environment variables
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

# Create a Twilio client
client = Client(account_sid, auth_token)

# List of phone numbers and corresponding voicemail URLs
phone_numbers_and_urls = {
    '+12403059007': 'http://your-server.com/voicemail1.mp3',
    '+14044446018': 'http://your-server.com/voicemail2.mp3',
    # Add more entries as needed
}

for to_number, voicemail_url in phone_numbers_and_urls.items():
    call = client.calls.create(
        machine_detection='Enable',
        url=f'http://your-server.com/your-voicemail-twiml?voicemail_url={voicemail_url}',
        to=to_number,
        from_='+18339854826'
    )

print(call.sid)
