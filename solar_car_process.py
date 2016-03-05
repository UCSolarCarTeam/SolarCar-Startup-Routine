#!/usr/bin/env python3

import sys
import subprocess
import logging
import shlex
import time

import settings


class SolarCarProcess:
        
    def __init__(self, path):
        self.path = path
        self.process = subprocess.Popen(path)
        self.timesRestarted = 0
        
    def start(self):
        self.process = subprocess.Popen(self.path)
        self.timesRestarted += 1
    
    def check_status(self):
        return self.process.poll()

    
class Domovoi:
        
    def run(self):
        with open(sys.argv[1]) as file:
            solar_car_processes = [SolarCarProcess(shlex.split(path)) for path in file.read().splitlines()]
        
        # Check processes and respond accordingly
        while True:
            for solar_car_process in solar_car_processes:
                if solar_car_process.check_status():
                    if solar_car_process.timesRestarted == settings.MAX_RESTART:
                        logging.critical("%s reached %d restart(s) with signal %d",
                            solar_car_process.path, settings.MAX_RESTART, solar_car_process.process.returncode)
                        solar_car_processes.remove(solar_car_process)
                    else:
                        logging.warning("%s crash number %d with signal %d",
                            solar_car_process.path, solar_car_process.timesRestarted + 1, solar_car_process.process.returncode)
                        solar_car_process.start()
            time.sleep(settings.SLEEP_TIME)
    
