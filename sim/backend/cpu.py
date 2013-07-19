#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import backend
from backend import alu



class CPU(object):
    """Represents one CPU. This contains the alu and some registers."""
    def __init__(self, bus):
        backend.LOGGER.log("init CPU completed","INFO")

        # create instance of submodule
        self.__alu = alu.ALU(self)
        self.__bus = bus
        # create cpu register
        self.__create_cpu_regs()

        self._mem = None

    def init_mem(self):
        self._mem = self.__bus.get_mem()
        sp = self._mem.get_ram_end()
        self._core_regs["sp"] = sp

    def __create_cpu_regs(self):
        # TODO: maybe use orderd dict to make the print easier
        # or just use list and ommit the 'r'
        self._gp_regs = {"r0":  0, "r1":  0, "r2":  0, "r3":  0, 
                         "r4":  0, "r5":  0, "r6":  0, "r7":  0, 
                         "r8":  0, "r9":  0, "r10": 0, "r11": 0, 
                         "r12": 0, "r13": 0, "r14": 0, "r15": 0, 
                         "r16": 0, "r17": 0, "r18": 0, "r19": 0, 
                         "r20": 0, "r21": 0, "r22": 0, "r23": 0, 
                         "r24": 0, "r25": 0, "r26": 0, "r27": 0, 
                         "r28": 0, "r29": 0, "r30": 0, "r31": 0}

        self._core_regs = {"ip": 0, "sp": 0}
        self._sreg = {"z": False, # zero
                      "c": False, # carry
                      "n": False, # negative
                     }

    def next_step(self):
        """Run one cpu clock cycle."""

        # get instruction at 'ip'
        raw_instr = self._mem.get_address(self._core_regs["ip"])

        instr = (raw_instr & 0x000000ff)
        flags = (raw_instr & 0x0000ff00) >> 8
        op1   = (raw_instr & 0x00ff0000) >> 16
        op2   = (raw_instr & 0xff000000) >> 24

        flags_vec = [False] * 8
        flags_vec[0] = True if ((flags & (1 << 0)) > 0) else False
        flags_vec[1] = True if ((flags & (1 << 1)) > 0) else False
        flags_vec[2] = True if ((flags & (1 << 2)) > 0) else False
        flags_vec[3] = True if ((flags & (1 << 3)) > 0) else False
        flags_vec[4] = True if ((flags & (1 << 4)) > 0) else False
        flags_vec[5] = True if ((flags & (1 << 5)) > 0) else False
        flags_vec[6] = True if ((flags & (1 << 6)) > 0) else False
        flags_vec[7] = True if ((flags & (1 << 7)) > 0) else False

        self.__alu.instructions[instr](flags_vec, op1, op2)

    def readahead(self):
        return self._mem.get_address(self._core_regs["ip"] + 1)

    def print_regs(self):
        list_of_regs = ["r0",  "r1",  "r2",  "r3",  "r4",  "r5",  "r6",  "r7",
                        "r8",  "r9",  "r10", "r11", "r12", "r13", "r14", "r15",
                        "r16", "r17", "r18", "r19", "r20", "r21", "r22", "r23",
                        "r24", "r25", "r26", "r27", "r28", "r29", "r30", "r31"]
        for e in list_of_regs:
            print("%4s: 0x%08X" % (e, self._gp_regs[e]))

        print("=====")

        list_of_regs = ["ip", "sp"]
        for e in list_of_regs:
            print("%4s: 0x%08X" % (e, self._core_regs[e]))

        list_of_regs = ["z", "c", "n"]
        for e in list_of_regs:
            print("%4s: %r" % (e, self._sreg[e]))            
















