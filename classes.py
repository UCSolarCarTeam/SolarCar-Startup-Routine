
import subprocess

class SolarCarProcess:
        
    def __init__(self, path):
        self.path = path
        self.process = subprocess.Popen(path)
        self.timesRestarted = 0
        
    def start(self):
        self.process = subprocess.Popen(self.path)
    
    def check_status(self):
        return self.process.poll()
    
    

