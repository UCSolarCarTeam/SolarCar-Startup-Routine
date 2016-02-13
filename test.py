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
            
    #check processes and respond accordingly
    while True:
        if (p0.poll() is not None):
            #print(programs[0] + " died")
            p0 = subprocess.Popen(programs[0])
        if (p1.poll() is not None):
            #print(programs[1] + " died")
            p1 = subprocess.Popen(programs[1]) 
        '''
        if (p2.poll() is not None):
            #print(programs[2] + " died")
            p2 = subprocess.Popen(programs[2])
        if (p3.poll() is not None):
            #print(programs[3] + " died")
            p3 = subprocess.Popen(programs[3])
        '''
        
        time.sleep(2)
        
if __name__ == '__main__':
    main()