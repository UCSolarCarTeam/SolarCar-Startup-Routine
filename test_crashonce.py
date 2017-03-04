import subprocess

def test_logs():
    domovoi_noruntest = subprocess.Popen(["./domovoi_tst.py", "DomovoiTests/TestProcessFiles/p_crashonce.txt"], stderr=subprocess.PIPE)
    domovoi_noruntest.wait()
    f = open("testlog", "r")
    content = f.readlines()
    f.close()
    for x in content:
        if "WARNING" in x:
            assert 1
            return
    assert 0 

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
    assert timesRestarted[0] == 1
