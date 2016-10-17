#!/usr/bin/env python3

import subprocess


class SolarCarProcess:
    
    def __init__(self,path):
        self.path = path
        self.timesRestarted = 0

    '''
    Attempt to start the process.
    '''
    def start(self):
        try:
            self.process = subprocess.Popen(self.path, stderr=subprocess.PIPE, universal_newlines=True)
        except OSError:
            raise

    def restart(self):
        self.process = subprocess.Popen(self.path, stderr=subprocess.PIPE, universal_newlines=True)
        self.timesRestarted += 1

    def check_status(self):
        return self.process.poll() # Returns true if the process has terminated.
    
