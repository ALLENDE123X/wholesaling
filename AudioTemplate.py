import requests
import csv

CHUNK_SIZE = 1024
api_key = '44c511f653147f937b9d41c80e81c208'  # Replace with your actual API key
api_url = 'https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL'

headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": f"{api_key}"  # Use 'Authorization' header for the API key
}

model_id = "eleven_multilingual_v2"
voice_settings = {
    "stability": 0.35,
    "similarity_boost": 0.5
}
# Buyer mp3
with open('output.mp3', 'wb') as output_file:
    with open('ActualBuyerList.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for ind, row in enumerate(csv_reader):
            if ind < 5:
                name = row["Real Estate Company Name"]
                address = row["Street Address"]
                
                text = f"Hello there {name}, we saw that you matched for a listing at {address}. Give us a call when you can, thank you!"
                
                data = {
                    "text": text,
                    "model_id": model_id,
                    "voice_settings": voice_settings
                }

                response = requests.post(api_url, json=data, headers=headers)

                if response.status_code == 200:
                    output_file_name = f'output_buyer_{ind}.mp3'
                    with open(output_file_name, 'wb') as output_file:
                        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                            if chunk:
                                output_file.write(chunk)
                else:
                    print(f"Failed with status code: {response.status_code}")

# Property Owner mp3
with open('output.mp3', 'wb') as output_file:
    with open('ActualPropertyOwnerList.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for ind, row in enumerate(csv_reader):
            if ind < 5:
                name = row["Owner first name"]
                address = row["Street address"]
                
                text = f"Hello there {name}, we saw that a buyer was matched with your listing at {address}. Give us a call when you can, thank you!"
                
                data = {
                    "text": text,
                    "model_id": model_id,
                    "voice_settings": voice_settings
                }

                response = requests.post(api_url, json=data, headers=headers)

                if response.status_code == 200:
                    output_file_name = f'output_property_{ind}.mp3'
                    with open(output_file_name, 'wb') as output_file:
                        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                            if chunk:
                                output_file.write(chunk)
                else:
                    print(f"Failed with status code: {response.status_code}")