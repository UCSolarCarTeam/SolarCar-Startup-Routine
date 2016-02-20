#!/usr/bin/env python3

import sys
import subprocess
import time

import settings

def main():
    
    
    class Process:
        
        def __init__(self, path, process):
            self.path = path
            self.process = process
            self.timesRestarted = 0
            
            
    fileName = open(sys.argv[1])
    programs = fileName.read().splitlines()
    fileName.close()

    # Start up programs in separate processes
    processes = [subprocess.Popen(program) for program in programs]
    
    solarCarProcesses = [Process(path, process) for path, process in zip(programs, processes)]
    
    # Check processes and respond accordingly
    while True:
        for solarCarProcess in solarCarProcesses:
            if solarCarProcess.process.poll() is not None:
                if solarCarProcess.timesRestarted > settings.MAX_RESTART:
                    print(solarCarProcess.path, "exceeded", settings.MAX_RESTART, "restarts")
                    return
                solarCarProcess.process = subprocess.Popen(solarCarProcess.path)
                solarCarProcess.timesRestarted += 1
        time.sleep(settings.SLEEP_TIME)
        
if __name__ == '__main__':
    main()
    