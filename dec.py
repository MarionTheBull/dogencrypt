#!/usr/bin/env python

import re
import sys
import platform
from zipfile import _ZipDecrypter

script, vim_file = sys.argv
jic = []	#just in case there are more than one words that will call a cleartext output file.

def attack( key ):
    f = open( vim_file, 'rb' )
    zd = _ZipDecrypter( key.rstrip() )

    f.read(12)
    if re.search( '^[\s\x00-\x7F]+$', ''.join( zd(c) for c in f.read() ) ) is not None:
        print(key.rstrip())
#		If you uncomment jic, make sure to comment out sys.exit() in this else statement.
#		jic.append( key.rstrip() )
        sys.exit()
    f.close()

def wordlist_generation():
    if "Windows" in platform.system():
        list = open('wordlist.txt', 'r')
    elif "Linux" in platform.system():
        list = open( '/usr/share/dict/words', 'r' )
    else:
        raise SystemError("System not recognized!")
    for item in list:
        attack( item )
    list.close()

#   JIC Lines Below
#   print( str( "These are all potential keys: " ) )
#   for each in jic:
#       print each

if __name__ is "__main__":
    wordlist_generation()
