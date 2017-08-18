from heapq import heappush, heappop
import copy
def answer(maze):
    height = len(maze)
    width = len(maze[0])
    maze_info = []
    for i in range(height):
        maze_info.append([-1]*width)
    maze_info[0][0] = 1
    priority_queue = [(1,0,0)]
    while priority_queue:
        dist, x, y = heappop(priority_queue)
        points = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        dist = maze_info[x][y] + 1
        for i,j in points:
            if i >= 0 and i < height and j >= 0 and j < width and maze[i][j] == 0:
                if maze_info[i][j] == -1 or maze_info[i][j] > dist:
                    maze_info[i][j] = dist
                    heappush(priority_queue, (maze_info[i][j], i, j))
    result = maze_info[-1][-1] if maze_info[-1][-1] != -1 else None
    for x, row in enumerate(maze):
        for y, node in enumerate(row):
            if node == 1:
                maze[x][y] = 0
                new_maze_info = copy.deepcopy(maze_info)
                points = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
                dist = None
                for i,j in points:
                    if i >= 0 and i < height and j >= 0 and j < width and maze[i][j] == 0 and new_maze_info[i][j] != -1:
                        dist = min(dist, new_maze_info[i][j] + 1) if dist else new_maze_info[i][j] + 1
                if not dist:
                    maze[x][y] = 1
                    continue
                new_maze_info[x][y] = dist
                priority_queue = [(dist, x, y)]
                while priority_queue:
                    dist, new_x, new_y = heappop(priority_queue)
                    points = [(new_x - 1, new_y), (new_x + 1, new_y), (new_x, new_y - 1), (new_x, new_y + 1)]
                    dist = new_maze_info[new_x][new_y] + 1
                    for i,j in points:
                        if i >= 0 and i < height and j >= 0 and j < width and maze[i][j] == 0:
                            if new_maze_info[i][j] == -1 or new_maze_info[i][j] > dist:
                                new_maze_info[i][j] = dist
                                heappush(priority_queue, (new_maze_info[i][j], i, j))
                if new_maze_info[-1][-1] != -1:
                    result = min(result, new_maze_info[-1][-1]) if result else new_maze_info[-1][-1]
                maze[x][y] = 1
    return result
