#!/usr/bin/env python

import random

from local_images import local_images
from google_plus_images import google_plus_images

gallery_size = 8;

output_file = 'gallery.html';
gallery_file = open (output_file, 'w');

image_data = local_images + google_plus_images

for image in random.sample(image_data, gallery_size):
    if image[0] == 'local':
        image_url = '<!--#echo var="MY_DOCUMENT_ROOT"-->/files/images/photos/%s' % image[1]
        image_thumb_url = '<!--#echo var="MY_DOCUMENT_ROOT"-->/files/images/photos/%s' % image[2]
    elif image[0] == 'googleplus':
        image_url = image[1]
        image_thumb_url = image[2]
    gallery_file.write('		  <a href="%s"><img class="thumbnail-photo" src="%s" alt="Some recent moments!" /></a>\n' % (image_url, image_thumb_url));
gallery_file.close();
