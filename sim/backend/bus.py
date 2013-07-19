#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import backend

class BUS(object):
    """Manages all hardware blocks and makes them accessible for other blocks.
    TODO: This probably should be static?!
    """

    def __init__(self):
        backend.LOGGER.log("init BUS completed","INFO")
#        self.__modules = [] # TODO: maybe make specific vars or dict for modules
        self.__cpu = None
        self.__mem = None

#    def register_module(self, module):
#        self.__modules.append(module)
#        # TODO: check if 'module' is a module

    def register_cpu(self, module):
        self.__cpu = module

    def register_mem(self, module):
        self.__mem = module

    def print_modules(self):
        print(self.__cpu)
        print(self.__mem)

    def get_cpu(self):
        return self.__cpu

    def get_mem(self):
        return self.__mem
