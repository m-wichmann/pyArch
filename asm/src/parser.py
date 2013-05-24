#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import src.isa

class Parser(object):
    def __init__(self):
        self.__instr = src.isa.instructions

    def parse(self, tokens):
        jumpmark_address = {}
        address_counter = 0
        tokens_to_remove = []

        # calculate all addresses for jumpmarks
        for t in tokens:
            if ":" in t["instr"]:
                jumpmark_address[t["instr"].replace(":","")] = address_counter
                tokens_to_remove.append(t)
            else:
                address_counter = address_counter + self.__instr[t["instr"]][2]

        for t in tokens_to_remove:
            tokens.remove(t)

        for t in tokens:
            raw_op1 = t["op1"] if t["op1"] != None else str(0)
            raw_op2 = t["op2"] if t["op2"] != None else str(0)

            if "@" in raw_op1:
                t["op1"] = str(jumpmark_address[raw_op1.replace("@","")])
            if "@" in raw_op2:
                t["op2"] = str(jumpmark_address[raw_op2.replace("@","")])

        parsed_tokens = []

        for t in tokens:
            (op_code, argc, memc) = self.__instr[t["instr"]]

            raw_op1 = t["op1"] if t["op1"] != None else str(0)
            raw_op2 = t["op2"] if t["op2"] != None else str(0)

            op1 = int(raw_op1.replace("r",""))
            op2 = raw_op2.replace("$", "")
            try:
                op2 = int(op2.replace("r",""))
            except ValueError:
                op2 = int(op2.replace("r",""), 16)

            flags = 0
            i = t["instr"]
            if i == 'ld' or i == 'st':
                if not "$" in raw_op2:
                    flags = flags | (1 << 0)   

                parsed_tokens.append((op_code, flags, op1, 0)) # instruction

                address0 = ((op2 & 0x000000ff) >> 0)
                address1 = ((op2 & 0x0000ff00) >> 8)
                address2 = ((op2 & 0x00ff0000) >> 16)
                address3 = ((op2 & 0xff000000) >> 24)

                parsed_tokens.append((address0,address1,address2,address3)) # address
            elif (i == 'jmp' or i == 'breq' or i == 'brne' or i == 'brp' or i == 'brn'):
                if not "r" in raw_op1:
                    flags = flags | (1 << 0)
                parsed_tokens.append((op_code, flags, op1, op2))
            else:
                if not "r" in raw_op2:
                    flags = flags | (1 << 0)
                parsed_tokens.append((op_code, flags, op1, op2)) # instruction

        return parsed_tokens


















