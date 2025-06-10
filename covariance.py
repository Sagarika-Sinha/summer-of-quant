#Covariance:Portfolio diversification
import numpy as np
from expectation_and_variance import *
def covariance(xvalues,yvalues,probs):
    x=np.array(xvalues)
    y=np.array(yvalues)
    px=np.sum(probs,axis=1)
    py=np.sum(probs,axis=0)
    ex=np.sum(x*px)
    ey=np.sum(y*py)
    cov=0
    for i in range(len(x)):
        for j in range(len(y)):
            cov+=(x[i]-ex)*(y[j]-ey)*probs[i][j]
    return cov
def correlation(xvalues,yvalues,probs):
    cov=covariance(xvalues,yvalues,probs)
    varx=variance(xvalues,np.sum(probs,axis=1))
    vary=variance(yvalues,np.sum(probs,axs=0))
    return cov/(np.sqrt(varx)*np.sqrt(vary))