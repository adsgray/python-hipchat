#!/usr/bin/python

from urllib2 import Request, urlopen
import json
import sys
import re

userurl = "https://api.hipchat.com/v2/user?max-results=1000"

# http://stackoverflow.com/questions/22020247/how-to-post-to-hipchat-from-python
# why is this such a pain in the ass? using curl doesn't require the authorization: Bearer %s header...
def fetchuserjson(url, token):
    """
    Fetch raw response from url, using V2TOKEN as auth header
    """
    headers = { "content-type": "application/json", "authorization": "Bearer %s" % token }
    request = Request(url, headers=headers)
    uo = urlopen(request)
    rawresponse = ''.join(uo)
    uo.close()
    return rawresponse

def usermatch(userjson, regex):
    """
    Iterate over json object, return list of dicts name,mention
    """
    userlist = []
    for user in userjson['items']:
        if regex.match(user['name']):
            userlist.append({'name': user['name'], 'mention_name': user['mention_name']})
    return userlist


def getusermatches(token, regex=None):
    """
    Fetch users and return those whose name matches regex.
    If regex is None construct from sys.argv
    """
    
    # glom all args into a regex
    if regex == None:
        searchspec = '.*'.join(sys.argv[1:])
        regex = re.compile(searchspec, re.IGNORECASE)

    return usermatch(json.loads(fetchuserjson(userurl, token)), regex)

