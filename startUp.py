#!/usr/bin/env python3

import sys
import subprocess
import time

import settings
import classes

def main():
    with open(sys.argv[1]) as file:
        solarCarProcesses = [classes.Process(path, subprocess.Popen(path)) for path in file.read().splitlines()]

    # Check processes and respond accordingly
    while True:
        for solarCarProcess in solarCarProcesses:
            if solarCarProcess.process.poll():
                solarCarProcess.process = subprocess.Popen(solarCarProcess.path)
                solarCarProcess.timesRestarted += 1
            if solarCarProcess.timesRestarted > settings.MAX_RESTART:
                print(solarCarProcess.path, "exceeded", settings.MAX_RESTART, "restarts")
                solarCarProcesses.remove(solarCarProcess)
        time.sleep(settings.SLEEP_TIME)
        
if __name__ == '__main__':
    main()

