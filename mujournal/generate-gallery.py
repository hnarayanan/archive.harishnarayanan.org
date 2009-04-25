#!/usr/bin/python

import random

numberneeded = 8;
outputfile = 'gallery.html';

imagedata = [
#('hiking08/20080713_0933.jpg', 'hiking08/thumbnails/20080713_0933.jpg'),
#('hiking08/20080713_0936.jpg', 'hiking08/thumbnails/20080713_0936.jpg'),
('hiking08/20080713_0939.jpg', 'hiking08/thumbnails/20080713_0939.jpg'),
('hiking08/20080713_0946.jpg', 'hiking08/thumbnails/20080713_0946.jpg'),
#('hiking08/20080713_0947.jpg', 'hiking08/thumbnails/20080713_0947.jpg'),
('hiking08/20080713_0949.jpg', 'hiking08/thumbnails/20080713_0949.jpg'),
('hiking08/20080713_0954.jpg', 'hiking08/thumbnails/20080713_0954.jpg'),
('hiking08/20080713_0960.jpg', 'hiking08/thumbnails/20080713_0960.jpg'),
('hiking08/20080713_0962.jpg', 'hiking08/thumbnails/20080713_0962.jpg'),
('hiking08/20080713_0969.jpg', 'hiking08/thumbnails/20080713_0969.jpg'),
('hiking08/20080713_0972.jpg', 'hiking08/thumbnails/20080713_0972.jpg'),
('hiking08/20080713_0975.jpg', 'hiking08/thumbnails/20080713_0975.jpg'),
('hiking08/20080713_0978.jpg', 'hiking08/thumbnails/20080713_0978.jpg'),
#('hiking08/20080713_0984.jpg', 'hiking08/thumbnails/20080713_0984.jpg'),
('hiking08/20080713_0985.jpg', 'hiking08/thumbnails/20080713_0985.jpg'),
('hiking08/20080713_0989.jpg', 'hiking08/thumbnails/20080713_0989.jpg'),
#('hiking08/20080713_0999.jpg', 'hiking08/thumbnails/20080713_0999.jpg'),
#('hiking08/20080713_1001.jpg', 'hiking08/thumbnails/20080713_1001.jpg'),
#('hiking08/20080713_1003.jpg', 'hiking08/thumbnails/20080713_1003.jpg'),
('hiking08/20080713_1005.jpg', 'hiking08/thumbnails/20080713_1005.jpg'),
('hiking08/20080713_1010.jpg', 'hiking08/thumbnails/20080713_1010.jpg'),
('hiking08/20080713_1017.jpg', 'hiking08/thumbnails/20080713_1017.jpg'),
('summer08/00.jpg', 'summer08/thumbnails/00.jpg'),
('summer08/01.jpg', 'summer08/thumbnails/01.jpg'),
('summer08/02.jpg', 'summer08/thumbnails/02.jpg'),
('summer08/03.jpg', 'summer08/thumbnails/03.jpg'),
('summer08/04.jpg', 'summer08/thumbnails/04.jpg'),
('summer08/05.jpg', 'summer08/thumbnails/05.jpg'),
('summer08/06.jpg', 'summer08/thumbnails/06.jpg'),
('asgardstrand08/20080923_1053.jpg', 'asgardstrand08/thumbnails/20080923_1053.jpg'),
('asgardstrand08/20080923_1062.jpg', 'asgardstrand08/thumbnails/20080923_1062.jpg'),
('asgardstrand08/20080923_1079.jpg', 'asgardstrand08/thumbnails/20080923_1079.jpg'),
#('asgardstrand08/20080923_1091.jpg', 'asgardstrand08/thumbnails/20080923_1091.jpg'),
('asgardstrand08/20080923_1098.jpg', 'asgardstrand08/thumbnails/20080923_1098.jpg'),
('frisbee08/20080705_0911.jpg', 'frisbee08/thumbnails/20080705_0911.jpg'),
('frisbee08/20080705_0913.jpg', 'frisbee08/thumbnails/20080705_0913.jpg'),
('cbc08/20081107_1124.jpg', 'cbc08/thumbnails/20081107_1124.jpg'),
('cbc08/20081107_1129.jpg', 'cbc08/thumbnails/20081107_1129.jpg'),
('cbc08/20081107_1139.jpg', 'cbc08/thumbnails/20081107_1139.jpg'),
('mbp08/20081120_1171.jpg', 'mbp08/thumbnails/20081120_1171.jpg'),
('mbp08/20081120_1183.jpg', 'mbp08/thumbnails/20081120_1183.jpg'),
('mbp08/20081120_1184.jpg', 'mbp08/thumbnails/20081120_1184.jpg'),
('mbp08/20081120_1185.jpg', 'mbp08/thumbnails/20081120_1185.jpg'),
('mbp08/20081120_1188.jpg', 'mbp08/thumbnails/20081120_1188.jpg'),
('art/word-list.png', 'art/thumbnails/word-list.png')
];

possibilities = range (0,len(imagedata),1);
chosen = random.sample(possibilities,numberneeded);

galleryfile = open (outputfile,'w');

for imagenumber in chosen:
    galleryfile.write('		  <a href="<!--#echo var="MY_DOCUMENT_ROOT"-->/files/images/photos/'+imagedata[imagenumber][0]+'"><img class="thumbnail-photo" src="<!--#echo var="MY_DOCUMENT_ROOT"-->/files/images/photos/'+imagedata[imagenumber][1]+'" alt="Some recent moments!" /></a>\n');

galleryfile.close();
