import os
import subprocess

def test_errorlog():
    domovoi_noruntest = subprocess.Popen(["./domovoi_tst.py", "DomovoiTests/TestProcessFiles/p_norun.txt"], stderr=subprocess.PIPE)
    domovoi_noruntest.wait()
    f = open("testlog", "r")
    content = f.readlines()
    for x in content:
        if "CRITICAL" in x:
            assert 1
            f.close()
            return
    f.close()
    assert 0

def test_numprocesses():
    f = open("testlog", "r")
    content = f.readlines()
    tmp = []
    numProcesses = []
    for x in content:
        if "Processes" in x:
            tmp.append(x)
    if len(tmp) == 0:
        assert 0
    for string in tmp:
        [numProcesses.append(int(s)) for s in string.split() if s.isdigit()]
    for i in range(len(numProcesses)-1):
        if numProcesses[i+1] != (numProcesses[i] - 1):
            assert 0
            f.close()
            return
    f.close()
    assert 1
    
       

