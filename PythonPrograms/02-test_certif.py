#! /usr/bin/env python3
import os
import requests



headers=["title","name","date","feedback"]
InDir = "/data/feedback/"
url = "http://34.69.198.211/feedback/"

def process_txtfile(text_file):
    dict = {}
    file = InDir + text_file
    with open(file,'r') as reader:
        for i, line in enumerate(reader):
            dict[headers[i]]=line.strip()
    return dict

def compile_result(folder):
    result = []
    for txtfile in os.listdir(folder):
        if txtfile.endswith('.txt'):
            result.append(process_txtfile(txtfile))
    return result

if __name__ == "__main__":
    Result = compile_result(InDir)
    for p in Result:
        response = requests.post(url,data = p)
        if response.status_code != 201:
            raise Exception("failure to post feedbacks.code status: {}".format(response.status_code)
