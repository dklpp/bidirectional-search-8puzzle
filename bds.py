from tester import *
from path import *
from validation import *
from transform import *
from moves import *
import time


class Node():
    def __init__(self, state, parent, prev_move, depth): # constructor
        self.state = state
        self.parent = parent
        self.previous_move = prev_move
        self.depth = depth


# main func where the task is solved directly
def bds(s_state, f_state, rows, cols):
    if(s_state == f_state):
        print("The inital state is goal state")
        return 0

    # 2 states from which BFS is starting
    start_RootNode = Node(transfer_list_to_state(s_state, cols, rows), None, None, 0)
    goal_RootNode = Node(transfer_list_to_state(f_state, cols, rows), None, None, 0)

    # hash tables where all the states are stored and if they are explored
    # key - is state_to_string(state)
    hash_table1 = {}
    hash_table2 = {}

    start_queue = []
    goal_queue = []
    start_explored = []
    goal_explored = []

    start_queue.append(start_RootNode) # in start queue append the initial node
    goal_queue.append(goal_RootNode) # in goal queue append the goal node (state)
    hash_table1[state_to_string(start_RootNode.state, rows, cols)] = start_RootNode
    hash_table2[state_to_string(goal_RootNode.state, rows, cols)] = goal_RootNode

    start = time.time()

    while (len(start_queue) > 0 and len(goal_queue) > 0):
        # choose one of each of the 2 offsprings , where the unprocessed nodes are located
        temp1 = start_queue.pop(0) # remove 0
        temp2 = goal_queue.pop(0)

        # if from the initial state this state (that we took from goal queue) was already explored, it means both directions have met
        if(hash_table1.get(state_to_string(temp2.state, rows, cols)) != None):  # if None, it means state is not explored yet
            end = time.time()
            total_depth = temp2.depth + hash_table1.get(state_to_string(temp2.state, rows, cols)).depth # adding each depth to calculate total depth
            print("Path cost: " + str(total_depth))
            print("start_queue: "+ str(len(start_queue)))
            print("goal_queue: " + str(len(goal_queue)))
            print("start_explored: " + str(len(start_explored)))
            print("goal_explored: " + str(len(goal_explored)))
            print("PATH:")
            print_path_recursively(hash_table1.get(state_to_string(temp2.state, rows, cols)))
            print("-------------------------------- Met here ---------------------------------------------------")
            print("||||||  " + str(transition_dir(temp2.previous_move)) + "  ||||||||")
            print_path(temp2.parent)
            print("\n")
            print("Total time: " + str(round(end - start, 2)) + " seconds")
            return 0

        # if from the goal state this state (took from start queue) was already explored, it means both directions have met
        elif(hash_table2.get(state_to_string(temp1.state, rows, cols)) != None):
            end = time.time()
            total_depth = temp1.depth + hash_table2.get(state_to_string(temp1.state, rows, cols)).depth
            print("Path cost: " + str(total_depth))
            print("start_queue: " + str(len(start_queue)))
            print("goal_queue: " + str(len(goal_queue)))
            print("start_explored: " + str(len(start_explored)))
            print("goal_explored: " + str(len(goal_explored)))
            print("Path:")
            print_path_recursively(temp1)
            print("-------------------------------- Met here ---------------------------------------------------")
            print("||||||  " + str(transition_dir(hash_table2.get(state_to_string(temp1.state, rows, cols)).previous_move)) + "  ||||||||")
            print_path(hash_table2.get(state_to_string(temp1.state, rows, cols)).parent)
            print("\n")
            print("Total time: " + str(round(end - start, 2)) + " seconds")
            return 0


        """ Processing the node direction from the initial state """
        up_1 = Node(up(temp1.state), temp1, "up", temp1.depth + 1)    # create a node, representing the state obtained by moving the blank tile in the temp1 state to the right
        if (up_1.state != False and temp1.previous_move != "down"):    #  check if the movement in this dir is acceptable
            if(hash_table1.get(state_to_string(up_1.state, rows, cols)) == None): # if such state wasn't generated before, move on
                start_queue.append(up_1)    # new node is added to the end list for unprocessed
                hash_table1[state_to_string(up_1.state, rows, cols)] = up_1   # insert the new state into the hash table with the key to the given node


        down_1 = Node(down(temp1.state), temp1, "down", temp1.depth + 1) # creating a node
        if (down_1.state != False and temp1.previous_move != "up"):
            if (hash_table1.get(state_to_string(down_1.state, rows, cols)) == None): # if such state wasn't generated before
                start_queue.append(down_1) # new  node is added to the end of the list
                hash_table1[state_to_string(down_1.state, rows, cols)] = down_1

        right_1 = Node(right(temp1.state), temp1, "right", temp1.depth + 1)
        if (right_1.state != False and temp1.previous_move != "left"): # check if the state is valid and prevent move back
            if (hash_table1.get(state_to_string(right_1.state, rows, cols)) == None): # check if the state was explored before
                start_queue.append(right_1) # add new node to the start queue
                hash_table1[state_to_string(right_1.state, rows, cols)] = right_1 # inserting into hash table

        left_1 = Node(left(temp1.state), temp1, "left", temp1.depth + 1)
        if (left_1.state != False and temp1.previous_move != "right"):
            if (hash_table1.get(state_to_string(left_1.state, rows, cols)) == None):
                start_queue.append(left_1)
                hash_table1[state_to_string(left_1.state, rows, cols)] = left_1



        """ Node processing in the direction from the end (goal) state """
        up_2 = Node(up(temp2.state), temp2, "up", temp2.depth + 1)
        if (up_2.state != False and temp2.previous_move != "down"):
            if (hash_table2.get(state_to_string(up_2.state, rows, cols)) == None):
                goal_queue.append(up_2)
                hash_table2[state_to_string(up_2.state, rows, cols)] = up_2

        down_2 = Node(down(temp2.state), temp2, "down", temp2.depth + 1)
        if (down_2.state != False and temp2.previous_move != "up"):
            if (hash_table2.get(state_to_string(down_2.state, rows, cols)) == None):
                goal_queue.append(down_2)
                hash_table2[state_to_string(down_2.state, rows, cols)] = down_2

        right_2 = Node(right(temp2.state), temp2, "right", temp2.depth + 1)
        if (right_2.state != False and temp2.previous_move != "left"):
            if (hash_table2.get(state_to_string(right_2.state, rows, cols)) == None):
                goal_queue.append(right_2)
                hash_table2[state_to_string(right_2.state, rows, cols)] = right_2

        left_2 = Node(left(temp2.state), temp2, "left", temp2.depth + 1)
        if (left_2.state != False and temp2.previous_move != "right"):
            if (hash_table2.get(state_to_string(left_2.state, rows, cols)) == None):
                goal_queue.append(left_2)
                hash_table2[state_to_string(left_2.state, rows, cols)] = left_2

        # at the end move both processed nodes to the list for processed nodes
        start_explored.append(temp1)
        goal_explored.append(temp2)

    # no solution if they haven't met
    for i in start_RootNode.state:
        print(i)
    print("----------------")
    for j in goal_RootNode.state:
        print(j)
    print("\nThere is no solution.")


"""     Test for 3x2
start_state = [0,1,2,3,4,5]
goal_state = [3,4,5,0,1,2]
        Test for 3x3
start_state = [0,1,2,3,4,5,6,7,8]
goal_state = [8,0,6,5,4,7,2,3,1]
         Test for 4x2 
start_state = [0,1,2,3,4,5,6,7]
goal_state = [3,2,5,4,7,6,1,0]
        Test for 5x2
start_state = [0,1,2,3,4,5,6,7,8,9]
goal_state = [4,3,2,6,1,9,8,7,5,0]

        Test for 2x3 
start_state = 1 5 2 4 3 0
goal_state = 1 2 3 4 5 0
"""