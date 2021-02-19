#!/bin/python3

class Class1:
    def __init__(self):
        #create mapping file
        self.f_mapping = open("mapping.csv","w+")
        self.angle_col1 = []
        self.dista_col2 = []

    def split_file(self):
        #cook LIDARPoints file
        with open("LIDARPoints.csv", "r+") as f:
            for elem in f.readlines():
                self.angle_col1.append(float(elem.split(",")[0]))
                self.dista_col2.append(float(elem.split(",")[1]))

    def do_each_sweep(self):
        line_num = 0 
        for i in range(34):
            num_line =  int(self.dista_col2[line_num])
            check_first_angle = self.dista_col2[line_num+2] - self.dista_col2[line_num+1]
            if(check_first_angle > 0):
                distance_plus = True
            else:
                distance_plus = False
            self.single_sweep(num_line, line_num, distance_plus) 
            line_num = line_num+num_line+1

    def single_sweep(self, num_line, line_num, distance_plus):
        #for i in range(int(self.dista_col2[num_line]) - 1):
        print(num_line-1)
        for i in range(int(num_line-1)):
            if distance_plus: 
                if (self.dista_col2[line_num+i+1]-self.dista_col2[line_num+i]<0):
                    print("changed at: $i")
                    print(line_num+i)
                    distance_plus = False
            else:
                if (self.dista_col2[line_num+i+1]-self.dista_col2[line_num+i]>0):
                    print("changed at: $i")
                    print(line_num+i)
                    distance_plus = True 


            
object = Class1()
object.split_file()
object.do_each_sweep()

