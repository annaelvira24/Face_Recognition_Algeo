from main import *
import sys
import os

def errormsg():
	if (os.name == 'nt'):
		print("Use 'python startapp.py <command>'")
	else:
		print("Use 'python3 startapp.py <command>'")
	print(
'''
Available commands:
- run
- random-sample
- test-image
- test-accuracy
- new-db
- new-db-with-hist
'''
	)

if (len(sys.argv) > 1):
	if (sys.argv[1] == "run"):
		if (os.name == 'nt'):
			os.system("python gui.py")
		else:
			os.system("python3 gui.py")
	elif (sys.argv[1] == "test-accuracy"):
		accurate()
	elif (sys.argv[1] == "test-image"):
		testrun()
	elif (sys.argv[1] == "random-sample"):
		pickSamples()
	elif (sys.argv[1] == "new-db-with-hist"):
		generateDB(True)
	elif (sys.argv[1] == "new-db"):
		generateDB(False)
	else:
		errormsg()
else:
	errormsg()