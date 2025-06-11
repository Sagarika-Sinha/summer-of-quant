#brownian motion:starts at 0---increment is independent of the past---coninuous
#increment is gaussian---normal distribution with mean 0 and variance=time increment
#mean=0---variance is time increment--covariance(w(t),w(s))=min(t,s)---non differentiable as path is jagged everywhere
#its a markov process
import numpy as np
import matplotlib.pyplot as plt
t=1
n=500
dt=t/n
timeaxis=np.linspace(0,t,n)
dw=np.sqrt(dt)*np.random.randn(n)
w=np.cumsum(dw)        #since
plt.plot(timeaxis,w)
plt.title("Simulated Brownian Motion")
plt.xlabel("Time")
plt.ylabel("W(t)")
plt.savefig("graph2.png")
