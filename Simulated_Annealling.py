from random import randint, sample
import random
import itertools
from time import time
import math
import sys
#pip install numpy on pip folder from the python folder (shift right click to open command prompt)
#python-> script-> pip
import numpy as np
#uncomment this code to print full matrix rather than the abbreviated one
# np.set_printoptions(threshold=np.nan)
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

    def AcceptanceProbs(self, new, old, temp): 
        if new or old is not None: 
            if (new < old): # if new is less than old
                return 1.0
            else:
                return math.exp((old-new)/temp) # return e**x of (the old - new divide by temp)
        else:
            return 0

    def Neigh_solution(self, set = []): #declare the function
        if len(set) != 0: # if the legth of the set doesn't equal to 0
            randPosSet = randint(0, len(set)) #randPosSet equals zero of random instance
            #and the length of the set of the random instance
            randPosSet1 = randint(0, len(set)-1) #randPosSet1 equals zero of random instance
            # and length of the set minus 1 of the random instance
            set_1 = list(set)           
            if len(self.S) == len(set_1):# if lenght of S equals the lenght of set1
                print ("No Neighbouring Solution")
            else:
                for i in range(0, self.n): #for loop in range 0 and the legnth of S
                    if self.S[i] in set_1: # i value of S in set1
                        randPosSet = randint(0, len(set)) #randPosSet equals
                        #zero random instance and the lenght of the set of random instance
                    else:
                        set_1[randPosSet1] = self.S[i] 
                        break

            return set1 # return set1
        
    def Cal_Cost(self,set):
        if not set:
            return
        else:   
            return sum(set)

def Simulted_Annealing(self):
        solution = self.greedy_algorithm() #solution equals greedy_algorithm
        prev_cost = self.Cal_Cost(solution) # previous cost = solution of calculate cost
        Temp = 1.0 
        TempMin = 0.00001
        alpha = 0.09
        if len(solution) == 0: #if the length of the solution is equal to 0
            return True # return true
        while Temp > TempMin: # while the temperature is greater the the minimum temperature
            i = 1 # i equals to 1
            while i <= 3: # while i is less than or equals to 3
                solution1 = self.Neigh_solution(solution) # solution 1 equals solution
                #neightbouring solution
                print("Initial Solution: " +str(solution) + " Cost: " + str(previous_cost))
                # print statement
                new_cost = self.Cal_Cost(solution1)# new cost equals solution 1 of calculated cost
                print("Neighbouring Solution: " +str(solution1)  + " Cost: " + str(new_cost))
                #print statement
                ap = self.AcceptanceProbs(prev_cost, new_cost,Temp)
                #ap equals 
                if ap > random and sum(solution1) <= self.t: #if ap is less than random and
                    # sum of solution 1 is less than and equals to t
                    solution = list(solution1) # solution equals to the list of solution 1
                    prev_cost = new_cost # previous cost equals new cost
                i = i + 1 #i = i plus 1
            Temp = Temp*alpha # Temp equals Temp times alpha
        return solution

instance = SSP() #generate instance of SSP Class and initialise
instance.random_yes_instance(4)
print(instance)
instance.try_at_random()
print("Solution: " +str(instance.sim_anneal()))
instance.greedy_algorithm()
