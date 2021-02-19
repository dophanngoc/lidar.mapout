#!/bin/python3

import pandas as pd

xstart = 1    
ystart = 1
xend = 2
yend = 2

fightpath = pd.read_csv('FlightPath.csv')
senspoint = pd.read_csv('LIDARPoints.csv')
mapping = pd.read_csv('Mapping.csv', sep=',', encoding="utf-8")

fightpath.head()
senspoint.head()
mapping.head()
row = [xstart, ystart, xend, yend]
mapping.loc[mapping.index.max()+1] = [xstart, ystart, xend, yend]
mapping.to_csv("map.csv", index=False)
