import os

"""
 Configuration Manager for give the interpretor the way how the files will be held.
"""
class ConfigureManager(object):


    FILE = object
    CPU_FLAG = str
    CHOST = str
    CXXHOST = str
    USE_FLAG = str

    def __init__(self,*args, **kargs):
        assert args is not None, "Function need have at least one argument."
        FILE = self.loadFile(kargs.get('path'))


    def loadFile(self, path):
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

    def isFileValid(self, path):
         print ("Not implemented.")

    @staticmethod
    def getCPUFlag(self):
        assert self.FILE is None, "Need make.conf file"

