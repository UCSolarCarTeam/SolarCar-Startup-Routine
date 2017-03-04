import subprocess

def test_domovoiRan():
    domovoi_runtest = subprocess.Popen(["./domovoi_tst.py", "DomovoiTests/TestProcessFiles/p_valid.txt"], stderr=subprocess.PIPE)
    domovoiReturnCode = domovoi_runtest.wait()
    errorMessages = domovoi_runtest.communicate()[1]
    if len(errorMessages) != 0:
        assert 0
        return
    if domovoiReturnCode != 0:
        assert 0
        return 
    assert 1
