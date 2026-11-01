visited = set()

def dfs(a, b):
    if (a, b) in visited:
        return

    visited.add((a, b))
    print((a, b))

    if a == 2 or b == 2:
        print("Goal Reached")
        return

    dfs(4, b)          # Fill Jug1
    dfs(a, 3)          # Fill Jug2
    dfs(0, b)          # Empty Jug1
    dfs(a, 0)          # Empty Jug2

    transfer = min(a, 3-b)
    dfs(a-transfer, b+transfer)

    transfer = min(b, 4-a)
    dfs(a+transfer, b-transfer)

dfs(0, 0)

'''
Theory:-
The Water Jug Problem is a classic Artificial Intelligence problem used to demonstrate state space search techniques. 
The problem consists of two water jugs with fixed capacities and an unlimited water supply. 
The objective is to obtain a specific amount of water by performing operations such as filling, emptying, and pouring water between the jugs.
Depth First Search (DFS) is an uninformed search algorithm that explores a branch completely before backtracking. 
It uses a Stack (LIFO) data structure, either explicitly or through recursion.

Depth First Search (DFS) is an uninformed search algorithm used in Artificial Intelligence for traversing or searching a graph or state space.
DFS starts from the root node and explores one branch completely before moving to another branch.
DFS uses a Stack (LIFO - Last In First Out) data structure.
In Python, DFS is commonly implemented using recursion, where the function calls itself to explore deeper nodes.

The algorithm continues exploring until:
The goal node is found, or 
All nodes have been visited. 
DFS is memory efficient because it stores only the current path from the root to a leaf node.

Characteristics of DFS:-
Uninformed search technique. 
Uses Stack (LIFO). 
Explores deeper nodes first. 
Uses recursion or stack implementation. 
Requires less memory than BFS. 

Advantages:-
Easy to implement. 
Requires less memory. 
Suitable for deep search spaces. 
Useful in backtracking problems. 

Limitations:-
Does not guarantee the shortest path. 
Can get stuck in deep branches. 
May revisit nodes if not marked as visited.
In the Water Jug Problem, each state is represented as:
(Jug1, Jug2)
where Jug1 and Jug2 represent the amount of water in each jug.
DFS explores possible states until it reaches the goal state.

Advantages of DFS:-
Simple to implement. 
Requires less memory than BFS. 
Suitable for deep search spaces. 

Limitations of DFS:-
Does not guarantee the shortest path. 
May get trapped in deep branches. 
Can revisit states if not handled properly.

Algorithm:-
Start. 
Define the capacities of the two jugs. 
Define the initial state (0,0). 
Use DFS to explore possible states. 
Generate all valid successor states: 
Fill Jug1 
Fill Jug2 
Empty Jug1 
Empty Jug2 
Pour Jug1 into Jug2 
Pour Jug2 into Jug1 
Mark visited states. 
If the goal amount is found, display the solution. 
Otherwise, continue searching. 
Stop

Applications:-
Problem-solving in Artificial Intelligence. 
State space search problems. 
Resource allocation problems. 
Puzzle solving. 
Robot planning systems. 
Game tree exploration. 
Pathfinding applications. 

Result:-
The Water Jug Problem was successfully solved using the Depth First Search (DFS) algorithm.
The algorithm explored states recursively and reached the goal state containing 2 liters of water.

Conclusion:-
The experiment successfully demonstrated the implementation of the Depth First Search (DFS) algorithm for solving the Water Jug Problem. 
DFS explored the state space recursively and found a valid sequence of operations to achieve the desired quantity of water.
'''
