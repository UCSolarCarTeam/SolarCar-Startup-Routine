#!/usr/bin/env python3

import sys
import logging

from solar_car_process import Domovoi

def main():
    logging.basicConfig(filename = sys.argv[2], format = '%(asctime)s - %(levelname)s - %(message)s')
    domovoi = Domovoi()
    domovoi.run()
        
if __name__ == '__main__':
    main()

