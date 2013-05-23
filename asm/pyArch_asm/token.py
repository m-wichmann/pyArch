#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Tokenizer(object):
    def __init__(self):
        pass

    def tokenize(self, lines):
        lines_cut = []
        tokens = []

        for line in lines:
            pos = line.find('#')
            pos = len(line) if pos == -1 else pos
            line = line[:pos]
            if len(line) > 0:
                lines_cut.append(line)

        for l in lines_cut:
            token = {}
            temp = l.split()
            token["instr"] = temp[0]
            try:
                token["op1"]   = temp[1].replace(',','')
            except IndexError:
                token["op1"] = None
            try:
                token["op2"] = temp[2]
            except IndexError:
                token["op2"] = None

            tokens.append(token)

        return tokens
