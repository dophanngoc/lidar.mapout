#!/bin/python3

import pandas as pd

fightpath = pd.read_csv('FlightPath.csv')
df = pd.read_csv('LIDARPoints.csv')

print(df)
df['y'] = 0

for i in range(10): 
    df['y'].iloc[i] = df['533'].iloc[i]
#distance =  senspoint.iloc[:,2]
#print(distance)
#for row in range(10):
#   row = [float(val) for val in row]
    
