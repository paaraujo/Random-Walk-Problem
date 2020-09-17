import numpy as np
from math import sqrt 

#initial_point = [0,0]
def run(samples):
    # initialization
    size = 1000000000 # 1 billion - IMPORTANT! Check your available memory
    cycles = samples // size
    remain = samples % size
    # running cycles
    finalX = finalY = 0
    for i in range(cycles):
        directions = np.random.rand(size,1) * 2*np.pi 
        finalX  += np.sum(np.cos(directions))
        finalY  += np.sum(np.sin(directions))
    # running remain
    directions = np.random.rand(remain,1) * 2*np.pi 
    finalX  += np.sum(np.cos(directions))
    finalY  += np.sum(np.sin(directions))
    # returning euclidean distance from the origin [0,0]
    return sqrt(pow(finalX,2) + pow(finalY,2))

# main loop
N = [pow(10,10)] # 100 billions
stat = np.zeros(len(N))
for j, n in enumerate(N):
    stat[j] = run(n)
    
dN = np.sqrt(N)
print("Square(s) of N: ",dN)
print("Simulated distance(s): ", stat)