#!/usr/bin/env bash

SVN=`svn info /usr/share/PuntoVenta/ | grep 'Revisión:' | sed 's/Revisión://g'`;

cp /usr/share/PuntoVenta/splash.png /tmp/splash.png;
convert /tmp/splash.png -font helvetica -pointsize 15 -fill black -fill white -draw "text 8 25 $SVN" /tmp/splash_.png;
rm -f /tmp/splash.png;

exit 0;
