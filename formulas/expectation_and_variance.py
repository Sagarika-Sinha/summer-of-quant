#Expectation:Estimating returns and pricing
#Variance:Measures volatality
import numpy as np
def expectation(values,probs):
    return np.sum(np.array(values)*np.array(probs))
def variance(values,probs):
    avg=expectation(values,probs)
    return np.sum((np.array(values)-avg)**2*np.array(probs))
def std_deviation(values,probs):
    return np.sqrt(variance(values,probs))