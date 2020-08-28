#!/usr/bin/env python3
import os
import requests

user = os.environ.get('USER')
InDir = "/home/"+user+"/supplier-data/images/"
url = "http://localhost/upload/"

def process_Images(folder,urlink):
    for imgfile in os.listdir(folder):
        if imgfile.endswith('.jpeg'):
            filepath = folder + imgfile
            with open(filepath,'rb') as img:
                response = requests.post(urlink, files = {'file':img})
                if response.status_code != 201:
                    raise Exception("failure to post images.code status: {}".format(response.status_code))

if __name__ == "__main__":
    process_Images(InDir,url)
