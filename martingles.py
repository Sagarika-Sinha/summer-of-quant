#martingle property:best prediction of the future is the present-no trend or drift
#expected gain/loss is zero
#basically, expected future value is simply the current value hence the graph shown below appears trendless
#to show wt**2-t is a martingle:
import matplotlib.pyplot as plt
import numpy as np
T=1
dt=0.01
N=int(T/dt)
t=np.linspace(0,T,N)
dw=np.sqrt(dt)*np.random.randn(N)
W=np.cumsum(dw)
M=W**2-T
plt.plot(t,M)
plt.title("Martingle")
plt.xlabel("Time")
plt.ylabel("$W_t^2-t$")
plt.savefig("plot3.png")
