## Word Exporter Challenge

This repo makes a call to Capio's API, given an API key and transaction id, creates a new MS Word file, and writes the information provided from the API call in the form of a timestamp indicating when the specific sentence started, and the actual sentence. The program also marks words with less than 75% confidence, as indicated by the API response, in red.

The program is written in Python3 and utilizes three main libraries:
1. requests - makes http request to Capio's API
2. json - turns the API response into more manageable json format
3. python-docx - used to write the information into a MS Word file

To run the program:
1. Clone the repo.
2. Run requirements.txt in your terminal. This will install python-docx.
3. There are two options to run the program:
    - At the bottom of word_exporter.py, add a line calling the WordExporter object. For example: WordExporter(<API key>, <transaction_id).
    - Run python3 in your terminal and then run WordExporter(<API key>, <transaction_id).

Please note if incorrect API key and/or transaction id is provided, the program will return the error code provided by the API.

tests.py includes the tests written for this program. To run the tests, run 'python3 tests.py' in your terminal. If any test fails, a print statement will be printed in the terminal window, specifying the type of test failed and the specific test case.
