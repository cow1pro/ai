def is_safe(maze, x, y, n):
    return x >= 0 and y >= 0 and x < n and y < n and maze[x][y] == 1

def solve_maze_util(maze, x, y, sol, n):
    if x == n - 1 and y == n - 1 and maze[x][y] == 1:
        sol[x][y] = 1
        return True
    
    if is_safe(maze, x, y, n):
        sol[x][y] = 1
        
        if solve_maze_util(maze, x + 1, y, sol, n):
            return True
        if solve_maze_util(maze, x, y + 1, sol, n):
            return True
        if solve_maze_util(maze, x - 1, y, sol, n):
            return True
        
        # If none of the above movements work, backtrack
        sol[x][y] = 0
        return False
    
    return False

def solve_maze(maze):
    n = len(maze)
    sol = [[0 for _ in range(n)] for _ in range(n)]
    
    if not solve_maze_util(maze, 0, 0, sol, n):
        print("No solution exists.")
        return False
    
    for row in sol:
        print(row)
    return True

maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]
solve_maze(maze)
