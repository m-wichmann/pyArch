#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

import pyArch
import pyArch.bus
import pyArch.sys
import pyArch.cpu
import pyArch.mem
import pyArch.ram
import pyArch.rom
import pyArch.mio

def pyArch_main(romfile, stepcount):
    cpu = __init(romfile)

    for i in range(stepcount):
        cpu.next_step()


def __init(romfile):
    # sys init
#    sys = pyArch.sys.SYS()

    # bus init
    bus = pyArch.bus.BUS()

    # cpu init
    cpu = pyArch.cpu.CPU(bus)

    # mem init
    ram = pyArch.ram.RAM()
    rom = pyArch.rom.ROM(romfile)
    mio = pyArch.mio.MIO()
    mem = pyArch.mem.MEM()
    mem.add_segment(rom)
    mem.add_segment(ram)
    mem.add_segment(mio)

    # populate bus
    bus.register_mem(mem)
    bus.register_cpu(cpu)

    return cpu


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--romfile", action="store", dest="romfile", help="romfile")
    parser.add_argument("-s", "--stepcount", action="store", dest="stepcount", help="stepcount")
    args = parser.parse_args()

    romfile = 'test.rom'
    stepcount = 10
    if args.romfile:
        romfile = args.romfile
    if args.stepcount:
        stepcount = int(args.stepcount)

    pyArch_main(romfile, stepcount)
