import numpy as np
from scipy.stats import norm
def black_scholes_call(S,K,T,r,sigma):
    d1=(np.log(S/K)+(r+0.5*sigma**2)*T)/(sigma*np.sqrt(T))
    d2=d1-sigma*np.sqrt(T)
    call_price=S*norm.cdf(d1)-K*np.exp(-r*T)*norm.cdf(d2)
    return call_price
s=100
k=110
t=1
r=0.05
sigma=0.2
print("call option price:",black_scholes_call(s,k,t,r,sigma))