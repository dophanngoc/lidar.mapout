#!/bin/bash

#Install packages
#sudo apt install python3-pip
#pip3 install pandas

#Map out to csv
python3 generate_map.py

#Check linear cordinate
#python3 optimize_map.py
sudo mv Mapping.csv output 
