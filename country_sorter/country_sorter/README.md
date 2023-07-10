# Purpose
IATACountrySorter takes a text file of comma separated IATA airport codes and 
an output directory, and breaks out each port code into a separate comma
separated file, sorted on the basis of country the airport is in. The files
are named based off of the ISO 3166-1 alpha 2 country code. 

This is pretty useful for the Matrix Airfare Search 
(https://oldmatrix.itasoftware.com) which does not let you search port codes
belonging to multiple countries! It was pretty inconvenient when I discovered 
this, so I spent a few hours making this instead of searching for flights.

# Usage

Need to install Python 3.x to run this! 
Get here: https://www.python.org/downloads/ 

After getting Python, download the latest release, and change to the folder in
the terminal. (i.e. `cd country_sorter/`)

Then install pip if you have not already, here 
https://pip.pypa.io/en/stable/installation/.

You want to make a virtual environment here, to run the python program inside
this, away from all other systems. Enter this to create it, 
`python3 -m venv country_sorter_env/`. Enter this to activate the environment
`source country_sorter_env/bin/activate`. 

Run `pip install -r requirements.txt` to get the packages required for the
program to work.

Taken from https://towardsdatascience.com/virtual-environments-104c62d48c54

Finally, run `python3 country_sorter [input file] [output directory]`!

# Implementation
- Read in the airports file
- Store the airports list in an array
- Go through each airports and store in an array of pairs of code and ISO 3166-1
  alpha 2 country code, gather a set of the country codes
- Sort the dictionary array by the country code
- Make a directory of export
- Make a file for each country code in the set
- Grab the airports belonging to each country code and print them to the file


# Debugging
First imported the airports data set and tested that the dictionary was created
properly by calling a dummy key and printing a value.

`print(airports["BOS"]['city'])`

Tested that a file can be opened 

Decided to move to C++ because this program felt more suited to that language

Needed to import airports data json file to C++ though

https://stackoverflow.com/questions/32205981/reading-json-files-in-c

Just made file to read in from instead using python

Switched back to Python because C++ was too hard to figure out maps and did not
feel that it was suited for this project

Pandas dataframe methods proved most useful

Made an exception for a bad input file

Made the file reading system to be used in parsing input file

Made the output directory argument be supported

Realised that I should make sure the user does not accidentally delete a
directory that is filled with files

Added a method to figure formatting

Tested with small data set

Done!