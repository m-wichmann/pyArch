#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main file to start a simulation."""

# TODO:
# - replace this file with something better
# - implement the whole 'system' thing -> build your own cpu

# cmd line parsing
import argparse

import src
import src.bus
import src.sys
import src.cpu
import src.mem
import src.ram
import src.rom
import src.mio

def pyArch_main(romfile, stepcount):
    """Simulator main method. Runs the code in 'romfile' for 'stepcount' steps."""
    cpu = __init(romfile)

    for i in range(stepcount):
        cpu.next_step()


def __init(romfile):
    """Init this system. In future the system should be configured by the user."""
    # sys init
#    sys = src.sys.SYS()

    # bus init
    bus = src.bus.BUS()

    # cpu init
    cpu = src.cpu.CPU(bus)

    # mem init
    ram = src.ram.RAM()
    rom = src.rom.ROM(romfile)
    mio = src.mio.MIO()
    mem = src.mem.MEM()
    mem.add_segment(rom)
    mem.add_segment(ram)
    mem.add_segment(mio)

    mem.print_segments()

    # populate bus
    bus.register_mem(mem)
    bus.register_cpu(cpu)

    # init mem specific parts in cpu
    cpu.init_mem()

    return cpu


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
