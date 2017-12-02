# copy and paste your answers into each of the below variables 
# NOTE: do NOT rename variables
# Modify the return statements to return the relevant values
# Include 1-2 sentences (as a python comment) above each answer explaining your reasoning.

import math

#Q1ai 
#Spliting and sorting involves reading and writing out all pages = (320/8)R(1IO) + 320W(2IO) = 680IO
io_split_sort = 680

#Q1aii
# 1 page for output, 7 wasted
merge_arity = 4

#Q1aiii 
# number_of_passes = ceil(log4(320/40)) = 2
merge_passes = 2

#Q1aiv 
# Each pass involves reading and writing out all pages = (320/8)R(1IO) + 320W(2IO) = 680IO
merge_pass_1 = 680

#Q1av
# total io cost = 680*(number_of_passes+initial_split_sort)=680*3=2040
total_io = 2040

#Q1bi 
def cost_initial_runs(B, N, P):
    # BEGIN YOUR CODE 
    # intial splitting and sorting
    # (N/P)(1IO) for reading, and N*2IO for writing
    return N/P+2*N
    # END YOUR CODE 

#Q1bii 
def cost_per_pass(B, N, P):
    # BEGIN YOUR CODE 
    # Each pass involves the reading and writing for all pages of the file
    # (N/P)(1IO) for reading, and N*2IO for writing
    return N/P+2*N
    #END YOUR CODE

#Q1biii
def num_passes(B, N, P):
    # BEGIN YOUR CODE 
    # arity of the merge
    merge_arity = ((B+1)/P)-1
    num_of_runs = N/(B+1)
    return math.ceil(math.log(num_of_runs,merge_arity))
    # END YOUR CODE

#Q1c 
# Save the optimal value here
P = 10

# Save a list of tuples of (P, io_cost) here, for all feasible P's
points = [(1, 5400.0),
          (2, 4500.0),
          (4, 4050.0),
          (5, 3960.0),
          (10, 3780.0),
          (20, 5535.0),
          (25, 5508.0)]

#Q2a 
#Join 1: Hashing R and S costs 2(P_R+P_S) IO. Matching R and S costs (P_R+P_S) IO. Writing out costs P_RS IO.
#Join 2: Hashing RS and T costs 2(P_RS+P_T) IO. Matching RS and T costs (P_RS+P_T) IO. Writing out costs P_RST IO.
#join1+join2 = 3(P_R+P_S)+P_RS+3(P_RS+P_T)+P_RST = 7560 IO in total.
IO_Cost_HJ_1 = 7560

#Join 1: Hashing T and S costs 2(P_T+P_S) IO. Matching T and S costs (P_T+P_S) IO. Writing out costs P_TS IO.
#Join 2: Hashing ST and R costs 2(P_ST+P_R) IO. Matching ST and R costs (P_ST+P_R) IO. Writing out costs P_RST IO.
#join1+join2 = 11160 IO in total.
IO_Cost_HJ_2 = 11160

#Join 1: Splitting & Sorting R and S costs sort(P_R)+sort(P_S) = 2P_R+4P_S IO. Scanning R and S costs (P_R+P_S) IO. Writing out costs P_RS IO.
#Join 2: Splitting & Sorting RS and T costs sort(P_RS)+sort(P_T) = 4P_RS+6P_T IO. Scanning RS and T costs (P_RS+P_T) IO. Writing out costs P_RST IO.
#sort(P) = 2N(ceil(log(B-1)(N/B))+1), given B is the number of buffer pages.
#join1+join2= 1160+15000 IO in total.
IO_Cost_SMJ_1 = 16160

#Join 1: Splitting & Sorting T and S costs sort(P_T)+sort(P_S)=6P_T+4P_S IO. Scanning T and S costs (P_T+P_S) IO. Writing out costs P_TS IO.
#Join 2: Splitting & Sorting ST and R costs sort(P_ST)+sort(P_R) = 6P_ST+2P_R IO. Scanning ST and R costs (P_ST+P_R) IO. Writing out costs P_RST IO.
#join1+join2= 16000+7560 IO in total.
IO_Cost_SMJ_2 = 23560

#Join 1: Joining R and S costs P_R+ceil(P_R/(B-2))*P_S+P_RS IO. 
#Join 2: Joining RS and T costs P_RS+ceil(P_RS/(B-2))*P_T+P_RST IO. 
#join+join2 = 320+8600 IO in total.
IO_Cost_BNLJ_1 = 8920

#Join 1: Joining T and S costs P_S+ceil(P_S/(B-2))*P_T+P_ST IO. Total 4600 IO.
#Join 2: Joining ST and R costs P_R+ceil(P_R/(B-2))*P_ST+P_RST IO. Total 760 IO.
#join1+join2=15200+1520=16720 IO in total.
IO_Cost_BNLJ_2 = 16720

#Q2b 
P_R = 20
P_S = 2000
P_T = 20
P_RS = 20
P_RST = 20
B = 32

#3(P_R+P_S)+P_RS = 6080
HJ_IO_Cost_join1 = 6080
#sort(P_RS)+sort(P_T)+P_RS+P_T+P_RST = 3P_RS+3P_T+P_RST = 140
SMJ_IO_Cost_join2 = 140

#sort(P_R)+sort(P_S)+P_R+P_S+P_RS = 3P_R+7P_S+P_RS = 14080
SMJ_IO_Cost_join1 = 14080
#3(P_RS+P_T)+P_RST = 140
HJ_IO_Cost_join2 = 140

#Q3ai
def lru_cost(N, M, B):
    # BEGIN YOUR CODE 
    if N>B+1:
        return N*M
    else:
        return N
    #END YOUR CODE

#Q3aii 
def mru_cost(N, M, B):
    #BEGIN YOUR CODE 
    if N<=B+1:
        return N
    else:
        buff = []
        cost = 0
        m = 0
        while m < M:
            for n in range(N):
                if len(buff)<B+1 and n not in buff:
                    buff.append(n)
                    mru = buff.index(n) # record the mru of buffer
                    cost+=1
                else:
                    if n not in buff:
                        buff[mru]=n
                        mru = buff.index(n)
                        cost+=1
                        if n == N-1:
                            m+=1
                    else:
                        mru = buff.index(n)
                        if n == N-1:
                            m+=1
    return cost
    #END YOUR CODE

#Q3aiii
# Provide a list of tuple (m, difference between LRU and MRU in terms of IO cost) here:
p3_lru_points = [(1, 0),
                 (2, 5),
                 (3, 10),
                 (4, 15),
                 (5, 20),
                 (6, 24),
                 (7, 28),
                 (8, 33),
                 (9, 38),
                 (10, 43),
                 (11, 48),
                 (12, 52),
                 (13, 56),
                 (14, 61),
                 (15, 66),
                 (16, 71),
                 (17, 76),
                 (18, 80),
                 (19, 84),
                 (20, 89)]

#Q3bi 
def clock_cost(N, M, B):
    #BEGIN YOUR CODE
    if N>B+1:
        return N*M
    else:
        return N
    #END YOUR CODE

#Q3bii 
# Provide a list of tuple (m vs the absolute value of the difference between LRU and CLOCK in terms of IO cost) here:
p3_clock_points = [(1, 0),
                 (2, 0),
                 (3, 0),
                 (4, 0),
                 (5, 0),
                 (6, 0),
                 (7, 0),
                 (8, 0),
                 (9, 0),
                 (10, 0),
                 (11, 0),
                 (12, 0),
                 (13, 0),
                 (14, 0),
                 (15, 0),
                 (16, 0),
                 (17, 0),
                 (18, 0),
                 (19, 0),
                 (20, 0)]

'''
Explanation here:
No. The CLOCK eviction policy does not prevent sequential flooding. It works in the same way as LRU.
'''

#Q4ai
def hashJoin(table1, table2, hashfunction,buckets):
    # Parition phase 
    t1Partition = partitionTable(table1,hashfunction,buckets)
    t2Partition = partitionTable(table2,hashfunction,buckets)
    # Merge phase
    result = []
    
    # ANSWER GOES HERE
    for i in range(0,buckets):
        t1 = t1Partition[i]
        t2 = t2Partition[i]
        for t1Entry in t1:
            for t2Entry in t2:
                if t2Entry.playername == t1Entry.playername:
                    result.append((t1Entry.teamname, t1Entry.playername, t2Entry.collegename))
    # To populate your output you should use the following code(t1Entry and t2Entry are possible var names for tuples)
    # result.append((t1Entry.teamname, t1Entry.playername, t2Entry.collegename))
    return result

#Q4aii
'''
Explanation here:
# The total number of entries output is reasonable, 12720 + 20 duplications (Andrew Jackson)
# However, the runtime is not reasonable.
# The runtime takes too long. For hash join, it should be much faster.
# The problem is that the hash function hashes data with skew, which increases match time.
# The algorithm can be more effective, with a better hash function.
'''

#Q4bi 
# partition- a table partition as returned by method partitionTable
# return value - a float representing the skew of hash function (i.e. stdev of chefs assigned to each restaurant)
import numpy
def calculateSkew(partition):
    # ANSWER STARTS HERE
    num_of_entry = []
    for i in range(0,len(partition)):
        num_of_entry.append(len(partition[i]))
    skew = numpy.std(num_of_entry)
    # ANSWER ENDS HERE
    return skew

#Q4bii 
# Design a better hash function and print the skew difference for 
def hBetter(x,buckets):
    rawKey = hash(x)
    return rawKey % buckets

#Q4biii 
res1 = hashJoin(teams, colleges, hBetter, buckets)

#speedup here = # Reduced from ~8000ms to ~200ms - 40 times faster than the previous hash function.
# The hash join is faster with less skew during the partition phase.

#Q4c
flocco_elite = True
