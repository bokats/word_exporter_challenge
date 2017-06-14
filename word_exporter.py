import requests
from docx import Document

class WordExporter(object):
    def __init__(self, transcript_id, API_key):
        self.API_response = self.get_transcript_from_API(transcript_id, API_key)

    def get_transcript_from_API(self, transcript_id, API_key):
        url = 'https://api.capio.ai/v1/speech/transcript/' + transcript_id
        headers = {'apiKey': API_key}
        return requests.get(url, headers=headers)

    def move_result_to_word_file(self):
        document = Document()
        document.save('test.docx')


w = WordExporter()
w.get_transcript_from_API('593f237fbcae700012ba8fcd', '262ac9a0c9ba4d179aad4c0b9b02120a')
w.move_result_to_word_file()
