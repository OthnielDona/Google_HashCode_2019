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
            photosVert.pop(0); photosVert.pop(i)
            matchPhotosVert(photosVert, collect, i)
        else:
            i += 1
            matchPhotosVert(photosVert, collect, i)

    return collect

def createSlide(collVert, photosHor, finalCollect = []):
    if collVert > 0 and photosHor > 0:
        alt = 1
        tags1 = []
        tags2 = []

        if alt:
            tags1 = collVert[0][2]
            tags2 = photosHor[0]['tags']
            
            if compareTags(tag1, tag2):
            finalCollect.append(str(collVert[0][0:2]))
            finalCollect
        else:
            tags1 = photosHor[0]['tags']
            tags2 = collVert[0][2]

def write_file(num, coll):
    with open('out_example.txt', 'wb') as f:
        f.write(num)
        for n in coll:
            f.write(n)



if __name__ == '__main__':
    # checked
    num, photosVertical, photosHorizontal = read_file('a_example.txt')

    collect_photos_vert = matchPhotosVert(photosVertical)

    # write_file(num, photosCollection)