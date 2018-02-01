#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import threading
import subprocess
from time import sleep


class bcolors:

    """
    Helper class for colored terminal display
    """

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
            print(bcolors.FAIL + string + bcolors.ENDC)

        if level == 'OK':
            print(bcolors.OKGREEN + string + bcolors.ENDC)

        if level == 'OK':
            print(bcolors.OKGREEN + string + bcolors.ENDC)

        if level == 'OKBLUE':
            print(bcolors.OKBLUE + string + bcolors.ENDC)

        if level == 'BOLD':
            print(bcolors.BOLD + string + bcolors.ENDC)


class Find():

    """
    Class to find programs and add to list
    """

    dict_result = []

    def __init__(self):
        pass

# ----------------------------------------------------------------------
# Find all installed programs in the system.
# ----------------------------------------------------------------------

    def findFile(self, name):
        if isinstance(name, list):
            for x in name:
                result = subprocess.call(['which', x])

                if result != 0:
                    print(bcolors.FAIL + x + " not found. \
                    Installation is needed." + bcolors.ENDC)

                    self.dict_result.append(x)

                else:
                    print(bcolors.OKGREEN + x + " found!"
                          + bcolors.ENDC)

        else:
            if result != 0:
                print(bcolors.FAIL + name + " not found. \
                Installation is needed." + bcolors.ENDC)
                self.dict_result.append(name)
            else:
                print(bcolors.OKGREEN + name + ' found!'
                      + bcolors.ENDC)

# ----------------------------------------------------------------------
# Get files for installation and install on computuer
# --------------------------------------------------------------------

    def installFiles(self):
        if isinstance(self.dict_result, list):
            for x in self.dict_result:
                if x == 'vscode':

                    if os.path.exists('vscode.deb'):

                        bcolors.printout("The file vscode.dev already exists, \
                         aborting download", 'Warning')

                        subprocess.call(['dpkg', '-i', 'vscode.deb'])

                        subprocess.call(['apt', 'install', '-f'])

                    else:

                        response = subprocess.call(
                            ['wget',
                             'https://az764295.vo.msecnd.net/stable/7c4205b5c6e52a53b81c69d2b2dc8a627abaa0ba/code_1.19.3-1516876437_amd64.deb',
                             '-O',
                             'vscode.deb']
                        )

                        if response == 0:
                            subprocess.call(['dpkg', '-i', 'vscode.deb'])
                            subprocess.call(['apt', 'install', '-f'])

                if x == 'dbeaver':
                    if os.path.exists('dbeaver.deb'):
                        bcolors.printout('The file dbeaver.deb already exists, \
                        aborting download', 'Warning')

                        subprocess.call(['dpkg', '-i', 'dbeaver.deb'])

                        subprocess.call(['apt', 'install', '-f'])

                    else:
                        response = subprocess.call(
                            ['wget',
                             'https://dbeaver.jkiss.org/files/dbeaver-ce_latest_amd64.deb',
                             '-O',
                             'dbeaver.deb'
                             ]
                        )

                        if response == 0:

                            subprocess.call(['dpkg', '-i', 'dbeaver.deb'])

                            subprocess.call(['apt', 'install', '-f'])

# Install all pending processes
            result = subprocess.call(['apt', 'install', x, '-y'])

            if result != 0:
                bcolors.printout(x + ' can\'t be installed \
                by apt. Manual installation is needed.', 'Error')

            else:
                bcolors.printout(x + ' is installed!', 'OK')

                if not response:

                    subprocess.call(['dpkg', '-i', 'dbeaver.deb'])

                    if not response:
                        subprocess.call(['dpkg', '-i', 'dbeaver.deb'])
                        subprocess.call(['apt', 'install', '-f'])
                    else:
                        bcolors.printout('An error occurred while installing \
                        the file. Please check manually.', 'Error')

                # -- Packages with tarball
                if x == 'eclipse-oxygen':
                    have_deb = os.path.exists('eclipse.tar.gz')

                    if have_deb is True:

                        bcolors.printout("The file eclipse.tar.gz \
                        already exists, aborting download", 'Warning')

                        subprocess.call(['tar', 'xfv', 'eclipse.tar.gz'])

                        bcolors.printout(x + 'was installed \
                        successfully', 'OK')
                    else:
                        response = subprocess.call([
                            'wget',
                            '--progress=dot',
                            'http://eclipse.c3sl.ufpr.br/technology/epp/downloads/release/oxygen/2/eclipse-jee-oxygen-2-linux-gtk-x86_64.tar.gz',
                            '-O',
                            'eclipse.tar.gz'
                        ])
                        if not response:
                            subprocess.call([
                                'tar',
                                'xfv',
                                'eclipse.tar.gz'
                            ])
                            bcolors.printout(x + 'was installed \
                            successfully', 'OK')

                        else:
                            bcolors.printout('An error occurred when \
                            downloading the file.', 'Error')

                result = subprocess.call(['apt', 'install', x, '-y'])
                if result != 0:
                    bcolors.printout(x + ' can\'t be \
                    installed by apt. Manual installation is needed.', 'Error')
                else:
                    bcolors.printout(x + ' is installed!', 'OK')


if __name__ == "__main__":

    bcolors.printout('Initalizing database...', 'OK')
    f = Find()

    program = [
        "git",
        "dbeaver",
        "docker",
        "vscode",
        "openjdk-8-jre",
        "eclipse"
    ]

    f.findFile(program)
    f.installFiles()
