#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

import src
import src.token
import src.parser
import src.output

def read_file(infile):
    fd = open(infile, 'r')
    lines = []
    for line in fd:
        line = line.replace('\n','')
        if len(line) > 0:
            lines.append(line)
    return lines

def pyArch_asm_main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--infile", action="store", dest="infile", help="infile")
    parser.add_argument("-o", "--outfile", action="store", dest="outfile", help="outfile")
    args = parser.parse_args()

    infile = 'test.s'
    outfile = 'test.out'

    if args.infile:
        infile = args.infile
    if args.outfile:
        outfile = args.outfile

    tokenizer = src.token.Tokenizer()
    parser = src.parser.Parser()
    output = src.output.Output()

    lines = read_file(infile)
    tokens = tokenizer.tokenize(lines)
    parsed_tokens = parser.parse(tokens)
    output.output_text(parsed_tokens, outfile)

if __name__ == '__main__':
    pyArch_asm_main()
