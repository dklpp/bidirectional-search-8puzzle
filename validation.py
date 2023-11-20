""" verify if the task is unsolvable, using inversion can be only for 3x3 case"""


# check if input is from 0 - (n-1)
def check_valid_input(input, m, n):
    for i in range(0, m * n, 1):
        if(input[i] >= 0 and input[i] < m * n): # in 3x3 case nums cannot be 10, 11, 12, etc.
            continue
        else:
            return False
    return True


# It is not possible to solve an instance of 8 puzzle if number of inversions is odd in the input state.
# Our goal state has 0 inversions, it means that our initial state must have even number of inversions.
# More about inversions in 8-puzzle problem: https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/
def solvable(s_state, f_state):
    s_list = s_state[:] # start state
    f_list = f_state[:] # finist state
    s_list.remove(0)
    f_list.remove(0)

    s_inversion = get_inversion(s_list)
    f_inversion = get_inversion(f_list)
    if(s_inversion % 2 == f_inversion % 2):  # in case of 3x3 it should be: s_inversion % 2 == 0
        return True
    else:
        print('\nThis initial state is unsolvable.\nNumber of inversions is odd number.\n')
        return False


# calculates amount of inversions for a state
def get_inversion(list_state):
    counter = 0

    help_list = list(range(1, len(list_state)+1))

    for i in range(0, len(list_state), 1):
        for j in range(0, len(list_state), 1):
            if(list_state[i] > help_list[j] and help_list[j] != 0):
                counter += 1
            elif(list_state[i] == help_list[j]):
                help_list[j] = 0
                break

    return counter