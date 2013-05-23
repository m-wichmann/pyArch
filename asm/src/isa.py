#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#class ISA(object):
#    def __init__(self):
#        pass

instructions =  {
#               instr:  (op_code, par_count, mem_count),                

                "nop":  (0x00, 0, 1),

                "mov":  (0x10, 2, 1),
                "ld":   (0x11, 1, 2), # address/value in second field
                "st":   (0x12, 1, 2), # address in second field
                "push": (0x13, 1, 1),
                "pop":  (0x14, 1, 1),

                "add":  (0x20, 2, 1),
                "sub":  (0x21, 2, 1),
                "mul":  (0x22, 2, 1),
                "div":  (0x23, 2, 1),
                "inc":  (0x2E, 1, 1),
                "dec":  (0x2F, 1, 1),

                "and":  (0x30, 2, 1),
                "or":   (0x31, 2, 1),
                "xor":  (0x32, 2, 1),
                "com":  (0x33, 1, 1),
                "neg":  (0x34, 1, 1),
                "lsl":  (0x35, 2, 1),
                "lsr":  (0x36, 2, 1),
                "rol":  (0x37, 2, 1),
                "ror":  (0x38, 2, 1),

                "jmp":  (0x50, 1, 1),

                "prt":  (0xA0, 1, 1),
                }
