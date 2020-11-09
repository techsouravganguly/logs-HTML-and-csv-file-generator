#!/usr/bin/env python3
import operator
import re
import sys
import csv
error={}
info={}
with open('syslog.log') as f:
  w=f.readlines()
for line in w:
  result = re.search(r"ticky: ERROR ([\w ]*) ", line)
  if result is not None:
    result = result.groups()
    if result[0] in error:
      error[result[0]]+=1
    else:
      error[result[0]]=1
  result1 = re.search(r"\(([\w\.]*)\)",line)
  result1 =result1.groups()
  if result1[0] not in info:
    info[result1[0]] = [0,0]
  result = re.search(r"ticky: ([A-Z]*)", line)
  result=result.groups()
  if result[0]=="ERROR":
    info[result1[0]][1]+=1
  else:
    info[result1[0]][0]+=1
error["Ticket doesn't exist"] = error["Ticket"]
del error["Ticket"]
s_info = sorted(info.items())
s_error = sorted(error.items(),key= operator.itemgetter(1),reverse=True)
s_error.insert(0,("Error","count"))
l_info =[]
for i in s_info:
  l_info.append((i[0],i[1][0],i[1][1]))
l_info.insert(0,("Username","INFO","ERROR"))
print(l_info)
with open('error_message.csv','w') as f:
  w=csv.writer(f)
  w=w.writerows(s_error)
with open('user_statistics.csv','w') as f:
  w=csv.writer(f)
  w=w.writerows(l_info)
