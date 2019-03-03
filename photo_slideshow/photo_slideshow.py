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
            collect.append([photosVert[0]['id'], photosVert[i]['id'], list(set(photosVert[0]['tags'] + photosVert[i]['tags']))])
            matchPhotosVert(collect, photosVert, i)
        else:
            i += 1
            matchPhotosVert(collect, photosVert, i)

    return collect

def matchPhoto(photosVert, photosHor):
    pass

def write_file(num, coll):
    with open('out_example.txt', 'wb') as f:
        f.write(num)
        for n in coll:
            f.write(n)



if __name__ == '__main__':
    # checked
    num, photosVertical, photosHorizontal = read_file('a_example.txt')

    photosVertDouble = []

    photosVertDouble = compareTags(photosVertDouble, photosVertical, 0)

    nouvellePhotos = photosVertDouble + photosHorizontal

    photosCollection = []

    photosCollection = compareTags(photosCollection, nouvellePhotos, 0)

    write_file(num, photosCollection)