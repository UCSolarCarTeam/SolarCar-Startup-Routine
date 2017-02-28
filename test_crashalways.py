import subprocess

def test_logs():
    domovoi_noruntest = subprocess.Popen(["./domovoi_tst.py", "DomovoiTests/TestProcessFiles/p_crashalways.txt"], stderr=subprocess.PIPE)
    domovoi_noruntest.wait()
    f = open("testlog", "r")
    content = f.readlines()
    f.close()
    warning_count = 0
    for x in content:
        if "WARNING" in x:
            warning_count +=1
    assert warning_count == 3 

def test_timesRestarted():
    f = open("testlog", "r")
    content = f.readlines()
    f.close()
    tmp = []
    timesRestarted = []
    for x in content:
        if "Restarted" in x:
            tmp.append(x)
    if len(tmp) == 0:
        assert 0
    for string in tmp:
        [timesRestarted.append(int(s)) for s in string.split() if s.isdigit()]
    for i in range(len(timesRestarted)-1):
        if timesRestarted[i+1] != (timesRestarted[i] + 1):
            assert 0
            return
    assert 1

def test_numprocesses():
    f = open("testlog", "r")
    content = f.readlines()
    f.close()
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
            return
    assert 1
