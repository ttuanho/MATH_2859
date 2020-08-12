# By
# ████████╗██╗   ██╗ █████╗ ███╗   ██╗    ██╗  ██╗ ██████╗ 
# ╚══██╔══╝██║   ██║██╔══██╗████╗  ██║    ██║  ██║██╔═══██╗
#    ██║   ██║   ██║███████║██╔██╗ ██║    ███████║██║   ██║
#    ██║   ██║   ██║██╔══██║██║╚██╗██║    ██╔══██║██║   ██║
#    ██║   ╚██████╔╝██║  ██║██║ ╚████║    ██║  ██║╚██████╔╝
#    ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝ ╚═════╝ 

# Email: ttuan.ho@outlook.com                                                         


from scipy.stats import norm, binom, poisson, expon, uniform
import numpy as np

"""
Ex4
"""

# % matlab version:
# binomcdf(1,6,0.5)
binom.cdf(1,6,0.5)

# % matlab version:
# poisscdf(1,6,0.5)
poisson.cdf(1,3)

"""
Ex5
"""
# % matlab version:
# 1 - normcdf(0.29)
# 1 - normcdf(100,96,14)
1 - norm.cdf(0.29)
1 - norm.cdf(100,96,14)

# % matlab version:
# normcdf(80,96,14)-normcdf(50,96,14)
norm.cdf(80,96,14)-norm.cdf(50,96,14)

# % matlab version:
# norminv(0.95)
norm.ppf(0.95)

# Interval that gives 90% = [mean +- sd * tinv(prob+(1-prob)/2)]
96 + 14 * norm.ppf(0.95) * np.array([-1, 1])



