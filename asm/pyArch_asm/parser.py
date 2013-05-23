#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pyArch_asm.isa

class Parser(object):
    def __init__(self):
        self.__instr = pyArch_asm.isa.instructions

    def parse(self, tokens):
        parsed_tokens = []

        for t in tokens:
            (op_code, argc) = self.__instr[t["instr"]]

            raw_op1 = t["op1"] if t["op1"] != None else str(0)
            raw_op2 = t["op2"] if t["op2"] != None else str(0)

            op1 = int(raw_op1.replace("r",""))
            op2 = raw_op2.replace("$", "")
            try:
                op2 = int(op2.replace("r",""))
            except ValueError:
                op2 = int(op2.replace("r",""), 16)

            if t["instr"] == 'ld' or t["instr"] == 'st':
                flags = 0
                if not "$" in raw_op2:
                    flags = flags | (1 << 0)   

                parsed_tokens.append((op_code, flags, op1, 0)) # instruction

                address0 = ((op2 & 0x000000ff) >> 0)
                address1 = ((op2 & 0x0000ff00) >> 8)
                address2 = ((op2 & 0x00ff0000) >> 16)
                address3 = ((op2 & 0xff000000) >> 24)

                parsed_tokens.append((address0,address1,address2,address3)) # address
            else:            
                flags = 0
                if not "r" in raw_op2:
                    flags = flags | (1 << 0)    

                parsed_tokens.append((op_code, flags, op1, op2)) # instruction

        return parsed_tokens
