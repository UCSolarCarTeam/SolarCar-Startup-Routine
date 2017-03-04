# Domovoi

Domovoi is a process runner that will attempt to restart programs after they have crashed. It also logs when and why a program crashes.

The name derives from Slavic folklore where a domovoi is a protective house spirit.

## Running

Run as ./domovoi.py [processesfile]
where processesfile is a text file formatted as the following:  

path/to/process1 arg1 arg2 args...  
path/to/process2

### Testing

To run a test, make sure you are in the directory with the domovoi_tst.py and run py.test (tests) linux and pytest (tests) on OSX.

To run all tests in the current directory just run py.test or pytest with no arguments.
