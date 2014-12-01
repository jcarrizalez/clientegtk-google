#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import cgi

print "Content-Type: text/html"
print "<html>"
print
print '''<head>
			<title>PuntoVenta - Cerrar</title>
			<link href="../css/personalizado/jquery-ui-1.10.3.custom.min.css" type="text/css" rel="stylesheet">
			<style>
				button.btn_login {
					font-size: 18px imortant!;
					width: 130px;
					height: 37px;
				}
			</style>
			<script src="../js/jquery/jquery-1.10.2.min.js" type="text/javascript"></script>
			<script src="../js/jquery/jquery-ui-1.10.4.custom.min.js" type="text/javascript"></script>
			<script language="JavaScript">
				$(function() {
					$('button#cerrar').button({ icons: { primary: "ui-icon-circle-close" } });
				});
			</script>
		</head>
		<body style='padding: 0; margin: 0; overflow: hidden; height: 100%;'>
			<form method=POST enctype=multipart/form-data action=http://127.0.0.1:8888/cgi-bin/cerrar.py>
				<input type='hidden' name='accion' value='cerrar'>
				<button id='cerrar' class='btn_login'>Cerrar</button>
			</form>
		</body>
	</html>'''
form = cgi.FieldStorage()
if form.has_key('accion'):
	#os.system("/usr/share/PuntoVenta/cerrar")
	os.system('wmctrl -c "ARAUCA"')