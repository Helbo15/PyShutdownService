# PyShutdownService
Detects when a file is in a specific location and delete the file, once done it will shutdown the computer

first set the path in the code to the folder you want to read the shutdown file from. could be onedrive or dropbox or any other folder. as long as it is a folder that will recieve a file called shutdown.txt

once done then Run the command:

Python PyShutdownService.py install

to install the service.

then go to windows services and set it up to automatic startup at boot. and start the service. 
it will currently look for a file in Onedrive\google\
