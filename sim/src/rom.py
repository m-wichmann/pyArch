#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import src

# The size of a ROM module is fixed to 65536 * 16 bit (256 kb)
#
# ROM content is read from a file. Only first 256 kb are read.
# TODO: handling of larger files has to happen somewhere else.

class ROM(object):
    """Represents one 256kb ROM block."""
    def __init__(self, filename):
        src.LOGGER.log("init ROM completed","INFO")
        self.__data = [0] * 65536
        self.__load_rom_content(filename)

    # load the inital rom content from a file
    # TODO: 
    # - better parsing. For now we expect following format: 01234567 abcdef01 00ff00ff...
    # - support for binary images
    def __load_rom_content(self, filename):
        fd = open(filename, 'r')
        i = 0
        for line in fd:
            temp_data = line.split()
            for t in temp_data:
                self.__data[i] = int(t,16)
                i = i + 1

    # a byte can only be set, since its a ROM
    def get_byte(self, address):
        """"""
        address = address % 65536
        return self.__data[address]

    # dump whole rom to console
    def dump_rom_whole(self):
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

    # dump rom segment around *address* to console
    def dump_rom_segment(self, address):
        ret = ""
        line_length = 8
        for i in range(address - 32, address + 48):
            i = i % 65536
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
