#Moment generating functions:encodes all moments like mean,variance etc. Used in deriving distributions and pricing
import numpy as np
def mgf(values,probs,t):
    values=np.array(values)
    probs=np.arraty(probs)
    return np.sum(np.exp(t*values)*probs)
#first derivative of mgf gives expectation of x
def first_moment_mgf(values,probs):
    from scipy.misc import derivative
    return derivative(lambda t:mgf(values,probs,t),0.0,dx=1e-6)
#second derivatve of mgf gives expectation of x**2
def second_moment_mgf(values,probs):
    from scipy.misc import derivative
    return derivative(lambda t:mgf(values,probs,t),0.0,dx=1e-6,n=2)
