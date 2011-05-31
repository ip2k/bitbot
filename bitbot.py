import urllib2
import json
import logging
import logging.handlers
import sqlitehandler
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('bitbot.conf')

# ---- INIT ----
def getRate():
    result = json.load(urllib2.urlopen(parser.get('mtgox', 'ApiTickerUrl')))
    return result['ticker']['buy']

print parser._sections['mtgox']
print getRate()


# ---- MAIN ----
# Create a logging object (after configuring logging)
logger = logging.getLogger('someLoggerNameLikeDebugOrWhatever')

# optionally, we could define a logger like so:
#myHandler = sqlitehandler.SQLiteHandler('debugLog.sqlite')

# set the lowest level of event to log.  If undefined, defaults to logging.WARNING
# valid levels: 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
logger.setLevel(logging.DEBUG)

# Add our custom logging handler to logger
# The arg we're passing is the name of the SQLite database file to use
logger.addHandler(sqlitehandler.SQLiteHandler('debugLog.sqlite'))

# test out the different log levels
logger.debug('Test 1')
logger.info('Test 2')
logger.warning('Test 3')
logger.error('Test 4')
logger.critical('Test 5')
