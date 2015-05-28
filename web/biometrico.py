#!/usr/bin/env python
"""
carga de archivos raw a la base de datos
"""
import sys, getopt
import psycopg2
from time import time
import os, errno
import ConfigParser

class Biometrico:

	def __init__(self):
		self.tipo = ""
		self.accion = ""
		self.datoID = ""
		self.servidorBD = ""
		self.BD = ""
		self.usuarioBD = ""
		self.claveBD = ""
		self.cursor = ""
		self.cadenaConexion = ""
		self.conexion = ""
		self.puertoBD = ""
		self.numero = ""
		self.estatus = ""
		self.ruta = ""
		self.mensaje = ""

	def registrar(self):
		if (self.cursor):

			prefijo = 'cliente' if self.tipo == 'C' else 'usuario'
			nombreArchivo = '%s_%s_%s_.tmp' % (prefijo, self.datoID, self.numero)
			
			self.validar()
			
			if self.estatus!='EXISTE':
				if ( os.path.isfile(nombreArchivo) ):
					try:
						puntero = open( nombreArchivo,'rb' )
						data = puntero.read()
						puntero.close()

						sql="INSERT INTO huellas (cliente_id, tipo, numero, huella, creado) VALUES (%s,%s,%s,%s, NOW())"

						self.cursor.execute(sql, ( self.datoID,self.tipo,self.numero,psycopg2.Binary(data) ) )
						self.conexion.commit()
					except:
						pass#print "ERROR"

	def verificar(self):
		if (self.cursor):
			try:
				sql = "SELECT cliente_id, huella, numero FROM huellas WHERE cliente_id=%s AND tipo=%s"
				self.cursor.execute(sql, (self.datoID, self.tipo ))
				listado = self.cursor.fetchall()
				self.estatus = 'NO_EXISTE'

				for data in listado:
					if data:
						cliente_id = data[0]
						huella = data[1]
						numero = data[2]
						prefijo = 'cliente' if self.tipo == 'C' else 'usuario'
						nombreArchivo = '%s_%s_%s_.tmp' % (prefijo, self.datoID, numero)
						puntero = open(nombreArchivo,'wb')
						puntero.write(huella)
						puntero.close()
						self.estatus = 'EXISTE'
				#print self.estatus
			except:
				pass#print "ERROR VERIFICAR"

	def modificar(self):
		if (self.cursor):

			prefijo = 'cliente' if self.tipo == 'C' else 'usuario'
			nombreArchivo = '%s_%s_%s_.tmp' % (prefijo, self.datoID, self.numero)
			
			self.validar()
			
			if self.estatus=='EXISTE':
				if ( os.path.isfile(nombreArchivo) ):
					try:
						puntero = open( nombreArchivo,'rb' )
						data = puntero.read()
						puntero.close()
						
						sql="DELETE FROM huellas WHERE cliente_id=%s AND tipo=%s AND numero=%s" 
						self.cursor.execute(sql, (self.datoID, self.tipo, self.numero))
						self.conexion.commit()
						'''
						sql="INSERT INTO huellas (cliente_id, tipo, numero, huella, creado) VALUES (%s,%s,%s,%s, NOW())"
						self.cursor.execute(sql, ( self.datoID,self.tipo,self.numero,psycopg2.Binary(data) ) )
						self.conexion.commit()
						''' 
					except:
						pass
					

	def ponerParametros(self, tipo, accion, datoID, servidorBD, BD, usuarioBD, claveBD, puertoBD, numero):
		self.tipo = tipo if tipo in ('C','U') else ""
		self.accion = accion if accion in ('VERIFICAR','MODIFICAR', 'REGISTRAR') else ""
		self.datoID = datoID if datoID.isdigit() else ""
		self.servidorBD = servidorBD
		self.BD = BD
		self.usuarioBD = usuarioBD
		self.claveBD = claveBD
		self.puertoBD = puertoBD
		self.numero = numero
		
		if self.tipo==None:
			self.mensaje = 'Falta el tipo'
		
		if self.accion==None:
			self.mensaje = self.mensaje + ', Falta la accion'
			
		if self.datoID==None:
			self.mensaje = self.mensaje + ', Falta el datoID'

		if self.servidorBD==None:
			self.mensaje = self.mensaje + ', Falta el Servidor'

		if self.BD==None:
			self.mensaje = self.mensaje + ', Falta la Base de Datos'
			
		if self.usuarioBD==None:
			self.mensaje = self.mensaje + ', Falta el usuario de la Base de Datos'

		if self.claveBD==None:
			self.mensaje = self.mensaje + ', Falta la clave de la Base de Datos'

		if self.puertoBD==None:
			self.mensaje = self.mensaje + ', Falta el puerto de la Base de Datos'

		if self.numero==None:
			self.mensaje = self.mensaje + ', Falta el numero de la huella'

		if self.mensaje:
			print self.mensaje
			
	def conectarBD(self):
		self.cadenaConexion = "host='%s' dbname='%s' user='%s' password='%s'" % (self.servidorBD, self.BD, self.usuarioBD, self.claveBD)
		try:
			self.conexion = psycopg2.connect(self.cadenaConexion)
			self.cursor = self.conexion.cursor()
		except:
			pass#print "ERROR CONECTAR"

	def obtenerConfig(self):
		if (self.cursor):
			try:

				nombreArchivo = 'biometrico.ini' 

				puntero = open( nombreArchivo,'w' )

				sql="SELECT * FROM parametros;"

				self.cursor.execute(sql)
				listado = self.cursor.fetchall()
				
				seccion = "Scanner"
				config = ConfigParser.ConfigParser()
				config.add_section(seccion)
				
				for data in listado:
					config.set(seccion, data[1], data[2])
					
				sql="SELECT count(cliente_id) AS cantidad FROM huellas WHERE cliente_id=%s GROUP BY cliente_id;" % (self.datoID,)

				self.cursor.execute(sql)
				listado = self.cursor.fetchall()
				
				seccion = "Usuario"
				config.add_section(seccion)
				for data in listado:
					config.set(seccion, 'cantidad',data[0])

				config.write(puntero)
			except:
				pass#print "ERROR CONFIG"

	def desconectarBD(self):
		if (self.cursor):
			try:
				self.cursor.close()
				self.conexion.close()
				self.conexion = None
				self.cadenaConexion = ""
			except:
				pass#print 'ERROR DESCONECTAR'

	def validar(self):
		if (self.cursor):
			sql = "SELECT cliente_id, huella, numero FROM huellas WHERE cliente_id=%s AND tipo=%s AND numero=%s"
			try:
				self.cursor.execute(sql, (self.datoID, self.tipo, self.numero ))
				data = self.cursor.fetchone()
				self.estatus = 'EXISTE' if data else 'NO_EXISTE'
			except:
				self.estatus = 'NO_EXISTE'

	def main(self, argv):
		#try:
		self.ponerParametros( argv[0], argv[1], argv[2], argv[3], argv[4], argv[5], argv[6], argv[7], argv[8] )
		self.conectarBD()
		self.obtenerConfig()

		if argv[1] == 'REGISTRAR':
			self.registrar()
		elif argv[1] == 'MODIFICAR':
			self.modificar()
		elif argv[1] == 'VERIFICAR':
			self.verificar()

		self.desconectarBD()
		#except:
		#	print "ERROR MAIN"

def main(argv):
	Biometrico().main(argv)
		
if __name__ == "__main__":
	main(sys.argv[1:])
