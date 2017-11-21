# Domovoi

Domovoi is a process runner that will attempt to restart programs after they have crashed. It also logs when and why a program crashes.

The name derives from Slavic folklore where a domovoi is a protective house spirit.

## Running

Run as ./domovoi.py primary or ./domovoi.py secondary

This will open Domovoi in either primary or secondary pi mode.
Secondary mode will attempt to open a process file called "display.txt"
Primary mode will first attempt to ping the secondary pi, if sucessful it will open "display.txt", otherwise it will open "race.txt"

A process file is a text file formatted as the following:

path/to/process1 arg1 arg2 args...  
path/to/process2

### Testing

To run a test, make sure you are in the directory with domovoi.py and run py.test linux and pytest on OSX
