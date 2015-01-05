#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import cgi

form = cgi.FieldStorage()
if form.has_key('accion'):
	#os.system('wmctrl -r "ARAUCA" -b toggle,shaded')
	os.system('xdotool search --name "ARAUCA" windowminimize')
	#os.system("wmctrl -k on")
	#wmctrl -r "ARAUCA" -b remove,fullscreen
