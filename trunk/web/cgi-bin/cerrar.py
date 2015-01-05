#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import cgi

form = cgi.FieldStorage()
if form.has_key('accion'):
	os.system("/usr/share/PuntoVenta/cerrar")


