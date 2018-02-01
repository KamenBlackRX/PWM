#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, os , threading
import subprocess
from time import sleep

"""
Class helper for colored terminal 
"""
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def printout(string, level):

        if level == 'Warning':
           print(bcolors.WARNING + string + bcolors.ENDC)
    
        if level == 'Error':
           print(bcolors.FAIL + string  + bcolors.ENDC)

        if level == 'OK':
	       print(bcolors.OKGREEN + string + bcolors.ENDC)

        if level == 'OKBLUE':
           print(bcolors.OKBLUE + string + bcolors.ENDC)

        if level == 'BOLD':
           print(bcolors.BOLD + string + bcolors.ENDC)

""" 
Class to find programs and add to list 
"""
class Find():

    dict_result = []

    def __init__(self):
        assert self.dict_result is not None, "Dicionario nao pode ser nulo"
    #----------------------------------------------------------------------
    # Find all installed prograns in system.
    #----------------------------------------------------------------------    
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
                print(bcolors.OKGREEN + 'Program '+ name + ' is found!' + bcolors.ENDC)

#----------------------------------------------------------------------
# Get files for instalation and install on computuer
# --------------------------------------------------------------------
    def installFiles(self):
        if isinstance(self.dict_result, list):
            for x in self.dict_result:
                if x == 'vscode':
		            if os.path.exists('vscode.deb'):
                        bcolors.printout("Arquivo vscode.dev já existe, abortando download", 'Warning')
                        subprocess.call(['dpkg', '-i', 'vscode.deb'])
                        subprocess.call(['apt', 'install', '-f']) 
                    else:	
    		            response = subprocess.call (['wget','https://az764295.vo.msecnd.net/stable/7c4205b5c6e52a53b81c69d2b2dc8a627abaa0ba/code_1.19.3-1516876437_amd64.deb', '-O', 'vscode.deb'])
		                if response == 0:
        		            subprocess.call(['dpkg', '-i', 'vscode.deb'])
			                subprocess.call(['apt', 'install', '-f'])
                        else:
                            bcolors.printout('Erro ao fazer o download.', 'Error')

	            if x == 'dbeaver':
		            if os.path.exists('dbeaver.deb'):
    		            bcolors.printout('Arquivo dbeaver.deb já existe, abortando download', 'Warning')
			            subprocess.call(['dpkg', '-i', 'dbeaver.deb'])
			            subprocess.call(['apt', 'install', '-f'])
		            else:
    	                response = subprocess.call (['wget','https://dbeaver.jkiss.org/files/dbeaver-ce_latest_amd64.deb', '-O', 'dbeaver.deb'])
		                if response == 0:
    		                subprocess.call(['dpkg', '-i', 'dbeaver.deb'])
			                subprocess.call(['apt', 'install', '-f'])
                else:
                    pass
                    		
		#Install all procress pendending.
	    result = subprocess.call(['apt','install', x , '-y'])
                
		if result != 0:
            bcolors.printout('The program ' + x + ' can\'t be installed by apt. Need manual installation','Error')
        else:
            bcolors.printout('Program ' + x + ' is installed!', 'OK')


if __name__ == "__main__":
    
    bcolors.printout('Initalizing database...', 'OK')
    f = Find()
    
    program = ["git", "dbeaver", "docker", "vscode", "openjdk-8-jre", "eclipse"]
    bcolors.printout('Database -> OK', 'OKBLUE')

    f.findFile(program)
    f.installFiles()

