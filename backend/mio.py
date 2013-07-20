#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import backend

class MIO(object):
    """Memory Mapped IO. Contains a 'memory segment' that is used to access the 'periphals'.
    TODO: this must be filled with specific registers and stuff.
    """

    def __init__(self):
        backend.LOGGER.log("init MIO completed","INFO")
        self.data = [0] * 65536

    def get_byte(self, address):
        address = address % 65536
        return self.data[address]

    def set_byte(self, address, byte_value):
        address = address % 65536
        self.data[address] = byte_value
