""""Create folders foto and rezult
upload photos to "foto" folder

in the "rezult" folder get a photo with the background removed"""

from rembg import remove
import glob

foto_extension=["*.jpg",'*.png','*.JPG','*.PNG','*.jpeg',"*.JPEG"]

all_photo=[]
for i in foto_extension:
    all_photo.extend(glob.glob('.\\foto/'+i))
print(all_photo)


for i in range(len(all_photo)):
    out='.\\rezult/'+all_photo[i].split('\\')[::-1][0]


    with open(all_photo[i], 'rb') as i:
        with open(out, 'wb') as o:
            input = i.read()
            output = remove(input)
            o.write(output)