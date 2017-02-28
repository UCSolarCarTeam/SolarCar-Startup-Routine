import subprocess

def test_exitCode():
    domovoi_noruntest = subprocess.Popen(["./domovoi_tst.py", "DomovoiTests/TestProcessFiles/p_goodexit.txt"], stderr=subprocess.PIPE)
    domovoi_noruntest.wait()
    f = open("testlog", "r")
    returnCode=""
    content = f.readlines()
    f.close()
    for x in content:
        if "Return Code" in x:
            returnCode=x
    if "0" in returnCode:
        assert 1
    else:
        assert 0

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
