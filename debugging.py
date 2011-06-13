import logging
import logging.handlers
import sqlitehandler
from termcolor import colored

class debug(object):
    # Create a logging object (after configuring logging)
    logger = logging.getLogger('bitbotDebugger')

    # optionally, we could define a logger like so:
    #myHandler = sqlitehandler.SQLiteHandler('debugLog.sqlite')

    # set the lowest level of event to log.  If undefined, defaults to logging.WARNING
    # valid levels: 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
    logger.setLevel(logging.DEBUG)

    # Add our custom logging handler to logger
    # The arg we're passing is the name of the SQLite database file to use
    logger.addHandler(sqlitehandler.SQLiteHandler('debugLog.sqlite'))


    def __init__(self, f):
        self.f = f

    def __call__(self):
        self.logger.debug('Going to call ' + self.f.__name__)
        #print colored("Going to call" + self.f.__name__, 'cyan')

# TODO: fix the self.f call because it doesn't work properly

        self.f() # actually call whatever we're decorating
        self.logger.debug('Done calling ' + self.f.__name__)
        #print colored("Done calling" + self.f.__name__, 'blue')
"""
class logThing(object):
    def __init__(self, loggername, loglevel)
    # Create a logging object (after configuring logging)
    logger = logging.getLogger(loggername)

    # optionally, we could define a logger like so:
    #myHandler = sqlitehandler.SQLiteHandler('debugLog.sqlite')

    # set the lowest level of event to log.  If undefined, defaults to logging.WARNING
    # valid levels: 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
    logger.setLevel(loglevel)

    # Add our custom logging handler to logger
    # The arg we're passing is the name of the SQLite database file to use
    logger.addHandler(sqlitehandler.SQLiteHandler('debugLog.sqlite'))
    return logger
"""
