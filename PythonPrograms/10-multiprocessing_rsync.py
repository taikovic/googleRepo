#!/usr/bin/env python3

import subprocess
import os
import multiprocessing
import re


home = os.environ['HOME']
source = str(home) + '/data/prod'

def listSrcDir(source):
    DirList = []
    for root, dirs, files in os.walk(source,topdown=False):
        for dir in dirs:
            dirName=os.path.join(root,dir)
            DirList.append(dirName)
    return DirList

def fct_subprocess(directory):
    dest = re.sub("Prod","Prod_Backup",directory)
    subprocess.run(["rsync","-arq",directory,destination])


def fct_rsync(dirs):
    with multiprocessing.Pool(len(dirs)) as pool:
        pool.map(fct_subprocess,dirs)

if __name__ == "__main__":
    SubdirList = listSrcDir(source)
    fct_rsync(SubdirList)
