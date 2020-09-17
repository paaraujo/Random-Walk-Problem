import numpy as np

#initial_point = [0,0]
def run(steps):
    # initialization
    numExp = 10000000
    directions = np.random.rand(steps,numExp) * 2*np.pi 
    Xs = np.sum(np.cos(directions),axis=0)
    Ys = np.sum(np.sin(directions),axis=0)
    dN2 = np.mean(np.square(Xs) + np.square(Ys))
    dN_  = np.sqrt(dN2)
    dN = np.mean(np.sqrt(np.square(Xs) + np.square(Ys)))
    return [dN2,dN_,dN]

# main loop
N = [5,10,15,20,25] # number of steps

stat = np.zeros(len(N))
for i,n in enumerate(N):
    print('N =',N[i],' [dN2, sqrt(dN2), dN] =',run(n))