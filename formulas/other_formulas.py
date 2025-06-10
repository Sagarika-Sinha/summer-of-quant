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

