#!/usr/bin/env python 

# Make sure you replace the API and/or APP key below
# with the ones for your account

from datadog import initialize, api

options = {
    'api_key': '71ab1488cdc9e808c2f8bcca940ca154',
    'app_key': '4777281b7ce988e619c66691b651d3e3b26b4b06'
}

initialize(**options)

# Get all monitor details
print api.Monitor.get_all()
