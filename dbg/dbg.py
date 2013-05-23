#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

import src

def pyArch_dbg_main():

    parser = argparse.ArgumentParser()
#    parser.add_argument("-i", "--infile", action="store", dest="infile", help="infile")
    args = parser.parse_args()

#    infile = 'test.s'
#    if args.infile:
#        infile = args.infile


if __name__ == '__main__':
    pyArch_dbg_main()
