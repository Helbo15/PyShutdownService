from PyShutdownService import PyShutdownService
#from pathlib import Path

#shutdownPath = 'H:\\OneDrive\\Google\\'
#filenamePath = shutdownPath + 'shutdown.txt'
#if Path(filenamePath).exists():
#    Path(filenamePath).unlink()

objTest = PyShutdownService('pythonService')
objTest.isrunning = True
objTest.main()

