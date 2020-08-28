#!/usr/bin/env python3
import os
import requests



user = os.environ.get('USER')
headers=["name","weight","description"]
InDir = "/home/"+user+"/supplier-data/descriptions/"
url = "http://localhost/fruits/"

def process_txtfile(folder,text_file):
    dict = {}
    file = folder + text_file
    with open(file,'r') as reader:
        for i, line in enumerate(reader):
            if line.strip()!= '':
                dict[headers[i]] = line.strip()
    dict["weight"] = dict["weight"].replace('lbs','').strip()
    dict["image_name"] = text_file.replace('.txt','.JPEG')
    return dict

def compile_result(folder):
    result = []
    for txtfile in os.listdir(folder):
        if txtfile.endswith('.txt'):
            result.append(process_txtfile(folder,txtfile))
    return result

if __name__ == "__main__":
    Result = compile_result(InDir)
    for p in Result:
        response = requests.post(url, json = p)
        if response.status_code != 201:
            raise Exception("failure to post json files.code status: {}".format(response.status_code))
