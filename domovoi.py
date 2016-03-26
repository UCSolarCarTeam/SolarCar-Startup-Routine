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
    def start_processes(self, solar_car_processes):
        for solar_car_process in solar_car_processes:
            try:
                solar_car_process.start()
            except OSError as e:
                logging.critical(e)
                self.kill_processes(solar_car_processes)
                raise

    def kill_processes(self, solar_car_processes):
        for solar_car_process in solar_car_processes:
            try:
                solar_car_process.process.kill()
            except AttributeError:
                pass
            solar_car_processes.remove(solar_car_process)

    def parse_file(self, processes_file):
        with open(processes_file) as file:
            return([SolarCarProcess(shlex.split(path)) for path in file.read().splitlines()])

    def run(self, processes_file):
        solar_car_processes = self.parse_file(processes_file)
        self.start_processes(solar_car_processes)
        # Check processes and respond accordingly
        while True:
            for solar_car_process in solar_car_processes:
                if solar_car_process.check_status():
                    if solar_car_process.timesRestarted == settings.MAX_RESTART:
                        logging.critical("%s reached %d restart(s) with exit code %d",
                            os.path.basename(solar_car_process.path[0]), settings.MAX_RESTART, solar_car_process.process.returncode)
                        solar_car_processes.remove(solar_car_process)
                    else:
                        logging.warning("%s crash number %d with exit code %d",
                            os.path.basename(solar_car_process.path[0]), solar_car_process.timesRestarted + 1, solar_car_process.process.returncode)
                        solar_car_process.restart()
                        startup_error = solar_car_process.process.communicate()[1]
                        if startup_error:
                            logging.error("%s unable to startup: %s",
                                os.path.basename(solar_car_process.path[0]), startup_error)
                            solar_car_processes.remove(solar_car_process)
            time.sleep(settings.SLEEP_TIME)
   

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('processes_file', help='text file of solar car processes')
    args = parser.parse_args()
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(filename='logs/%s' % time.asctime(), format='%(asctime)s - %(levelname)s - %(message)s')
    domovoi = Domovoi()
    domovoi.run(args.processes_file)
        
if __name__ == '__main__':
    main()

