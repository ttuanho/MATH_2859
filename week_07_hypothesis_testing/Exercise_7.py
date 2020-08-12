# By
# ████████╗██╗   ██╗ █████╗ ███╗   ██╗    ██╗  ██╗ ██████╗ 
# ╚══██╔══╝██║   ██║██╔══██╗████╗  ██║    ██║  ██║██╔═══██╗
#    ██║   ██║   ██║███████║██╔██╗ ██║    ███████║██║   ██║
#    ██║   ██║   ██║██╔══██║██║╚██╗██║    ██╔══██║██║   ██║
#    ██║   ╚██████╔╝██║  ██║██║ ╚████║    ██║  ██║╚██████╔╝
#    ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝ ╚═════╝ 

# Email: ttuan.ho@outlook.com                                                         


from scipy.stats import norm, binom, poisson, expon, uniform
from scipy import stats
import numpy as np
from scipy.stats import ttest_ind
import statsmodels.api as sm 
import pylab as py
"""
Ex
"""



"""
Ex3:
Consider again the astronaut exercise (Exercise 4) from the week 5 exercises. The change in heart
rate (in beats per minute) is as follows:
15 32.5 49 26 8 28
a) Is there evidence that astronaut pulse rate has in fact increased under simulated weightlessness? Use a hypothesis test to answer this question, via Matlab’s ttest function.
b) Is this consistent with your results from last week?
c) Produce a normal quantile plot of the data. How reasonable is the normality assumption for these
data?
"""
data=np.array([15,32.5,49,26,8,28])
n = len(data)
zeros = np.zeros((n,))
m = np.mean(data)
s = np.std(data, ddof=1)

# % matlab version:
# [h,p] = ttest(data, 0,'tail', 'right');p

# stat, p = ttest_ind(data, zeros)
# print('t=%.3f, p=%.3f' % (stat, p))

tObs = (m - 0) / (s / ((n)**(1/2)))
# % matlab version:
# pValue = tcdf(t,n-1)
# pValue in python
pValue = stats.t.sf(tObs, n-1)
print(f"p-Value is {pValue}")

# produce qqplot of data
# % matlab version:
# qqplot(data)
sm.qqplot(data)
py.show()

