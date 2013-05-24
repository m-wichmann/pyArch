#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""The ALU contains all possibile operations."""

# TODO:
# - flags: carry!!!
# - signed numbers testing
# - refactor name 'alu'

import src

class ALU(object):
    def __init__(self, cpu):
        # store pointer to cpu, since the operations need the registers
        self.__cpu = cpu
        # register all instructions
        self.__register_instr()
        src.LOGGER.log("init ALU completed","INFO")

    def __register_instr(self):
        """This method basically links the op_codes (byte value isntructions) to python methods."""
        # set up instruction vector
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
        self.instructions[0x3F] = self.__OP_tst

        self.instructions[0x50] = self.__OP_jmp
        self.instructions[0x60] = self.__OP_breq
        self.instructions[0x61] = self.__OP_brne
        self.instructions[0x62] = self.__OP_brp
        self.instructions[0x63] = self.__OP_brn
        self.instructions[0x8F] = self.__OP_cmp

        self.instructions[0xA0] = self.__OP_prt

    ##### Util         #####
    def __increase_ip(self, amount):
        """Increse isntruction pointer by 'amount'."""
        self.__cpu._core_regs["ip"] = self.__cpu._core_regs["ip"] + amount

    def __set_sreg_s_z(self, number):
        """Update sind and zero flag for 'number'."""
        # zero flag
        if number == 0:
            self.__cpu._sreg["z"] = True
        else:
            self.__cpu._sreg["z"] = False

        # negative flag
        if (number & (1<<31)) == (1<<31):
            self.__cpu._sreg["n"] = True
        else:
            self.__cpu._sreg["n"] = False

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
        src.LOGGER.log("instruction: nop","DEBUG")
        self.__increase_ip(1)

    ## Data handling ##
    def __OP_mov(self, flags, op1, op2):
        """0x10"""
        src.LOGGER.log("instruction: mov","DEBUG")
        self.__cpu._gp_regs["r" + str(op1)] = self.__cpu._gp_regs["r" + str(op2)]
        src.LOGGER.log("  r%i = r%i" % (op1, op2), "DEBUG")
        self.__increase_ip(1)

    def __OP_ld(self, flags, op1, op2):
        """0x11"""
        src.LOGGER.log("instruction: ld","DEBUG")
        readahead = self.__cpu.readahead()
        if (flags[0]):
            value = readahead
        else:
            value = self.__cpu._mem.get_address(readahead)
        self.__cpu._gp_regs["r" + str(op1)] = value
        src.LOGGER.log("  r%i = %i" % (op1, value), "DEBUG")
        self.__increase_ip(2)

    def __OP_st(self, flags, op1, op2):
        """0x12"""
        src.LOGGER.log("instruction: st","DEBUG")
        address = self.__cpu.readahead()
        self.__cpu._mem.set_address(address, self.__cpu._gp_regs["r" + str(op1)])
        src.LOGGER.log("  0x%08X = %i" % (address, op1), "DEBUG")
        self.__increase_ip(2)

    def __OP_push(self, flags, op1, op2):
        """0x13"""
        src.LOGGER.log("instruction: push","DEBUG")

        num_op1 = self.__cpu._gp_regs["r" + str(op1)]
        sp = self.__cpu._core_regs["sp"]

        self.__cpu._mem.set_address(sp, num_op1)

        self.__cpu._core_regs["sp"] = self.__cpu._core_regs["sp"] - 1

        src.LOGGER.log("  stack push: 0x%08X" % (num_op1), "DEBUG")
        self.__increase_ip(1)

    def __OP_pop(self, flags, op1, op2):
        """0x14"""
        src.LOGGER.log("instruction: pop","DEBUG")

        self.__cpu._core_regs["sp"] = self.__cpu._core_regs["sp"] + 1

        sp = self.__cpu._core_regs["sp"]
        num = self.__cpu._mem.get_address(sp)

        self.__cpu._gp_regs["r" + str(op1)] = num

        src.LOGGER.log("  stack pop: 0x%08X -> r%i" % (num, op1), "DEBUG")
        self.__increase_ip(1)

    ## Arithmetic ##
    def __OP_add(self, flags, op1, op2):
        """0x20"""
        src.LOGGER.log("instruction: add","DEBUG")

        op_number = flags[0]

        num_op1 = self.__cpu._gp_regs["r" + str(op1)]
        num_op2 = op2 if op_number else self.__cpu._gp_regs["r" + str(op2)]

        ret = (num_op1 + num_op2) & 0xffffffff

        self.__set_sreg_s_z(ret)

        self.__cpu._gp_regs["r" + str(op1)] = ret
        src.LOGGER.log("  %i + %i = %i" % (num_op1, num_op2, ret), "DEBUG")
        self.__increase_ip(1)

    def __OP_sub(self, flags, op1, op2):
        """0x21"""
        src.LOGGER.log("instruction: sub","DEBUG")

        op_number = flags[0]

        num_op1 = self.__cpu._gp_regs["r" + str(op1)]
        num_op2 = op2 if op_number else self.__cpu._gp_regs["r" + str(op2)]

        ret = (num_op1 - num_op2) & 0xffffffff

        self.__set_sreg_s_z(ret)

        self.__cpu._gp_regs["r" + str(op1)] = ret
        src.LOGGER.log("  %i - %i = %i" % (num_op1, num_op2, ret), "DEBUG")
        self.__increase_ip(1)

    def __OP_mul(self, flags, op1, op2):
        """0x22"""
        src.LOGGER.log("instruction: mul","DEBUG")

        op_number = flags[0]

        num_op1 = self.__cpu._gp_regs["r" + str(op1)]
        num_op2 = op2 if op_number else self.__cpu._gp_regs["r" + str(op2)]

        ret = (num_op1 * num_op2) & 0xffffffff

        self.__set_sreg_s_z(ret)

        self.__cpu._gp_regs["r" + str(op1)] = ret
        src.LOGGER.log("  %i * %i = %i" % (num_op1, num_op2, ret), "DEBUG")
        self.__increase_ip(1)

    def __OP_div(self, flags, op1, op2):
        """0x23"""
        src.LOGGER.log("instruction: div","DEBUG")

        op_number = flags[0]

        num_op1 = self.__cpu._gp_regs["r" + str(op1)]
        num_op2 = op2 if op_number else self.__cpu._gp_regs["r" + str(op2)]

        ret = (num_op1 / num_op2) & 0xffffffff

        self.__set_sreg_s_z(ret)

        self.__cpu._gp_regs["r" + str(op1)] = ret
        src.LOGGER.log("  %i / %i = %i" % (num_op1, num_op2, ret), "DEBUG")
        self.__increase_ip(1)

    def __OP_inc(self, flags, op1, op2):
        """0x2E"""
        src.LOGGER.log("instruction: inc","DEBUG")

        ret = (self.__cpu._gp_regs["r" + str(op1)] + 1) & 0xffffffff
        self.__cpu._gp_regs["r" + str(op1)] = ret
        self.__set_sreg_s_z(ret)

        src.LOGGER.log("  inc: r%i -> 0x%08X" % (op1, self.__cpu._gp_regs["r" + str(op1)]), "DEBUG")
        self.__increase_ip(1)

    def __OP_dec(self, flags, op1, op2):
        """0x2F"""
        src.LOGGER.log("instruction: dec","DEBUG")

        ret = (self.__cpu._gp_regs["r" + str(op1)] - 1) & 0xffffffff
        self.__cpu._gp_regs["r" + str(op1)] = ret
        self.__set_sreg_s_z(ret)

        src.LOGGER.log("  dec: r%i -> 0x%08X" % (op1, self.__cpu._gp_regs["r" + str(op1)]), "DEBUG")
        self.__increase_ip(1)

    ## Logic ##
    def __OP_and(self, flags, op1, op2):
        """0x30"""
        src.LOGGER.log("instruction: and","DEBUG")

        op_number = flags[0]

        num_op1 = self.__cpu._gp_regs["r" + str(op1)]
        num_op2 = op2 if op_number else self.__cpu._gp_regs["r" + str(op2)]

        ret = num_op1 & num_op2

        self.__set_sreg_s_z(ret)

        self.__cpu._gp_regs["r" + str(op1)] = ret
        src.LOGGER.log("  %i & %i = %i" % (num_op1, num_op2, ret), "DEBUG")
        self.__increase_ip(1)

    def __OP_or(self, flags, op1, op2):
        """0x31"""
        src.LOGGER.log("instruction: or","DEBUG")

        op_number = flags[0]

        num_op1 = self.__cpu._gp_regs["r" + str(op1)]
        num_op2 = op2 if op_number else self.__cpu._gp_regs["r" + str(op2)]

        ret = num_op1 | num_op2

        self.__set_sreg_s_z(ret)

        self.__cpu._gp_regs["r" + str(op1)] = ret
        src.LOGGER.log("  %i | %i = %i" % (num_op1, num_op2, ret), "DEBUG")
        self.__increase_ip(1)

    def __OP_xor(self, flags, op1, op2):
        """0x32"""
        src.LOGGER.log("instruction: xor","DEBUG")

        op_number = flags[0]

        num_op1 = self.__cpu._gp_regs["r" + str(op1)]
        num_op2 = op2 if op_number else self.__cpu._gp_regs["r" + str(op2)]

        ret = num_op1 ^ num_op2

        self.__set_sreg_s_z(ret)

        self.__cpu._gp_regs["r" + str(op1)] = ret
        src.LOGGER.log("  %i ^ %i = %i" % (num_op1, num_op2, ret), "DEBUG")
        self.__increase_ip(1)

    def __OP_com(self, flags, op1, op2):
        """0x33"""
        src.LOGGER.log("instruction: com","DEBUG")

        num_op = self.__cpu._gp_regs["r" + str(op1)]

        ret = (~num_op) & 0xffffffff

        self.__set_sreg_s_z(ret)

        self.__cpu._gp_regs["r" + str(op1)] = ret
        src.LOGGER.log("  com: %i -> %i" % (num_op, ret), "DEBUG")
        self.__increase_ip(1)

    def __OP_neg(self, flags, op1, op2):
        """0x34"""
        src.LOGGER.log("instruction: neg","DEBUG")

        num_op = self.__cpu._gp_regs["r" + str(op1)]

        ret = ((~num_op) + 1) & 0xffffffff

        self.__set_sreg_s_z(ret)

        self.__cpu._gp_regs["r" + str(op1)] = ret
        src.LOGGER.log("  neg: %i -> %i" % (num_op, ret), "DEBUG")
        self.__increase_ip(1)

    def __OP_lsl(self, flags, op1, op2):
        """0x35"""
        src.LOGGER.log("instruction: lsl","DEBUG")

        num_op = self.__cpu._gp_regs["r" + str(op1)]

        ret = (num_op << op2) & 0xffffffff

        self.__set_sreg_s_z(ret)

        self.__cpu._gp_regs["r" + str(op1)] = ret
        src.LOGGER.log("  lsl: %i -> %i" % (num_op, ret), "DEBUG")
        self.__increase_ip(1)

    def __OP_lsr(self, flags, op1, op2):
        """0x36"""
        src.LOGGER.log("instruction: lsr","DEBUG")

        num_op = self.__cpu._gp_regs["r" + str(op1)]

        ret = (num_op >> op2) & 0xffffffff

        self.__set_sreg_s_z(ret)

        self.__cpu._gp_regs["r" + str(op1)] = ret
        src.LOGGER.log("  lsr: %i -> %i" % (num_op, ret), "DEBUG")
        self.__increase_ip(1)

    def __OP_rol(self, flags, op1, op2):
        """0x37"""
        src.LOGGER.log("instruction: rol","DEBUG")

        num_op = self.__cpu._gp_regs["r" + str(op1)]

        ret = num_op
        for i in range(op2):
            ret = ((ret << 1) | ((ret & 0x80000000) >> 31)) & 0xffffffff

        self.__set_sreg_s_z(ret)

        self.__cpu._gp_regs["r" + str(op1)] = ret
        src.LOGGER.log("  rol: %i -> %i" % (num_op, ret), "DEBUG")
        self.__increase_ip(1)

    def __OP_ror(self, flags, op1, op2):
        """0x38"""
        src.LOGGER.log("instruction: ror","DEBUG")

        num_op = self.__cpu._gp_regs["r" + str(op1)]

        ret = num_op
        for i in range(op2):
            ret = ((ret >> 1) | ((ret & 1) << 31)) & 0xffffffff

        self.__set_sreg_s_z(ret)

        self.__cpu._gp_regs["r" + str(op1)] = ret
        src.LOGGER.log("  ror: %i -> %i" % (num_op, ret), "DEBUG")
        self.__increase_ip(1)

    def __OP_tst(self, flags, op1, op2):
        src.LOGGER.log("instruction: tst","DEBUG")

        num_op = self.__cpu._gp_regs["r" + str(op1)]
        self.__set_sreg_s_z(num_op)
        src.LOGGER.log("  tst: %i" % (num_op), "DEBUG")
        self.__increase_ip(1)

    ## Reserved ##


    ## Control flow ##
    def __OP_jmp(self, flags, op1, op2):
        """0x50"""
        src.LOGGER.log("instruction: jmp","DEBUG")

        num_op = 0
        if flags[0]:    # relative
            num_op = self.__cpu._core_regs["ip"] + op1
        else:           # absolute
            num_op = self.__cpu._gp_regs["r" + str(op1)]

        self.__cpu._core_regs["ip"] = num_op

        src.LOGGER.log("  jmp: -> 0x%08X" % (num_op), "DEBUG")
    
    def __OP_breq(self, flags, op1, op2):
        """0x60"""
        src.LOGGER.log("instruction: breq","DEBUG")

        condition = self.__cpu._sreg["z"]
        if condition:
            num_op = 0
            if flags[0]:    # relative
                num_op = self.__cpu._core_regs["ip"] + op1
            else:           # absolute
                num_op = self.__cpu._gp_regs["r" + str(op1)]

            self.__cpu._core_regs["ip"] = num_op
            src.LOGGER.log("  breq: -> 0x%08X" % (num_op), "DEBUG")
        else:
            self.__increase_ip(1)
            src.LOGGER.log("  breq: -> --------", "DEBUG")

    def __OP_brne(self, flags, op1, op2):
        """0x61"""
        src.LOGGER.log("instruction: brne","DEBUG")

        condition = not self.__cpu._sreg["z"]
        if condition:
            num_op = 0
            if flags[0]:    # relative
                num_op = self.__cpu._core_regs["ip"] + op1
            else:           # absolute
                num_op = self.__cpu._gp_regs["r" + str(op1)]

            self.__cpu._core_regs["ip"] = num_op
            src.LOGGER.log("  brne: -> 0x%08X" % (num_op), "DEBUG")
        else:
            self.__increase_ip(1)
            src.LOGGER.log("  brne: -> --------", "DEBUG")

    def __OP_brp(self, flags, op1, op2):
        """0x62"""
        src.LOGGER.log("instruction: brp","DEBUG")

        condition = not self.__cpu._sreg["n"]
        if condition:
            num_op = 0
            if flags[0]:    # relative
                num_op = self.__cpu._core_regs["ip"] + op1
            else:           # absolute
                num_op = self.__cpu._gp_regs["r" + str(op1)]

            self.__cpu._core_regs["ip"] = num_op
            src.LOGGER.log("  brp: -> 0x%08X" % (num_op), "DEBUG")
        else:
            self.__increase_ip(1)
            src.LOGGER.log("  brp: -> --------", "DEBUG")

    def __OP_brn(self, flags, op1, op2):
        """0x60"""
        src.LOGGER.log("instruction: brn","DEBUG")

        condition = self.__cpu._sreg["n"]
        if condition:
            num_op = 0
            if flags[0]:    # relative
                num_op = self.__cpu._core_regs["ip"] + op1
            else:           # absolute
                num_op = self.__cpu._gp_regs["r" + str(op1)]

            self.__cpu._core_regs["ip"] = num_op
            src.LOGGER.log("  brn: -> 0x%08X" % (num_op), "DEBUG")
        else:
            self.__increase_ip(1)
            src.LOGGER.log("  brn: -> --------", "DEBUG")

    def __OP_cmp(self, flags, op1, op2):
        """0x8F"""
        src.LOGGER.log("instruction: cmp","DEBUG")

        num_op1 = self.__cpu._gp_regs["r" + str(op1)]
        num_op2 = self.__cpu._gp_regs["r" + str(op2)]

        ret = num_op1 - num_op2
        self.__set_sreg_s_z(ret)

        src.LOGGER.log("  cmp: 0x%08X - 0x%08X" % (num_op1, num_op2), "DEBUG")
        self.__increase_ip(1)

    ## Systemcalls ##
    def __OP_prt(self, flags, op1, op2):
        """0xA0"""
        src.LOGGER.log("instruction: prt","DEBUG")

        print("r%i: 0x%08X" % (op1, self.__cpu._gp_regs["r" + str(op1)]))
        self.__increase_ip(1)



















