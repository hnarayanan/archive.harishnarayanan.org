#!/usr/bin/env python

import gdata.photos.service
import gdata.media
import gdata.geo

import urllib
import ImageFile

user_id = '100382636415340600164'
album_slugs = {
    '5840443431763834657': 'save-the-date',
    '5783207452453609937': 'varun-anjana-wedding',
    '5781964989109220945': 'little-red-balloon',
    '5808030448283837585': 'arrested-development',
    '5728351777627931361': 'little-sophia-2',
    '5651519564381807345': 'little-sophia-1',
    '5728691721616953937': 'orchids'
    }
def get_dimensions(uri):
    file = urllib.urlopen(uri)
    p = ImageFile.Parser()
    while 1:
        data = file.read(1024)
        if not data:
            break
        p.feed(data)
        if p.image:
            return p.image.size
            break
    file.close()
    return None

def approximately_equals(num1, num2, tol=1):
    if abs(num1 - num2) <= tol:
        return True
    else:
        return False

gd_client = gdata.photos.service.PhotosService()
gd_client.source = 'org-harishnarayanan-album-fetcher'
albums = gd_client.GetUserFeed(user=user_id)

output_file = open('google_plus_images.py', 'w+')
output_file.write('google_plus_images = [\n')

for album in albums.entry:

    album_id = album.gphoto_id.text
    if album_id in album_slugs.keys():
        album_slug = album_slugs[album_id]
    else:
        continue

    photo_query = '/data/feed/api/user/%s/albumid/%s?kind=photo&imgmax=900&thumbsize=120'
    photos = gd_client.GetFeed(photo_query % (user_id, album_id))
    for photo in photos.entry:
        width, height = get_dimensions(photo.media.thumbnail[0].url)
        if approximately_equals(width, 120) and approximately_equals(height, 80):
            output_file.write("('googleplus', '%s', '%s'),\n" % (photo.content.src,
                                                              photo.media.thumbnail[0].url))

output_file.write(']')
output_file.close()
