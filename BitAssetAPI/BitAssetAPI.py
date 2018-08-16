#!/usr/bin/python
# -*- coding: utf-8 -*-

# To access the REST API of BitAsset

from HttpsMD5Util import HttpsRequest
import time

class BitAssetBase(object):

    RESOURCES_URL = {
        'symbols':'/v1/cash/public/symbols',       
        'currencies': '/v1/cash/public/currencies',
        'time': '/v1/cash/public/server-time',        
        'depth': '/v1/cash/public/query-depth?contractId',      
        'balance': '/v1/cash/accounts/balance',
        'active': '/v1/cash/accounts/order/active',
        'order': '/v1/cash/trade/order',
        'cancel': '/v1/cash/trade/order/cancel',      
        'order_info': '/v1/cash/accounts/order/get',
        'orders_info': '/v1/cash/accounts/orders/get',
    }
    Symbols = ('USDT-CNYT','BTC-CNYT','ETH-CNYT','BCH-CNYT','LTC-CNYT','BTC-USDT','ETH-USDT','BCH-USDT','LTC-USDT','ETH-BTC','BCH-BTC','LTC-BTC')

    def __init__(self, url, api_key, secret_key):
        """
        Constructor for class of BitAssetBase.
        :param url: Base URL for REST API of Future
        :param api_key: String of API KEY
        :param secret_key: String of SECRET KEY
        :return: None
        """
        self._url = url
        self._api_key = api_key
        self._secret_key = secret_key
        self._request = HttpsRequest(self._url)


class BitAssetMarketAPI(BitAssetBase):

    def __init__(self, url, api_key, secret_key):
        """
        Constructor for class of BitAssetMarketAPI.
        :param url: Base URL for REST API of Future
        :param api_key: String of API KEY
        :param secret_key: String of SECRET KEY
        :return: None
        """
        super(BitAssetMarketAPI, self).__init__(url, api_key, secret_key)

    @classmethod
    def build_request_string(cls, name, value, params='', choice=()):
        if value:
            if value in choice:
                return params + '&' + name + '=' + str(value) if params else name + '=' + str(value)
            else:
                raise ValueError('{0} should be in {1}'.format(value), choice)
        else:
            return params

    # BitAsset交易对信息
    def symbols(self):
        """
        :param null:
        :return:
        """
        return self._request.get(BitAssetBase.RESOURCES_URL['symbols'],'')    
     # BitAsset币种信息
    def currencies(self):
        """
        :param null:
        :return:
        """
        return self._request.get(BitAssetBase.RESOURCES_URL['currencies'])   
    # BitAsset系统时间
    def servertime(self):
        """
        :param null:
        :return:
        """
        return self._request.get(BitAssetBase.RESOURCES_URL['time'])     
    
    # BitAsset期货市场深度信息    
    def depth(self,contractId):
        """
        :param contractId:
        :return:
        """
        print(BitAssetBase.RESOURCES_URL['depth']+'='+contractId)
        return self._request.get(BitAssetBase.RESOURCES_URL['depth']+'='+contractId)        

class BitAssetDealsAPI(BitAssetBase):

    def __init__(self, url, api_key, secret_key):
        """
        Constructor for class of BitAssetFuture.
        :param url: Base URL for REST API of Future
        :param api_key: String of API KEY
        :param secret_key: String of SECRET KEY
        :return: None
        """
        super(BitAssetDealsAPI, self).__init__(url, api_key, secret_key)

    # 期货全仓账户信息
    def accounts_balance(self):
        timstamp = int(round(time.time()*1000))
        params = {'apiAccessKey': self._api_key,
                   'apiTimeStamp':timstamp
                  }
        params['apiSign'] = HttpsRequest.build_sign(params, self._secret_key)
        return self._request.get(BitAssetBase.RESOURCES_URL['balance'], params)
    #下单    
    def trade(self,contractId,side,price,quantity,orderType):
        '''
        contractId：交易对id
        side：buy:1 sell:-1
        price：价格
        quantity：数量
        orderType：1(限价)3(市价)
        '''
        timstamp = int(round(time.time()*1000))
        params = {'apiAccessKey': self._api_key,
                   'apiTimeStamp':timstamp
                  }
        params['apiSign'] = HttpsRequest.build_sign(params, self._secret_key)
        bodys={'contractId':contractId,
               'side':side,
               'price':price,
               'quantity':quantity,
               'orderType':orderType      
        }
        return self._request.post(BitAssetBase.RESOURCES_URL['order'], params,bodys)  
    #撤单
    def cancel(self,orderId,contractId):
        '''
        contractId：交易对id
        orderId:委托单id
        '''
        timstamp = int(round(time.time()*1000))
        params = {'apiAccessKey': self._api_key,
                   'apiTimeStamp':timstamp,
                   'orderId':orderId
                  }
        params['apiSign'] = HttpsRequest.build_sign(params, self._secret_key)
        bodys={'contractId':contractId,
               'originalOrderId':orderId    
        }
        return self._request.post(BitAssetBase.RESOURCES_URL['cancel'], params,bodys)   
    #获取订单信息
    def get_order_info(self,orderId):
        '''
        orderId:委托单id
        '''
        timstamp = int(round(time.time()*1000))
        params = {'apiAccessKey': self._api_key,
                   'apiTimeStamp':timstamp,
                   'orderId':orderId
                  }
        params['apiSign'] = HttpsRequest.build_sign(params, self._secret_key)
        return self._request.get(BitAssetBase.RESOURCES_URL['order_info'], params)     
    #批量获取订单
    def get_orders_info(self,orderList):
        timstamp = int(round(time.time()*1000))
        params = {'apiAccessKey': self._api_key,
                   'apiTimeStamp':timstamp
                  }
        params['apiSign'] = HttpsRequest.build_sign(params, self._secret_key)
        bodys=orderList
        return self._request.post(BitAssetBase.RESOURCES_URL['orders_info'], params,bodys)    