# Hipchat - a ~~single~~ couple of API call via python

Never mind why, but I need to look up people's Hipchat short mention\_name on
the command line.

The src/hipchat.py file provides a function for doing this. src/example.py is
a script that prints out the results. 

Edit: I also wanted to have our custom HipChat emoticons in Adium. src/adium.py
provides functions for downloading the images and creating the Emoticons.plist
XML file required by Adium.

Then:

1. Put the images and the .plist file into a directory called BLAH.AdiumEmoticonset
2. zip -r blah.zip BLAH.AdiumEmoticonset/
3. In finder, double-click on the zip file. Adium will then install the
   emoticon set.
