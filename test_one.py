import os
import subprocess

try:
    subprocess.Popen(["./domovoi.py", "DomovoiTests/TestProcessFiles/p_norun.txt"])
except OSError:
    print("There was an error")
       
