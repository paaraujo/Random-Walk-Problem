import matplotlib.pyplot as plt
from random import random
from math   import sin, cos, pi, sqrt 

N = 100
initial_point = [0,0]
last_point = initial_point

for i in range(N):
    direc = random() * 2 * pi
    curr_point = [last_point[0]+cos(direc),last_point[1]+sin(direc)]
    plt.plot([last_point[0],curr_point[0]],[last_point[1],curr_point[1]])#'b'
    last_point = curr_point

plt.show()
print("Square of N: ",sqrt(N))
print("Simulated distance: ", sqrt(pow(initial_point[0]-last_point[0],2)+pow(initial_point[1]-last_point[1],2)))