import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
#import seaborn as sns

#Number of tosses
n =  20

#Probability of a head
p = 1/2

#Simulating the probability using the binomial random variable

simlen = 100000

data_binom = binom.rvs(n,p,size=simlen) #Simulating the event of tossing a coin 20 times and noting the number of heads

fav_count = np.count_nonzero(data_binom >= 12)  #Finding the number of times there are at least 12 heads in the simulation data

print(fav_count/simlen)  #printing the probability of answering at least 12 questions correctly out of 20
