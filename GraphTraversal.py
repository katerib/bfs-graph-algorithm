def solve_puzzle(board, source, destination):
    """
    Identifies all passable cells on the board and stores their passable neighboring cells.
    Calls BFS algorithm on dictionary of passable cells/neighbors.
    :param board: list of lists ; each list represents a row in rectangular puzzle
        elements are either '-' for empty (passable), or '#' for obstacle (impassable)
    :param source: tuple representing indices of starting position
    :param destination: tuple representing indices of goal/target position
    :return: list of tuples representing indices of each position in the path
        first tuple is source, last tuple is destination
        if no valid path is found, returns None
    """
    cells = {}

    n = len(board)
    for row in range(n):
        for col in range(len(board[row])):
            if board[row][col] == '-':                      # first check if valid/empty
                neighbors = []                              # find all valid neighbors
                if col > 0 and board[row][col-1] == '-':                    # LEFT cell is empty
                    neighbors.append((row, col-1))
                if col < len(board[row])-1 and board[row][col+1] == '-':    # RIGHT cell is empty
                    neighbors.append((row, col+1))
                if row > 0 and board[row-1][col] == '-':                    # UPPER cell is empty
                    neighbors.append((row-1, col))
                if row < n-1 and board[row+1][col] == '-':                  # LOWER cell is empty
                    neighbors.append((row+1, col))
                cells[(row, col)] = neighbors            # store current cell:neighbors in dictionary
    return bfs(cells, source, destination)               # now bfs traversal


def bfs(board, source, destination):
    """
    Implements BFS algorithm to find shortest passable path between source and destination.
    Uses a queue.
    :param board: dictionary of passable cells and their passable neighbors
    :param source: same as source passed to solve_puzzle
    :param destination: same as destination passed to solve_puzzle
    :return: if destination is found, returns path. otherwise, returns None
    """
    board_queue = [(source, [source])]                  # initialize queue, only add source to path
    visited = set()
    while board_queue:
        current, path = board_queue.pop(0)              # pop current cell
        if current == destination:
            return path
        elif current in visited:
            continue
        visited.add(current)                            # mark current as 'seen'
        for neighbor in board[current]:
            if neighbor not in visited:                 # if valid, not visited, and not destination
                update_path = path+[neighbor]           # new path by appending neighbor
                board_queue.append((neighbor, update_path))
    return None                                         # if no valid path found, return None object
