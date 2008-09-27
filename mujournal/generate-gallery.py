#!/usr/bin/python

import random

numberneeded = 4;
outputfile = 'gallery.html';

imagedata = [
('hiking08/20080713_0933.jpg', 'hiking08/thumbnails/20080713_0933.jpg'),
('hiking08/20080713_0936.jpg', 'hiking08/thumbnails/20080713_0936.jpg'),
('hiking08/20080713_0939.jpg', 'hiking08/thumbnails/20080713_0939.jpg'),
('hiking08/20080713_0946.jpg', 'hiking08/thumbnails/20080713_0946.jpg'),
('hiking08/20080713_0947.jpg', 'hiking08/thumbnails/20080713_0947.jpg'),
('hiking08/20080713_0949.jpg', 'hiking08/thumbnails/20080713_0949.jpg'),
('hiking08/20080713_0954.jpg', 'hiking08/thumbnails/20080713_0954.jpg'),
('hiking08/20080713_0960.jpg', 'hiking08/thumbnails/20080713_0960.jpg'),
('hiking08/20080713_0962.jpg', 'hiking08/thumbnails/20080713_0962.jpg'),
('hiking08/20080713_0969.jpg', 'hiking08/thumbnails/20080713_0969.jpg'),
('hiking08/20080713_0972.jpg', 'hiking08/thumbnails/20080713_0972.jpg'),
('hiking08/20080713_0975.jpg', 'hiking08/thumbnails/20080713_0975.jpg'),
('hiking08/20080713_0978.jpg', 'hiking08/thumbnails/20080713_0978.jpg'),
('hiking08/20080713_0984.jpg', 'hiking08/thumbnails/20080713_0984.jpg'),
('hiking08/20080713_0985.jpg', 'hiking08/thumbnails/20080713_0985.jpg'),
('hiking08/20080713_0989.jpg', 'hiking08/thumbnails/20080713_0989.jpg'),
('hiking08/20080713_0999.jpg', 'hiking08/thumbnails/20080713_0999.jpg'),
('hiking08/20080713_1001.jpg', 'hiking08/thumbnails/20080713_1001.jpg'),
('hiking08/20080713_1003.jpg', 'hiking08/thumbnails/20080713_1003.jpg'),
('hiking08/20080713_1005.jpg', 'hiking08/thumbnails/20080713_1005.jpg'),
('hiking08/20080713_1010.jpg', 'hiking08/thumbnails/20080713_1010.jpg'),
('hiking08/20080713_1017.jpg', 'hiking08/thumbnails/20080713_1017.jpg'),
('moments08/00.jpg', 'moments08/thumbnails/00.jpg'),
('moments08/01.jpg', 'moments08/thumbnails/01.jpg'),
('moments08/02.jpg', 'moments08/thumbnails/02.jpg'),
('moments08/03.jpg', 'moments08/thumbnails/03.jpg'),
('moments08/04.jpg', 'moments08/thumbnails/04.jpg'),
('moments08/05.jpg', 'moments08/thumbnails/05.jpg'),
('moments08/06.jpg', 'moments08/thumbnails/06.jpg'),
('asgardstrand08/20080923_1053.jpg', 'asgardstrand08/thumbnails/20080923_1053.jpg'),
('asgardstrand08/20080923_1062.jpg', 'asgardstrand08/thumbnails/20080923_1062.jpg'),
('asgardstrand08/20080923_1079.jpg', 'asgardstrand08/thumbnails/20080923_1079.jpg'),
('asgardstrand08/20080923_1091.jpg', 'asgardstrand08/thumbnails/20080923_1091.jpg'),
('asgardstrand08/20080923_1098.jpg', 'asgardstrand08/thumbnails/20080923_1098.jpg'),
];

possibilities = range (0,len(imagedata),1);
chosen = random.sample(possibilities,numberneeded);

galleryfile = open (outputfile,'w');

for imagenumber in chosen:
    galleryfile.write('		  <a href="<!--#echo var="MY_DOCUMENT_ROOT"-->/files/images/photos/'+imagedata[imagenumber][0]+'"><img class="thumbnail-photo" src="<!--#echo var="MY_DOCUMENT_ROOT"-->/files/images/photos/'+imagedata[imagenumber][1]+'" alt="" /></a>\n');

galleryfile.close();
