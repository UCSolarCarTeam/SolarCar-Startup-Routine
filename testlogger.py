#!/usr/bin/env python3

class TestLog:
        
    def __init__(self):
        self.logfile = open("testlog", "w")
    
    def __del__(self):
        self.logfile.close()

    def critical(self):
        self.logfile.write("CRITICAL\n")
    
    def warning(self):
        self.logfile.write("WARNING\n")
    
    def error(self):
        self.logfile.write("ERROR\n")
    
    def timesRestarted(self, num):
        message = "Times Restarted: " + str(num) + "\n"
        self.logfile.write(message)

    def numberOfProcesses(self, num):
        message = "Number of Processes: " + str(num) + "\n"
        self.logfile.write(message) 

    def returnCode(self, num):
        message = "Return Code: " + str(num) + "\n"
        self.logfile.write(message)      
