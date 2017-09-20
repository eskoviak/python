#!/usr/bin/env python

import json
import urllib.request

environments = {
    'RWSJAMS' : 'http://rwsjamswebcln/JAMS/api/'
    }

payload = {
    'username' : 'ed.skoviak@redwingshoes.com',
    'password' : 'Patt0nGen#'
}

headers = {
    'content-type' : 'application/x-www-form-urlencoded'
}

if __name__ == '__main__':


    baseURL = environments['RWSJAMS']
    urlLogin = baseURL+'authentication/login'
    print ('Call Url: ' + urlLogin)
    data = urllib.parse.urlencode(payload)
    data = data.encode('ascii')
    try:
        request = urllib.request.Request(urlLogin, data=data, headers=headers)
        response = urllib.request.urlopen(request)
        token = json.loads(response.read())['access_token']
        print('Token: ' + token)
    except urllib.error.HTTPError as he:
        print(he)

    urlAgent = baseURL+'agent'
    print('Call Url: ' + urlAgent)