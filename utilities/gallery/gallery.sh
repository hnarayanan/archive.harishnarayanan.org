#!/usr/bin/env bash

output_file=index.html

cat gallery-header.html > ${output_file}

for file in ${1}/*.jpg
do
    echo '	          <a href="<!--#echo var="MY_DOCUMENT_ROOT"-->/files/images/photos/'${file}'" title=""><img class="thumbnail-photo" src="<!--#echo var="MY_DOCUMENT_ROOT"-->/files/images/photos/'`dirname ${file}`'/thumbnails/'`basename ${file}`'" alt="<!--#echo var="pagetitle" -->" /></a>' >> ${output_file}_tmp
done

sort -R ${output_file}_tmp >> ${output_file}
rm ${output_file}_tmp

cat gallery-footer.html >> ${output_file}