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
class Find(object):

    dict_result = []

    uid = os.getuid()
    gid = os.getgid()

    def __init__(self):
        assert self.dict_result is not None, "Dicionario nao pode ser nulo"

    def _chown(self, path, uid, gid):
        os.chown(path, uid, gid)
        for item in os.listdir(path):
            itempath = os.path.join(path, item)
            if os.path.isfile(itempath):
                os.chown(itempath, uid, gid)
            elif os.path.isdir(itempath):
                os.chown(itempath, uid, gid)
                self._chown(itempath, uid, gid)

    """
        Find all installed prograns in system.
    """
    def findFile(self, name):
        if isinstance(name, list):
            for x in name:
                result = subprocess.call(['which', x])
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

    """
     Get files for instalation and install on computuer
    """
    def installFiles(self):
        if isinstance(self.dict_result, list):
            for x in self.dict_result:
                # -- Packages with deb installer
                if x == 'code':
                    have_deb = os.path.exists('vscode.deb')
                    if have_deb is True:
                        bcolors.printout("Arquivo vscode.dev já existe, abortando download", 'Warning')
                        subprocess.call(['dpkg', '-i', 'vscode.deb'])
                        subprocess.call(['apt', 'install', '-f'])
                    else:
                        response = subprocess.call([
                            'wget',
                            '--progress=dot',
                            'https://az764295.vo.msecnd.net/stable/7c4205b5c6e52a53b81c69d2b2dc8a627abaa0ba/code_1.19.3-1516876437_amd64.deb',
                            '-O',
                            'vscode.deb'
                        ])
                        if not response:
                            subprocess.call([
                                'dpkg',
                                '-i',
                                'vscode.deb'
                            ])
                            subprocess.call([
                                'apt',
                                'install',
                                '-f'
                            ])
                        else:
                            bcolors.printout('Erro ao fazer o download.','Error')

                if x == 'dbeaver':
                    have_deb = os.path.exists('dbeaver.deb')
                    if have_deb:
                        bcolors.printout('Arquivo dbeaver.deb já existe, abortando download', 'Warning')
                        subprocess.call(['dpkg', '-i', 'dbeaver.deb'])
                    else:
                        subprocess.call(['apt', 'install', '-f'])
                        response = subprocess.call ([
                            'wget',
                            '--progress=dot',
                            'https://dbeaver.jkiss.org/files/dbeaver-ce_latest_amd64.deb', '-O', 'dbeaver.deb'])

                        if not response:
                            subprocess.call(['dpkg', '-i', 'dbeaver.deb'])
                            if not response:
                                subprocess.call(['dpkg', '-i', 'dbeaver.deb'])
                                subprocess.call(['apt', 'install', '-f'])
                            else:
                                bcolors.printout('Erro ao instalar o arquivo, Favor checar manualmente.', 'Error')

                # -- Packages with tarball
                if x == 'eclipse-oxygen':
                    have_deb = os.path.exists('eclipse.tar.gz')
                    if have_deb is True:
                        bcolors.printout("Arquivo eclipse.tar.gz já existe, abortando download", 'Warning')
                        subprocess.call(['tar', 'xfv', 'eclipse.tar.gz'])
                        bcolors.printout('Corrigindo as permissões do eclipse', 'Warning')
                        self._chown('eclipse', self.uid, self.gid)
                        bcolors.printout('Programa ' + x + 'foi instalado com sucesso', 'OK')
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

                            self._chown('eclipse/', self.uid, self.gid)
                            bcolors.printout('Programa ' + x + ' foi instalado com sucesso', 'OK')

                        else:
                            bcolors.printout('Erro ao fazer o download.','Error')

                result = subprocess.call(['apt','install', x , '-y'])

                if result != 0:
                    bcolors.printout('The program ' + x + ' can\'t be installed by apt. Need manual installation', 'Error')
                else:
                    bcolors.printout('Program ' + x + ' is installed!', 'OK')

if __name__ == "__main__":

    bcolors.printout('Initalizing database...', 'OK')
    f = Find()

    program = [
        "git",
        "pgadmin3",
        "dbeaver",
        "docker",
        "docker.io",
        "code",
        "openjdk-8-jre",
        "eclipse-oxygen"
    ]

    bcolors.printout('Database -> OK', 'OKBLUE')

    f.findFile(program)
    f.installFiles()