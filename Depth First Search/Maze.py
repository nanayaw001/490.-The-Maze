def hasPath(maze, start, destination):
    def dfs(x, y):
        if x == destination[0] and y == destination[1]:
            return True
        if (x, y) in visited:
            return False
        
        visited.add((x, y))
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            newX, newY = x, y
            while 0 <= newX + dx < len(maze) and 0 <= newY + dy < len(maze[0]) and maze[newX + dx][newY + dy] != 1:
                newX += dx
                newY += dy
            if dfs(newX, newY):
                return True
        
        return False
    
    visited = set()
    return dfs(start[0], start[1])

# Test cases
maze1 = [[0,0,1,0,0], [0,0,0,0,0], [0,0,0,1,0], [1,1,0,1,1], [0,0,0,0,0]]
start1 = [0,4]
destination1 = [3,2]
print(hasPath(maze1, start1, destination1))  # Output: False

maze2 = [[0,0,0,0,0], [1,1,0,0,1], [0,0,0,0,0], [0,1,0,0,1], [0,1,0,0,0]]
start2 = [4,3]
destination2 = [0,1]
print(hasPath(maze2, start2, destination2))  # Output: False

maze3 = [[0,0,0,0,0], [1,1,0,0,1], [0,0,0,0,0], [0,1,0,0,1], [0,1,0,0,0]]
start3 = [0,0]
destination3 = [3,2]
print(hasPath(maze3, start3, destination3))  # Output: True
