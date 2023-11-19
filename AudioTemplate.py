import requests
import csv

CHUNK_SIZE = 1024
api_key = '5965b6fc42fe6f082c03bb3dada1eb37'
api_url = 'https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL'

headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": api_key
}

model_id = "eleven_multilingual_v2"
voice_settings = {
    "stability": 0.35,
    "similarity_boost": 0.5
}

with open('output.mp3', 'wb') as output_file:
    with open('ActualBuyerList.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for ind, row in enumerate(csv_reader):
            name = row["Name"]
            address = row["Address"]
            
            text = f"Hey there {name}, we saw that you matched for a listing at {address}. Give us a call when you can, thank you!"
            # Should we state: "This is an automated message?"
            
            data = {
                "text": text,
                "model_id": model_id,
                "voice_settings": voice_settings
            }

            response = requests.post(api_url, json=data, headers=headers)

            if response.status_code == 200:
                output_file_name = f'output_{ind}.mp3'
                with open(output_file_name, 'wb') as output_file:
                    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                        if chunk:
                            output_file.write(chunk)
            else:
                print(f"Failed with status code: {response.status_code}")
