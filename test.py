from word_exporter import WordExporter
import docx
from docx.shared import RGBColor

class WordExporterTests(object):

    def test_correct_API_call(self):
        w = WordExporter('593f237fbcae700012ba8fcd', '262ac9a0c9ba4d179aad4c0b9b02120a')
        if w.error_code is not None:
            print('Fail correct API call test')

    def test_incorrect_API_key(self):
        w = WordExporter('593f237fbcae700012ba8fcd', '262ac9a0c02120a')
        if w.error_code is None:
            print('Fail incorrect API key test')

    def test_incorrect_transcript_id(self):
        w = WordExporter('593', '262ac9a0c9ba4d179aad4c0b9b02120a')
        if we.error_code is None:
            print('Fail incorrect transcript id test')

    def test_time_reformatting(self):
        w = WordExporter('593', '262ac9a0c9ba4d179aad4c0b9b02120a')
        if w.reformat_time(0.12421412) != '00:00:00.12':
            print('Time reformatting test fail', 0.12421412)
        if w.reformat_time(0.9988) != '00:00:01.00':
            print('Time reformatting test fail', 0.9988)
        if w.reformat_time(59.998) != '00:01:00.00':
            print('Time reformatting test fail', 59.998)
        if w.reformat_time(61.02) != '00:01:01.02':
            print('Time reformatting test fail', 61.02)
        if w.reformat_time(122.998) != '00:02:03.00':
            print('Time reformatting test fail', 122.598)
        if w.reformat_time(200) != '00:03:20.00':
            print('Time reformatting test fail', 200)
        if w.reformat_time(3599.998) != '01:00:00.00':
            print('Time reformatting test fail', 3599.998)


t = WordExporterTests()
t.test_correct_API_call()
t.test_incorrect_API_key()
t.test_time_reformatting()
