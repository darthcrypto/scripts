#!/usr/bin/env python

import datadog
from datadog import initialize, api

import sys

options = {
    'api_key': '71ab1488cdc9e808c2f8bcca940ca154',
    'app_key': '4777281b7ce988e619c66691b651d3e3b26b4b06'
}

initialize(**options)

#find api hosts to mute
api1 = api.Infrastructure.search(q='hosts:i-063d717ee2b1d893a')
api2 = api.Infrastructure.search(q='hosts:i-058690297ba8ca62c')
api3 = api.Infrastructure.search(q='hosts:i-0eb8643ffb3005147')
api4 = api.Infrastructure.search(q='hosts:i-0341a31088d2cc1c2')


api5 = api.Infrastructure.search(q="

#mute hosts
#api.Host.mute(api1['results']['hosts'][0])
#api.Host.mute(api2['results']['hosts'][0])
#api.Host.mute(api3['results']['hosts'][0])
#api.Host.mute(api4['results']['hosts'][0])

#unmute hosts
#api.Host.unmute(api1['results']['hosts'][0])
#api.Host.unmute(api2['results']['hosts'][0])
#api.Host.unmute(api3['results']['hosts'][0])
#api.Host.unmute(api4['results']['hosts'][0])

print api1
print api2
print api3
print api4

