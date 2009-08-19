#!/usr/bin/python

import random

numberneeded = 8;
outputfile = 'gallery.html';

imagedata = [
('hiking08/20080713_0939.jpg', 'hiking08/thumbnails/20080713_0939.jpg'),
('hiking08/20080713_0946.jpg', 'hiking08/thumbnails/20080713_0946.jpg'),
('hiking08/20080713_0949.jpg', 'hiking08/thumbnails/20080713_0949.jpg'),
('hiking08/20080713_0954.jpg', 'hiking08/thumbnails/20080713_0954.jpg'),
('hiking08/20080713_0960.jpg', 'hiking08/thumbnails/20080713_0960.jpg'),
('hiking08/20080713_0962.jpg', 'hiking08/thumbnails/20080713_0962.jpg'),
('hiking08/20080713_0969.jpg', 'hiking08/thumbnails/20080713_0969.jpg'),
('hiking08/20080713_0975.jpg', 'hiking08/thumbnails/20080713_0975.jpg'),
('hiking08/20080713_0989.jpg', 'hiking08/thumbnails/20080713_0989.jpg'),
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
('asgardstrand08/20080923_1079.jpg', 'asgardstrand08/thumbnails/20080923_1079.jpg'),
('asgardstrand08/20080923_1098.jpg', 'asgardstrand08/thumbnails/20080923_1098.jpg'),
('frisbee08/20080705_0913.jpg', 'frisbee08/thumbnails/20080705_0913.jpg'),
('cbc08/20081107_1124.jpg', 'cbc08/thumbnails/20081107_1124.jpg'),
('cbc08/20081107_1129.jpg', 'cbc08/thumbnails/20081107_1129.jpg'),
('cbc08/20081107_1139.jpg', 'cbc08/thumbnails/20081107_1139.jpg'),
('mbp08/20081120_1183.jpg', 'mbp08/thumbnails/20081120_1183.jpg'),
('mbp08/20081120_1184.jpg', 'mbp08/thumbnails/20081120_1184.jpg'),
('mbp08/20081120_1188.jpg', 'mbp08/thumbnails/20081120_1188.jpg'),
# ('art/word-list.png', 'art/thumbnails/word-list.png'),
('art/20090426_1468.jpg', 'art/thumbnails/20090426_1468.jpg'),
('molly30/20090509_1504.jpg', 'molly30/thumbnails/20090509_1504.jpg'),
('molly30/20090509_1524.jpg', 'molly30/thumbnails/20090509_1524.jpg'),
('molly30/20090509_1532.jpg', 'molly30/thumbnails/20090509_1532.jpg'),
('molly30/20090509_1545.jpg', 'molly30/thumbnails/20090509_1545.jpg'),
('molly30/20090509_1546.jpg', 'molly30/thumbnails/20090509_1546.jpg'),
('molly30/20090509_1551.jpg', 'molly30/thumbnails/20090509_1551.jpg'),
('molly30/20090509_1655.jpg', 'molly30/thumbnails/20090509_1655.jpg'),
('molly30/20090509_1658.jpg', 'molly30/thumbnails/20090509_1658.jpg'),
('molly30/20090509_3881.jpg', 'molly30/thumbnails/20090509_3881.jpg'),
('agwedding/20090704_2655.jpg', 'agwedding/thumbnails/20090704_2655.jpg'),
('agwedding/20090704_2656.jpg', 'agwedding/thumbnails/20090704_2656.jpg'),
('agwedding/20090704_2670.jpg', 'agwedding/thumbnails/20090704_2670.jpg'),
('agwedding/20090704_2673.jpg', 'agwedding/thumbnails/20090704_2673.jpg'),
('agwedding/20090704_2681.jpg', 'agwedding/thumbnails/20090704_2681.jpg'),
('agwedding/20090704_2689.jpg', 'agwedding/thumbnails/20090704_2689.jpg'),
('agwedding/20090704_2697.jpg', 'agwedding/thumbnails/20090704_2697.jpg'),
('agwedding/20090704_2701.jpg', 'agwedding/thumbnails/20090704_2701.jpg'),
('agwedding/20090704_2718.jpg', 'agwedding/thumbnails/20090704_2718.jpg'),
('agwedding/20090704_2722.jpg', 'agwedding/thumbnails/20090704_2722.jpg'),
('agwedding/20090704_2727.jpg', 'agwedding/thumbnails/20090704_2727.jpg'),
('agwedding/20090704_2757.jpg', 'agwedding/thumbnails/20090704_2757.jpg'),
('agwedding/20090704_2778.jpg', 'agwedding/thumbnails/20090704_2778.jpg'),
('agwedding/20090704_2804.jpg', 'agwedding/thumbnails/20090704_2804.jpg'),
('agwedding/20090704_2810.jpg', 'agwedding/thumbnails/20090704_2810.jpg'),
('agwedding/20090704_2823.jpg', 'agwedding/thumbnails/20090704_2823.jpg'),
('agwedding/20090704_2848.jpg', 'agwedding/thumbnails/20090704_2848.jpg'),
('agwedding/20090704_2851.jpg', 'agwedding/thumbnails/20090704_2851.jpg'),
('agwedding/20090707_2871.jpg', 'agwedding/thumbnails/20090707_2871.jpg'),
('agwedding/20090707_2872.jpg', 'agwedding/thumbnails/20090707_2872.jpg'),
('agwedding/20090707_2874.jpg', 'agwedding/thumbnails/20090707_2874.jpg'),
('agwedding/20090707_2885.jpg', 'agwedding/thumbnails/20090707_2885.jpg'),
('agwedding/20090707_2886.jpg', 'agwedding/thumbnails/20090707_2886.jpg'),
('smogen09/20090817_3031.jpg', 'smogen09/thumbnails/20090817_3031.jpg'),
('smogen09/20090817_3001.jpg', 'smogen09/thumbnails/20090817_3001.jpg'),
('smogen09/20090817_3015.jpg', 'smogen09/thumbnails/20090817_3015.jpg'),
('smogen09/20090817_3003.jpg', 'smogen09/thumbnails/20090817_3003.jpg'),
('smogen09/20090817_2905.jpg', 'smogen09/thumbnails/20090817_2905.jpg'),
('smogen09/20090817_2958.jpg', 'smogen09/thumbnails/20090817_2958.jpg'),
('smogen09/20090817_2920.jpg', 'smogen09/thumbnails/20090817_2920.jpg'),
('smogen09/20090817_2964.jpg', 'smogen09/thumbnails/20090817_2964.jpg'),
('smogen09/20090817_2991.jpg', 'smogen09/thumbnails/20090817_2991.jpg'),
('smogen09/20090817_3043.jpg', 'smogen09/thumbnails/20090817_3043.jpg'),
('smogen09/20090817_3036.jpg', 'smogen09/thumbnails/20090817_3036.jpg'),
('smogen09/20090817_3056.jpg', 'smogen09/thumbnails/20090817_3056.jpg'),
('smogen09/20090817_3063.jpg', 'smogen09/thumbnails/20090817_3063.jpg'),
('smogen09/20090817_2892.jpg', 'smogen09/thumbnails/20090817_2892.jpg'),
('smogen09/20090817_2895.jpg', 'smogen09/thumbnails/20090817_2895.jpg'),
('smogen09/20090817_3058.jpg', 'smogen09/thumbnails/20090817_3058.jpg'),
];

possibilities = range (0, len(imagedata), 1);
chosen = random.sample(possibilities, numberneeded);

galleryfile = open (outputfile, 'w');

for imagenumber in chosen:
    galleryfile.write('		  <a href="<!--#echo var="MY_DOCUMENT_ROOT"-->/files/images/photos/' + imagedata[imagenumber][0]+'"><img class="thumbnail-photo" src="<!--#echo var="MY_DOCUMENT_ROOT"-->/files/images/photos/' + imagedata[imagenumber][1] + '" alt="Some recent moments!" /></a>\n');

galleryfile.close();