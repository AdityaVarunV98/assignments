import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
#import seaborn as sns

#Number of rolls
n =  4

#Probability of a doublet
p = 1/6

#k is the possible values of the doublets
k_values = list(range(n+1))

#y gives the probability values for each of the values of k
y = [binom.pmf(k,n,p) for k in k_values]

print(y[2])   #printing the probability of the number of doublets being 2

