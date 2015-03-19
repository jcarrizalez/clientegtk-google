#!/usr/bin/env bash

#SVN=`svn info /usr/share/PuntoVenta/ | grep 'Revisión:' | sed 's/Revisión://g'`;
RUTarauca=`pwd`;
cd /usr/share/PuntoVenta/;
SVN=`git rev-list HEAD --count`;
cd $RUTarauca;
cp /usr/share/PuntoVenta/splash.png /tmp/splash.png;
convert /tmp/splash.png -font helvetica -pointsize 15 -fill black -fill white -draw  "text 8 25 'Revisión: $SVN'" /tmp/splash_.png;
rm -f /tmp/splash.png;
exit 0;
