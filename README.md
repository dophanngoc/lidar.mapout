# Introduction

The goal of this project was to use given Flight Plan and data scan of Lidar sensor 
, which rotate 360 degree in 1D dimension to map out dimension of the room.
The LIDARPoint.csv show angle and distances of multiple sweeps and FlightPlan show location
of sensor at correscponding sweep.

# Idea

Notice that whenever sensor scan through corner of wall, the distance change the linear state
Based that point and apply 1D basic geometric knowledge, we can exacly determine the cordinate of wall corner  relatively.
 
# Run
Dev enviroment: Ubuntu 20.04.2.0 LTS

```
chmod +x run.sh
./run.sh
```
Check output:

```
ls output/Mapping.csv
```
# Project Organization
    
    ├── LICENSE            <- Open Source AF 
    ├── README.md          <- You're reading it
    │
    ├── output /           <- Data output directory
    │   └── Mapping.csv    <- The dimension of room 
    │
    │
    ├── test_function /    <- Source code for test funtions in this project
    |
    ├── run.sh             <- main program, run this on Unix system 
    ├── generate.py        <- Source code to generate map dimension csv file
    ├── FlightPlan.csv     <- File describes drone flight plan 
    └── LIDARPoint.csv     <- File describes data output after n sweeps scan

