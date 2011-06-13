import urllib2
import json

class API(object):
    def __init__(self, email, password, ApiTickerUrl, ApiGetFundsUrl, ApiSellUrl):
        self.email, self.password, self.ApiTickerUrl, self.ApiGetFundsUrl, self.ApiSellUrl = email, password, ApiTickerUrl, ApiGetFundsUrl, ApiSellUrl

    def getBuyRate(self):
        result = json.load(urllib2.urlopen(self.ApiTickerUrl))
        return result['ticker']['buy']

    def getBuyRate(self):
        result = json.load(urllib2.urlopen(self.ApiTickerUrl))
        return result['ticker']['buy']

    def getBuyRate(self):
        result = json.load(urllib2.urlopen(self.ApiTickerUrl))
        return result['ticker']['buy']


    def getBuyRate(self):
        result = json.load(urllib2.urlopen(self.ApiTickerUrl))
        return result['ticker']['buy']

    def getBuyRate(self):
        result = json.load(urllib2.urlopen(self.ApiTickerUrl))
        return result['ticker']['buy']

