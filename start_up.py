#!/usr/bin/env python3

import sys
import time

import settings
import classes

def main():
    with open(sys.argv[1]) as file:
        solar_car_processes = [classes.SolarCarProcess(path) for path in file.read().splitlines()]

    # Check processes and respond accordingly
    while True:
        for solar_car_process in solar_car_processes:
            if solar_car_process.check_status():
                solar_car_process.start()
                solar_car_process.timesRestarted += 1
                if solar_car_process.timesRestarted == settings.MAX_RESTART:
                    print(solar_car_process.path, "reached", settings.MAX_RESTART, "restarts")
                    solar_car_processes.remove(solar_car_process)
        time.sleep(settings.SLEEP_TIME)
        
if __name__ == '__main__':
    main()

