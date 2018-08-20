#Erin Cox
from collections import defaultdict

def solve(graph, node, isAdding, lastAction):
    #goal value
    if node[1:] == [0, 0, 0]:
        print("win")
        print(node[0])
        print()
        
    else:
        #get all possible combinations for moving people between banks
        actions = getActions(node, isAdding)
        for action in actions:
            newNode = buildNewNode(node, action, isAdding)
            graph[newNode[0]].append(newNode)
            if validState(newNode, lastAction, action):
                solve(graph, newNode, not isAdding, action)
                
def getActions(node, isAdding):
    localNode = node
    #to invert bank 2 to bank 1
    if isAdding:
        localNode = ['unused', 3 - node[1], 3 - node[2], 1]
    actions = []
    if localNode[1] >= 1:
        actions.append([1, 0, 1])
    if localNode[1] >= 2:
        actions.append([2, 0, 1])
    if localNode[2] >= 1:
        actions.append([0, 1, 1])
    if localNode[2] >= 2:
        actions.append([0, 2, 1])
    if localNode[1] >= 1 and localNode[2] >= 1:
        actions.append([1, 1, 1])
    return actions

def buildNewNode(parent, action, isAdding):
    node = [parent[0] + '.' + str(action[0]) + str(action[1]) + str(action[2]), parent[1], parent[2], parent[3]]
    if isAdding:
        node[1] += action[0]
        node[2] += action[1]
        node[3] += action[2]
    else:
        node[1] -= action[0]
        node[2] -= action[1]
        node[3] -= action[2]       
    return node

def validState(node, lastAction, currentAction):
    localNode = ['unused', 3 - node[1], 3 - node[2], 1]
    if node[2] > node[1] and node[1] > 0:
        return False
    if localNode[2] > localNode[1] and localNode[1] > 0:
        return False
    #initial state of bank 1
    if node[1:] == [3, 3, 1]:
        return False
    if lastAction == currentAction:
        return False
    return True

def main():
    #initialize root node with node[0] = node name, node[1] = 3 missionaries, node[2] = 3 cannibals, node[3] = bank 1
    node = ["root", 3, 3, 1]
    #initialize graph
    graph = defaultdict(list)
    graph["root"] = node
    solve(graph, node, False, None)    
    
main()