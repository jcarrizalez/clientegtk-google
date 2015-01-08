#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import cgi

print "Content-Type: text/html"
print "Access-Control-Allow-Origin: *"
print "Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept"
print "<html>"
print


os.system('gcalctool 2> /tmp/log_arauca')

form = cgi.FieldStorage()
if form["tecla"].value=="F1":
	os.system('echo "TECLA FUNCTION"')
elif form["tecla"].value=="F10":
	os.system('gcalctool 2> /tmp/log_arauca')
else:
	os.system('echo "TECLA FUNCTION"')
	
'''	
fich=open("/usr/share/PuntoVenta/web/control",'r')
os.system("rm -f control");
texto=fich.read() 
lista=texto.split('\n')
fich.close() 
control=lista[0]

print control
'''

