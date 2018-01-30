import sys, os , threading
import subprocess
from time import sleep


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

""" Find programs and add to list """
class Find():

    dict_result = []

    def __init__(self):
       pass
    
    def findFile(self, name):
       if isinstance(name, list):
           for x in name:
	       result = subprocess.call(['which',x])
	       if result != 0:
	          print(bcolors.FAIL + "Program " + x + " not found. Need installation" + bcolors.ENDC)
		  self.dict_result.append(x)
	       else:
	          print(bcolors.OKGREEN + "Program " + x + " is found!" + bcolors.ENDC)
       else:
           if result != 0:
               print(bcolors.FAIL + "Program " + name + " not found. Need installation" + bcolors.ENDC)
               self.dict_result.append(name)

           else:
               print(bcolors.OKGREEN + "Program %s is found!" + bcolors.ENDC)

    def installFiles(self):
        if isinstance(self.dict_result, list):
            for x in self.dict_result:
		if x == 'visualcode':
			reponse = subprocess.call (['wget','https://go.microsoft.com/fwlink/?LinkID=760868', '-O', 'vscode.deb'])
			if response == 0:
			    subprocess.call(['dpkg', '-i', 'vscode.deb'])
			    subprocess.call(['apt', 'install', '-f']) 
		if x == 'dbeaver':
#                        subprocess.call (['wget','https://go.microsoft.com/fwlink/?LinkID=760868'])

	        result = subprocess.call(['apt','install', x , '-y'])
                if result != 0:
                   print(bcolors.FAIL + "the program " + x + " cant be installed by apt. Need manual installation" + bcolors.ENDC)
                else:
                   print(bcolors.OKGREEN + "Program " + x + " is installed!" + bcolors.ENDC)
		   
	else:
	   print(bcolors.OKGREEN + "Program " + x + "is installed!" + bcolors.ENDC)




if __name__ == "__main__":
    print ("Initalizing database...")
    f = Find()
    program = ["dbeaver", "docker", "visualcode", "openjdk-8-jre", "eclipse"]
    f.findFile(program)
    f.installFiles()

