import random
from validation import *
#from main import bds
from bds import *

# helper function for tester (generating a random state)
def generate_random_list(num):
    a = list(range(0, num))
    b = list()
    #print(a)
    while(len(a) > 0):
        c = random.choice(a)
        a.remove(c)
        b.append(c)
    return b


# function for testing
def tester(m, n):
    while(True):
        start_state = generate_random_list(m * n) # generate mn random numbers
        goal_state = generate_random_list(m * n)
        if(solvable(start_state, goal_state)):
            bds(start_state, goal_state, m, n) # call main function for solving task directly
            break