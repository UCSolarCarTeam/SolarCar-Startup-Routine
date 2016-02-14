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
    
    #start up programs in separate processes
    p0 = subprocess.Popen(programs[0])
    p1 = subprocess.Popen(programs[1])
    '''
    p2 = subprocess.Popen(programs[2])
    p3 = subprocess.Popen(programs[3])
    '''
    
    MAXRESTART = 10
    timesRestarted = [0, 0, 0, 0]
    
    #check processes and respond accordingly
    while True:
        if(p0.poll() is not None):
            #print(programs[0], "died")
            p0 = subprocess.Popen(programs[0])
            timesRestarted[0] += 1
            if (timesRestarted[0] > MAXRESTART):
                print(programs[0], "exceeded", MAXRESTART, "restarts")
                return
        if(p1.poll() is not None):
            #print(programs[1], "died")
            p1 = subprocess.Popen(programs[1])
            timesRestarted[1] += 1
            if (timesRestarted[1] > MAXRESTART):
                print(programs[1], " exceeded", MAXRESTART, " restarts")
                return     
        '''
        if(p2.poll() is not None):
            #print(programs[2], "died")
            p2 = subprocess.Popen(programs[2])
            timesRestarted[2] += 1
            if (timesRestarted[2] > MAXRESTART):
                print(programs[2], "exceeded", MAXRESTART, "restarts")
                return
        if(p3.poll() is not None):
            #print(programs[3], "died")
            p3 = subprocess.Popen(programs[3])
            timesRestarted[3] += 1
            if (timesRestarted[3] > MAXRESTART):
                print(programs[3], "exceeded", MAXRESTART, "restarts")
                return  
        '''
        
        time.sleep(2)
        
if __name__ == '__main__':
    main()