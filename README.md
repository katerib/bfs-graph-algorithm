# Graph Traversal
Portfolio Project submission for Analysis of Algorithms, received a perfect score. 

## Prompt
There exists a 2D puzzle of size M*N with N rows and M columns (M and N are not always equal). Each cell in the puzzle is either empty (marked by a hyphen '-') or contains a barrier (marked by an octothorpe '#'). Two puzzle coordinates are provided: (a,b) and (x,y). The goal is to start at the coordinate (a,b) and reach coordinate (x,y) in the minimum number of moves. Valid moves include left, right, up, and down by one cell as long as the cell does not contain a barrier. Diagonal moves and moves to a non-empty cell are not permitted.

### Input

A valid input will contain: `(board, source, destination)`

**Board**: a list of lists, each list represents a row in the rectangular puzzle

**Source**: a tuple representing the indices of the starting position

**Destination**: a tuple representing the indices of the goal position

### Output

A list of tuples representing the indices of each position in the graph. The first tuple will contain the starting position, the last tuple should contain the destination coordinates, and the tuples in between will contain the visited cells.

If there is no valid path, return the None object.

## Breadth-First Search Algorithm

I used a BFS algorithm to traverse the graph by visiting each layer of cells and their neighbors. 

### Time Complexity

The time complexity of my solution is `O(M*N)` because each cell and its neighbors are visited during the BFS traversal. Creating the graph is `O(M*N)`, where M and N are rows and columns, respectively. 

BFS Traversal takes `O(|V| + |E|)` time, where V and E are each equal to `O(M*N)`.

Therefore, the time complexity is `O(2(M*N))`, or `O(M*N)`.