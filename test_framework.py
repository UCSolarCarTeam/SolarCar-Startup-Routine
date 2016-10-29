#This contains two tests that will be tested using the pytest framework


def func(x):
	return x+2

def test_pass():
	#This test should pass
	assert func(2) < 10

def test_fail():
	#This test should fail
	assert func(2) > 10
