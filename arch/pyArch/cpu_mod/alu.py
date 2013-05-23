#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# TODO:
# - flags: carry, sign...!!!

import pyArch

class ALU(object):

    def __init__(self, cpu):
        self.__cpu = cpu
        self.__register_instr()
        pyArch.LOGGER.log("init ALU completed","INFO")

    def __register_instr(self):
        self.instructions = [self.__OP_nop] * 256
        self.instructions[0x00] = self.__OP_nop

        self.instructions[0x10] = self.__OP_mov
        self.instructions[0x11] = self.__OP_ld
        self.instructions[0x12] = self.__OP_st
        self.instructions[0x13] = self.__OP_push
        self.instructions[0x14] = self.__OP_pop

        self.instructions[0x20] = self.__OP_add
        self.instructions[0x21] = self.__OP_sub
        self.instructions[0x22] = self.__OP_mul
        self.instructions[0x23] = self.__OP_div
        self.instructions[0x2E] = self.__OP_inc
        self.instructions[0x2F] = self.__OP_dec

        self.instructions[0x30] = self.__OP_and
        self.instructions[0x31] = self.__OP_or
        self.instructions[0x32] = self.__OP_xor
        self.instructions[0x33] = self.__OP_com
        self.instructions[0x34] = self.__OP_neg
        self.instructions[0x35] = self.__OP_lsl
        self.instructions[0x36] = self.__OP_lsr
        self.instructions[0x37] = self.__OP_rol
        self.instructions[0x38] = self.__OP_ror

        self.instructions[0x50] = self.__OP_jmp

        self.instructions[0xA0] = self.__OP_prt

    ##### Util         #####
    def __increase_ip(self, amount):
        self.__cpu._core_regs["ip"] = self.__cpu._core_regs["ip"] + amount

    ##### Instructions #####
    def __OP_template(self, flags, op1, op2):
        # read flags
        # fetch data
        # run instruction
        # update IP
        pass

    ## Basic instructions ##
    def __OP_nop(self, flags, op1, op2):
        """0x00"""
        pyArch.LOGGER.log("instruction: nop","DEBUG")
        self.__increase_ip(1)

    ## Data handling ##
    def __OP_mov(self, flags, op1, op2):
        """0x10"""
        pyArch.LOGGER.log("instruction: mov","DEBUG")
        self.__cpu._gp_regs["r" + str(op1)] = self.__cpu._gp_regs["r" + str(op2)]
        pyArch.LOGGER.log("  r%i = r%i" % (op1, op2), "DEBUG")
        self.__increase_ip(1)

    def __OP_ld(self, flags, op1, op2):
        """0x11"""
        pyArch.LOGGER.log("instruction: ld","DEBUG")
        readahead = self.__cpu.readahead()
        if (flags[0]):
            value = readahead
        else:
            value = self.__cpu._mem.get_address(readahead)
        self.__cpu._gp_regs["r" + str(op1)] = value
        pyArch.LOGGER.log("  r%i = %i" % (op1, value), "DEBUG")
        self.__increase_ip(2)

    def __OP_st(self, flags, op1, op2):
        """0x12"""
        pyArch.LOGGER.log("instruction: st","DEBUG")
        address = self.__cpu.readahead()
        self.__cpu._mem.set_address(address, self.__cpu._gp_regs["r" + str(op1)])
        pyArch.LOGGER.log("  0x%08X = %i" % (address, op1), "DEBUG")
        self.__increase_ip(2)

    def __OP_push(self, flags, op1, op2):
        """0x13"""
        pyArch.LOGGER.log("instruction: push","DEBUG")

        num_op1 = self.__cpu._gp_regs["r" + str(op1)]
        sp = self.__cpu._core_regs["sp"]

        self.__cpu._mem.set_address(sp, num_op1)

        self.__cpu._core_regs["sp"] = self.__cpu._core_regs["sp"] + 1

        pyArch.LOGGER.log("  stack push: 0x%08X" % (num_op1), "DEBUG")
        self.__increase_ip(1)

    def __OP_pop(self, flags, op1, op2):
        """0x14"""
        pyArch.LOGGER.log("instruction: pop","DEBUG")

        self.__cpu._core_regs["sp"] = self.__cpu._core_regs["sp"] - 1

        sp = self.__cpu._core_regs["sp"]
        num = self.__cpu._mem.get_address(sp)
        self.__cpu._gp_regs["r" + str(op1)] = num

        pyArch.LOGGER.log("  stack pop: 0x%08X -> r%i" % (num, op1), "DEBUG")
        self.__increase_ip(1)

    ## Arithmetic ##
    def __OP_add(self, flags, op1, op2):
        """0x20"""
        pyArch.LOGGER.log("instruction: add","DEBUG")

        op_number = flags[0]

        num_op1 = self.__cpu._gp_regs["r" + str(op1)]
        num_op2 = op2 if op_number else self.__cpu._gp_regs["r" + str(op2)]

        ret = num_op1 + num_op2
        self.__cpu._gp_regs["r" + str(op1)] = ret
        pyArch.LOGGER.log("  %i + %i = %i" % (num_op1, num_op2, ret), "DEBUG")
        self.__increase_ip(1)

    def __OP_sub(self, flags, op1, op2):
        """0x21"""
        pyArch.LOGGER.log("instruction: sub","DEBUG")

        op_number = flags[0]

        num_op1 = self.__cpu._gp_regs["r" + str(op1)]
        num_op2 = op2 if op_number else self.__cpu._gp_regs["r" + str(op2)]

        ret = num_op1 - num_op2
        self.__cpu._gp_regs["r" + str(op1)] = ret
        pyArch.LOGGER.log("  %i - %i = %i" % (num_op1, num_op2, ret), "DEBUG")
        self.__increase_ip(1)

    def __OP_mul(self, flags, op1, op2):
        """0x22"""
        pyArch.LOGGER.log("instruction: mul","DEBUG")

        op_number = flags[0]

        num_op1 = self.__cpu._gp_regs["r" + str(op1)]
        num_op2 = op2 if op_number else self.__cpu._gp_regs["r" + str(op2)]

        ret = num_op1 * num_op2
        self.__cpu._gp_regs["r" + str(op1)] = ret
        pyArch.LOGGER.log("  %i * %i = %i" % (num_op1, num_op2, ret), "DEBUG")
        self.__increase_ip(1)

    def __OP_div(self, flags, op1, op2):
        """0x23"""
        pyArch.LOGGER.log("instruction: div","DEBUG")

        op_number = flags[0]

        num_op1 = self.__cpu._gp_regs["r" + str(op1)]
        num_op2 = op2 if op_number else self.__cpu._gp_regs["r" + str(op2)]

        ret = num_op1 / num_op2
        self.__cpu._gp_regs["r" + str(op1)] = ret
        pyArch.LOGGER.log("  %i / %i = %i" % (num_op1, num_op2, ret), "DEBUG")
        self.__increase_ip(1)

    def __OP_inc(self, flags, op1, op2):
        """0x2E"""
        pyArch.LOGGER.log("instruction: inc","DEBUG")

        self.__cpu._gp_regs["r" + str(op1)] = self.__cpu._gp_regs["r" + str(op1)] + 1

        pyArch.LOGGER.log("  inc: r%i -> 0x%08X" % (op1, self.__cpu._gp_regs["r" + str(op1)]), "DEBUG")
        self.__increase_ip(1)

    def __OP_dec(self, flags, op1, op2):
        """0x2F"""
        pyArch.LOGGER.log("instruction: dec","DEBUG")

        self.__cpu._gp_regs["r" + str(op1)] = self.__cpu._gp_regs["r" + str(op1)] - 1

        pyArch.LOGGER.log("  dec: r%i -> 0x%08X" % (op1, self.__cpu._gp_regs["r" + str(op1)]), "DEBUG")
        self.__increase_ip(1)

    ## Logic ##
    def __OP_and(self, flags, op1, op2):
        """0x30"""
        pyArch.LOGGER.log("instruction: and","DEBUG")

        op_number = flags[0]

        num_op1 = self.__cpu._gp_regs["r" + str(op1)]
        num_op2 = op2 if op_number else self.__cpu._gp_regs["r" + str(op2)]

        ret = num_op1 & num_op2

        self.__cpu._gp_regs["r" + str(op1)] = ret
        pyArch.LOGGER.log("  %i & %i = %i" % (num_op1, num_op2, ret), "DEBUG")
        self.__increase_ip(1)

    def __OP_or(self, flags, op1, op2):
        """0x31"""
        pyArch.LOGGER.log("instruction: or","DEBUG")

        op_number = flags[0]

        num_op1 = self.__cpu._gp_regs["r" + str(op1)]
        num_op2 = op2 if op_number else self.__cpu._gp_regs["r" + str(op2)]

        ret = num_op1 | num_op2

        self.__cpu._gp_regs["r" + str(op1)] = ret
        pyArch.LOGGER.log("  %i | %i = %i" % (num_op1, num_op2, ret), "DEBUG")
        self.__increase_ip(1)

    def __OP_xor(self, flags, op1, op2):
        """0x32"""
        pyArch.LOGGER.log("instruction: xor","DEBUG")

        op_number = flags[0]

        num_op1 = self.__cpu._gp_regs["r" + str(op1)]
        num_op2 = op2 if op_number else self.__cpu._gp_regs["r" + str(op2)]

        ret = num_op1 ^ num_op2

        self.__cpu._gp_regs["r" + str(op1)] = ret
        pyArch.LOGGER.log("  %i ^ %i = %i" % (num_op1, num_op2, ret), "DEBUG")
        self.__increase_ip(1)

    def __OP_com(self, flags, op1, op2):
        """0x33"""
        pyArch.LOGGER.log("instruction: com","DEBUG")

        num_op = self.__cpu._gp_regs["r" + str(op1)]

        ret = (~num_op) & 0xffffffff

        self.__cpu._gp_regs["r" + str(op1)] = ret
        pyArch.LOGGER.log("  com: %i -> %i" % (num_op, ret), "DEBUG")
        self.__increase_ip(1)

    def __OP_neg(self, flags, op1, op2):
        """0x34"""
        pyArch.LOGGER.log("instruction: neg","DEBUG")

        num_op = self.__cpu._gp_regs["r" + str(op1)]

        ret = ((~num_op) + 1) & 0xffffffff

        self.__cpu._gp_regs["r" + str(op1)] = ret
        pyArch.LOGGER.log("  neg: %i -> %i" % (num_op, ret), "DEBUG")
        self.__increase_ip(1)

    def __OP_lsl(self, flags, op1, op2):
        """0x35"""
        pyArch.LOGGER.log("instruction: lsl","DEBUG")

        num_op = self.__cpu._gp_regs["r" + str(op1)]

        ret = (num_op << op2) & 0xffffffff

        self.__cpu._gp_regs["r" + str(op1)] = ret
        pyArch.LOGGER.log("  lsl: %i -> %i" % (num_op, ret), "DEBUG")
        self.__increase_ip(1)

    def __OP_lsr(self, flags, op1, op2):
        """0x36"""
        pyArch.LOGGER.log("instruction: lsr","DEBUG")

        num_op = self.__cpu._gp_regs["r" + str(op1)]

        ret = (num_op >> op2) & 0xffffffff

        self.__cpu._gp_regs["r" + str(op1)] = ret
        pyArch.LOGGER.log("  lsr: %i -> %i" % (num_op, ret), "DEBUG")
        self.__increase_ip(1)

    def __OP_rol(self, flags, op1, op2):
        """0x37"""
        pyArch.LOGGER.log("instruction: rol","DEBUG")

        num_op = self.__cpu._gp_regs["r" + str(op1)]

        ret = num_op
        for i in range(op2):
            ret = ((ret << 1) | ((ret & 0x80000000) >> 31)) & 0xffffffff

        self.__cpu._gp_regs["r" + str(op1)] = ret
        pyArch.LOGGER.log("  rol: %i -> %i" % (num_op, ret), "DEBUG")
        self.__increase_ip(1)

    def __OP_ror(self, flags, op1, op2):
        """0x38"""
        pyArch.LOGGER.log("instruction: ror","DEBUG")

        num_op = self.__cpu._gp_regs["r" + str(op1)]

        ret = num_op
        for i in range(op2):
            ret = ((ret >> 1) | ((ret & 1) << 31)) & 0xffffffff

        self.__cpu._gp_regs["r" + str(op1)] = ret
        pyArch.LOGGER.log("  ror: %i -> %i" % (num_op, ret), "DEBUG")
        self.__increase_ip(1)

    ## Reserved ##


    ## Control flow ##
    def __OP_jmp(self, flags, op1, op2):
        """0x50"""
        pyArch.LOGGER.log("instruction: jmp","DEBUG")

        num_op = 0
        if flags[0]:    # relative
            num_op = self.__cpu._core_regs["ip"] + op1
        else:           # absolute
            num_op = self.__cpu._gp_regs["r" + str(op1)]

        self.__cpu._core_regs["ip"] = num_op

        pyArch.LOGGER.log("  jmp: -> 0x%08X" % (num_op), "DEBUG")
    

    ## Systemcalls ##
    def __OP_prt(self, flags, op1, op2):
        """0xA0"""
        pyArch.LOGGER.log("instruction: prt","DEBUG")

        print("r%i: 0x%08X" % (op1, self.__cpu._gp_regs["r" + str(op1)]))
        self.__increase_ip(1)



















