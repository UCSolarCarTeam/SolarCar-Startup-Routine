# Domovoi

Domovoi is a process runner that will attempt to restart programs after they have crashed. It also logs when and why a program crashes.

The name derives from Slavic folklore where a domovoi is a protective house spirit.

## Running

Run as ./domovoi.py -p or ./domovoi.py --primary

This will open Domovoi in primary pi mode, which will attempt to open a process file named "primary.txt".
Running the program without arguments will open Domovoi in secondary pi mode, which will attempt to open a process file named "secondary.txt" 

A process file is a text file formatted as the following:

path/to/process1 arg1 arg2 args...  
path/to/process2

### Testing

To run a test, make sure you are in the directory with domovoi.py and run py.test linux and pytest on OSX
