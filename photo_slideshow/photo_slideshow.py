from collections import defaultdict
from math import *
import random
from random import shuffle


def read_file(fname):
    # nombre de photo
    num = 0
    # collection de photo vertical
    photosVert = []
    # collection de photo horizontal
    photosHor = []
    # id de photo
    id = 0

    with open(fname) as f:
        num = int(f.readline())
        for line in f.readlines():
            val = line.split()
            if val[0] == 'V':
                photosVert.append({
                    'id':id,
                    'orientation':val[0],
                    'numtags':int(val[1]),
                    'tags':val[2:]
                })
                id += 1
            else:
                photosHor.append({
                    'id':id,
                    'orientation':val[0],
                    'numtags':int(val[1]),
                    'tags':val[2:]
                })
                id += 1

    return num, photosVert, photosHor

def compareTags(tag1, tag2):
    if len((set(tag1)).intersection(set(tag2))) < 1 :
        return False
    else:
        return True

def matchPhotosVert(photosVert, collect = []):
    if len(photosVert) > 1:
        i = 1
        for photo in photosVert:
            if compareTags(photosVert[0]['tags'], photosVert[i]['tags']):
                collect.append({
                    'ids':str(photosVert[0]['id']) + ' ' + str(photosVert[i]['id']),
                    'tags':list(set(photosVert[0]['tags'] + photosVert[i]['tags']))
                })
                photosVert.pop(i); photosVert.pop(0)
            else:
                i += 1

    return collect

def createSlide(collPhotos, slide = []):
    if len(collPhotos) > 1:
        i = 1
        for photo in collPhotos:
            if compareTags(collPhotos[0]['tags'], collPhotos[i]['tags']):
                slide.append(str(collPhotos[0]['ids']))
                slide.append(str(collPhotos[i]['ids']))
                collPhotos.pop(i), collPhotos.pop(0)
                if len(collPhotos) == 1:
                    slide.append(str(collPhotos[0]['ids']))
                    return slide
            else:
                i += 1
    elif len(collPhotos) == 1:
        slide.append(str(collPhotos[0]['ids']))
        return slide

    return slide

def write_file(num, coll):
    with open('e_output.txt', 'w') as f:
        f.write(str(num)+'\n')
        for n in coll:
            f.write(str(n)+'\n')



if __name__ == '__main__':
    # checked
    num, photosVertical, photosHorizontal = read_file('e_shiny_selfies.txt')

    collect_photos_vert = matchPhotosVert(photosVertical)
    collect_photos_hor = []
    for photo in photosHorizontal:
        collect_photos_hor.append({'ids':photo['id'], 'tags':photo['tags']})

    collect_photos = collect_photos_vert + collect_photos_hor
    
    slideshow=[]
    while len(slideshow) < 19427:
        perm = list(range(len(collect_photos)))
        random.shuffle(perm)
        collect_photos = [collect_photos[index] for index in perm]

        # print(collect_photos)
        
        slideshow = createSlide(collect_photos)
        
        print(len(slideshow))
        pass
    

    write_file(len(slideshow), slideshow)