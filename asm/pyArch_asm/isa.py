#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#class ISA(object):
#    def __init__(self):
#        pass

instructions =  {
                "nop":  (0x00, 0),

                "mov":  (0x10, 2),
                "ld":   (0x11, 1), # address/value in second field
                "st":   (0x12, 1), # address in second field
                "push": (0x13, 1),
                "pop":  (0x14, 1),

                "add":  (0x20, 2),
                "sub":  (0x21, 2),
                "mul":  (0x22, 2),
                "div":  (0x23, 2),
                "inc":  (0x2E, 1),
                "dec":  (0x2F, 1),

                "and":  (0x30, 2),
                "or":   (0x31, 2),
                "xor":  (0x32, 2),
                "com":  (0x33, 1),
                "neg":  (0x34, 1),
                "lsl":  (0x35, 2),
                "lsr":  (0x36, 2),
                "rol":  (0x37, 2),
                "ror":  (0x38, 2),

                "prt":  (0xA0, 1),
                }
