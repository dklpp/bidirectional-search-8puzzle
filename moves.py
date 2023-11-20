# get position of a certain number from the state
# (finding the position of exact number)
def get_x_y(state, num):
    for i in range(0, len(state), 1):
        for j in range(0, len(state[i]), 1):
            if(state[i][j] == num):
                return i, j


def up(state): # state - 2D list
    new_state = [row[:] for row in state] # copy of input array
    pos_0_x, pos_0_y = get_x_y(new_state, 0) # find position of 0 (blank tile)
    if((pos_0_x - 1) < 0): # check if moving up is a valid move (if the row index is already 0, we cannot move up)
        return False
    else:
        # swap values between blank tile and tile above
        temp = new_state[pos_0_x][pos_0_y]      # store the value of position of blank tile
        new_state[pos_0_x][pos_0_y] = new_state[pos_0_x - 1][pos_0_y]   # on position of blank tile put value of tile above
        new_state[pos_0_x - 1][pos_0_y] = temp  #  move blank tile above (on position of tile above)
        return new_state


def down(state):
    new_state = [row[:] for row in state]
    pos_0_x, pos_0_y = get_x_y(new_state, 0)
    if ((pos_0_x + 1) > (len(new_state) - 1) ):   # check if moving down is VALID (if we are not at the bottom of our space)
        return False
    else:
        temp = new_state[pos_0_x][pos_0_y]  # store the value of position of blank tile
        new_state[pos_0_x][pos_0_y] = new_state[pos_0_x + 1][pos_0_y]  # on position of blank line put value of tile below
        new_state[pos_0_x + 1][pos_0_y] = temp  # put blank tile below
        return new_state


def right(state):
    new_state = [row[:] for row in state]
    pos_0_x, pos_0_y = get_x_y(new_state, 0)
    if ((pos_0_y + 1) > (len(new_state[0]) - 1)):  #  check if we can move right
        return False
    else:
        temp = new_state[pos_0_x][pos_0_y]  # store the value of position of blank tile
        new_state[pos_0_x][pos_0_y] = new_state[pos_0_x][pos_0_y + 1]  # on blank tile position, put tile that is right
        new_state[pos_0_x][pos_0_y + 1] = temp  # put blank tile right
        return new_state


def left(state):
    new_state = [row[:] for row in state]
    pos_0_x, pos_0_y = get_x_y(new_state, 0)
    if((pos_0_y - 1) < 0):  # check if action is valid
        return False
    else:
        temp = new_state[pos_0_x][pos_0_y]      # store the value of position of blank tile
        new_state[pos_0_x][pos_0_y] = new_state[pos_0_x][pos_0_y - 1]  # on blank tile position, put tile that is left
        new_state[pos_0_x][pos_0_y - 1] = temp  # put blank tile left
        return new_state
