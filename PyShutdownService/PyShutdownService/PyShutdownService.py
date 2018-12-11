import time
from pathlib import Path
from SMWinservice import SMWinservice
import subprocess

class PyShutdownService(SMWinservice):
    _svc_name_ = 'PyShutdownService'
    _svc_display_name_ = 'Python Shutdown Service'
    _svc_description_ = 'Python Delete File And Shutdown Service'

    def start(self):
        self.shutdownPath = 'H:\\OneDrive\\Google\\'
        self.isrunning=True

    def stop(self):
        self.isrunning= False

    def main(self):
        while self.isrunning:  
            filenamePath = self.shutdownPath + 'shutdown.txt'
            if Path(filenamePath).exists():
                Path(filenamePath).unlink()
                cmdCommand = "Shutdown -s -t 1"
                process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
                # Do work here

            time.sleep(2)

if __name__ =='__main__':
    PyShutdownService.parse_command_line()