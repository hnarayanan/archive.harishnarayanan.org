#!/bin/sh

siteroot='http://home.simula.no/~harish/'
echo '<?xml version="1.0" encoding="UTF-8"?>'
echo '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
cd ..
for folder in `find . -maxdepth 3 -name 'index.html'`
do
    echo '<url>'
    echo '  <loc>'$siteroot`dirname $folder | cut -c 3-`'</loc>'
    echo '  <lastmod>'`find $folder -name 'index.html' -printf "%AY-%Am-%Ad\n"`'</lastmod>'
    echo '</url>'
done
echo '</urlset>'