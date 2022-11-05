import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from algorithm import get_edge_list

import sys
print(sys.setrecursionlimit(100000000))

# CONSTANTS

FILE_CSV = "100+3.csv"
INIT_POSITION = 0
MAX_GAS =  800
INIT_GAS = 800


df = pd.read_csv(FILE_CSV) #create dataframe
#intialize coordinate arrays x,y for villages and resupplys
matplot_x = []
matplot_y = []
matplot_x_resup =[]
matplot_y_resup =[]

edgeList = get_edge_list(FILE_CSV, INIT_POSITION, MAX_GAS, INIT_GAS)

#iterate through rows of dataframe and append coordinates to array
for index , rows in df.iterrows():

    if rows[4] != 0:
        matplot_x.append(rows[1])
        matplot_y.append(rows[2])
    else:
        matplot_x_resup.append(rows[1])
        matplot_y_resup.append(rows[2])

#print the scatter plot using the given arrays
plt.scatter(matplot_x, matplot_y, color = 'blue')
plt.scatter(matplot_x_resup, matplot_y_resup, color = 'red')

#take the master edge list from the algorithm and draw the path it takes.
for toplist in edgeList:

    x1 = df.iloc[toplist[0], 1]
    y1 = df.iloc[toplist[0], 2]

    x2 = df.iloc[toplist[1], 1]
    y2 = df.iloc[toplist[1], 2]

    x = [x1,x2]
    y = [y1,y2]
    plt.plot(x,y)
    
        
        
plt.show()

fromNodes = []
toNodes =[]
for list in edgeList:
    fromNodes.append(list[0])
    toNodes.append(list[1])

finalData = {'From':fromNodes, 'To':toNodes}

dataframe = pd.DataFrame(data=finalData)
dataframe.to_csv('team1_'+FILE_CSV)