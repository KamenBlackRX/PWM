#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, os , threading
import subprocess
from time import sleep
from output.sysout import sysout
from config.confman import ConfigureManager


"""
Class to find programs and add to list
"""
class Find(object):

    dict_result = []

    def __init__(self):
        assert self.dict_result is not None, "Dicionario nao pode ser nulo"

    """
     Find all installed prograns in system.
    """
    def findFile(self, name):
        if isinstance(name, list):
            for x in name:
                result = subprocess.call(['which', x])
                if result != 0:
                    sysout.printout('Program ' + x + ' not found! Need installation', 'Error')
                    self.dict_result.append(x)
                else:
                    sysout.printout('Program ' + x + ' is found!', 'OK')
        else:
            if result != 0:
                sysout.printout('Program ' + name + ' not found! Need installation', 'Error')
                self.dict_result.append(name)
            else:
                sysout.printout('Program '+ name + ' is found!', 'OK')

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
                        sysout.printout("Arquivo vscode.dev já existe, abortando download", 'Warning')
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
                            sysout.printout('Erro ao fazer o download.','Error')
                            if not response:
                                subprocess.call([
                                    'dpkg',
                                    '-i',
                                    'vscode.deb'
                                ])
                            else:
                                sysout.printout('Erro ao fazer o download.', 'Error')

                if x == 'dbeaver':
                    have_deb = os.path.exists('dbeaver.deb')
                    if have_deb:
                        sysout.printout('Arquivo dbeaver.deb já existe, abortando download', 'Warning')
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
                                sysout.printout('Erro ao instalar o arquivo, Favor checar manualmente.', 'Error')

                # -- Packages with tarball
                if x == 'eclipse-oxygen':
                    have_deb = os.path.exists('eclipse.tar.gz')
                    if have_deb is True:
                        sysout.printout("Arquivo eclipse.tar.gz já existe, abortando download", 'Warning')
                        subprocess.call(['tar', 'xfv', 'eclipse.tar.gz'])
                        sysout.printout('Programa ' + x + 'foi instalado com sucesso', 'OK')
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

                            sysout.printout('Programa ' + x + 'foi instalado com sucesso', 'OK')

                        else:
                            sysout.printout('Erro ao fazer o download.','Error')

                result = subprocess.call(['apt','install', x , '-y'])
                if result != 0:
                    sysout.printout('The program ' + x + ' can\'t be installed by apt. Need manual installation', 'Error')
                else:
                    sysout.printout('Program ' + x + ' is installed!', 'OK')

if __name__ == "__main__":

    sysout.printout("Checking dependencies...", 'OK')
    conf = ConfigureManager(path='config/configuration_test.conf')
    conf.getCPUFlag()


"""
    sysout.printout('Initalizing database...', 'OK')
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

    sysout.printout('Database -> OK', 'OKBLUE')

    f.findFile(program)
    f.installFiles()
"""