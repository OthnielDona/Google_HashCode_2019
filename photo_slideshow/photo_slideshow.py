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
    if set(tag1) < set(tag2) or set(tag2) < set(tag1):
        return False
    else:
        return True

def matchPhotosVert(photosVert, collect = [], i = 1):
    if len(photosVert) > 1:
        if compareTags(photosVert[0]['tags'], photosVert[i]['tags']):
            collect.append({
                'ids':str(photosVert[0]['id']) + ' ' + str(photosVert[i]['id']),
                'tags':list(set(photosVert[0]['tags'] + photosVert[i]['tags']))
            })
            photosVert.pop(i); photosVert.pop(0)
            matchPhotosVert(photosVert, collect, i)
        else:
            i += 1
            matchPhotosVert(photosVert, collect, i)

    return collect

def createSlide(collPhotos, slide = [], i = 1):
    if len(collPhotos) > 1:
        if compareTags(collPhotos[0]['tags'], collPhotos[i]['tags']):
            slide.append(str(collPhotos[0]['ids']))
            slide.append(str(collPhotos[i]['ids']))
            collPhotos.pop(i), collPhotos.pop(0)
            if len(collPhotos) == 1:
                slide.append(str(collPhotos[0]['ids']))
                return slide
            createSlide(collPhotos, slide, i)
        else:
            i += 1
            createSlide(collPhotos, slide, i)
    elif len(collPhotos) == 1:
        slide.append(str(collPhotos[0]['ids']))
        return slide

    return slide

def write_file(num, coll):
    with open('slideshow.txt', 'w') as f:
        f.write(str(num)+'\n')
        for n in coll:
            f.write(str(n)+'\n')



if __name__ == '__main__':
    # checked
    num, photosVertical, photosHorizontal = read_file('a_example.txt')

    collect_photos_vert = matchPhotosVert(photosVertical)
    collect_photos_hor = []
    for photo in photosHorizontal:
        collect_photos_hor.append({'ids':photo['id'], 'tags':photo['tags']})

    collect_photos = collect_photos_hor + collect_photos_vert

    slideshow = createSlide(collect_photos)
    
    write_file(len(slideshow), slideshow)