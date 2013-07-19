def init_pyArch():
    global LOGGER
    LOGGER = None

    if LOGGER == None:
        LOGGER = initLogger()

    LOGGER.log("init PyArch completed","INFO")


def initLogger():
    from backend import logger
    return logger.PyArchLogger()


init_pyArch()

# TODO:
# add modules to this list if 'import * from backend' should import them!
__all__ = ["alu", "bus", "cpu", "mem", "mio", "ram", "rom", "sys"]
