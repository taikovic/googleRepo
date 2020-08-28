#!/usr/bin/env python3
import os
import shutil
from PIL import Image
import requests

size = (600, 400)
user = os.environ.get('USER')
inDir  = "/home/"+user+"/supplier-data/images/"


for infile in os.listdir(inDir):
    if not infile.startswith('.') and infile.endswith('.tiff'):
       source_file = os.path.join(inDir,infile)
       outfile = infile.replace('.tiff','.jpeg')
       target_file = os.path.join(inDir,outfile)
       with Image.open(source_file) as im:
            im.convert("RGB").resize(size).save(target_file,"JPEG")
