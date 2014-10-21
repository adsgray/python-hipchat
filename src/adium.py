#!/usr/bin/python

import urllib
import json
import re

# utils for Adium stuff
# download emoticons
# create Adium Emoticons.plist xml file

fnamepat = re.compile(r"^https://.*/([^/]+)$")

def download_item(item):
    m = fnamepat.match(item['url'])
    if not m:
        return False

    fname = m.group(1)

    urllib.urlretrieve(item['url'], fname)
    return True


def hipchat_emoticon_download(raw):
    emot = json.loads(raw)['items']
    for item in emot:
        download_item(item)
    return


def item_xml(item):
    m = fnamepat.match(item['url'])
    if not m:
        return ""

    fname = m.group(1)

    return """
    <key>%s</key>
    <dict>
        <key>Equivalents</key>
        <array>
            <string>(%s)</string>
        </array>
        <key>Name</key>
        <string>(%s)</string>
    </dict>""" % (fname, item['shortcut'], item['shortcut'])


def preamble_xml():
    return """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>AdiumSetVersion</key>
    <real>1.3</real>
    <key>Emoticons</key>
    <dict>
    """

def postamble_xml():
    return """</dict>
  </dict>
</plist>
    """

def hipchat_emoticon_plist(raw):
    emot = json.loads(raw)['items']
    items_xml = ""
    for item in emot:
        items_xml += item_xml(item)
    return preamble_xml() + items_xml + postamble_xml()

