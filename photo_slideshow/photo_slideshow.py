def read_file(fname):
    # nombre de photo
    num = 0
    # collection de photo
    photos = []
    # id de photo
    id = 0

    lines = open(fname).readlines()
    num = int(lines[0])
    for line in lines[1:]:
        val = line.split() 
        photos.append({'id':id, 'orientation':val[0], 'numtag':int(val[1]), 'tags':val[2:]})
        id += 1

    return num, photos

def compareTags(temp, photosVert, i):
    if len(photosVert) > 1:
        if compareTagsNumber(photosVert[0], photosVert[i]) > 0 and
        compareTagsNumber(photosVert[0], photosVert[i]) < min(photosVert[0]['numtag'], photosVert[i]['numtag']):
            temp.append([photosVert.pop(0), photosVert.pop(i)])
            compareTags(temp, photosVert, i)
        else:
            i += 1
            compareTags(temp, photosVert, i)

    return temp

def compareTagsNumber(photo1, photo2):
    x = 0
    if len(photo1['tags']) > 0:
        if photo1['tags'][0] in photo2['tags']:
            photo1['tags'].pop(0)
            x += 1
            compareTagsNumber(photo1, photo2)
        else:
            photo1['tags'].pop(0)
            compareTagsNumber(photo1, photo2)

    return x

def regroupPhotosVert(photos):
    temp = []
    for photo in photos:
        if photo['orientation'] == 'V':
            temp.append(photo)

    return temp

def regroupPhotosHor(photos):
    temp = []
    for photo in photos:
        if photo['orientation'] == 'H':
            temp.append(photo)

    return temp

def matchPhoto(photosVert, photosHor):
    pass

def write_file(num, coll):
    with open('out_example.txt', 'wb') as f:
        f.write(num)
        for n in coll:
            f.write(n)



if __name__ == '__main__':
    # checked
    num, photos = read_file('a_example.txt')

    # checked
    photosVertical = regroupPhotosVert(photos)
    photosHorizontal = regroupPhotosHor(photos)

    photosVertDouble = []

    photosVertDouble = compareTags(photosVertDouble, photosVertical, 0)

    nouvellePhotos = photosVertDouble + photosHorizontal

    photosCollection = []

    photosCollection = compareTags(photosCollection, nouvellePhotos, 0)

    write_file(num, photosCollection)