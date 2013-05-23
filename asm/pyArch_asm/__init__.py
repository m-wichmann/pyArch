def init_pyArch_asm():
    global LOGGER
    LOGGER = None

    if LOGGER == None:
        LOGGER = initLogger()

    LOGGER.log("init PyArch asm completed","INFO")


def initLogger():
    import pyArch_asm.logger
    return pyArch_asm.logger.PyArchLogger()

init_pyArch_asm()
