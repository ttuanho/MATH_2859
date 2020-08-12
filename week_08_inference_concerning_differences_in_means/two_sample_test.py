# By
# ████████╗██╗   ██╗ █████╗ ███╗   ██╗    ██╗  ██╗ ██████╗ 
# ╚══██╔══╝██║   ██║██╔══██╗████╗  ██║    ██║  ██║██╔═══██╗
#    ██║   ██║   ██║███████║██╔██╗ ██║    ███████║██║   ██║
#    ██║   ██║   ██║██╔══██║██║╚██╗██║    ██╔══██║██║   ██║
#    ██║   ╚██████╔╝██║  ██║██║ ╚████║    ██║  ██║╚██████╔╝
#    ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝ ╚═════╝ 

# Email: ttuan.ho@outlook.com                                                         


# Does whether or not you are doing a double degree affect how much sleep you get? 
# Use the class data 𝚑𝚘𝚞𝚛𝚜𝚂𝚕𝚎𝚙𝚝.𝚌𝚜𝚟 to test this hypothesis.
import pandas as pd
import statistics
import scipy
import numpy as np
from scipy import stats

data = pd.read_csv("../datasets/hoursSlept.csv")
print(f"{data}")
print(f"{data.info()}")
data1 = [float(i) for i in data['sleep'].tolist()]
dd = data['doubleDegree'].tolist()
data2 = []
for di in dd:
    if (di == 'Yes'):
        data2.append(float(1)) 
    else:
        data2.append(float(0)) 

n1 = len(data1)
n2 = len(data2)
m1 = statistics.mean(data1)
m2 = statistics.mean(data2)
s1 = np.std(data1)
s2 = np.std(data2)
sp2= ( ((n1-1)*s1**2+(n2-1)*s2**2) / (n1 + n2 - 2) ) ** (1/2)

# test stats #
t = (m1 - m2) / sp2 / ((1/n1 + 1/n2) ** (1/2))
print(f"t-statistics={t}")

# % matlab version:
# pValue = tcdf(t,n1+n2-2)

pValue = stats.t.sf(t,n1+n2-2)
print(f"pValue={pValue}")

