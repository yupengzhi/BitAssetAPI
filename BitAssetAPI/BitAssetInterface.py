#!/usr/bin/python
# -*- coding: utf-8 -*-

#from OKCoinSpotAPI import OKCoinSpot
#from OKCoinFutureAPI import OKCoinFuture
from BitAssetAPI import BitAssetMarketAPI,BitAssetDealsAPI

# init apikey，secretkey and RESTURL
#APIKEY = 'ak7b68c889d04045e5'
#SECRETKEY = 'b44f7c6a6ef44d9c84d7b4da2e02c8a1'
#RESTURL = 'http://api.bitasset.com'
APIKEY='ak178f82404a714188'
SECRETKEY='1ce9a832919d403a839ff4293cea10d8'
RESTURL = 'http://tapi.bitasset.cc:7005/'

marketApi = BitAssetMarketAPI(RESTURL, APIKEY, SECRETKEY)
print (u' 现货行情 ')
print (marketApi.servertime())
print (marketApi.currencies())
print (marketApi.symbols())
print (marketApi.depth("12"))




dealApi = BitAssetDealsAPI(RESTURL, APIKEY, SECRETKEY)
print(dealApi.accounts_balance())
#print(dealApi.trade('12','1','12','10','1'))
#print(dealApi.cancel('1534139092429211', '12'))
print(dealApi.get_order_info('1534139092429211'))
orderList=['1534139092429211']
print(dealApi.get_orders_info(orderList))




#print(dealApi.future_position_4fix('btc_usd', 'this_week','1'))
#dealApi.future_trade('btc_usd', 'this_week', price='8000', amount='10',trade_type='1', match_price='1', lever_rate='10')

# 现货API
#okcoinSpot = OKCoinSpot(OKCOINRESTURL, APIKEY, SECRETKEY)

# 期货API
#okcoinFuture = OKCoinFuture(OKCOINRESTURL, APIKEY, SECRETKEY)

#print (u' 现货行情 ')
#print (okcoinSpot.ticker('btc_usd'))

#print (u' 现货深度 ')
#print (okcoinSpot.depth('btc_usd'))

#print (u' 现货历史交易信息 ')
#print (okcoinSpot.trades())

#print (u' 用户现货账户信息 ')
#print (okcoinSpot.userinfo())

#print (u' 现货下单 ')
#print (okcoinSpot.trade('ltc_usd','buy','0.1','0.2'))

#print (u' 现货批量下单 ')
#print (okcoinSpot.batchTrade('ltc_usd','buy','[{price:0.1,amount:0.2},{price:0.1,amount:0.2}]'))

#print (u' 现货取消订单 ')
#print (okcoinSpot.cancelOrder('ltc_usd','18243073'))

#print (u' 现货订单信息查询 ')
#print (okcoinSpot.orderinfo('ltc_usd','18243644'))

#print (u' 现货批量订单信息查询 ')
#print (okcoinSpot.ordersinfo('ltc_usd','18243800,18243801,18243644','0'))

#print (u' 现货历史订单信息查询 ')
#print (okcoinSpot.orderHistory('ltc_usd','0','1','2'))

#print (u' 期货行情信息')
#print (okcoinFuture.future_ticker('ltc_usd','this_week'))

#print (u' 期货市场深度信息')
#print (okcoinFuture.future_depth('btc_usd','this_week','6'))

#print (u'期货交易记录信息')
#print (okcoinFuture.future_trades('ltc_usd','this_week'))

#print (u'期货指数信息')
#print (okcoinFuture.future_index('ltc_usd'))

#print (u'美元人民币汇率')
#print (okcoinFuture.exchange_rate())

#print (u'获取预估交割价')
#print (okcoinFuture.future_estimated_price('ltc_usd'))

#print (u'获取全仓账户信息')
#print (okcoinFuture.future_userinfo())

#print (u'获取全仓持仓信息')
#print (okcoinFuture.future_position('ltc_usd','this_week'))

#print (u'期货下单')
#print (okcoinFuture.future_trade('ltc_usd','this_week','0.1','1','1','0','20'))

#print (u'期货批量下单')
#print (okcoinFuture.future_batchTrade('ltc_usd','this_week','[{price:0.1,amount:1,type:1,match_price:0},{price:0.1,amount:3,type:1,match_price:0}]','20'))

#print (u'期货取消订单')
#print (okcoinFuture.future_cancel('ltc_usd','this_week','47231499'))

#print (u'期货获取订单信息')
#print (okcoinFuture.future_orderinfo('ltc_usd','this_week','47231812','0','1','2'))

#print (u'期货逐仓账户信息')
#print (okcoinFuture.future_userinfo_4fix())

#print (u'期货逐仓持仓信息')
#print (okcoinFuture.future_position_4fix('ltc_usd','this_week',1))
