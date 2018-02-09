import os, sys
import shlex
from output.sysout import sysout

"""
 Configuration Manager for give the interpretor the way how the files will be held.
"""
class ConfigureManager(object):

    FILE = dict
    CPU_FLAG = None
    CHOST = None
    CXXHOST = None
    CFLAGS = None
    CXXFLAGS = None
    MAKE = None
    USE_FLAG = None

    def __init__(self,*args, **kargs):
        """
            Constructor of class.
            @param path -> path from file
        """
        assert kargs.get('path') is not None, "Function need have at least one argument."
        self.FILE = self.loadFileAsDict(kargs.get('path'))


    def loadFileAsList(self, path):
        """
            Load file into File descriptor. Handle all exceptions.
            @param path String to file path.
        """
        if self.isFileValid(path):
            print("Can not be null")
        else:
            result = open(path, 'r')
            if result:
               file_content = result.readlines()
               for x in file_content:
                   pass
            else:
                pass


    def loadFileAsDict(self, path):
        """
            Load file in File descriptor and return all his content intro dict.
            @param str path  String to file path
            @return dict  Dictonary with configuration list
        """
        with open(path) as fd:
            settings = {var: shlex.split(value) for var, value in [line.split('=', 1) for line in fd]}
            if fd.closed is False:
                fd.close()
        return settings


    def isFileValid(self, path):
        print ("Not implemented.")


    def getCPUFlag(self):
        """
            Get the cpu flags from make file and set globaly.
        """
        assert self.FILE is not None, "Need make.conf file"
        self.CPU_FLAG = self.FILE.get('CPUFLAGS')[0]
        return self.CPU_FLAG

    def getCHOSTFlags(self):
        """
            Get the Host GCC flags from make file and set globaly
        """
        assert self.FILE is not None, "Need make.conf file"
        self.CHOST = self.FILE.get('CHOST')[0]
        return self.CPU_FLAG

    def getCXXHOSTFlags(self):
        """
            Get the Host GCC flags from make file and set globaly
        """
        assert self.FILE is not None, "Need make.conf file"
        self.CXXHOST = self.FILE.get('CHOST')[0]
        return self.CPU_FLAG

    def getCFlags(self):
        """
            Get the Host C flags from make file and set globaly
        """
        assert self.FILE is not None, "Need make.conf file"
        self.CFLAGS = self.FILE.get('CFLAGS')[0]
        return self.CPU_FLAG


    def getCXXFlags(self):
        """
            Get the Host C++ flags from make file and set globaly
        """
        assert self.FILE is not None, "Need make.conf file"
        self.CXXFLAGS = self.FILE.get('CXXFLAGS')[0]
        return self.CPU_FLAG


    def getMakeOptsFlags(self):
        """
            Get the Make jobs flag from make file and set globaly
        """
        assert self.FILE is not None, "Need make.conf file"
        self.MAKE = self.FILE.get('MAKEOPTS')[0]
        return self.CPU_FLAG


    def createOutput(self):
        self.getCHOSTFlags()
        self.getCXXHOSTFlags()
        self.getCFlags()
        self.getCPUFlag()
        self.getCXXFlags()
        self.getMakeOptsFlags()

        sysout.printout('---------------------Enabled variables --------------------------\n' +
                'CHOST: ' + self.CHOST + '\n' +
                'CXXHOST: ' + self.CXXHOST + '\n' +
                'CFLAGS: ' + self.CFLAGS + '\n' +
                'CPU_FLAG: ' + self.CPU_FLAG + '\n' +
                'CXXFLAGS: ' + self.CXXFLAGS + '\n' +
                'CXXHOST: ' + self.CXXHOST + '\n'
        )




