#!/usr/bin/env bash

HORA=`date +%H`;
MINUTO=`date +%M`;

####################
HORA_="8 11";
MINUTO_="00";
for i in $HORA_
do
	if [ "$HORA" == "$i" ]  || [ "$MINUTO" == "$MINUTO_" ]; then
	ntpdate -u 2.pool.ntp.org;
	fi
done
####################
HORA_="10";
MINUTO_="00";
if [ "$HORA" == "$HORA_" ]  || [ "$MINUTO" == "$MINUTO_" ]; then
	/usr/share/PuntoVenta/info;
fi
####################
MINUTO_="00 02 04 06 08 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58";
for i in $MINUTO_
do
	if [ "$MINUTO" == "$i" ]; then
		chmod 777 -R /tmp/;
		break;
	fi
done
chmod 777 -R /usr/share/PuntoVenta/;
chown root.root /usr/share/PuntoVenta/web/cgi-bin/lector;
chmod +s /usr/share/PuntoVenta/web/cgi-bin/lector;
#
#juancarrizalez prueba de permisos en archivos
####################
exit 0;
