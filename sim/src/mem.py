#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import src



class MEM(object):
    """Memory Manager. Pastes all memory segments together and handles calls to the segments.
    Needs exactly one MMP instance. RAM and ROM instances can be added as needed.
    """
    
    # every mem segment is 256 kb large. 
    # 0x00000000 - 0x0000ffff
    # 0x00010000 - 0x0001ffff
    # ...
    # 0xffff0000 - 0xffffffff


    def __init__(self):
        src.LOGGER.log("init MEM completed","INFO")
        # set up list of mem segments
        self.__mem_segments = [None] * 65536

    def get_ram_base(self):
        """Get base address of ram"""
        for s in self.__mem_segments:
            if isinstance(s, src.ram.RAM):
                return (self.__mem_segments.index(s) * 65536)
        return None

    def get_ram_end(self):
        """Can be used as stack pointer"""
        last = None
        for s in self.__mem_segments:
            if isinstance(s, src.ram.RAM):
                last = s

        if last != None:
            return ((self.__mem_segments.index(last) * 65536) + 65535)

        return None

    def add_segment(self, segment):
        """Register a segment with the mem"""
        # search for first free slot
        for i in range(len(self.__mem_segments)):
            e = self.__mem_segments[i]
            if e == None:
                self.__mem_segments[i] = segment
                break

    def print_segments(self):
        """Print all registered segments"""
        for i in range(len(self.__mem_segments)):
            e = self.__mem_segments[i]
            if e != None:
                print('0x%08X' % (i * 65536), end='    ')
                print(e)

    def get_address(self, address):
        """Get byte at 'address' in global memory map."""
        rel = address % 65536
        base = int((address - rel) / 65536)
        seg = self.__mem_segments[base]
        return seg.get_byte(rel)

    def set_address(self, address, value):
        """Set byte at 'address' with 'value' in global memory map."""
        rel = address % 65536
        base = int((address - rel) / 65536)
        seg = self.__mem_segments[base]
        seg.set_byte(rel, value)









