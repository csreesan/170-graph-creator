#!/usr/bin/env python

""" Traveling salesman problem solved using Simulated Annealing.
"""
from scipy import *
from pylab import *

def Distance(dist_dict, i, j):
    return dist_dict[i][j]

def TotalDistance(dom_list, dist_dict):
    dist=0
    for i in range(len(dom_list)-1):
        dist += Distance(dist_dict,dom_list[i],dom_list[i+1])
    dist += Distance(dist_dict,dom_list[i],dom_list[i+1])
    return dist
    
def reverse(dom_list, n):
    nct = len(dom_list)
    nn = (1+ ((n[1]-n[0]) % nct))/2 # half the lenght of the segment to be reversed
    # the segment is reversed in the following way n[0]<->n[1], n[0]+1<->n[1]-1, n[0]+2<->n[1]-2,...
    # Start at the ends of the segment and swap pairs of cities, moving towards the center.
    for j in range(int(nn)):
        k = (n[0]+j) % nct
        l = (n[1]-j) % nct
        (dom_list[k],dom_list[l]) = (dom_list[l],dom_list[k])  # swap
    
def transpt(dom_list, n):
    nct = len(dom_list)
    
    new_list=[]
    # Segment in the range n[0]...n[1]
    for j in range( (n[1]-n[0])%nct + 1):
        new_list.append(dom_list[ (j+n[0])%nct ])
    # is followed by segment n[5]...n[2]
    for j in range( (n[2]-n[5])%nct + 1):
        new_list.append(dom_list[ (j+n[5])%nct ])
    # is followed by segment n[3]...n[4]
    for j in range( (n[4]-n[3])%nct + 1):
        new_list.append(dom_list[ (j+n[3])%nct ])
    return new_list

def cylce_val(dist_dict, cycle):
    total_cost = 0
    for i in range(len(cycle) - 1):
        total_cost += dist_dict[cycle[i]][cycle[i + 1]]
    return total_cost


def solve_for_cycle(dom_set, dist_dict, source):

    print("######", "solve_for_cycle")

    dom_list = list(dom_set)
    ncity = len(dom_list)        # Number of cities to visit
    maxTsteps = 120    # Temperature is lowered not more than maxTsteps
    #Tstart = 0.8       # Starting temperature - has to be high enough
    Tstart = 1.2
    fCool = 0.9        # Factor to multiply temperature at each cooling step
    maxSteps = 100*ncity     # Number of steps at constant temperature
    maxAccepted = 10*ncity   # Number of accepted steps at constant temperature

    Preverse = 0.7      # How often to choose reverse/transpose trial move


    # Distance of the travel at the beginning
    dist = TotalDistance(dom_list, dist_dict)

    # Stores points of a move
    n = zeros(6, dtype=int)
    nct = ncity # number of cities
    
    T = Tstart # temperature
    
    for t in range(maxTsteps):  # Over temperature

        accepted = 0
        for i in range(maxSteps): # At each temperature, many Monte Carlo steps
            
            while True: # Will find two random cities sufficiently close by
                # Two cities n[0] and n[1] are choosen at random
                n[0] = int((nct)*rand())     # select one city
                n[1] = int((nct-1)*rand())   # select another city, but not the same
                if (n[1] >= n[0]): n[1] += 1   #
                if (n[1] < n[0]): (n[0],n[1]) = (n[1],n[0]) # swap, because it must be: n[0]<n[1]
                nn = (n[0]+nct -n[1]-1) % nct  # number of cities not on the segment n[0]..n[1]
                if nn>=3: break
        
            # We want to have one index before and one after the two cities
            # The order hence is [n2,n0,n1,n3]
            n[2] = (n[0]-1) % nct  # index before n0  -- see figure in the lecture notes
            n[3] = (n[1]+1) % nct  # index after n2   -- see figure in the lecture notes
            
            if Preverse > rand(): 
                # Here we reverse a segment
                # What would be the cost to reverse the path between city[n[0]]-city[n[1]]?
                de = Distance(dist_dict, dom_list[n[2]],dom_list[n[1]]) + Distance(dist_dict, dom_list[n[3]],dom_list[n[0]]) - Distance(dist_dict, dom_list[n[2]],dom_list[n[0]]) - Distance(dist_dict, dom_list[n[3]],dom_list[n[1]])
                
                if de<0 or exp(-de/T)>rand(): # Metropolis
                    accepted += 1
                    dist += de
                    reverse(dom_list, n)
            else:
                # Here we transpose a segment
                nc = (n[1]+1+ int(rand()*(nn-1)))%nct  # Another point outside n[0],n[1] segment. See picture in lecture nodes!
                n[4] = nc
                n[5] = (nc+1) % nct
        
                # Cost to transpose a segment
                de = -Distance(dist_dict, dom_list[n[1]],dom_list[n[3]]) - Distance(dist_dict, dom_list[n[0]],dom_list[n[2]]) - Distance(dist_dict, dom_list[n[4]],dom_list[n[5]])
                de += Distance(dist_dict, dom_list[n[0]],dom_list[n[4]]) + Distance(dist_dict, dom_list[n[1]],dom_list[n[5]]) + Distance(dist_dict, dom_list[n[2]],dom_list[n[3]])
                
                if de<0 or exp(-de/T)>rand(): # Metropolis
                    accepted += 1
                    dist += de
                    dom_list = transpt(dom_list, n)
                    
            if accepted > maxAccepted: break
        
        
        # print("T=%10.5f , distance= %10.5f , accepted steps= %d" %(T, dist, accepted))

        # print(cylce_val(dist_dict, dom_list + [dom_list[0]]))
        T *= fCool             # The system is cooled down
        if accepted == 0: 

            break  # If the path does not want to change any more, we can stop
    source_index = dom_list.index(source)
    return dom_list[source_index:] + dom_list[:source_index] + [source]
    