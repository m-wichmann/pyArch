#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import backend

class SYS(object):
    """This is supposed to represent one system config. So here should be contained: memory layout, cpu/alu selection, 'reset button'."""
    def __init__(self):
        backend.LOGGER.log("init SYS completed","INFO")
