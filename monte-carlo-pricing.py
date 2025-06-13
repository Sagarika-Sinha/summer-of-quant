import numpy as np
#monte carlo simulation is used when analytic solution doesn't exist
def monte_carlo_call(S0,K,T,r,sigma,n_paths=10000):
    np.random.seed(42)
    Z=np.random.standard_normal(n_paths)
    ST=S0*np.exp((r-0.5*sigma**2)*T+sigma*np.sqrt(T)*Z)
    payoff=np.maximum(ST-K,0)
    return np.exp(-r*T)*np.mean(payoff)
print("Monte Carlo Call Price",monte_carlo_call(100,110,1,0.5,0.2))