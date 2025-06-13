#Itô’s Lemma is the stochastic calculus equivalent of the chain rule in regular calculus.
#asset prices don't follow straight paths, they evolve stochastically
#the following formula is derived by solving the SDE for GBM by using Ito's calculus
import matplotlib.pyplot as plt
import numpy as np
def simulate_gbm_paths(S0,mu,sigma,T,N,M):
    dt=T/N
    t=np.linspace(0,T,N)
    S=np.zeros((M,N))
    S[:,0]=S0
    for i in range(1,N):
         Z=np.random.standard_normal(M)
         S[:,i]=S[:,i-1]*np.exp((mu-0.5*sigma**2)*dt+sigma*np.sqrt(dt)*Z)
    return t,S
t,paths=simulate_gbm_paths(100,0.1,0.2,1,252,100)
plt.plot(t,paths.T,alpha=0.3)
plt.title("Simulated GBM Paths")
plt.xlabel("Time")
plt.ylabel("Asset Price")
plt.savefig("GBM Paths.png")

