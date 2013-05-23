def init_pyArch():
    global LOGGER
    LOGGER = None

    if LOGGER == None:
        LOGGER = initLogger()

    LOGGER.log("init PyArch completed","INFO")


def initLogger():
    import pyArch.logger
    return pyArch.logger.PyArchLogger()


init_pyArch()
