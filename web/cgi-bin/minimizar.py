#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import cgi

print "Content-Type: text/html"
print "Access-Control-Allow-Origin: *"
print "Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept"
print "<html>"
print

form = cgi.FieldStorage()
if form.has_key('accion'):
	os.system('wmctrl -r ".ARAUCA." -b toggle,shaded 2> /tmp/log_arauca')
	os.system('xdotool search --name ".ARAUCA." windowminimize 2> /tmp/log_arauca')
