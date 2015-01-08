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

accion=form["accion"].value# impresoras , imprimir


f=open("/usr/share/PuntoVenta/.CONFIG_PUNTO.EXE",'r')
texto=f.read() 
a=texto.split('\n')
f.close() 
connex=a[0].split('=')[1]
puerto=a[1].split('=')[1]
tienda=a[9].split('=')[1]
clavep=a[10].split('=')[1]
dominio=a[13].split('=')[1]
certif=a[2].split('=')[1]
ip=a[11].split('=')[1].split('|')[0]
cotiza=a[3].split('=')[1].split('|')[0]
factur=a[4].split('=')[1].split('|')[0]
devolu=a[5].split('=')[1].split('|')[0]
ntodeb=a[6].split('=')[1].split('|')[0]
ntocre=a[7].split('=')[1].split('|')[0]
report=a[8].split('=')[1].split('|')[0]

if dominio != "":
	ruta=dominio
else:
	ruta=connex+puerto

if certif == "si":
	cert="https://"
else:
	cert="http://"	

if accion == "impresoras":
	print "cotizacion="+cotiza
	print "facturacion="+factur
	print "devolucion="+devolu
	print "nota_debito="+ntodeb
	print "nota_credito="+ntocre
	print "reporte="+report
elif accion == "imprimir":
	id_=form["id"].value
	tipo=form["tipo"].value
	nombre=form["nombre"].value
	archivo="/tmp/"+nombre+".pdf"
	salida="/tmp/salida_impresora"

	if tipo == "FAC":
		impresora = factur
	elif tipo == "COT":
		impresora = cotiza
	elif tipo == "DEV":
		impresora = devolu
	elif tipo == "NCR":
		impresora = ntocre
	elif tipo == "NDB":
		impresora = ntodeb  
	else:
		impresora = report

	if impresora != "NO USAR":
		#comando="wget -O "+archivo+" "+cert+"192.168.98.75:2002"+"/Navegador/imprimir?valores=tienda_-_"+tienda+"_._clave_-_"+clavep+"_._ip_-_"+ip+"_._id_-_"+id_+";evince "+archivo;
		comando="wget -O "+archivo+" "+cert+ruta+"/Navegador/imprimir?valores=tienda_-_"+tienda+"_._clave_-_"+clavep+"_._ip_-_"+ip+"_._id_-_"+id_+";evince "+archivo;
		lpr="lp -d "+impresora+' -n "1" -o media=letter -o sides=two-sided-long-edge '+archivo+" > "+salida
		os.system(lpr);
		lectura="cat "+salida+" | grep 'la id solicitada' | wc -l > "+salida+";rm -f "+salida
		f=open(salida+"2",'r')
		os.system(salida+"2");
		t=f.read()
		f.close()
		print t
	else:
		print 2

'''
0 no imprimio
1 exito enviado a la impresora
2 impresora no configurada
'''

