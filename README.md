## Word Exporter Challenge

This repo makes a call to Capio's API, given an API key and transaction id, creates a new MS Word file, and writes the information provided from the response in the form of a timestamp indicating when the specific sentence started, and the actual sentence. The program also marks words with less than 75% confidence, as indicated by the API response, in red.

## Set up and execution instructions
The program is written in Python3 and utilizes three main libraries:
1. requests - makes http request to Capio's API
2. json - turns the API response into more manageable json format
3. python-docx - used to write the information into a MS Word file

To run the program:
1. Clone the repo.
2. Run `requirements.txt` in your terminal. This will install python-docx and requests.
3. Go to the `program_script` folder in the repo.
3. There are two options to run the program:
    - At the bottom of `word_exporter.py`, add a line calling the WordExporter object.  For example: `WordExporter(<transaction_id>, <API key>)`.
    - Run python3 in your terminal and then run `WordExporter(<transaction_id>, <API key>)`.
4. Once the program is executed properly, there will be a MS Word file named after the transaction id saved in the same directory

Please note if incorrect API key and/or transaction id is provided, the program will return the error code provided by the API.

In the `program_script` folder, `tests.py` includes the tests written for this program. To run the tests, run `python3 tests.py` in your terminal. If any test fails, a print statement will be printed in the terminal window, specifying the type of test failed and the specific test case. If no tests fail, nothing will be printed.

###Program structure

The main program is encapsulated in a class called `WordExporter`. It takes 2 arguments as parameters: transcript id related to a specific conversation and API key specific to Capio's API. The attributes of the class include the response from the API call, the docx file reference, and an error code to be used in case of bad response from the API.

Once the main object is instantiated, the program makes a call to Capio's REST API with the given parameters and saves the response in a class attribute called `API_response`. Then the program checks if the response is valid through its response code. If not valid, it returns the error code of the response and terminates. If valid, it then creates a new MS Word file, converts the start time of each sentence into an appropriate time format and checks if a word in each sentence has confidence less than 75%. If so, the word is marked with red in the MS Word file. Each sentences is added with a correct time stamp and text provided from the API response on a separate line.
