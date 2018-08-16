#!/usr/bin/python
# -*- coding: utf-8 -*-

# 用于进行https请求，以及MD5加密，生成签名的工具类

import http.client
import urllib.parse
import json
import hashlib
from hashlib import sha1
import hmac
import requests

class HttpsRequest(object):

    def __init__(self, url):
        """
        Constructor for class of HttpsRequest.
        :param url: Base URL for the Request methods
        :return: None
        """
        self.__url = url
        print(url)

    @classmethod
    def build_sign(cls, params, secret_key):
        """
        To build MD5 sign for user's parameters.
        :param params: User's parameters usually in the format of a dict
        :param secret_key: String of SECRET KEY
        :return: Signed string encrypted by MD5
        """
        sign = ''
        if hasattr(params, 'items'):
            for key in sorted(params.keys()):
                sign += key + '=' + str(params[key]) + '&'
            #data = sign + 'secret_key=' + secret_key
            data = sign[:-1]
            print(data)
        else:
            raise TypeError('{0} should has attributes of "items"'.format(params))
        #return hashlib.md5(data.encode('utf8')).hexdigest().upper()
        sha = sha1()
        sha.update(bytes(secret_key,'utf8'))
        secret = sha.hexdigest()
        print("secret:"+secret)
        signature = hmac.new(bytes(secret, 'utf8'), bytes(data, 'utf8'), digestmod=hashlib.sha256).hexdigest()
        return signature
    
    #@classmethod
    def build_request_string(cls,params):
        """
        To build MD5 sign for user's parameters.
        :param params: User's parameters usually in the format of a dict
        :param secret_key: String of SECRET KEY
        :return: Signed string encrypted by MD5
        """
        sign = ''
        if hasattr(params, 'items'):
            for key in sorted(params.keys()):
                sign += key + '=' + str(params[key]) + '&'
            #data = sign + 'secret_key=' + secret_key
            data = sign[:-1]
        else:
            raise TypeError('{0} should has attributes of "items"'.format(params))
        return data

    def get(self, resource, params=''):
        """
        GET method to request resources.
        :param resource: String of URL for resources
        :param params: String of user's parameters without encryption
        :return: JSON of the response of the GET request
        """
        print("Get")
        print(self.__url)       
        r = requests.get(self.__url+resource,params)
        '''
        conn = http.client.HTTPSConnection(self.__url, timeout=10)
        print(resource)        
        #conn.request('GET', resource + '?' + params)
        conn.request("HEAD", "/")
        response = conn.getresponse()
        data = response.read().decode('utf-8')
        conn.close()
        '''
        return json.loads(r.text)

    def post(self, resource, params_dict,body_params=''):
        """
        POST method to request resources.
        :param resource: String of URL for resources
        :param params_dict: User's parameters to be encrypted, usually in the format of a dict
        :return: Response of the GET request
        """
        #print(resource)
        #print(params_dict)
        #body = urllib.parse.urlencode(body_params)
        para = self.build_request_string(params_dict)
        print(self.__url+resource+'?'+para)
        r = requests.post(url=self.__url+resource+'?'+para,json=body_params)
        return r.text
'''       
        headers = {
            'Content-type': 'application/x-www-form-urlencoded',
        }
        conn = http.client.HTTPSConnection(self._url, timeout=10)
        body = urllib.parse.urlencode(params_dict)
        conn.request("POST", resource, body, headers)
        response = conn.getresponse()
        data = response.read().decode('utf-8')
        conn.close()
        return data
''' 
