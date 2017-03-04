import subprocess

def test_domovoiExit():
    domovoi_noruntest = subprocess.Popen(["./domovoi_tst.py", "DomovoiTests/TestProcessFiles/p_invalid.txt"], stderr=subprocess.PIPE)
    domovoiReturnCode = domovoi_noruntest.wait()
    if domovoiReturnCode is None:
        assert 0
        return
    assert 1

def test_errorlog():
    f = open("testlog", "r")
    content = f.readlines()
    f.close()
    for x in content:
        if "CRITICAL" in x:
            assert 1
            return
    assert 0
