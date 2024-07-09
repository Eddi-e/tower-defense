

import random
import pygame



def find_next_to(coord):
    coord_x = coord[0]
    coord_y = coord[1]
    return [(coord_x+1,coord_y),(coord_x-1,coord_y),(coord_x,coord_y+1),(coord_x,coord_y-1)]

def check_if_not_in_grid(coord,grid_size):
    if coord[0] <= -1 or coord[1] <= -1 or coord[0] >= grid_size or coord[1] >= grid_size:
        return True
    else:
        return False

def find_path(grid_size,start,end):
    path_search = True
    path = [start]
    dead_end = []
    while path_search:
        possible_next = find_next_to(path[-1])
        if end in possible_next:
            path_search = False
            path.append(end)
            return path
        else:
            for x in possible_next[:]:
                if check_if_not_in_grid(x,grid_size) or x in path or x in dead_end:
                    possible_next.remove(x)
            if len(possible_next) == 0:
                dead_end.append(path.pop())
            else:
                path.append(possible_next[random.randrange(0,len(possible_next))])
        
def make_grid(size):
    return([[0 for i in range(size)] for j in range(size)])

def get_start_and_end(grid_size):
    border_coords = [(0,x) for x in range(grid_size)]+[(grid_size-1,x) for x in range(grid_size)]+[(x,0) for x in range(1,grid_size-1)]+[(x,grid_size-1) for x in range(1,grid_size-1)]
    
    start = border_coords[random.randrange(0,len(border_coords))]
    end_check = True
    while end_check:
        end = border_coords[random.randrange(0,len(border_coords))]
        if end != start:
            end_check = False
    return (start,end)


class Game_rect():
    def __init__(self,size,top_left_corner_pos):
        self.rect = pygame.Rect(top_left_corner_pos[0],top_left_corner_pos[1],size,size)
        self.top_left_corner_pos = top_left_corner_pos
        self.colour = "brown"
    def draw_rect(self,surface):
        pygame.draw.rect(surface,self.colour,self.rect)

class Path_rect(Game_rect):
    def __init__(self,size,top_left_corner_pos,order):
        Game_rect.__init__(self,size,top_left_corner_pos)
        self.order = order
        self.colour = "black"
    


def make_grid_rect(grid,size):
    starting_coord = (100,100)
    rect = []
    for row_num,row in enumerate(grid):
        for item_num,item in enumerate(row):
            if item == 0:
                rect.append(Game_rect(size,(starting_coord[0]+size*item_num,starting_coord[1]+size*row_num)))
            else:
                rect.append(Path_rect(size,(starting_coord[0]+size*item_num,starting_coord[1]+size*row_num),item))
    return (rect)




def main():
    grid_size = 10
    grid = make_grid(grid_size)


    start_and_end = get_start_and_end(grid_size)
    start = start_and_end[0]
    end = start_and_end[1]

    print(start)
    print(end)
    path = find_path(grid_size,start,end)

    print(path)

    for count, coord in enumerate(path):
        grid[coord[0]][coord[1]] = count+1

    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in grid]))


    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    running = True
    square_size = int(400/grid_size)

    screen.fill("white")
    rectangle_grid = make_grid_rect(grid,square_size)

    for rectangle in rectangle_grid:
        rectangle.draw_rect(screen)

    while running:
        #poll events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
        #render here
        clock.tick(60)
    pygame.quit()

    return 0

if __name__ == "__main__":
    main()