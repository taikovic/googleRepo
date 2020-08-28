#!/usr/bin/env python3
import os
from datetime import datetime
import reports
import emails

user = os.environ.get('USER')
InDir = "/home/"+user+"/supplier-data/descriptions/"
headers=["name","weight"]

def process_txtfile(folder,text_file):
    dict = {}
    file = folder + text_file
    with open(file,'r') as reader:
        for i, line in enumerate(reader):
            if line.strip() != '' and i<2:
                dict[headers[i]] = line.strip()
    return dict

def compile_result(folder):
    result = []
    for txtfile in os.listdir(folder):
        if txtfile.endswith('.txt'):
            result.append(process_txtfile(folder,txtfile))
    return result

def generate_paragraph(list):
    paragraph = ''
    for dict in list:
        for key,val in dict.items():
            paragraph += str(key) +": "+ str(val) + str('\n')
        paragraph += str('\n')
    return paragraph

if __name__ == "__main__":

    Day = datetime.today().strftime('%b %d, %Y')
    title = "Processed Update on " + str(Day)
    Result = compile_result(InDir)
    paragraph = generate_paragraph(Result)
    additional_info = paragraph.replace('\n','<br/>')
    reports.generate_report("/tmp/processed.pdf", title, additional_info)
    #Sending email:
    message = emails.generate_email("automation@example.com", "{}@example.com".format(user), "Upload Complete - Online Fruit Store", "All fruits are uploaded to our website successfully. A detailed list is attached to this email.", "/tmp/processed.pdf")
    send_email(message)
