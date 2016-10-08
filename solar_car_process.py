#!/usr/bin/env python3

import subprocess


class SolarCarProcess:
    
    def __init__(self,path): #Initializes
        self.path = path
        self.timesRestarted = 0

    def start(self): #Start the process 
        try:
            self.process = subprocess.Popen(self.path, stderr=subprocess.PIPE, universal_newlines=True)
        except OSError:
            raise

    def restart(self):
        self.process = subprocess.Popen(self.path, stderr=subprocess.PIPE, universal_newlines=True)
        self.timesRestarted += 1

    def check_status(self): 
        return self.process.poll() #True if the process has terminated
    
