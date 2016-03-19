#!/usr/bin/env python3

import logging
import subprocess


class SolarCarProcess:
    
    def __init__(self,path):
        try:
            self.path = path
            self.process = subprocess.Popen(path, stderr=subprocess.PIPE, universal_newlines=True)
            self.timesRestarted = 0
        except OSError as e:
            raise OSError(e)

    def start(self):
        try:
            self.process = subprocess.Popen(self.path, stderr=subprocess.PIPE, universal_newlines=True)
            self.timesRestarted += 1
        except OSError as e:
            raise OSError(e)

    def check_status(self):
        return self.process.poll()
    
