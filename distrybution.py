# import matplotlib.pyplot as plt
# import numpy as np
# import scipy.stats as stats
# import math
# from numpy import random
# import seaborn as sns
#
#
# mu = 30
# variance = 2
# sigma = math.sqrt(variance)
# x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
# plt.plot(x, stats.norm.pdf(x, mu, sigma))
# plt.ylabel('Density')
# plt.xlabel('Mean delivery time')
# plt.show()
#
#
# def draw_z_score(x, cond, mu, sigma, title):
#     y = stats.norm.pdf(x, mu, sigma)
#     z = x[cond]
#     plt.plot(x, y)
#     plt.fill_between(z, 0, stats.norm.pdf(z, mu, sigma))
#     plt.title(title)
#     plt.show()
#
# x = np.arange(-3, 3, 0.001)
# z0 = -0.75
# draw_z_score(x, x<z0, 0, 1, 'z<-0.75')

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.poisson(lam=50, size=1000), hist=True, label='poisson')
plt.show()
