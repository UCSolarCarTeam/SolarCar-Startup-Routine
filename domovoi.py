#!/usr/bin/env python3

import argparse
import logging
import os
import shlex
import sys
import time

import settings

from solar_car_process import SolarCarProcess


class Domovoi:
        
    def run(self, processes_file):
        with open(processes_file) as file:
            solar_car_processes = [SolarCarProcess(shlex.split(path)) for path in file.read().splitlines()]
        
        # Check processes and respond accordingly
        while True:
            for solar_car_process in solar_car_processes:
                if solar_car_process.check_status():
                    if solar_car_process.timesRestarted == settings.MAX_RESTART:
                        logging.critical("%s reached %d restart(s) with signal %d",
                            os.path.basename(solar_car_process.path[0]), settings.MAX_RESTART, solar_car_process.process.returncode)
                        solar_car_processes.remove(solar_car_process)
                    else:
                        solar_car_process.start()
                        logging.warning("%s crashed and restarted",
                            os.path.basename(solar_car_process.path[0]))
            time.sleep(settings.SLEEP_TIME)
   

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('processes_file')
    parser.add_argument('log_file')
    args = parser.parse_args()
    logging.basicConfig(filename=args.log_file, format='%(asctime)s - %(levelname)s - %(message)s')
    domovoi = Domovoi()
    domovoi.run(args.processes_file)
        
if __name__ == '__main__':
    main()

