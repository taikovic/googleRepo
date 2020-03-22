#!/usr/bin/env python3
import sys
import re
import operator
import csv



error_msg_file = "__error_message.csv__"
user_stat_file = "user_statistics.csv"
def ranking_error(logfile):
    error={}
    per_user={}
    with open(logfile,'r')as file:
        for line in file.readlines():
            print(line)
            msg = re.search(r"(\w+): (\w+) ([\w ]+)\[*.*\]*\(+([\w]+)\)+",line)
            print(msg.group())
            key = msg[3].strip()
            print(key)
            user = msg[4].strip()
            print(key)
            if user not in per_user:
                per_user[user]=[0,0]
            if msg[2] =='ERROR':
                error[key] = error.get(key,0)+1
                per_user[user][1]=per_user.get(user,0)[1] + 1
            elif msg[2] == 'INFO':
                per_user[user][0]=per_user.get(user,0)[0] + 1
    file.close()
    error = sorted(error.items(), key = operator.itemgetter(1), reverse = True)
    per_user= sorted(per_user.items(), key= operator.itemgetter(0),reverse=False)
    error.insert(0,("Error","Count"))
    per_user.insert(0,("Username",["INFO","ERROR"]))
    return error,per_user

def write_error_report(error_list,report_file):
    with open(report_file,"w+") as f:
        for error in error_list:
            err, count = error
            f.write(str(err) + ',' + str(count) +'\n')
    f.close()

def write_user_report(users_list,report_file):
    with open(report_file,"w+") as f:
        for user in users_list:
            username,stat = user
            f.write(str(username) + ',' + str(stat[0]) + ',' + str(stat[1])+'\n')
    f.close()



def main():
    error,per_user = ranking_error(sys.argv[1])
    write_error_report(error,"error_msg_new.csv")
    write_user_report(per_user,"user_new.csv")

if __name__== "__main__":
    main()
