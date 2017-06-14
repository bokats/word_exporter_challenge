import requests, json
from docx import Document

class WordExporter(object):
    def __init__(self, transcript_id, API_key):
        self.API_response = self.get_transcript_from_API(transcript_id, API_key)
        self.word_file = Document()
        # self.write_transcript_to_file(self.API_response)

    def get_transcript_from_API(self, transcript_id, API_key):
        url = 'https://api.capio.ai/v1/speech/transcript/' + transcript_id
        headers = {'apiKey': API_key}
        return requests.get(url, headers=headers).json()

    def write_transcript_to_file(self, content):
        for message in content:
            raw_time = message['result'][0]['alternative'][0]['words'][0]['from']
            self.word_file.add_paragraph(time)

        self.word_file.save('test.docx')

    def reformat_time(self, raw_time):
        hours = int(raw_time / 3600)
        raw_time -= hours * 3600
        minutes = int(raw_time / 60)
        raw_time -= minutes * 60
        seconds = int(raw_time)
        raw_time -= seconds
        centiseconds = int(raw_time * 100)

        if hours < 10:
            formatted_hours = '0' + str(hours)
        else:
            formatted_hours = str(hours)
        if minutes < 10:
            formatted_minutes = '0' + str(minutes)
        else:
            formatted_minutes = str(minutes)
        if seconds < 10:
            formatted_seconds = '0' + str(seconds)
        else:
            formatted_seconds = str(seconds)

        if centiseconds < 10:
            formatted_centiseconds = '0' + str(centiseconds)
        else:
            formatted_centiseconds = str(centiseconds)

        return formatted_hours + ":" + formatted_minutes + ":" + formatted_seconds \
        + '.' + formatted_centiseconds

w = WordExporter('593f237fbcae700012ba8fcd', '262ac9a0c9ba4d179aad4c0b9b02120a')
print(w.reformat_time(0.6523523532))
