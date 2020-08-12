# By
# ████████╗██╗   ██╗ █████╗ ███╗   ██╗    ██╗  ██╗ ██████╗ 
# ╚══██╔══╝██║   ██║██╔══██╗████╗  ██║    ██║  ██║██╔═══██╗
#    ██║   ██║   ██║███████║██╔██╗ ██║    ███████║██║   ██║
#    ██║   ██║   ██║██╔══██║██║╚██╗██║    ██╔══██║██║   ██║
#    ██║   ╚██████╔╝██║  ██║██║ ╚████║    ██║  ██║╚██████╔╝
#    ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝ ╚═════╝ 

# Email: ttuan.ho@outlook.com                                                         

import scipy.stats

"""
Ex2 
"""

# %  matlab version:
# f = finv(0.95, 5, 60)
fValue = scipy.stats.f.isf(0.95, 5, 60)

# %  matlab version:
# p_value = 1 - fcdf(F, df1, df2)
# python version:
# p_value = 1 - scipy.stats.f.cdf(F, df1, df2)
p_value = 1 - scipy.stats.f.cdf(4.2, 5, 60)

"""
Ex3
"""



"""
Ex4
"""
# % matlab version:
# stressMod = fitlm(Group, Rate, 'CategoricalVars',[1]);
# anova(stressMod)



"""
Ex5
"""




