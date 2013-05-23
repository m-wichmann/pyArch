def init_pyArch_asm():
    global LOGGER
    LOGGER = None

    if LOGGER == None:
        LOGGER = initLogger()

    LOGGER.log("init PyArch asm completed","INFO")


def initLogger():
    import src.logger
    return src.logger.PyArchLogger()

init_pyArch_asm()
