#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import cgi

print "Content-Type: text/html"
print "<html>"
print
print '''<head>
			<title>PuntoVenta - Minimizar</title>
			<style>
				button.btn_login {
					font-size: 18px imortant!;
					width: 32px;
					height: 32px;
					background: none;
					border: none;
					color: #ffffff;
					cursor: pointer;
				}
			</style>
		</head>
		<body style='padding: 0; margin: 0; overflow: hidden; height: 100%;'>
			<form method=POST enctype=multipart/form-data action=http://127.0.0.1:8888/cgi-bin/minimizar.py>
				<input type='hidden' name='accion' value='minimizar'>
				<button id='minimizar' class='btn_login'>-</button>
			</form>
		</body>
	</html>'''
form = cgi.FieldStorage()
if form.has_key('accion'):
	os.system('wmctrl -r "ARAUCA" -b toggle,shaded')

	#os.system("evince /home/desarrollo/mozilla.pdf")
	#os.system("wmctrl -k on")
	#wmctrl -r "ARAUCA" -b remove,fullscreen
