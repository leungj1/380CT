from random import randint, sample
from itertools import chain, combinations
from time import time
import time

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

    def dynamicProgramming(self):
        if self.t < 0 or self.t > sum (self.S): # T = sum(S)
          return False

        sub_sum = [False] * (self.t + 1 )
        sub_sum[0] = True
        d = 0
        while not sub_sum[self.t] and d < self.n:
          a = self.S[d]
          p = self.t
          while not sub_sum[self.t] and p >= a:
            if not sub_sum[p] and sub_sum[p - a]:
              sub_sum[p] = True
            p -= 1
          d += 1
        return sub_sum[self.t]

for n in range(10,20):
    start_time = time.time()
    instance = SSP()
    instance.random_yes_instance(n)
    instance.dynamicProgramming()
    print (instance.dynamicProgramming())
    for i in range(1):
        print("%d\t%6f" % (n,(time.time() - start_time)/100))
print ("----------------------------------------------------")
print (instance.dynamicProgramming())
print("--- %s seconds ---" % (time.time() - start_time))
