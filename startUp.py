#!/usr/bin/env python3

import sys
import subprocess
import time
#process names from text file stored into array
#sleep after each check for 2 secs


def main(): 
    #read program names from file and put them into an array
    fileName = open(sys.argv[1])
    programs = fileName.read().splitlines()
    fileName.close()
    
    numberOfPrograms = programs.__len__()
    MAX_RESTART = 10
    timesRestarted = [0] * numberOfPrograms
    
    #start up programs in separate processes
    processes = []
    for i in range(numberOfPrograms):
        processes.append(subprocess.Popen(programs[i]))
    
    #check processes and respond accordingly
    while True:
        for i in range(numberOfPrograms):
            if(processes[i].poll() is not None):
                if(timesRestarted[i] > MAX_RESTART):
                    print(programs[i], "exceeded", MAX_RESTART, "restarts")
                    return
                processes[i] = subprocess.Popen(programs[i])
                timesRestarted[i] += 1          
        time.sleep(2)
    
if __name__ == '__main__':
    main()