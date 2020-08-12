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

"""
Ex2
"""

data = np.array([15.2,14.2,14.0,12.2,14.4,12.5,14.3,14.2,13.5,11.8,15.2])
# a) Construct a 99% two-sided confidence interval on the mean temperature.
# % matlab verson:
# tCrit=tinv(0.995,10)
tCrit = stats.t.ppf(0.995,10)

# interval  is :
np.mean(data) + np.std(data) / ((len(data))**(1/2)) * tCrit * np.array([-1,1])


# c) Suppose that we wanted to be 95% confident that the error in estimating the mean temperature is
# less than 0.4°C. What sample size should be used?
# % matlab verson:
# tStar = tinv(0.975,10)
# s / sqrt(n) * tStar < 0.4

"""
Ex3:
The wall thickness of 25 glass 2-litre bottles was measured by a quality-control engineer. 
The sample mean was m = 4.05 millimetres, and the sample standard deviation was s = 0.08 
millimetre. Find a 95% lower confidence bound for mean wall thickness. Interpret the interval 
you have obtained. Assume the normal distribution for wall thickness.
"""

m = 4.05
n = 25
alpha = 0.05
s = 0.08

tStar = stats.t.ppf(0.95,n-1)

# The lower bound is:
float(m) - s / ((float(n))**(1/2)) * tStar

"""
Ex6:
The article “Repeatability and Reproducibility for Pass/Fail data” (J. of Testing and Eval., 1997, 
151-153) reported that in n = 48 trials in a particular laboratory, 16 resulted in ignition of a 
particular type of substrate by a lighted cigarette. Find a 95% approximate confidence interval for 
π, the true long-run proportion (or probability) of all such trials that would result in ignition.
"""
n = float(48)
k = float(16)
pHat = 16/48

print(f"Checking if the the sample is large enough:")
print(f"n*pHat*(1-pHat)>5={n*pHat*(1-pHat)>5}")

# tStar = norm.ppf(0.975)
tStar = 1.96
print(f"95% CI for pi:")
res = pHat + (tStar * ((pHat*(1-pHat)/n)**(1/2)) * np.array([-1,1]))
print(f"{res}")


