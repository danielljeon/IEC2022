# Internal Engineering Competition 2022 | Programming

## Competition Information

- IEC 2022 Programming Competitor’s
  Package: [Google Doc](https://docs.google.com/document/d/1a5tQoRyLkcyT6mQJk7dbhZ7-1skbybjSj0k-wlDEmvE/edit?usp=sharing)
  .

- Test cases and Code can be found in the `case` directory in this repo.

- `case/test_case_generator.py` is used to generate test cases.

- `case/result_evaluator.py` is used to evaluate solutions submitted by each
  individual team.

- `case/requirements.txt` is specifically imports packages used
  in `case/test_case_generator.py`.

## Problem
The goal of this challenge is to determine the best route for a mobile hospital visiting villages in order to serve the most patients possible given a constrained travel distance. The challenge's second goal is to use a GUI to graphically depict the path.

## Solution

We use the pandas library in python in order to iterate over the test dataset that has been provided to us. Our initial steps is to create a dictionary where the index of the dictionary corresponds to an index in the dataset. 

Brute force method has been used in order to find the most optimal solution. Each village is represented as a node on a 2-d plane sicne the x,y coordinates have already been provided to us in the dataset. 

Our algorithmn uses the euclidean distances of the nodes added to our chosen data structure and finds the shortest distance between the current node and the next availiable node.
The path created is dependent on ensuring the mobile hospital uses the shortest possible distance.

Once the mobile hospital runs out of the available distance, the mobile hospital tries to find the nearest resupply unit and the distance is restored to 0. 


## Issues
One of the main issues we ran into was determining which next available node should be visted. Depending on the start node our algorithm needs to find all possible distances to neighbouring node. One improvement we could have implemented in our code would have been to come up with a range of distances to determine if taking a longer path would have helped more patients.
