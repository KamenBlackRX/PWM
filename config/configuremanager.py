import os
import shlex

"""
 Configuration Manager for give the interpretor the way how the files will be held.
"""
class ConfigureManager(object):

    FILE = dict
    CPU_FLAG = str
    CHOST = str
    CXXHOST = str
    CFLAGS = str
    CXXFLAGS = str
    MAKE = str
    USE_FLAG = str

    def __init__(self,*args, **kargs):
        """
            Constructor of class.
            @param path -> path from file
        """
        assert args is not None, "Function need have at least one argument."
        FILE = self.loadFileAsDict(kargs.get('path'))


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


#http://189.41.233.110:4200


    def isFileValid(self, path):
         print ("Not implemented.")

    @staticmethod
    def getCPUFlag(self):
        assert self.FILE is None, "Need make.conf file"
        self.CPU_FLAG = self.FILE.get('CPU_FLAG')
        return self.CPU_FLAG

    @staticmethod
    def getCFlags(self):
        pass

    @staticmethod
    def getCXXFlags(self):
        pass

    @staticmethod
    def getMakeOptsFlags(self):
        pass