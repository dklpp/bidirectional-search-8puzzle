""" Transforming list to string or to 2D list """


# functions that represent state, to transform from 1D list to 2D list
def transfer_list_to_state(input, m, n):
    state = []
    helper_state = []
    m = int(m)
    n = int(n)
    row = 0
    for i in range(0, (m * n) + 1, 1):
        if(i // m == row):
            helper_state.append(input[i])     # input[i]
        else:
            if(i == m * n):
                state.append(helper_state[:])
                return state
            else:
                row += 1
                state.append(helper_state[:])
                helper_state.clear()
                helper_state.append(input[i])


def transfer_state_to_list(state):
    list = []
    for i in state:
        for j in range(0, len(state[0]), 1):
            list.append(i[j])
    return list


# turn the status to string, it is used for key in hash table
def state_to_string(state,m,n):
    string = ""
    for i in range(0, m, 1):
        for j in range(0, n, 1):
            string += str(state[i][j]) + " "
    return string


def string_to_list(string):
    a_list = string.split()
    a = map(int, a_list)
    b = list(a)
    return b