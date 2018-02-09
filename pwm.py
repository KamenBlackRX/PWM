#!/usr/bin/python
# -*- coding: utf-8 -*-

from config.confman import ConfigureManager
if __name__ == "__main__":

    print ("Checking dependencies...")
    print ("Debug Output\n")
    conf = ConfigureManager(path='config/configuration_test.conf')
    conf.createOutput()