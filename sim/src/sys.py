#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import src

class SYS(object):
    """This is supposed to represent one system config. So here should be contained: memory layout, cpu/alu selection, 'reset button'."""
    def __init__(self):
        src.LOGGER.log("init SYS completed","INFO")
