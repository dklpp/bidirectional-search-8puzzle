import random
import time
from moves import *
from validation import *
from path import *
from tester import *
from transform import *
from bds import *

MINIMUM = 2 # min is 2x2 array


class Node():
    def __init__(self, state, parent, prev_move, depth): # constructor
        self.state = state
        self.parent = parent
        self.previous_move = prev_move
        self.depth = depth


columns = int()
rows = int()

while(1):
    print('\t\t\t\t\tBIDIRECTIONAL SEARCH FOR 8-PUZZLE PROBLEM')
    print("--------------------------------------------------------------------------------------------")
    print("manual = Enter input mannualy: enter the field size and then enter states (init, goal)")
    print("tester = Enter the field size and then examples are generated")
    print("quit = End the program")
    option = input("\nChoose option (manual/tester/quit): ")
    if(option == "manual"):
        print("Enter parameters of the surface (2x2,3x2,3x3,4x2,5x2)")
        rows = input("Num of rows: ")
        columns = input("Num of columns: ")
        if(rows.isnumeric() and columns.isnumeric()):
            rows = int(rows)
            columns = int(columns)
            if(rows >= MINIMUM and columns >= MINIMUM):
                print("Be careful not to repeat the numbers")
                print("Enter like this: 0 1 2 3 4 5 6 7 8")
                init_state = input("Enter the initial state:")
                end_state = input("Enter the goal state:")
                start_state = string_to_list(init_state)
                goal_state = string_to_list(end_state)
                if(len(start_state) == rows * columns and len(goal_state) == rows * columns):
                    if(columns == 3 and rows == 3):        # if 3x3 check if it's solvable by inversion
                        if (solvable(start_state, goal_state)):
                            bds(start_state, goal_state, rows, columns)
                    else:
                        bds(start_state, goal_state, rows, columns)
    elif(option == "tester"):
        print("Enter the parameters of the field (2x2,3x2,3x3,4x2,5x2)")
        rows = input("Num of rows: ")
        columns = input("Num of cols: ")
        if (rows.isnumeric() and columns.isnumeric()):
            rows = int(rows)
            columns = int(columns)
            if (rows >= MINIMUM and columns >= MINIMUM):
                tester(rows, columns)
    elif (option == "quit"):
        print('Exit the program..')
        exit()

