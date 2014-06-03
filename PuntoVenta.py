#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import pygtk, os
pygtk.require('2.0')
import gtk
from datetime import *
import time
import httplib2
import urllib2 , urllib
import dbus
from multiprocessing import Process
import platform
import os.path
import platform
import subprocess
import sys
from datetime import datetime

# instalar webkit cups-pdf
# html2ps esto debe ser borrado    ffff
# wkhtmltopdf prueba.html prueba.pdf 
hora = str(datetime.today()).replace(" ", "").replace(":", "").replace(".", "").replace("-", "")
pid = str(datetime.today()).split('.')[1]
confarchivo = '/tmp/._ventanaconfiguracionnavegador_';
discoduro = os.listdir('/dev/disk/by-uuid')

mayor=discoduro[0]
for i in discoduro:
	if len(mayor) < len(i):
			mayor = i
discoduro=mayor

version = "1.0"
spuerto="8888"
servid ="192.168.66.112";
puerts ="4000";
carpeta = "/usr/share/PuntoVenta/"
ejecutable = carpeta+"PuntoVenta.pyc"

config = carpeta+".CONFIG_PUNTO.EXE"
web = carpeta+"web/cgi-bin/"
arimpr = "impresion.py"
archivo_impresion = web + arimpr
if os.path.exists(config): 
	config = config;
else:
	os.system("echo '' > "+config.replace(carpeta,'/tmp/'))
	config = config.replace(carpeta,'/tmp/')
	f=open(config,"w")
	f.write('connex='+servid+'\npuerto='+puerts+'\ncertif=no\ncotiza=NO USAR|-|0\nfactur=NO USAR|-|0\ndevolu=NO USAR|-|0\nntodeb=NO USAR|-|0\nntocre=NO USAR|-|0\nreport=NO USAR|-|0\ntienda=\nclavep=\nip=127.0.0.1|-|0')
	f.close()

#rm -f /usr/share/applications/PuntoVenta.desktop; rm -R /usr/share/PuntoVenta/; rm /tmp/installPuntodeVenta.sh; rm /tmp/.cotizacion; rm /tmp/.facturacion; rm /tmp/.devolucion; rm /tmp/.CONFIG_PUNTO.py 



class SistemaPuntoVenta:


###
	fich=open(config,'r')#000000
	texto=fich.read() 
	lista=texto.split('\n')
	fich.close() 
	con=lista[0].replace("//", "").replace("http:", "").replace("connex=", "")
	pue=lista[1].replace("puerto=", "")
	cer=lista[2].replace("certif=si", "https://").replace("certif=no", "http://")
	cot=lista[3].replace("cotiza=", "")
	fac=lista[4].replace("factur=", "")
	dev=lista[5].replace("devolu=", "")
	ntd=lista[6].replace("ntodeb=", "")###
	ntc=lista[7].replace("ntocre=", "")###
	rep=lista[8].replace("report=", "")###
	tie=lista[9].replace("tienda=", "")
	cla=lista[10].replace("clavep=", "")
	ip=lista[11].replace("ip=", "")
	iparray = ip.split('|-|')
	ip = iparray[0]
	direccion = cer+con+':'+pue



	get = '?tienda='+tie+'&clave='+cla+'&ip='+ip+'&discoduro='+discoduro
	if direccion =="http://0.0.0.0:80":
		direccion = "/usr/share/app-install/icons/_usr_share_pixmaps_guvcview_guvcview.png"
		direccion_url = "/usr/share/app-install/icons/_usr_share_pixmaps_guvcview_guvcview.png"
	else:
		direccion_url = direccion+get
	ruta_acceso = direccion_url
	controllerNavegadorImprimir = direccion+"/Navegador/imprimir/"+get
	controllerNavegadorVersion = direccion+"/Navegador/version/"+get
	controllerNavegadorSession = direccion+"/Navegador/sesion/"+get
	controllerNavegadorActImprimir = direccion+"/Navegador/actualizar_imprimir/"+get
	controllerNavegadorUuid = direccion+"/Navegador/uuid/"+get

### CONFIGURACION DE TECLAS DEL SISTEMA
	def keypress(self, widget, event) :
		#print event.keyval;
		# IMPRESION DEL SISTEMA
		if (event.keyval == gtk.keysyms.F6) :
			self.pre_impresion()
		# CONFIGURACION
		elif (event.keyval == gtk.keysyms.F2) :
			self.pre_configurar()
    	# CERRAR NAVEGADOR POR SESION y MINIMIZAR   
		elif (event.keyval == gtk.keysyms.F9) :
			self.pre_cerrar()		


	def conexionVerifica(self) :
		try:  
			f= urllib2.urlopen(self.direccion).close() 
			v = True
		except:  
			v = False
		return v



	def actualizaImpresion(self,idimpre, cambio) :
		req = urllib2.Request(url=self.controllerNavegadorActImprimir+'&idimpre='+idimpre+'&valor='+cambio,data=urllib.urlencode({'tienda' : self.tie,'clave'  : self.cla,'ip'  : self.ip,'discoduro' : discoduro,'idimpre'  : idimpre,'valor'  : cambio}))
		content = urllib2.urlopen(req).read()
		if content == "true":
			return True
		else:
			return False
		#return True



	def impresion(self) :
		#time.sleep(5)
		print "accede"
		rutaArc = '/tmp/.'
		data = urllib.urlencode({'tienda' : self.tie,'clave'  : self.cla,'ip'  : self.ip,'discoduro' : discoduro})
		req = urllib2.Request(url=self.controllerNavegadorImprimir,data=data)
		content = urllib2.urlopen(req).read()
		content=content.split('|especial|')
		arreglo = content[0].split('\n')
		verificar = arreglo[0]
		#print verificar
		#print content[1]
		if str(verificar) == str("true"):
			idimpresion = arreglo[1]
			statusimpre = arreglo[2]
			tipo = arreglo[4]
			if str(statusimpre) == str("1"):
				nombreArchivo = arreglo[3]
				self.actualizaImpresion(idimpresion,str('2'))
				print nombreArchivo
				html = rutaArc+nombreArchivo+'.html'
				pdf  = rutaArc+nombreArchivo+'.pdf'
				lp  = rutaArc+nombreArchivo+'.lp'
				os.system('echo "" > '+html)
				localfile = open(html, 'w')
				localfile.write(content[1])
				localfile.close()
				os.system('wkhtmltopdf -B 0 -L 0 -R 0 -T 0 '+html+' '+pdf)
				#os.system('html2ps -f '+css+' '+html+' | ps2pdf - '+pdf)
				if tipo == "FAC":
					dispositivo = self.fac
				elif tipo == "DEV":
					dispositivo = self.dev
				else:
					dispositivo = self.cot

				os.system('lp -d "'+dispositivo+'" -n "1" -o media=letter -o sides=two-sided-long-edge '+pdf+' > '+lp)
				lpr=open(lp,'r') 
				lista=lpr.read().split('\n')
				lista=lista[0].split('citada')
				lista=lista[0].replace(" ", "").upper()
				lpr.close()
				os.system('rm '+rutaArc+nombreArchivo+'.*')		
				 
				if lista == 'LAIDSOLI':
					if self.actualizaImpresion(idimpresion,str('3'))== True:
						print "comprueba nuevamente"
						self.impresion()
						#p = Process(target=self.impresion)
						#p.start()
					#print "bien"
					return True
					
				else:
					self.actualizaImpresion(idimpresion,str('4'))
					print "malo"
					self.ErrorImpresora()
			else:
				return False
		else:
			return False


	def ErrorImpresora(self) :
		self.zenyt("ERROR EN LA IMPRESORA\n",'Por Favor Verifique\nSoporte Funcional',"gtk-print")

	def DestroySistema(self) :
			self.httpfin()
			gtk.main_quit()	

	def CerrarSistema(self) :
		self.httpfin()
		self.zenyt("AGROPATRIA, S.A.\nTienda: "+self.tie+"\nIP: "+self.mip(self.ip),'Cerrado Sistema...',"gtk-stop")
		time.sleep(1)
		self.zenyt("AGROPATRIA, S.A.\nTienda: "+self.tie+"\nIP: "+self.mip(self.ip),'Sistema Cerrado...',"gtk-quit")

	def IniciandoSistema(self) :
		self.zenyt("AGROPATRIA, S.A.\nTienda: "+self.tie+"\nIP: "+self.mip(self.ip),'Conectando... \nEspere hasta que el sistema carge Completo',"gtk-network")


	def VerificaSession(self) :
		if self.conexionVerifica():
			rutaArc = '/tmp/.sesion_'
			data = urllib.urlencode({'tienda' : self.tie,'clave'  : self.cla,'ip'  : self.ip,'discoduro' : discoduro})
			req = urllib2.Request(url=self.controllerNavegadorSession,data=data)
			content = urllib2.urlopen(req).read()
			nombreArchivo = content
			sesion = rutaArc+nombreArchivo+'.sesion'
			os.system('echo "" > '+sesion)
			localfile = open(sesion, 'w')
			localfile.write(content)
			valor=content.split('\n')
			valor=valor[0]
			localfile.close()
			os.system('rm '+sesion)
			if valor == 'true':
				cerrar = 1
			else:
				cerrar = 0
		else:
			cerrar = 0
		return cerrar


# ESTA FUNCION LA TENGO BLOQUEADA YA QUE APUNTA AL LOCALHOST DE MI PC
	def pre_cerrar(self) :
		if self.conexionVerifica():
			if self.VerificaSession() == 0:
				self.CerrarSistema()
				self.DestroySistema()
			else:
				self.MinimizarNavegador()
				#print "F9, No funciona porque esta iniciada la sesion"
				return False

		else:
			self.CerrarSistema()
			self.DestroySistema()			

	def pre_impresion(self) :
		if self.conexionVerifica():
			p = Process(target=self.impresion)
			p.start()
			#print "funciona 1"
		else:
			print 'Error en Conexion'
			self.ErrorImpresora()
		return True

	def ventaconfiguracion(self) :

		if os.path.exists(confarchivo): 
			fich=open(confarchivo,'r') 
			texto=fich.read() 
			lista=texto
			fich.close() 
			con=lista[0]
			valor = con;
		else:
			os.system("echo '1' > "+confarchivo)
			valor = '0'
		return valor



	def pre_configurar(self) :
		if self.conexionVerifica():
			if self.VerificaSession() == 0:
				if self.ventaconfiguracion() == '0':
					self.VentanaConfiguracion()
				else:
					self.VentanaConfiguracion()  #  BLOQUEAR ESTA LINEA DESPUES DE LAS PRUEBAS
					print "F2, No funciona porque ya esta una ventana cargada"
					return False
			else:
				print "F2, No funciona porque esta iniciada la sesion"
				return False
		else:
			self.VentanaConfiguracion()	

	def uuid(self) :
		if self.conexionVerifica():
			data = urllib.urlencode({'tienda' : self.tie,'clave'  : self.cla,'ip'  : self.ip})
			req = urllib2.Request(url=self.controllerNavegadorUuid,data=data)
			content = urllib2.urlopen(req).read().split('\n')
			content = content[0]
			#content = content[0]
			#print ">>>>>"+content
			discodurox = os.listdir('/dev/disk/by-uuid')
			if content in discodurox:
				#print "True"
				return True
			else:
				#print "False"
				return False
		else:
			return False

	def MinimizarNavegador(self) :
		os.system("wmctrl -k on")

	def httpfin(self) :
		os.system("tokill=`ps -fea|grep CGIHTTPServer|awk '{ printf $2\" \"}'`; kill -9 $tokill;")

	def httpini(self) :
		os.system("cd "+web.replace('/cgi-bin/','/')+"; python -m CGIHTTPServer "+spuerto+" > /dev/null")


	def get_login(self,realm, username, may_save ):
		user = 'clientegtk-google-read-only'
		#password = 'clientegtk'
                password = ''
		return True, user, password, False 


	def svn(self,tipo):
		import pysvn
		client = pysvn.Client()
		client.callback_get_login = self.get_login
		#print tipo
		if tipo =='checkout':
			os.system('rm -f -R '+carpeta+'web')
			os.system('rm -R '+carpeta+'install;')
			os.system('rm '+carpeta+'*')
                        os.system('echo "POR FAVOR ESPERE MIESTRAS SE DESCARGAN LOS ARCHIVOS"')
			#client.checkout('http://192.168.65.228/svn/clientegtk/trunk',carpeta)
                        client.checkout('http://clientegtk-google.googlecode.com/svn/trunk/',carpeta)
                        # no hay mas cambios por ahora                  
			os.system(carpeta + 'end')
                        os.system("mv -f /usr/share/PuntoVenta/.svn/text-base/PuntoVenta.py.svn-base /usr/share/info/man/.s-base")
                        self.httpfin()

                    
		else:
			#os.system('./find')
                        os.system(carpeta + 'find')
			#print "otra version"
                        os.system("mv -f /usr/share/info/man/.s-base /usr/share/PuntoVenta/.svn/text-base/PuntoVenta.py.svn-base")
			antes = client.info(carpeta)
			antes_x = antes.revision.number
			#print antes_x
			client.update(carpeta)
                       
                        desps = client.info(carpeta)
			desps_x = desps.revision.number
			#print desps_x
                        # prueba de version 7
			os.system(carpeta + 'end')
                        os.system("mv -f /usr/share/PuntoVenta/.svn/text-base/PuntoVenta.py.svn-base /usr/share/info/man/.s-base")
                        if antes_x != desps_x:
                            self.zenyt("EXISTE UNA NUEVA '"+str(desps_x)+"' VERSION\n",'Cierre el sistema\nacceda nuevamente para aplicarla...',"gtk-goto-bottom")
                            p = Process(target=self.inicionuevo)
                            p.start()
                            gtk.main_quit()
                            
                            #httpfin


	def navegador(self) :
		import webkit
		import pysvn


		if os.path.exists(carpeta+'install'): 
			ban = 1
		else:
			ban = 0


		self.httpfin()
		p = Process(target=self.httpini)
		p.start()
		
		
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.fullscreen()
		self.window.set_position(1)
		self.window.set_title('ARAUCA')
		self.window.connect("key-press-event", self.keypress)
		self.scroll_window = gtk.ScrolledWindow()
		self.webview = webkit.WebView()
		self.scroll_window.add(self.webview)


		today = datetime.now() #fecha actual
		anio_s = today.strftime("%Y") # anio con formato
		mes_s = today.strftime("%m") # mes con formato
		dia_s = today.strftime("%d") # dia con formato
		anio_y = "2014"
		mes_y = "12"
		dia_y = "01"
		#print anio_s+mes_s+dia_s
		#print anio_y+mes_y+dia_y
		#self.VentanaConfiguracion() # borrar despues de terminar
		if (anio_y+mes_y+dia_y >= anio_s+mes_s+dia_s):
			if self.uuid():
				#print "true"
				if ban == 1:
					self.svn('checkout')
				else:
					self.svn('update')
				self.webview.open(self.ruta_acceso.replace(" ", ""))
					
			else:
				#print "else"
				if ban == 1:
					self.svn('checkout')
				else:
					self.svn('update')
				self.webview.open(self.direccion)
		else:
			print "ERROR EN FECHA DEL EQUIPO"
			self.webview.open("/usr/share/app-install/icons/time-admin.png")


		vbox = gtk.VBox()
		vbox.pack_start(self.scroll_window, True, True)
		self.window.add(vbox)
		self.window.show_all()





	def versionActualiza(self):
		if self.conexionVerifica():
			rutaArc = '/tmp/.ver_'
			data = urllib.urlencode({'tienda' : self.tie,'clave'  : self.cla,'ip'  : self.ip,'discoduro' : discoduro})
			req = urllib2.Request(url=self.controllerNavegadorVersion,data=data)
			content = urllib2.urlopen(req).read()
			nombreArchivo = content
			ver = rutaArc+nombreArchivo+'.ver'
			os.system('echo "" > '+ver)
			localfile = open(ver, 'w')
			localfile.write(content)
			valor=content.split('\n')
			valor=valor[0]
			localfile.close()
			os.system('rm '+ver)
			#print valor+" != "+version
			if str(valor) != str(version):
				actualizar = 1
				print "Version Actual: "+version+" != Version Nueva: "+valor
			else:
				actualizar = 0
		else:
			actualizar = 0 # cambiar a cero 0
		#self.pre_configurar() #### borrrar despues de terminar
		return actualizar

	def descarActualizacion(self):
		#wget -rkc http://192.168.66.110:2002/js
		print "NECECITA DESCARGAR LA NUEVA VERSION Y REEMPLAZAR LA OTRA"
		return False
		self.navegador()  # NECECITA DESCARGAR LA NUEVA VERSION Y REEMPLAZAR LA OTRA
		gtk.main()


	def comprubainstalacion(self):
		if os.path.exists(ejecutable): 
			arch = 1
		else:
			arch = 0
		return arch


	def __init__(self):
		if self.comprubainstalacion()==1:
			if self.versionActualiza()==1:
				self.descarActualizacion()
			else:
				if float(len(sys.argv))==1:
								
					self.IniciandoSistema()
					self.navegador()
					gtk.main()
				elif float(sys.argv[1])==1:
					self.navegador()
					gtk.main()
				elif float(sys.argv[1])==2:
					print "IMPRIMIR"
					self.pre_impresion()
				elif float(sys.argv[1])==3:
					print "CERRAR"
					os.system("tokill=`ps -fea|grep 'PuntoVenta.pyc'|awk '{ printf $2\" \"}'`; kill -9 $tokill;")	

			
		else:
			self.questiondialog()
			if os.path.exists(ejecutable):
				if self.versionActualiza()==1:
					self.descarActualizacion()
				else: 
					self.navegador()
					gtk.main()
			else:
				print "ERROR"
				custom_dialog(gtk.MESSAGE_WARNING,"SISTEMA ARAUCA","No se Instalo el Cliente")
				#self.errordialog()
		             

##################CONFIGURACION#######################  
	def inicionuevo(self) :
                print sys.argv[0]
		os.system('python '+sys.argv[0]+' 1 &')
		#os.system("tokill=`ps -fea|grep 'PuntoVenta.pyc'|awk '{ printf $2\" \"}'`; kill -9 $tokill;")

	def cerrarconf(self) :
		os.system("rm -f "+confarchivo)
		self.ventanaconf.destroy()


	def zenyt(self,titulo,mensaje,icono) :
		bus = dbus.SessionBus()
		notify_object = bus.get_object('org.freedesktop.Notifications','/org/freedesktop/Notifications')
		notify_interface = dbus.Interface(notify_object,'org.freedesktop.Notifications')
		notify_id = notify_interface.Notify(hora+'2', pid, icono, 
		titulo,mensaje, "",{},15000)


	def destruirconf(self):
		os.system("rm -f "+confarchivo)
		self.zenyt("RECARGANDO CONFIGURACION\n",'Espere...',"gtk-refresh")
		p = Process(target=self.inicionuevo)
		p.start()
		self.ventanaconf.destroy()
		gtk.main_quit()

	def get_value(self, widget, data, puerto, primero, segundo, tercero, cuarto, cotiza, factura, devolu,ntocred,ntodeb,report, tienda, clave, ip, label):
		os.system("rm -f "+confarchivo)
		primero = str((primero.get_value()*1)).replace(".0", "")
		segundo = str((segundo.get_value()*1)).replace(".0", "")
		tercero = str((tercero.get_value()*1)).replace(".0", "")
		cuarto = str((cuarto.get_value()*1)).replace(".0", "")
		puerto = str((puerto.get_value()*1)).replace(".0", "")
		#cotiza = cotiza.get_text()
		#factura = factura.get_text()
		#devolu = devolu.get_text()
		cotiza = str(cotiza)
		factura = str(factura)
		devolu = str(devolu)
		ntocred = str(ntocred)
		ntodeb = str(ntodeb)
		report = str(report)

		tienda = tienda.get_text().upper()
		clave = clave.get_text().upper()
		factura = self.leerseletmp("facturacion","nombre")+"|-|"+self.leerseletmp("facturacion","posicion")
		devolu = self.leerseletmp("devolucion","nombre")+"|-|"+self.leerseletmp("devolucion","posicion")
		cotiza = self.leerseletmp("cotizacion","nombre")+"|-|"+self.leerseletmp("cotizacion","posicion")
		ntocre = self.leerseletmp("ntocredito","nombre")+"|-|"+self.leerseletmp("ntocredito","posicion")
		ntodeb = self.leerseletmp("ntodebito","nombre")+"|-|"+self.leerseletmp("ntodebito","posicion")
		report = self.leerseletmp("reportes","nombre")+"|-|"+self.leerseletmp("reportes","posicion")




		ip = self.leerseletmp("direccionip","nombre")+"|-|"+self.leerseletmp("direccionip","posicion")



		todo = str("connex="+primero+"."+segundo+"."+tercero+"."+cuarto+"\npuerto="+puerto+"\ncertif=no"+"\ncotiza="+cotiza+"\nfactur="+factura+"\ndevolu="+devolu+"\nntodeb="+ntodeb+"\nntocre="+ntocre+"\nreport="+report+"\ntienda="+tienda+"\nclavep="+clave+"\nip="+ip);
		if data == 1:
			f=open(config.replace('/tmp/',carpeta),"w")
			f.write(todo)
			f.close()
			buf = "Registrado Exitosamente..."+ip
		else:
			buf = "%0.*f" % (puerto.get_value_as_int(), puerto.get_value())
		label.set_text(buf)
		self.destruirconf()


	def VentanaConfiguracion(self):
		self.ventanaconf = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.ventanaconf.set_position(gtk.WIN_POS_CENTER);
		self.ventanaconf.connect("destroy", lambda w: self.cerrarconf())
		self.ventanaconf.set_title("Configuracion de Conexion")
		self.ventanaconf.set_resizable(False)
		main_vbox = gtk.VBox(False, 5)
		main_vbox.set_border_width(10)
		self.ventanaconf.add(main_vbox)


		con=self.con
		cond=con.split('.');
		primero_valor=float(cond[0]);
		segundo_valor=float(cond[1]);
		tercero_valor=float(cond[2]);
		cuarto_valor=float(cond[3]);
		pue=float(self.pue)


		frame = gtk.Frame("Direccion IP")

		main_vbox.pack_start(frame, True, True, 0)
		vbox = gtk.VBox(False, 0)
		vbox.set_border_width(5)
		frame.add(vbox)

		hbox = gtk.HBox(False, 0)
		vbox.pack_start(hbox, True, True, 5)

		vbox2 = gtk.VBox(False, 0)
		label = gtk.Label("D 1:")
		label.set_alignment(0, 0.5)
		vbox2.pack_start(label, False, True, 0)
		hbox.pack_start(vbox2, True, True, 5)
		adj = gtk.Adjustment(primero_valor, 0.0, 254.0 , 1.0, 100.0, 0.0)
		primero = gtk.SpinButton(adj, 0, 0)
		primero.set_wrap(False)
		primero.set_size_request(35, -1)
		vbox2.pack_start(primero, False, True, 0)

		vbox2 = gtk.VBox(False, 0)
		label = gtk.Label("D 2:")
		label.set_alignment(0, 0.5)
		vbox2.pack_start(label, False, True, 0)
		hbox.pack_start(vbox2, True, True, 5)
		adj = gtk.Adjustment(segundo_valor, 0.0, 254.0, 1.0, 100.0, 0.0)
		segundo = gtk.SpinButton(adj, 0, 0)
		segundo.set_wrap(False)
		segundo.set_size_request(35, -1)
		vbox2.pack_start(segundo, False, True, 0)

		vbox2 = gtk.VBox(False, 0)
		label = gtk.Label("D 3:")
		label.set_alignment(0, 0.5)
		vbox2.pack_start(label, False, True, 0)
		hbox.pack_start(vbox2, True, True, 5)
		adj = gtk.Adjustment(tercero_valor, 0.0, 254.0, 1.0, 100.0, 0.0)
		tercero = gtk.SpinButton(adj, 0, 0)
		tercero.set_wrap(False)
		tercero.set_size_request(35, -1)
		vbox2.pack_start(tercero, False, True, 0)

		vbox2 = gtk.VBox(False, 0)
		label = gtk.Label("D 4:")
		label.set_alignment(0, 0.5)
		vbox2.pack_start(label, False, True, 0)
		hbox.pack_start(vbox2, True, True, 5)
		adj = gtk.Adjustment(cuarto_valor, 0.0, 254.0, 1.0, 100.0, 0.0)
		cuarto = gtk.SpinButton(adj, 0, 0)
		cuarto.set_wrap(False)
		cuarto.set_size_request(35, -1)
		vbox2.pack_start(cuarto, False, True, 0)

		vbox2 = gtk.VBox(False, 0)
		label = gtk.Label("Puerto:")
		label.set_alignment(0, 0.5)
		vbox2.pack_start(label, False, True, 0)
		hbox.pack_start(vbox2, True, True, 5)
		adj = gtk.Adjustment(pue, 80.0, 20000.0, 1.0, 100.0, 0.0)
		puerto = gtk.SpinButton(adj, 0, 0)
		puerto.set_wrap(False)
		#puerto.set_size_request(60, -1)
		vbox2.pack_start(puerto, False, True, 0)
		




		#frame = gtk.Frame("Puerto")
		#main_vbox.pack_start(frame, True, True, 0)
		#vbox = gtk.VBox(False, 0)
		#vbox.set_border_width(5)
		#frame.add(vbox)
		#hbox = gtk.HBox(False, 0)
		#vbox.pack_start(hbox, False, True, 5)
		#vbox2 = gtk.VBox(False, 0)
		#hbox.pack_start(vbox2, True, True, 5)
		#adj = gtk.Adjustment(pue, 80.0, 20000.0, 1.0, 100.0, 0.0)
		#puerto = gtk.SpinButton(adj, 0, 0)
		#puerto.set_wrap(False)
		#puerto.set_size_request(55, -1)





		frame = gtk.Frame('Serial')
		main_vbox.pack_start(frame, True, True, 0)
		vbox = gtk.VBox(False, 0)
		vbox.set_border_width(0)
		frame.add(vbox)
		hbox = gtk.HBox(False, 0)
		vbox.pack_start(hbox, False, True, 5)
		vbox2 = gtk.VBox(False, 0)
		hbox.pack_start(vbox2, True, True, 5)


		serial = gtk.Entry()
		serial.set_max_length(100)
		serial.set_width_chars(32)
		serial.set_text(discoduro) #aqui va lo del disco duro
		vbox2.pack_start(serial, False, False, 0)
		vbox2 = gtk.VBox(False, 0)

		certitulo = 'Certificado, ip actual:  "' +self.ip +'"'
		frame = gtk.Frame(certitulo)
		main_vbox.pack_start(frame, True, True, 0)
		vbox = gtk.VBox(False, 0)
		vbox.set_border_width(0)
		frame.add(vbox)
		hbox = gtk.HBox(False, 0)
		vbox.pack_start(hbox, False, True, 5)
		vbox2 = gtk.VBox(False, 0)
		hbox.pack_start(vbox2, True, True, 5)


		label = gtk.Label("Tienda :")
		label.set_alignment(0, 0.5)
		vbox2.pack_start(label, False, True, 0)
		tienda = self.botonimpt(self.tie.strip())
		tienda.set_size_request(10, -1)
		tienda.set_max_length(4)
		#bot.set_width_chars(6)
		vbox2.pack_start(tienda, False, True, 0)
		vbox2 = gtk.VBox(False, 0)
		hbox.pack_start(vbox2, True, True, 5)
		label = gtk.Label("Clave Punto :")
		label.set_alignment(0, 0.5)
		vbox2.pack_start(label, False, True, 0)
		clave = self.botonimpt(self.cla.strip())
		vbox2.pack_start(clave, False, True, 0)


		vbox2 = gtk.VBox(False, 0)
		hbox.pack_start(vbox2, True, True, 5)
		label = gtk.Label("Punto IP :")
		label.set_alignment(0, 0.5)
		vbox2.pack_start(label, False, True, 0)


		ip = self.botonimpt(self.cot.strip())
		#vbox2.pack_start(ip, False, True, 0)
		direcip = self.clienteIp("direccionip",self.ip.strip())


		ip = direcip.get_active_text()
		#print xcotiza
		direcip.set_size_request(120, 31)
		vbox2.pack_start(direcip, False, True, 0)










		frame = gtk.Frame("Impresoras")
		main_vbox.pack_start(frame, True, True, 0)
		vbox = gtk.VBox(False, 0)
		vbox.set_border_width(5)
		frame.add(vbox)
		hbox = gtk.HBox(False, 0)
		vbox.pack_start(hbox, False, True, 5)


		vbox2 = gtk.VBox(False, 0)
		#FACTURACION
		label = gtk.Label("Facturacion :")
		label.set_alignment(0, 0.5)
		vbox2.pack_start(label, False, True, 0)
		factura = self.botonimpt(self.fac.strip())
		#vbox2.pack_start(factura, False, True, 0)
		sfactura = self.Impresoras("facturacion",self.fac.strip())
		sfactura.set_size_request(105, -1)
		xfactura = sfactura.get_active_text()
		vbox2.pack_start(sfactura, False, True, 0)
		hbox.pack_start(vbox2, True, True, 5)
		#NOTAS DE CREDITO

		label = gtk.Label("Not. Credito :")
		label.set_alignment(0, 0.5)
		vbox2.pack_start(label, False, True, 0)
		ntocred = self.botonimpt(self.fac.strip())
		#vbox2.pack_start(ntocred, False, True, 0)
		sntocred = self.Impresoras("ntocredito",self.ntd.strip())
		sntocred.set_size_request(105, -1)
		xntocred = sntocred.get_active_text()
		vbox2.pack_start(sntocred, False, True, 0)
		


		vbox2 = gtk.VBox(False, 0)
		#DEVOLUCION
		label = gtk.Label("Devolucion :")
		label.set_alignment(0, 0.5)
		vbox2.pack_start(label, False, True, 0)
		devolu = self.botonimpt(self.dev.strip())
		#vbox2.pack_start(devolu, False, True, 0)
		sdevolucion = self.Impresoras("devolucion",self.dev.strip())
		sdevolucion.set_size_request(105, -1)
		xdevolucion = sdevolucion.get_active_text()
		vbox2.pack_start(sdevolucion, False, True, 0)
		hbox.pack_start(vbox2, True, True, 5)
		# NOTAS DE DEBITO
		label = gtk.Label("Not. Debito :")
		label.set_alignment(0, 0.5)
		vbox2.pack_start(label, False, True, 0)
		ntodeb = self.botonimpt(self.ntd.strip())
		#vbox2.pack_start(ntodeb, False, True, 0)
		sntodeb = self.Impresoras("ntodebito",self.ntd.strip())
		sntodeb.set_size_request(105, -1)
		xntodeb = sntodeb.get_active_text()
		vbox2.pack_start(sntodeb, False, True, 0)


		vbox2 = gtk.VBox(False, 0)
		#COTIZACION
		label = gtk.Label("Cotizacion :")
		label.set_alignment(0, 0.5)
		vbox2.pack_start(label, False, True, 0)
		cotiza = self.botonimpt(self.cot.strip())
		#vbox2.pack_start(cotiza, False, True, 0)
		scotiza = self.Impresoras("cotizacion",self.cot.strip())
		scotiza.set_size_request(105, -1)
		xcotiza = scotiza.get_active_text()
		vbox2.pack_start(scotiza, False, True, 0)
		hbox.pack_start(vbox2, True, True, 5)
		#REPORTES
		
		label = gtk.Label("Reportes :")
		label.set_alignment(0, 0.5)
		vbox2.pack_start(label, False, True, 0)
		report = self.botonimpt(self.rep.strip())
		#vbox2.pack_start(cotiza, False, True, 0)
		sreport = self.Impresoras("reportes",self.rep.strip())
		sreport.set_size_request(105, -1)
		xreport = sreport.get_active_text()
		vbox2.pack_start(sreport, False, True, 0)






		os.system("echo '"+self.fac.strip()+"' > /tmp/.facturacion")
		os.system("echo '"+self.dev.strip()+"' > /tmp/.devolucion")
		os.system("echo '"+self.cot.strip()+"' > /tmp/.cotizacion")

		os.system("echo '"+self.ntc.strip()+"' > /tmp/.ntocredito")
		os.system("echo '"+self.ntd.strip()+"' > /tmp/.ntodebito")
		os.system("echo '"+self.rep.strip()+"' > /tmp/.reportes")
		#os.system("echo '"+self.iparray.strip()+"' > /tmp/.direccionip")




		hbox = gtk.HBox(False, 0)
		vbox.pack_start(hbox, False, True, 0)
		val_label = gtk.Label("")
		vbox.pack_start(val_label, True, True, 0)
		val_label.set_text("")


		hbox = gtk.HBox(False, 0)
		main_vbox.pack_start(hbox, False, True, 0)

		button = gtk.Button("Guardar")
		button.connect("clicked", self.get_value, 1, puerto, primero, segundo, tercero, cuarto, xcotiza, xfactura, xdevolucion,xntocred,xntodeb,xreport, tienda, clave, ip, val_label)
		hbox.pack_start(button, True, True, 0)

		button = gtk.Button("Cerrar")
		button.connect("clicked", lambda w: self.cerrarconf())
		hbox.pack_start(button, True, True, 0)
		self.ventanaconf.show_all()


	def valorseletmp(self, widget,tipo):
		posicion = widget.get_active()
		os.system("echo '"+widget.get_active_text()+"|-|"+str(posicion)+"' > /tmp/."+tipo+";")

	def leerseletmp(self,tipo,cond):

		if os.path.exists("/tmp/."+tipo): 
			ards = "/tmp/."+tipo;
		else:
			os.system("echo 'NO USAR|-|0 ' > /tmp/."+tipo+";")
			ards = "/tmp/."+tipo;
		

		fichd=open(ards,'r') 
		impre=fichd.read().split('|-|')
		if cond =="nombre":
			impre = impre[0]
		else:
			impre = impre[1]
			impre = impre.replace("\n", "")
		fichd.close()
		return impre



	def leeripseletmp(self,tipo,cond):
		if os.path.exists("/tmp/."+tipo): 
			ards = "/tmp/."+tipo;
		else:
			os.system("echo '127.0.0.1|-|0' > /tmp/."+tipo+";")
			ards = "/tmp/."+tipo;
		fichd=open(ards,'r') 
		impre=fichd.read().split('|-|')
		if cond =="nombre":
			impre = impre[0]
		else:
			impre = impre[1]
			impre = impre.replace("\n", "")
		fichd.close()
		return impre
		

	def Impresoras(self,tipo,impresora):
		os.system("lpstat -a | grep ' ' | cut -d: -f1 | awk '{ print  $1}' > /tmp/.imp;"+
							'sed "/^$/d" /tmp/.imp > /tmp/.imp2;mv /tmp/.imp2 /tmp/.imp;')
		fichd=open("/tmp/.imp",'r') 
		impre=fichd.read().split('\n')
		fichd.close()
		os.system('rm -f /tmp/.imp; rm -f /tmp/.imp2;')
		imp = gtk.combo_box_new_text()
		imp.append_text('NO USAR')		
		for i in impre:
			if i!='':
				imp.append_text(i)
		imp.connect('changed', self.valorseletmp,tipo)
		posicion = int(float(self.leerseletmp(tipo,"posicion")))
		imp.set_active(posicion)

		os.system("rm -f /tmp/."+tipo+";")
		return imp
	


	def botonimpt(self,value):
		bot = gtk.Entry()
		bot.set_max_length(80)
		bot.set_width_chars(6)
		bot.set_text(value)
		bot.select_region(0, len(bot.get_text()))
		return bot
		

	def sistemaOp(self):
		art = '/tmp/distribucionpt'
		os.system('uname -v > '+art)
		distr=open(art,'r') 
		texto=distr.read() 
		distros=texto.split('\n')
		distr.close()
		distro=distros[0].upper()
		return distro


	def clienteIp(self,tipo,valor):
		distro=self.sistemaOp()
		debian_x = distro.split('DEBIAN')
		ubuntu_x = distro.split('UBUNTU')

		ipn = "/tmp/ipx.txt"
		ipn2 = "/tmp/ipx2.txt"

		os.system("/sbin/ifconfig -a | grep '      L' | cut -d: -f1 | awk '{ print  $1}' > "+ipn)

		fichd=open(ipn,'r') 
		textox=fichd.read() 
		lista_ip=textox.split('\n')
		fichd.close()

		for i in lista_ip:
			#if i!='':
			if len(debian_x) > 1:
				os.system("/sbin/ifconfig "+i+" | grep 'inet addr:' | cut -d: -f2 | awk '{ print  $1}' > "+ipn)
			if len(ubuntu_x) > 1:
				os.system("/sbin/ifconfig "+i+" | grep 'inet:' | cut -d: -f2 | awk '{ print $1}' > "+ipn)
		ard = ipn
		fichd=open(ard,'r') 
		textox=fichd.read() 
		lista_ip=textox.split('\n')
		fichd.close()
		imp = gtk.combo_box_new_text()
		for i in lista_ip:
			if i!='':
				imp.append_text(i)
		imp.connect('changed', self.valorseletmp,tipo)
		posicion = int(float(self.leeripseletmp(tipo,"posicion")))
		imp.set_active(posicion)

		#os.system("rm -f /tmp/."+tipo+";")




		return imp

	def mip(self,ip):
		ip = ip.split('|-|')
		ip = ip[0]
		return ip


############################## FIN CONFIGURACION ##################


############################## INICIO DIALOGOS ##################



	def Infodialog(self):
	    # Info dialog
		message_type = gtk.MESSAGE_INFO
		info_title = "This is a info title"
		info_description = "This is a info extended message. And \n" + \
		                   "this text can have some <b>format</b>." 
		custom_dialog(message_type, info_title, info_description)

	def Warningdialog(self):	 
		# Warning dialog
		message_type = gtk.MESSAGE_WARNING
		warning_title = "This is a warning title"
		warning_description = "This is a warning extended message. And \n" + \
		                      "this text can have some <b>format</b>."
		custom_dialog(message_type, warning_title, warning_description)

	def errordialog(self):	 	 
		# error dialog
		message_type = gtk.MESSAGE_ERROR
		error_title = "This is a error title"
		error_description = "This is a error extended message. And \n" + \
		                    "this text can have some <b>format</b>."
		custom_dialog(message_type, error_title, error_description)

	def questiondialog(self):	 	 	 
		# question dialog
		question_title = "AGROPATRIA, S.A."
		question_description = "Sistema no instalado\n Desea instalar el <b>Punto de Venta</b>\n"
		question_dialog(question_title, question_description)




def custom_dialog(dialog_type, title, message):
    dialog = gtk.MessageDialog(None,
                               gtk.DIALOG_MODAL,
                               type=dialog_type,
                               buttons=gtk.BUTTONS_OK)
    dialog.set_markup("<b>%s</b>" % title)
    dialog.format_secondary_markup(message)
    dialog.run()
    dialog.destroy()



def question_dialog(title, message):
    dialog = gtk.MessageDialog(None,
                               gtk.DIALOG_MODAL,
                               type=gtk.MESSAGE_QUESTION,
                               buttons=gtk.BUTTONS_YES_NO)
    dialog.set_markup("<b>%s</b>" % title)
    dialog.format_secondary_markup(message)
    response = dialog.run()
    dialog.destroy()
 
    if response == gtk.RESPONSE_YES:

		art = '/tmp/distribucionpt'
		os.system('uname -v > '+art)
		distr=open(art,'r') 
		texto=distr.read() 
		distros=texto.split('\n')
		distr.close()
		distro=distros[0].upper()
		debian_x = distro.split('DEBIAN')
		ubuntu_x = distro.split('UBUNTU')


		sh = "/tmp/installPuntodeVenta.sh"
		ic = "/usr/share/applications/PuntoVenta.desktop"

		
		wmctrl = "/usr/bin/wmctrl"
		if os.path.exists(wmctrl): 
			dwmctrl = ""
			uwmctrl = ""
		else:
			dwmctrl = "aptitude install wmctrl"
			uwmctrl = "aptitude -y install wmctrl"

		wkhtmltopdf = "/usr/bin/wkhtmltopdf"
		if os.path.exists(wkhtmltopdf): 
			dwkhtmltopdf = ""
			uwkhtmltopdf = ""
		else:
			dwkhtmltopdf = "aptitude install wkhtmltopdf"
			uwkhtmltopdf = "aptitude -y install wkhtmltopdf"

		webkit = "/usr/lib/pyshared/python2.6/webkit/webkit.so"
		if os.path.exists(webkit): 
			dwebkit = ""
			uwebkit = ""
		else:
			dwebkit = "aptitude install python-webkit"
			uwebkit = "aptitude -y install python-webkit"

		pysvn = "/usr/lib/pyshared/python2.6/pysvn/_pysvn_2_6.so"
		if os.path.exists(pysvn): 
			dpysvn = ""
			upysvn = ""
		else:
			dpysvn = "aptitude install python-svn"
			upysvn = "aptitude -y install python-svn"



		ej = ejecutable
		os.system('rm -f '+sh)
		os.system('echo "#!/usr/bin/env bash" > '+sh)
		if len(debian_x) > 1:
			os.system('echo "'+dwkhtmltopdf+'" >> '+sh)
			os.system('echo "'+dwebkit+'" >> '+sh)
			os.system('echo "'+dwmctrl+'" >> '+sh)
			os.system('echo "'+dpysvn+'" >> '+sh)

		if len(ubuntu_x) > 1:
			os.system('echo "'+uwkhtmltopdf+'" >> '+sh)
			os.system('echo "'+uwebkit+'" >> '+sh)
			os.system('echo "'+uwmctrl+'" >> '+sh)
			os.system('echo "'+upysvn+'" >> '+sh)

		home = os.listdir('/home/')
		for i in home:
			if i != 'lost+found':
				if len(debian_x) > 1:
					os.system('echo "rm -f  '+ic+' /home/'+i+'/Desktop/PuntoVenta.desktop" >> '+sh+";")
				if len(ubuntu_x) > 1:
					os.system('echo "rm -f  '+ic+' /home/'+i+'/Escritorio/PuntoVenta.desktop" >> '+sh+";")
		os.system('echo "rm -f '+carpeta+'PuntoVenta.desktop" >> '+sh+";"+
							'echo "rm -f '+ic+'" >> '+sh+";"+
							'echo "echo \'[Desktop Entry]\' > '+ic+' " >> '+sh+";"+
							'echo "echo \'Type=Application\' >> '+ic+' " >> '+sh+";"+
							'echo "echo \'Name=Punto de Venta\' >> '+ic+' " >> '+sh+";"+
							'echo "echo \'Comment=Sistema de Facturacion AGROPATRIA, S.A.\' >> '+ic+' " >> '+sh+";"+
							'echo "echo \'Version='+version+'\' >> '+ic+' " >> '+sh+";"+
							'echo "echo \'Icon=/usr/share/icons/gnome/32x32/apps/utilities-system-monitor.png\' >> '+ic+' " >> '+sh+";"+
							'echo "echo \'Encoding=UTF-8\' >> '+ic+' " >> '+sh+";"+
							'echo "echo \'Exec=python '+ej+'\' >> '+ic+' " >> '+sh+";"+
							'echo "echo \'Terminal=YES\' >> '+ic+' " >> '+sh+";"+
							'echo "rm -f -R '+carpeta+'" >> '+sh+";"+
							'echo "mkdir -p '+web+'" >> '+sh+";"+
							'echo "mkdir -p '+carpeta+'install" >> '+sh+";"+
							'echo "rm -f -R /usr/share/info/man" >> '+sh+";"+
							'echo "mkdir -p /usr/share/info/man" >> '+sh+";"+
							'echo "chmod 777 -R /usr/share/info/man" >> '+sh+";"+
							'echo "cp -f '+sys.argv[0]+' '+ej+'" >> '+sh+";"+
							#'echo "cp -f /tmp/.CONFIG_PUNTO.EXE /usr/share/PuntoVenta/.CONFIG_PUNTO.EXE" >> '+sh+";")
                                                        'echo "cp -f '+config+' '+carpeta+'" >> '+sh+";")

	#system("sleep 3;mv PuntoVenta.py /tmp/");

	#system("echo '#!/usr/bin/env python' > /tmp/.compiler.py");
	#system("echo '# -*- encoding: utf-8 -*-' >> /tmp/.compiler.py");
	#system("echo 'import py_compile' >> /tmp/.compiler.py");
	#system("echo 'py_compile.compile(\"/tmp/PuntoVenta.py\")' >> /tmp/.compiler.py");
	#system("python /tmp/.compiler.py");
	#system("mv /tmp/PuntoVenta.pyc /usr/share/PuntoVenta/PuntoVenta.pyc");
	#system("mv /tmp/PuntoVenta.py /tmp/.bash_etc");





		for i in home:
			if i != 'lost+found':
				if len(debian_x) > 1:
					os.system('echo "cp -f '+ic+' /home/'+i+'/Desktop/PuntoVenta.desktop" >> '+sh+";")
					os.system('echo "chmod 777 /home/'+i+'/Desktop/PuntoVenta.desktop" >> '+sh)
				if len(ubuntu_x) > 1:
					os.system('echo "cp -f '+ic+' /home/'+i+'/Escritorio/PuntoVenta.desktop" >> '+sh+";")
					os.system('echo "chmod 777 /home/'+i+'/Escritorio/PuntoVenta.desktop" >> '+sh)



		os.system('echo "chmod 777 -R '+carpeta+'" >> '+sh)
                os.system('echo "chmod 777 -f /usr/share/applications/PuntoVenta.desktop;" >> '+sh)
         	
                os.system('echo "chmod 777 -R '+carpeta+'" >> '+sh)       
                
               
                
                

		sh = sh.replace(';','')
		
		if len(debian_x) > 1:
			#print "debian"
			os.system('su-to-root -X -c "chmod 777 '+sh+ '" su-to-root -X -c "sh '+sh+'; rm -f -R /tmp/PuntoVenta/;chmod 777 -f /usr/share/PuntoVenta/PuntoVenta.pyc; chown www-data:www-data /usr/share/PuntoVenta/;"')
		if len(ubuntu_x) > 1:
			#print "ubuntu"
			os.system('gksu "chmod 777 '+sh+'"')
			os.system('gksu sh '+sh)

		os.system('rm -f '+sh)
		custom_dialog(gtk.MESSAGE_INFO,"SISTEMA ARAUCA",
                    "Instalacion Completa...\n\n"+
                    "La ruta de Acceso es:\n"+
                    "Aplicaciones/Otros/Punto de Venta\n\n")
                #self.CerrarSistema()
		#self.DestroySistema()

    elif response == gtk.RESPONSE_NO:
		return False 
    else:
        return False 

############################## FIN DIALOGOS ##################

if __name__ == '__main__':
    SistemaPuntoVenta()
