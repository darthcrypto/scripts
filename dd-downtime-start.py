#!/usr/bin/env python

###INSTRUCTIONS###
# downtime-start.py is used for scheduling downtime for nodes in datadog
# it takes 3 arguments: tag, tag-value, and minutes-of-downtime
# downtime starts when the script is run
#EXAMPLE:
# if you wanted to schedule 15 minutes of downtime for all nodes tagged with the puppet_role rct 
# python dd-downtime-start.py -t puppet_role -v rct -m 15 

#modules
import datadog
from datadog import initialize, api
import time
import sys
import optparse

#datadog keys
options = {
    'api_key': '71ab1488cdc9e808c2f8bcca940ca154',
    'app_key': '4777281b7ce988e619c66691b651d3e3b26b4b06'
}

#initialize api connection
initialize(**options)

#parameters
parser = optparse.OptionParser()
parser.add_option('-t', action="store", help="tag-key")
parser.add_option('-v', action="store", help="tag-value")
parser.add_option('-m', action="store", help="minutes-of-downtime", type="int")
options, args = parser.parse_args()

#variables
start_ts = int(time.time())
end_ts = start_ts + (options.m * 60)
tags = '%s:%s' % (options.t, options.v)

#downtime
api.Downtime.create(scope=tags, start=start_ts, end=end_ts)

print "The nodes with a tag:value of %s will be scheduled for downtime in DataDog for %d minutes starting now" % (tags, options.m)
