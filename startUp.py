#!/usr/bin/env python3

import sys
import subprocess
import time
import settings

def main(): 
    fileName = open(sys.argv[1])
    programs = fileName.read().splitlines()
    fileName.close()
    
    numberOfPrograms = len(programs)
    timesRestarted = {program: 0 for program in programs}
    
    # Start up programs in separate processes
    processes = []
    for program in programs:
        processes.append(subprocess.Popen(program))
    
    # Check processes and respond accordingly
    while True:
        for i in range(numberOfPrograms):
            if processes[i].poll() is not None:
                if timesRestarted[programs[i]] > settings.MAX_RESTART:
                    print(programs[i], "exceeded", settings.MAX_RESTART, "restarts")
                    return
                processes[i] = subprocess.Popen(programs[i])
                timesRestarted[programs[i]] += 1
        time.sleep(2)
    
if __name__ == '__main__':
    main()
    