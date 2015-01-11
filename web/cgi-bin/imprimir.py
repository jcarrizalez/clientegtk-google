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

#elif accion == "estatus":
elif accion == "estatus":
	salida="/tmp/salida_impresora"
	f=open(salida,'r')
	t=f.read()
	t=t.split('\n')[0]
	a=t.split(' (')[0].replace('la id solicitada es ','')
	f.close()
	cola="lpstat -t | grep '"+a+"' > "+salida+"2"
	os.system(cola)
	f=open(salida+"2",'r')
	cola=f.read()
	cola=cola.split('\n')[0]
	f.close()
	impreso="lpstat -W completed | grep '"+a+"' |  wc -l > "+salida+"2"
	os.system(impreso)
	f=open(salida+"2",'r')
	impreso=f.read() 
	impreso=impreso.split('\n')[0]
	f.close()
	noimpreso="lpstat -W not-completed  | grep '"+a+"' |  wc -l > "+salida+"2"
	os.system(noimpreso)
	f=open(salida+"2",'r')
	noimpreso=f.read()
	noimpreso=noimpreso.split('\n')[0]
	f.close()
	if cola.find("imprimiendo "+a) >= 0:
		print "imprimiendo"
	elif cola.find(a) >= 0:
		print "en_cola_de_impresion"
	elif impreso =="1":
		print "impreso"
	elif noimpreso =="1":
		print "no_impreso"
	else:
		print "error_de_impresion"

	'''
	rm -f /home/desarrollo/PDF/*;
	echo ''> /tmp/salida_impresora;
	echo '' > /tmp/salida_impresora2;
	cp /tmp/FAC-001000000000000000128.pdf /tmp/FAC-001000000000000000129.pdf;
	cp /tmp/FAC-001000000000000000128.pdf /tmp/FAC-001000000000000000127.pdf;
	cp /tmp/FAC-001000000000000000128.pdf /tmp/FAC-001000000000000000126.pdf;
	cp /tmp/FAC-001000000000000000128.pdf /tmp/FAC-001000000000000000125.pdf;
	cp /tmp/FAC-001000000000000000128.pdf /tmp/FAC-001000000000000000124.pdf;
	lp -d PDF -n "1" -o media=letter -o sides=two-sided-long-edge /tmp/FAC-001000000000000000128.pdf > /tmp/salida_impresora;
	lp -d PDF -n "1" -o media=letter -o sides=two-sided-long-edge /tmp/FAC-001000000000000000129.pdf > /tmp/salida_impresora;
	lp -d PDF -n "1" -o media=letter -o sides=two-sided-long-edge /tmp/FAC-001000000000000000127.pdf > /tmp/salida_impresora;
	lp -d PDF -n "1" -o media=letter -o sides=two-sided-long-edge /tmp/FAC-001000000000000000126.pdf > /tmp/salida_impresora;
	lp -d PDF -n "1" -o media=letter -o sides=two-sided-long-edge /tmp/FAC-001000000000000000125.pdf > /tmp/salida_impresora;
	lp -d PDF -n "1" -o media=letter -o sides=two-sided-long-edge /tmp/FAC-001000000000000000124.pdf > /tmp/salida_impresora;
	echo 'listo';

	'''


	
elif accion == "descargar":
	id_=form["id"].value
	tipo=form["tipo"].value
	nombre=form["nombre"].value
	archivo="/tmp/"+nombre+".pdf"
	salida="/tmp/salida_descarga"
	comando="echo '' > "+salida+";wget -o "+salida+" -O "+archivo+" "+cert+ruta+"/Navegador/imprimir?valores=tienda_-_"+tienda+"_._clave_-_"+clavep+"_._ip_-_"+ip+"_._id_-_"+id_
	
	#comando="echo '' > /tmp/salida_descarga;wget -o /tmp/salida_descarga -O /tmp/FAC-001000000000000000128.pdf http://w3.id.tue.nl/fileadmin/id/objects/E-Atelier/Phidgets/Software/Flash/fl8_tutorials.pdf &"

	#comando="echo '' > /tmp/salida_descarga;wget -o /tmp/salida_descarga -O /tmp/FAC-001000000000000000128.pdf https://forja.rediris.es/docman/view.php/312/.../Postgres-Programmer.pdf &"
	os.system(comando)
	print 1
	
	
elif accion == "verificar":
	salida="/tmp/salida_descarga"
	f=open(salida,'r')
	t=f.read() 
	a=t.split('\n')
	f.close() 

	f=file(salida,"r")
	l=f.readlines()
	f.close()
	cadena=l[-2][62:-1]



	if cadena.find("guardado") >= 0:
		cade="Estado: Listo"
	elif cadena.find("100%") >= 0:
		cade="Estado: Listo"
	elif t.find("Grabando a:") >= 0:	
		cade="Estado: Descargando"
	elif t.find("esperando respuesta") >= 0:
		cade="Estado: Esperando Respuesta"
	elif t.find("Conectando con") >= 0:		
		cade="Estado: Conectando"
	elif t.find("--  http") >= 0:		
		cade="Estado: Conectando"
	print cade

	if t.find("Grabando a:") >= 0:	
		cade="Total: "+cadena
		if cade.find("guardado") >= 0:
			cade="Total: 100%"	
		
		
	else:
		cade="Total: 0%"		

	if cade=="Total: ":
		cade="Total: 0%"
	print cade
	
	
	
	

	if t.find("Longitud:") >= 0:
		cade="Peso:"+t.split('Longitud:')[1].split('[')[0]
		if cade !="Peso: no especificado ":
			cade="Peso: "+t.split('Longitud:')[1].split('[')[0].split('(')[1].split(')')[0]
	else:
		cade="Peso: Calculando.."
	print cade	
	


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
		lpr="echo '' > "+salida+"2;echo '' > "+salida+";lp -d "+impresora+' -n "1" -o media=letter -o sides=two-sided-long-edge '+archivo+" > "+salida
		os.system(lpr)
		#print lpr
		lectura="cat "+salida+" | grep 'la id solicitada' | wc -l > "+salida+"2;"
		os.system(lectura)
		f=open(salida+"2",'r')
		#os.system("rm -f "+salida+"2;rm -f "+salida+";rm -f /tmp/salida_descarga;")
		t=f.read()
		f.close()
		print t
		#os.system("evince "+archivo)
	else:
		print 2

'''
0 no imprimio
1 exito enviado a la impresora
2 impresora no configurada

wget --post-data "author=$autor&amp;email=$mail&amp;url=$url&amp;comment=$coment&amp;comment_parent=0&amp;submit=\"Publicar comentario\"&amp;comment_post_ID=$postid" $pagina/wp-comments-post.php


'''

