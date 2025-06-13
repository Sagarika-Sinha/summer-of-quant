#ou process:is used to model interest rates and volatality
import numpy as np
import matplotlib.pyplot as plt
def ornstein_uhlenbeck(x0,mu,theta,sigma,T,N):
    dt=T/N
    X=np.zeros(N)
    X[0]=x0
    for i in range(1,N):
        dw=np.random.normal(0,np.sqrt(dt))
        X[i]=X[i-1]+theta*(mu-X[i-1])*dt+sigma*dw
    return X
X_ou=ornstein_uhlenbeck(1.0,0.0,0.7,0.2,1,1000)
plt.plot(X_ou)
plt.title("OU Process")
plt.xlabel("Steps")
plt.ylabel("X(t)")
plt.savefig("OU.png")