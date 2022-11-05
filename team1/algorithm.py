
import matplotlib.pyplot as plt
import pandas as pd
import random

import math

def euclidean_distance(x1,x2,y1,y2):
    return math.dist([x1, y1], [x2, y2])

df = pd.read_csv("1000+10.csv")
print (df)

#Idea Simulated Annealing

#BACK BURNER OPTION

def simulate(init_state, df):
    initial_temp = 1000
    final_temp = 1
    decrement = 1

    current_temp = initial_temp

    while current_temp > final_temp:
        #Choose a neighbour
        neighbor = get_rand_neighbour(df, random.randint(1,100))

        # Check if neighbor is best so far
        cost_diff = get_cost(df.loc[0], df.loc[1])

        # print(current_temp)

        current_temp -= decrement

def get_cost(entry, neighbour):

    euclidean_weight = euclidean_distance(
        entry["x"] , neighbour["x"] , entry["y"] , neighbour["y"]
    )

    patient_weight = neighbour["patient_count"]

    return (patient_weight / euclidean_weight)

    #Pandas data entry:
    return
    raise NotImplementedError


visited = []

def find_nearest_neighbour(entry, data, is_resupply):

    #Euclidean distance, index
    best_neighbour = [0, 0]

    for index, row in data.iterrows():
        euclidean_weight = euclidean_distance(
        entry["x"] , row["x"] , entry["y"] , row["y"]
        )

        if(index == entry["index"]):
            continue
         
        if( (euclidean_weight < best_neighbour[0] or best_neighbour[0] == 0) and index not in visited):

            if(is_resupply is True and row["type"] == "resupply"):
                best_neighbour = [euclidean_weight, index]

            if(is_resupply is False and row["type"] == "village"):
                best_neighbour = [euclidean_weight, index]

    return best_neighbour       


edge_list = []

def nearest_algo(data, initial_index, max_gas, gas):

    edge_entry = [initial_index]

    print("ITERATION START GAS: "+str(gas))
    print(len(visited))

    gas_constant = 0.6
    gas_threshold = gas_constant*max_gas

    #If we need gas
    if(gas < gas_threshold):

        closest = find_nearest_neighbour(
            data.loc[initial_index], data, True
        )

        gas = max_gas

        # edge_entry.append(closest[1])
        # edge_list.append(edge_entry)

        nearest_algo(data, closest[1], max_gas, gas )

    #If we don't need gas, and can go to a village
    else:
        closest = find_nearest_neighbour(
                data.loc[initial_index] ,  data , False
        )

        #Do I have enough gas to go here?
        gas_spent = gas - closest[0]

        visited.append(closest[1])

        if( gas_spent > 0):

            nearest_algo(data, closest[1], max_gas, gas_spent )

    edge_entry.append(closest[1])
    edge_list.append(edge_entry)



def get_edge_list(data_title, initial_position, max_gas, gas):

    df = pd.read_csv(data_title)
    try:
        nearest_algo(df, initial_position, max_gas, gas)
    except RecursionError as err:
        print("OUT OF RAM BOYO")
        return edge_list

    return edge_list
