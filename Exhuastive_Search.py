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

    def Exhaustive_Search(self):
      #declare the function Exhaustive Search
       subset =  self.getSubset()
       total = 0
       #calls the function getSubsets to generate all the subsets for the initial set and return the subsets
       for set in subsets:
           #loop through every set of the subsets
           total = sum(set)
            #set the total to equal the sum of the current set
           print("Trying: ", set, ", sum:", total )
           #print the set that is currently being tested
           if (total == self.t):
            #if the total does not match the value of t which is the target value then solution has been found
              print("Solution: " +str(set))
              #print the solution out
              return Trues
            
instance = SSP()  #instance equals the SSP class
instance.random_yes_instance(4)
instance.Exhaustive_Search()
print( instance )

