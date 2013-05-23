#!/usr/bin/env python3
# -*- coding: utf-8 -*-

INSTR_PER_LINE = 8

class Output(object):
    def __init__(self):
        pass

    def output_text(self, tokens, outfile):
        fd = open(outfile, 'w')
        instr_counter = 0
        for t in tokens:
            instr = "%02X%02X%02X%02X" % tuple(reversed(t))

            instr_counter = instr_counter + 1
            if (instr_counter >= INSTR_PER_LINE):
                instr_counter = 0
                instr += "\n"
            else:
                instr += " "
            fd.write(instr)

        fd.close()

