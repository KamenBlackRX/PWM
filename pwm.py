#!/usr/bin/python
# -*- coding: utf-8 -*-
from config.confman import ConfigureManager
from core.downloadmanager import DownloadManager
from output.sysout import sysout
import time
def main():
    print ("Checking dependencies...")
    print ("Debug Output\n")

    conf = ConfigureManager(path='config/configuration_test.conf')
    conf.createOutput()
    f = DownloadManager()
    time.sleep(1)
    sysout.printout("Starting download depencies for first time", 'Warning')
    time.sleep(1)
    f.GetPackageFile(
        path='~/',
        name='tes.tar',
        version='1.0',
        download_path='https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.15.tar.xz')

if __name__ == "__main__":

    main()

