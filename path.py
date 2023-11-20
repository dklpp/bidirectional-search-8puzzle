# function for path
def print_path_recursively(node):
    if(node.parent == None):
        for one in node.state:
            print(one)
        return 0
    print_path_recursively(node.parent)
    print("||||||  " + str(node.previous_move) + "  ||||||||")
    for one in node.state:
        print(one)


def print_path(node): # opposite path in case of BFS in opposite direction (from the goal state)
    for one in node.state:
        print(one)
    if (node.parent != None):
        print("||||||  " + str(transition_dir(node.previous_move)) + "  ||||||||")
    if (node.parent == None):
        return 0
    print_path(node.parent)


# when output is from the end state, we need to output the opposite movements
def transition_dir(dir):
    if(dir == "up"):
        return "down"
    elif (dir == "down"):
        return "up"
    elif (dir == "left"):
        return "right"
    elif (dir == "right"):
        return "left"