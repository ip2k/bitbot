import urllib2
import json
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('bitbot.conf')

def getRate():
    result = json.load(urllib2.urlopen(parser.get('mtgox', 'ApiTickerUrl')))
    return result['ticker']['buy']

print parser._sections['mtgox']
print getRate()

