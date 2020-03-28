#!/usr/bin/env python
import subprocess
import multiprocessing


src = "/data/prod/"
dest = "/data/prod_backup/"
#subprocess.call(["rsync", "-arq", src, dest])

list=["rsync","-arq","src","dest"]

def get_list(src,dest):
        srclist,destlist = {},{}
        for dirname, subdirlist,filelist in os.walk(src):
                if dirname != '/data/prod/'
                        srclist.append(dirname)


def DailySync(srclist,destlist):
        with multiprocessing.Pool()as pool:
                pool.map(subprocess.call(["rsync","-arq"]),src,dest)

if __name__ == "__main__":
        DailySync(list)
