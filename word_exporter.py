import requests

class WordExporter(object):
    def __init__(self):
        self.API_response = []

    def get_transcript_from_API(self, transcript_id, API_key):
        url = 'https://api.capio.ai/v1/speech/transcript/' + transcript_id
        headers = {'apiKey': API_key}
        self.API_response = requests.get(url, headers=headers)



w = WordExporter()
w.get_transcript_from_API('593f237fbcae700012ba8fcd', '262ac9a0c9ba4d179aad4c0b9b02120a')
