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


tipo=form["tipo"].value
accion=form["accion"].value
dato_id=form["dato_id"].value
tiempo=form["tiempo"].value
sensibilidad=form["sensibilidad"].value
seguridad=form["seguridad"].value
posicion=form["posicion"].value
ip=form["ip"].value
basedatos=form["basedatos"].value
usuario=form["usuario"].value
clave=form["clave"].value
puerto=form["puerto"].value


comando="/usr/share/PuntoVenta/web/cgi-bin/lector "+tipo+" "+accion+" "+dato_id+" "+tiempo+" "+sensibilidad+" "+seguridad+" "+posicion+" "+ip+" "+basedatos+" "+usuario+" "+clave+" "+puerto+" > aviso";

#print comando
os.system(comando);
#os.system('/usr/share/PuntoVenta/web/cgi-bin/lector cliente verificar 15650075 2 7 4 1 192.168.98.74 biometrico admin j5d1j5 5432 > aviso');

fich=open("/usr/share/PuntoVenta/web/control",'r')
os.system("rm -f control");
texto=fich.read() 
lista=texto.split('\n')
fich.close() 
control=lista[0]

print control


