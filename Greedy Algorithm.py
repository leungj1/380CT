from random import randint, sample
import random
import itertools
from time import time
import math
import sys
import numpy as np #pip install numpy 
class SSP():
# Declare the class
    def __init__(self, S=[], t=0):
# Initiation
        self.S = S
# s is an array
        self.t = t
# t is 0
        self.n = len(S)
# n is the length of s
        #
        self.decision = False
#the decision is false
        self.total    = 0
#total is 0
        self.selected = []
# the selected is s

    def __repr__(self):
# return a printable representation of the object
        return "SSP instance: S="+str(self.S)+"\tt="+str(self.t)
    
    def random_instance(self, n, bitlength=10):
        max_n_bit_number = 2**bitlength-1
# maximum bit number is the bitlength square - 1
        self.S = sorted( [ randint(0,max_n_bit_number) for i in range(n) ] , reverse=True)
        # s is sorted in a forloop in range of n and it is beiween the number of 0 to the maximum bit number
        self.t = randint(0,n*max_n_bit_number)
# t is either 0 or n x the maximum bit number
        self.n = len( self.S )
#n is the lenght of s

    def random_yes_instance(self, n, bitlength=10):
        max_n_bit_number = 2**bitlength-1
# maximum bit number is the bitlength square - 1
        self.S = sorted( [ randint(0,max_n_bit_number) for i in range(n) ] , reverse=True)
        # s is sorted in a forloop in range of n and it is beiween the number of 0 to the maximum bit number
        self.t = sum( sample(self.S, randint(0,n)) )
# t is the sum of s or the random instances 0 or n
        self.n = len( self.S )
#n is the lenght of s

    ###

    def try_at_random(self):
        candidate = []
# candidate is an array
        total = 0
# total is 0
        while total != self.t:
# while total doesn't equal to t
            candidate = sample(self.S, randint(0,self.n))
# candidate equals to the 
            total     = sum(candidate)
# total equals to the sum x candidate
            print( "Trying: ", candidate, ", sum:", total )
# print statement

    def greedy_algorithm(self):
        total = 0 #0 equals to total
        subsets = [] #subset equals empty array
        for i in range(0, len(self.S)): # for loop in the range of 0 and the length of S
            if (sum(subsets) + self.S[i]<= self.t): # sum of the subsets plus the i value of the array S less than or equals to t
                subsets.append(self.S[i]) #subsets read the i value of the array S
                total = total + self.S[i] #total equals total plus i value of the array S
            else:
                print(total-self.t) #otherwise print the total - t
                break
        return subsets
    
    def getSubset(self):
        results = [] # result equals empty array 
        for i in range(0,len(self.S)+1): #for loop between the 0 and (the length of the array S) +1
            results += itertools.combinations(self.S,i)#use combinatorics to find all
            #possible non repeated subsets of the array            
        return results # return results

instance = SSP() #instance equals to SSP class
instance.random_yes_instance(4)
print( instance )
instance.greedy_algorithm()

      
