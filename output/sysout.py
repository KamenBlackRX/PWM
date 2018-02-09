"""
Class helper for colored terminal
"""
class sysout:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def printout(string, level='OK'):

        if level == 'Warning':
            print(sysout.WARNING + string + sysout.ENDC)

        if level == 'Error':
            print(sysout.FAIL + string  + sysout.ENDC)

        if level == 'OK':
            print(sysout.OKGREEN + string + sysout.ENDC)

        if level == 'OKBLUE':
            print(sysout.OKBLUE + string + sysout.ENDC)

        if level == 'BOLD':
            print(sysout.BOLD + string + sysout.ENDC)
