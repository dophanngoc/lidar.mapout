#!/bin/python3
from csv import writer
import math
import pandas as pd

class MAP_OUT:
    def __init__(self):
        #create mapping file
        self.f_mapping = open("Mapping.csv","w").close() 
        #para of LIDARPoint.csv
        self.map_header = ['xstart', 'xend', 'ystart', 'yend']
        self.angle_col1 = []
        self.dista_col2 = []
        #para of FlightPath.csv
        self.x_fly_plan = []
        self.y_fly_plan = []
        #mapping
        self.x_start = []
        self.y_start = []
        self.x_end = []
        self.y_end =[]
        self.sweep_num = 1
        self.is_start_point = False 

    def handle_csv_file(self):
        #split Lidar point file
        with open("LIDARPoints.csv", "r+") as f:
            for elem in f.readlines():
                self.angle_col1.append(float(elem.split(",")[0]))
                self.dista_col2.append(float(elem.split(",")[1]))
        #cool flight path file
        with open("FlightPath.csv", "r+") as f:
            for elem in f.readlines():
                self.x_fly_plan.append(float(elem.split(",")[0]))
                self.y_fly_plan.append(float(elem.split(",")[1]))

    def do_each_sweep(self):
        line_num = 0
        for sweep_num in range(34):
            num_line =  int(self.dista_col2[line_num])
            #first angle scan
            check_first_angle = self.dista_col2[line_num+2] - self.dista_col2[line_num+1]
            if(check_first_angle > 0):
                is_distance_plus = True
            else:
                is_distance_plus = False
            #write sweep number to Mapp.csv
            self.to_map_file(sweep_num,1,1,1)
            #first start point
            self.x_start, self.y_start = self.position_cal(line_num+1) 
            self.single_sweep(num_line, line_num, is_distance_plus)
            line_num = line_num+num_line+1

    def single_sweep(self, num_line, line_num, is_distance_plus):
        for i in range(int(num_line-1)):
            dista_diff_pre = self.dista_col2[line_num+i+1]-self.dista_col2[line_num+i]
            if self.dista_col2[line_num+i] == 0:
                #print("propably way out!")
                if self.is_start_point:
                    self.is_start_point = False
                    self.cal_cordinate(line_num+i)
                continue
            if is_distance_plus: 
                if (dista_diff_pre<0):
                    self.cal_cordinate(line_num+i)
                    is_distance_plus = False
                    self.is_start_point = False
            else:
                if (dista_diff_pre>0):
                    self.cal_cordinate(line_num+i) 
                    is_distance_plus = True 
                    self.is_start_point = False 

    def position_cal(self, line_num):
        sin_of_angle = math.sin(math.radians(self.angle_col1[line_num])) 
        cos_of_angle = math.cos(math.radians(self.angle_col1[line_num]))
        coner_height = abs(sin_of_angle)*self.dista_col2[line_num] 
        coner_width = abs(cos_of_angle)*self.dista_col2[line_num]
        x_length = coner_height+self.y_fly_plan[self.sweep_num*2]*1000
        y_length = coner_width+self.x_fly_plan[self.sweep_num*2]*1000
        return x_length, y_length

    def cal_cordinate(self, line_num): 
        if self.is_start_point == False:
            self.x_end, self.y_end = self.position_cal(line_num+1)
            #Write cordinate to Mapping.csv 
            self.to_map_file(self.x_start, self.x_end, self.y_start, self.y_end)
            #assign next start point with previous stop point
            self.y_start = self.y_end 
            self.x_start = self.x_end 
            self.is_start_point = True

    def to_map_file(self, x_start, x_end, y_start, y_end):
        list_of_elem = [x_start, y_start, x_end, y_end]
        with open("Mapping.csv", 'a+', newline='') as write_obj:
            csv_writer = writer(write_obj)
            csv_writer.writerow(list_of_elem)


def main():
    mapout = MAP_OUT()
    mapout.handle_csv_file()
    mapout.do_each_sweep()

if __name__ == "__main__":
    main()

