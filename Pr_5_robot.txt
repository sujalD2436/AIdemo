from collections import deque

grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

queue = deque([(start, [start])])
visited = set()

while queue:
    (x, y), path = queue.popleft()

    if (x, y) == goal:
        print("Path Found:")
        print(path)
        break

    visited.add((x, y))

    for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
        nx, ny = x + dx, y + dy
        if (0 <= nx < 4 and 0 <= ny < 4 and
            grid[nx][ny] == 0 and
            (nx, ny) not in visited):

            queue.append(((nx, ny), path + [(nx, ny)]))
            
'''
Robot Path Planning ==>

Objective:-
To understand the concept of robot path planning.
To study Breadth First Search (BFS) as a search technique.
To find the shortest path between two locations.
To apply BFS in a grid-based environment.
To analyze the efficiency of BFS in path planning problems.

Theory:-
Robot Path Planning is one of the important applications of Artificial Intelligence. 
The objective of path planning is to determine a valid and optimal path for a robot from a 
starting position to a destination while avoiding obstacles.

In AI, path planning problems can be represented as a graph where:
Each cell or location is considered a node.
Possible movements between cells are considered edges.
The robot searches for a path from the start node to the goal node.

Breadth First Search (BFS) is an uninformed search algorithm that explores nodes level by level.
BFS uses a Queue (FIFO) data structure and guarantees the shortest path when all movements have equal cost.
In Robot Path Planning, BFS starts from the robot's initial position and explores all neighboring positions. 
It continues expanding nodes until the goal position is reached. Since BFS explores nodes level by level, the first path found
is always the shortest path.

Characteristics of BFS:-
Uninformed search algorithm.
Uses FIFO Queue.
Complete search method.
Guarantees shortest path.
Suitable for grid and graph traversal.

Advantages:-
Simple to implement.
Finds shortest path.
Complete and optimal for equal-cost paths.
Widely used in robotics and navigation.

Limitations:-
Requires large memory.
Slow for large search spaces.
Explores many unnecessary nodes.

Algorithm:-
Start.
Define the grid environment.
Specify start and goal positions.
Insert the start position into the queue.
Remove the front node from the queue.
If the node is the goal, stop.
Generate valid neighboring positions.
Add unvisited neighbors to the queue.
Mark visited positions.
Repeat until the goal is found.
Display the shortest path.
Stop.

Observation Table:-
Step        Current Position        Action
1           (0,0)                   Start
2           (0,1)                   Move Right
3           (0,2)                   Move Right
4           (1,2)                   Move Down
5           (2,2)                   Move Down
6           (2,3)                   Move Right
7           (3,3)                   Goal Reached


Applications:-
Autonomous robot navigation.
Mobile robot path planning.
Warehouse automation systems.
GPS and route navigation.
Game AI movement planning.
Maze solving problems.
Drone navigation systems.
Industrial robotics.

Result:-
The Breadth First Search (BFS) algorithm was successfully implemented for Robot Path Planning. 
The algorithm explored nodes level by level and found the shortest path from the start position to the goal
position while avoiding obstacles.
'''
