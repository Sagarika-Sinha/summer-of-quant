#skewness:measures asymmetry
from expectation_and_variance import *
import numpy as np
def skewness(values,probs):
    avg=expected_value(values,probs)
    sigma=std_deviation(values,probs)
    return np.sum(((np.array(values)-avg)**3)*probs)/sigma**3
#kurtosis:measures tail risk
def kurtosis(values,probs): 
    avg=expected_value(values,probs)
    sigma=std_deviation(values,probs)
    return np.sum(((np.array(values)-avg)**4)*probs)/sigma**4
def portfolio_variance(w1,w2,var1,var2,cov):     #measure of volatality
    return w1**2*var1+w2**2*var2+2*w1*w2*cov     #w is the weight of the asset
#Markov's inequality:risk management by giving an upper bond on large losses
def markov_inequality(E,a):
    return E/a
#Chebyshev's inequality:useful when variance is known but distribution is unknown
def chebyshev_bound(k):
    return 1/(k**2)
#Law of large numbers:empirical average converges to expected return as data size increases
#Central Limit Theorem justifies normal approximation even if original data is not normal