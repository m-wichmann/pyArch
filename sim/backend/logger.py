#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Set up the logger fpr pyArch"""

import logging

class PyArchLogger(object):
    def __init__(self):
        self.__mylogger = logging.getLogger(__name__)
        self.__mylogger.setLevel(logging.DEBUG)

        fh = logging.FileHandler('log_sim.log')
        fh.setLevel(logging.DEBUG)

        sh = logging.StreamHandler()
        sh.setLevel(logging.ERROR)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        fh.setFormatter(formatter)
        sh.setFormatter(formatter)

        self.__mylogger.addHandler(fh)
        self.__mylogger.addHandler(sh)

        self.log("==========","INFO")


#    def __del__(self):
#        self.__mylogger.shutdown()


    # Loglevel: DEBUG, INFO, WARNING, ERROR, CRITICAL
    def log(self, msg, level):
        if level == "DEBUG":
            self.__mylogger.debug(msg)
        elif level == "INFO":
            self.__mylogger.info(msg)
        elif level == "WARNING":
            self.__mylogger.warning(msg)
        elif level == "ERROR":
            self.__mylogger.error(msg)
        elif level == "CRITICAL":
            self.__mylogger.critical(msg)
