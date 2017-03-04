#!/usr/bin/env python3

import argparse
import os
import shlex
import sys
import time

import settings

from solar_car_process import SolarCarProcess
from testlogger import TestLog

class Domovoi:
    '''
    Check the path of each process, throw an error if the path is invalid
    '''
    def check_paths(self, logger, solar_car_processes):
        for solar_car_process in solar_car_processes: # For each solar_car_process 
            if not os.path.exists(solar_car_process.path[0]):
                logger.critical()               
                exit()

    '''
    Try and start the processes, if an error occurs, kill the process
    '''
    def start_processes(self, logger, solar_car_processes): 
        for solar_car_process in solar_car_processes:
            try:
                solar_car_process.start()
            except OSError:
                logger.critical()     
                self.kill_processes(logger, solar_car_processes)
                raise

    '''
    Kill and remove all the processes from the list
    '''
    def kill_processes(self, logger, solar_car_processes):
        for solar_car_process in solar_car_processes:
            # Ensures that all processes are stopped
            try:
                solar_car_process.process.kill()
            except AttributeError: # Fails to kill everything
                pass
            solar_car_processes.remove(solar_car_process)
            logger.numberOfProcesses(len(solar_car_processes))

    '''
    Opens processes_file which should contain a list of paths to each SolarCarProcess, and makes an object for each one.
    '''
    def parse_file(self, processes_file):
        with open(processes_file) as file:
            return([SolarCarProcess(shlex.split(path)) for path in file.read().splitlines()])

    def run(self, logger, processes_file):
        solar_car_processes = self.parse_file(processes_file)
        logger.numberOfProcesses(len(solar_car_processes))
        self.check_paths(logger, solar_car_processes)
        self.start_processes(logger, solar_car_processes)
        
        # Watch over the processes and respond accordingly
        while len(solar_car_processes):
            for solar_car_process in solar_car_processes:
                if solar_car_process.check_status() != None:
                    logger.returnCode(solar_car_process.process.returncode)
                    if solar_car_process.process.returncode == 0: # Good exit, removes the process from the list
                        solar_car_processes.remove(solar_car_process)
                        logger.numberOfProcesses(len(solar_car_processes))
                    elif solar_car_process.timesRestarted == settings.MAX_RESTART: # If a process restarts too many times, print this and remove it.
                        logger.warning()
                        solar_car_processes.remove(solar_car_process)
                        logger.numberOfProcesses(len(solar_car_processes))
                    else:  # Log the crash 
                        logger.warning()
                        solar_car_process.restart()
                        logger.timesRestarted(solar_car_process.timesRestarted)
                        startup_error = solar_car_process.process.communicate()[1]# Communicate returns a tuple (stdoutdata, stderrdata)
                        if startup_error:# If there is a value in stderrdata, notify and remove it
                            logger.error()
                            solar_car_processes.remove(solar_car_process)
                            logger.numberOfProcesses(len(solar_car_processes))
            time.sleep(settings.SLEEP_TIME)# Wait 2 seconds before doing the for loop again
   

def main():
    parser = argparse.ArgumentParser()# Take in command line arguments
    parser.add_argument('processes_file', help='text file of solar car processes') # Adds in a positional argument for the process_file
    args = parser.parse_args()# Stores the arguments the user inputted
    logger = TestLog()
    domovoi = Domovoi()
    domovoi.run(logger, args.processes_file)# Uses the arguments stored earlier to run the program. 
        
if __name__ == '__main__':
    main()

