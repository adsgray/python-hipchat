#!/usr/bin/python

# put hipchat.py location in PYTHONPATH environment variable
import hipchat

V2TOKEN = "YOUR_PERSONAL_HIPCHAT_API_V2_TOKEN"

for user in hipchat.getusermatches(V2TOKEN):
    print "n:%s m: %s" % (user['name'], user['mention_name'])

