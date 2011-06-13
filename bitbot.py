import urllib2
import json
#from debugging import debug
from ConfigParser import SafeConfigParser
import mtgox

cfg= SafeConfigParser()
cfg.read('bitbot.conf')

# ---- INIT ----
#@debug
def getBuyRate():
    result = json.load(urllib2.urlopen(cfg.get('mtgox', 'ApiTickerUrl')))
    return result['ticker']['buy']

# ---- MAIN ----

# test out the different log levels
#logger.debug('Test 1')
#logger.info('Test 2')
#logger.warning('Test 3')
#logger.error('Test 4')
#logger.critical('Test 5')

#print parser._sections['mtgox']

print getBuyRate()

mtgox = mtgox.API(email=cfg.get('mtgox', 'email'), 
	password=cfg.get('mtgox', 'password'),
        ApiTickerUrl=cfg.get('mtgox', 'ApiTickerUrl'),
        ApiGetFundsUrl=cfg.get('mtgox', 'ApiGetFundsUrl'),
        ApiSellUrl=cfg.get('mtgox', 'ApiSellUrl'))

print mtgox.getBuyRate()
