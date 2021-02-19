#!/bin/python3

angle_col1 = []
dista_col2 = []
with open("test_col.csv", "r+") as f:
    for elem in f.readlines():
        angle_col1.append(float(elem.split(",")[0]))
        dista_col2.append(float(elem.split(",")[1]))

condition = True
check_fistagle = dista_col2[2] - dista_col2[1]
if(check_fistagle > 0):
    condition = True
else:
    condition = False
i=0
for i in range(4):
    if (angle_col1[i+1]-angle_col1[i]<0):
        print(angle_col1[i])
        print(dista_col2[i])
        condition = False
    i+=1


