def init_pyArch():
    global LOGGER
    LOGGER = None

    if LOGGER == None:
        LOGGER = initLogger()

    LOGGER.log("init PyArch completed","INFO")


def initLogger():
    import src.logger
    return src.logger.PyArchLogger()


init_pyArch()
