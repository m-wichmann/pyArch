#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main file to start a simulation."""

# TODO:
# - replace this file with something better
# - implement the whole 'system' thing -> build your own cpu

# cmd line parsing
import argparse

from backend import *


def pyArch_main(romfile, stepcount):
    """Simulator main method. Runs the code in 'romfile' for 'stepcount' steps."""
    cpu = __init(romfile)

    for i in range(stepcount):
        cpu.next_step()


def __init(romfile):
    """Init this system. In future the system should be configured by the user."""

    # sys init
    # TODO:
    # implement sys, so it does anything
    sys_ = sys.SYS()

    # bus init
    bus_ = bus.BUS()

    # cpu init
    cpu_ = cpu.CPU(bus_)

    # mem init
    ram_ = ram.RAM()
    rom_ = rom.ROM(romfile)
    mio_ = mio.MIO()
    mem_ = mem.MEM()
    mem_.add_segment(rom_)
    mem_.add_segment(ram_)
    mem_.add_segment(mio_)

    # populate bus
    bus_.register_mem(mem_)
    bus_.register_cpu(cpu_)

    # init mem specific parts in cpu
    cpu_.init_mem()

    return cpu_


if __name__ == '__main__':
    # cmd line argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--romfile", action="store", dest="romfile", help="romfile")
    parser.add_argument("-s", "--stepcount", action="store", dest="stepcount", help="stepcount")
    args = parser.parse_args()

    # define default values and read cmd line options
    romfile = 'test.rom'
    stepcount = 10
    if args.romfile:
        romfile = args.romfile
    if args.stepcount:
        stepcount = int(args.stepcount)

    # call main method
    pyArch_main(romfile, stepcount)
