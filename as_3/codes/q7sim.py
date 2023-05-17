import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom

#Number of tosses
n =  20

#Probability of a head
p = 1/2



#Simulating the probability using the binomial random variable

simlen = 100000

data_binom = binom.rvs(n,p,size=simlen) #Simulating the event of tossing a coin 20 times and noting the number of heads

fav_count = np.count_nonzero(data_binom >= 12)  #Finding the number of times there are at least 12 heads in the simulation data

print(fav_count/simlen)  #printing the probability of answering at least 12 questions correctly out of 20




#Simulating random variable using Gaussian distribution

data = np.random.normal(loc=n*p, scale=2.2360679775, size=simlen)   #generate sample of 100000 values that follow a normal distribution

fav_count = np.count_nonzero(data >= 11.5)  #Finding the number of times there are at least 12 heads in the simulation data (0.5 to account for the error)

print(fav_count/simlen)  #printing the probability of answering at least 12 questions correctly out of 20

