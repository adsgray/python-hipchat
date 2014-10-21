#!/usr/bin/python

# put hipchat.py location in PYTHONPATH environment variable
import adium

V2TOKEN = "YOUR_PERSONAL_TOKEN"

emoticons = hipchat.fetchemoticonjson(V2TOKEN)
adium.hipchat_emoticon_download(emoticons)
plist = adium.hipchat_emoticon_plist(emoticons)
print plist # redirect this to Emoticons.plist


