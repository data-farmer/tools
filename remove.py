#!/usr/bin/python
# encoding: utf-8
import sys, os
'''
mv:
-f, --force
    -i, --interactive
    -r, -R, --recursive
    -v, --verbose
      	--help
      	--version
'''
if len(sys.argv)<2:
    print "No action specified!"
    sys.exit()

if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    if option == 'version':
        print "v1.0"
    elif option == 'help':
        print "this is a help"
    else:
        print "No action specified!"
    sys.exit()

for i in sys.argv[1:]:
    if i.startswith("-"):
        print "option: " + i[1:]
    else:
        command = "mv -i " + i + " ~/.trash"
        os.system(command)
