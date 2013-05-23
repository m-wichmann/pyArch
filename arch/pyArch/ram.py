#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pyArch

# RAM
#
# Array with size x byte fields. Maybe dirty bit?!
# Maybe 2D Array incl. row and col decode?!
#
# Interface: get_byte(address)
#            set_byte(address, byte_value)
#
# RAM size is always 256 kb (65536 fields of 16 bit)
#

class RAM(object):

    def __init__(self):
        pyArch.LOGGER.log("init RAM completed","INFO")    
        self.__data = [0] * 65536

    def get_byte(self, address):
        address = address % 65536
        return self.__data[address]

    def set_byte(self, address, byte_value):
        address = address % 65536
        self.__data[address] = byte_value

    def dump_ram_whole(self):
        ret = ""
        line_length = 8
        for i in range(len(self.__data)):
            # print address
            if i % line_length == 0:
                print('0x%08X' % i, end='    ')

            # print values
            print('0x%08X' % self.__data[i], end=' ')

            # print new line
            if i % line_length == line_length - 1:
                print("")

    def dump_ram_segment(self, address):
        ret = ""
        line_length = 8
        for i in range(address - 16, address + 24):
            # print address
            if i % line_length == 0:
                if i == address:
                    print('0x%08X' % i, end='  > ')
                else:
                    print('0x%08X' % i, end='    ')

            # print values
            print('0x%08X' % self.__data[i], end=' ')

            # print new line
            if i % line_length == line_length - 1:
                print("")











