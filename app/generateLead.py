import os
from twilio.rest import Client

def generateleads():

    # Retrieve the values from environment variables
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']

    # Create a Twilio client
    client = Client(account_sid, auth_token)

    # List of phone numbers and corresponding voicemail URLs
    phone_numbers_and_urls = {
        '+12403059007': 'https://console.cloud.google.com/storage/browser/_details/wholesaler/output_0.mp3;tab=live_object?project=quantum-keep-405604',
        '+14044446018': 'https://console.cloud.google.com/storage/browser/_details/wholesaler/output_1.mp3;tab=live_object?project=quantum-keep-405604',
        '+16783278767': 'https://console.cloud.google.com/storage/browser/_details/wholesaler/output_2.mp3;tab=live_object?project=quantum-keep-405604',
        '+14046049705': 'https://console.cloud.google.com/storage/browser/_details/wholesaler/output_3.mp3;tab=live_object?project=quantum-keep-405604',
        '+12403059007': 'https://console.cloud.google.com/storage/browser/_details/wholesaler/output_4.mp3;tab=live_object?project=quantum-keep-405604',
        '+14044446018': 'https://console.cloud.google.com/storage/browser/_details/wholesaler/output_5.mp3;tab=live_object?project=quantum-keep-405604'
        # Add more entries as needed
    }

    for to_number, voicemail_url in phone_numbers_and_urls.items():
        twiml = f'''
        <Response>
            <Play>{voicemail_url}</Play>
        </Response>
        '''

        call = client.calls.create(
            machine_detection='DetectMessageEnd',
            twiml=twiml,
            to=to_number,
            from_='+18339854826'
        )

    print(call.sid)
