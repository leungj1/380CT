from random import randint, sample
import random
import itertools
from time import time
import time
import math
import sys
#pip install numpy on pip folder from the python folder (shift right click to open command prompt)
#python-> script-> pip
import numpy as np
#uncomment this code to print full matrix rather than the abbreviated one
# np.set_printoptions(threshold=np.nan)
class SSP():
    #initializing the SSP object
    def __init__(self, S=[], t=0):
        self.S = S #empty set to  start with
        self.t = t #target set to 0 initially
        self.n = len(S) #length of the set (i.e. number of elements)
        #
        self.decision = False 
        self.total    = 0
        self.selected = [] #empty set for the selected subset
    def __repr__(self):
        return "SSP instance: S="+str(self.S)+"\tt="+str(self.t)
    
    def random_instance(self, n, bitlength=10):
        max_n_bit_number = 2**bitlength-1
        self.S = sorted( [ randint(0,max_n_bit_number) for i in range(n) ] , reverse=True)
        self.t = randint(0,n*max_n_bit_number)
        self.n = len( self.S )
    #generate random SSP instance which will generate a solution
    def random_yes_instance(self, n, bitlength=10):
        max_n_bit_number = 2**bitlength-1
        #generate a random set of integers of length n
        #and store as reverse sorted
        self.S = sorted( [ randint(0,max_n_bit_number) for i in range(n) ] , reverse=False)
        #set the target value to the sum of a sample subset of the set
        #where the length of the sample set is a randint between 0 and n (4)
        self.t = sum( sample(self.S, randint(0,n)) )
        #set n property of object to length of the set 
        self.n = len( self.S )
        
    #try generating a solution randomly (greedy algorithm)
    def try_at_random(self):
        #initialise a empty set for the candidate
        candidate = []
        #current total of sum of subset
        total = 0
        #whilst the total sum is not equal to target keep trying
        while total != self.t:
            #get a random sample of between 0 and 4 elements to test
            candidate = sample(self.S, randint(0,self.n))
            #evaluate the total of the subset
            total     = sum(candidate)
            print( "Trying: ", candidate, ", sum:", total )
    
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
              return True
            
    def AcceptanceProbability(self, new, old, temp): 
        if new or old is not None:
            if (new < old):
                return 1.0
            else:
                return math.exp((old-new)/temp)
        else:
            return 0
     def GRASP(self, max_iter):
         best_candidate = 0
         while (i <=  max_iter):
             greedy_candidate = GreedyAlgorithm()
             grasp_candidate = LocalSearch(greedy_candidate)
     def local_search(self,greedy_set):
         candidate = []
         for i in range(0, self.n):
             for j in range(0, greedy_set):
                 if (self.S[i] not in greedy_set):
                    greedy_set[i]
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

for n in range(4,12):
    start_time = time.time()       
    instance = SSP() #instance equals the SSP class
    instance.random_yes_instance(n)
    instance.try_at_random()
    instance.Exhaustive_Search()
    print (instance.greedy_algorithm())
    for i in range (1):
        print("%d\t%6f" % (n,(time.time() - start_time)/100))
print ("----------------------------------------------------")
print (instance.dynamicProgramming())
print("--- %s seconds ---" % (time.time() - start_time))
#call the brute force method passing in a length  for the array instance to be generated
print("Solution: " +str(instance.sim_anneal()))
#instance.greedy_algorithm()
if (instance.dynamic_programming() == True):
    print("Solution Found")
else:
    print("No Solution Found")
