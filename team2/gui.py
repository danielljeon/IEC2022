import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('../case/100+3.csv', sep=',', header=None)

# Make the first column the headers
df.columns = df.iloc[0] 
df = df.drop(0)

# Conver the X and Y columns to integers
df = df.astype({'x':'int', 'y':'int'})

# Setup X,Y and Patient count variables 
X = np.array(df['x'])
Y = np.array(df['y'])

PATIENT_COUNT = np.array(df['patient_count'])
SOLUTION = [X[0:10], Y[0:10]]

#
solArr = []
for i in range(len(X[0:10])):
    solArr.append([X[i],Y[i]])


fig = plt.figure(figsize=(20,20))
ax = fig.add_subplot()

plt.title("Solution Team #2", fontsize=40, color='orange')

# Setting so the graph crosses in the centre
ax.spines['left'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_color('none')

# Setting the 
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.yaxis.set_ticks(np.arange(int(min(Y)), int(max(Y)), 75))
ax.xaxis.set_ticks(np.arange(int(min(X)), int(max(X)), 75))

# Add the count to the points
for i, count in enumerate(PATIENT_COUNT):
    if df.iloc[i]['type'] == 'resupply':
        ax.text(X[i] + 0.3, Y[i] + 0.3, 'RESUPPLY')
    else:
        ax.text(X[i] + 0.3, Y[i] + 0.5, count)
ax.scatter(X,Y, label='Stops')


plt.plot(SOLUTION[0], SOLUTION[1], 'ro', linestyle=':', label='Solution')

for i, point in enumerate(solArr):
    ax.text(point[0], point[1] - 15, f'Stop #{i+1}')
    
plt.legend(loc='upper left')
plt.show()