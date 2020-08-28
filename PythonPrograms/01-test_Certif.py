#!/usr/bin/env python3
import os
import shutil
from PIL import Image

size = (128, 128)
rotation_Degree = -90
inDir  = "/home/taikovic/Desktop/images_fork/"
outDir = "/home/taikovic/Desktop/Icons/"

for infile in os.listdir(inDir):
    #print(os.path.basename(infile))
    print(infile)
    #outfile = os.path.splitext(infile)[0] + ".JPEG"
    source_file = os.path.join(inDir,infile)
    print(source_file)
    #target_file = os.path.join(outDir,outfile)
    target_file = os.path.join(outDir,infile)
    print(target_file)
    with Image.open(source_file) as im:
        im.rotate(rotation_Degree).resize(size).save(target_file,"JPEG")
# curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=$11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF"
#> /dev/null | curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/
#{print $NF}' ./cookie`&id=11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" -o images.zip && sudo rm -rf cookie
=======================================================================
#!/usr/bin/env python3
import os
import shutil
from PIL import Image

size = (128, 128)
rotation_Degree = -90
inDir  = "/home/student-04-a4e4894fae4a/images/"
outDir = "/opt/icons/"

for infile in os.listdir(inDir):
    if not infile.startswith('.'):
       source_file = os.path.join(inDir,infile)
       target_file = os.path.join(outDir,infile)
       with Image.open(source_file) as im:
            im.convert("L").rotate(rotation_Degree).resize(size).save(target_file,"JPEG")

====================================================================
