import sys, os , threading
import subprocess
from time import sleep
from output.sysout import sysout
from config.confman import ConfigureManager


"""
Class to find programs and add to list
"""
class DownloadManager(object):

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



    def downloadFile(self, link, version, name, path):
        retval = subprocess.Popen(
            [
                "wget",
                "--progress=dot",
                link
                #"-O",
                #path + name
            ],
        ).communicate()

        print (retval[1])
        if retval > 0:
            sysout.printout("Error in download file dependencies", 'Error')

    def GetPackageFile(self, **kargs):
        """
            Download required source tarballs with thread management
            @param path
            @param name
            @param version
            @param download_path
        """
        assert kargs.get('path') is not None, "The path for download source can't be empty"
        assert kargs.get('name') is not None, "The name for download source can't be empty"
        assert kargs.get('version') is not None, "The version for download source can't be empty"
        assert kargs.get('download_path') is not None, "The link for download source can't be empty"

        path = kargs.get('path')
        name = kargs.get('name')
        version = kargs.get('version')
        download_path = kargs.get('download_path')

        t = threading.Thread(
            name="DownloadThread",
            target=self.downloadFile,
            args=(download_path, version, name,path)
        )
        t.start()


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
                        sysout.printout("Arquivo vscode.dev ja existe, abortando download", 'Warning')
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
                        sysout.printout('Arquivo dbeaver.deb ja existe, abortando download', 'Warning')
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
                        sysout.printout("Arquivo eclipse.tar.gz ja existe, abortando download", 'Warning')
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