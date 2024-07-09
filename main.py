

import random


def main():
    grid_size = 16
    grid = [[0 for i in range(grid_size)] for j in range(grid_size)]

    bordercoords = [(0,x) for x in range(grid_size)]+[(15,x) for x in range(grid_size)]+[(x,0) for x in range(1,grid_size-1)]+[(x,15) for x in range(1,grid_size-1)]

    start = bordercoords[random.randint(0,len(bordercoords))]
    endCheck = True
    while endCheck == True:
        end = bordercoords[random.randint(0,len(bordercoords))]
        if end != start:
            endCheck = False

    for coord in bordercoords:
        grid[coord[0]][coord[1]] = -1

    grid[start[0]][start[1]] = 1
    grid[end[0]][end[1]] = 1

    print(grid)
    return 0

if __name__ == "__main__":
    main()