

import random
import pygame
import sys



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
        self.colour = "gray"
    def draw_path_top_bottom(self,surface):
        size_zero = self.rect.size[0]
        size_one = self.rect.size[1]
        pygame.draw.rect(surface,self.colour,self.rect,width=1)
        #draws top line
        pygame.draw.line(surface,"black",self.top_left_corner_pos,(self.top_left_corner_pos[0]+size_zero,self.top_left_corner_pos[1]),3)
        #draws bottom line
        pygame.draw.line(surface,"black",(self.top_left_corner_pos[0],self.top_left_corner_pos[1]+size_one),(self.top_left_corner_pos[0]+size_zero,self.top_left_corner_pos[1]+size_one),3)
    def draw_path_left_right(self,surface):
        size_zero = self.rect.size[0]
        size_one = self.rect.size[1]
        pygame.draw.rect(surface,self.colour,self.rect,width=1)
        #draws left line
        pygame.draw.line(surface,"black",self.top_left_corner_pos,(self.top_left_corner_pos[0],self.top_left_corner_pos[1]+size_one),3)
        #draws right lime
        pygame.draw.line(surface,"black",(self.top_left_corner_pos[0]+size_zero,self.top_left_corner_pos[1]),(self.top_left_corner_pos[0]+size_zero,self.top_left_corner_pos[1]+size_one),3)
    def draw_path_top_right(self,surface):
        size_zero = self.rect.size[0]
        size_one = self.rect.size[1]
        pygame.draw.rect(surface,self.colour,self.rect,width=1)

        pygame.draw.line(surface,"black",self.top_left_corner_pos,(self.top_left_corner_pos[0]+size_zero,self.top_left_corner_pos[1]),3)
        pygame.draw.line(surface,"black",(self.top_left_corner_pos[0]+size_zero,self.top_left_corner_pos[1]),(self.top_left_corner_pos[0]+size_zero,self.top_left_corner_pos[1]+size_one),3)
    def draw_path_top_left(self,surface):
        pygame.draw.rect(surface,self.colour,self.rect,width=1)
        size_zero = self.rect.size[0]
        size_one = self.rect.size[1]
        pygame.draw.line(surface,"black",self.top_left_corner_pos,(self.top_left_corner_pos[0]+size_zero,self.top_left_corner_pos[1]),3)
        pygame.draw.line(surface,"black",self.top_left_corner_pos,(self.top_left_corner_pos[0],self.top_left_corner_pos[1]+size_one),3)
    def draw_path_bottom_left(self,surface):
        pygame.draw.rect(surface,self.colour,self.rect,width=1)

        size_zero = self.rect.size[0]
        size_one = self.rect.size[1]
        pygame.draw.line(surface,"black",(self.top_left_corner_pos[0],self.top_left_corner_pos[1]+size_one),(self.top_left_corner_pos[0]+size_zero,self.top_left_corner_pos[1]+size_one),3)
        pygame.draw.line(surface,"black",self.top_left_corner_pos,(self.top_left_corner_pos[0],self.top_left_corner_pos[1]+size_one),3)
    def draw_path_bottom_right(self,surface):
        pygame.draw.rect(surface,self.colour,self.rect,width=1)
        size_zero = self.rect.size[0]
        size_one = self.rect.size[1]
        pygame.draw.line(surface,"black",(self.top_left_corner_pos[0],self.top_left_corner_pos[1]+size_one),(self.top_left_corner_pos[0]+size_zero,self.top_left_corner_pos[1]+size_one),3)
        pygame.draw.line(surface,"black",(self.top_left_corner_pos[0]+size_zero,self.top_left_corner_pos[1]),(self.top_left_corner_pos[0]+size_zero,self.top_left_corner_pos[1]+size_one),3)


def make_grid_rect(grid,size):
    starting_coord = (100,100)
    grid_rect = []
    path_rect = []
    for row_num,row in enumerate(grid):
        for item_num,item in enumerate(row):
            if item == 0:
                grid_rect.append(Game_rect(size,(starting_coord[0]+size*item_num,starting_coord[1]+size*row_num)))
            else:
                path_rect.append(Path_rect(size,(starting_coord[0]+size*item_num,starting_coord[1]+size*row_num),item))
    rect = (grid_rect,path_rect)
    return (rect)

def draw_rectangle(rectangle_grid,screen):
    for rectangle in rectangle_grid:
        rectangle.draw_rect(screen)

def draw_path(path_grid,screen):
    prev_coords = (-1,-1)
    path_length_minus_one = len(path_grid)-1
    for path_num,path in enumerate(path_grid):
        path_corner = path.top_left_corner_pos
        print(path_corner)
        if path_num == 0:
            next_path = path_grid[path_num+1]
            next_path_coords = next_path.top_left_corner_pos
            if path_corner[0] == 100:
                if next_path_coords[1] < path_corner[1]:
                    path.draw_path_bottom_right(screen)
                elif next_path_coords[1] > path_corner[1]:
                    path.draw_path_top_right(screen)
                else:
                    path.draw_path_top_bottom(screen)
            elif path_corner[0] == 460:
                if next_path_coords[1] < path_corner[1]:
                    path.draw_path_bottom_left(screen)
                elif next_path_coords[1] > path_corner[1]:
                    path.draw_path_top_left(screen)
                else:
                    path.draw_path_top_bottom(screen)
            elif path_corner[1] == 100:
                if next_path_coords[0] > path_corner[0]:
                    path.draw_path_bottom_left(screen)
                elif next_path_coords[0] < path_corner[0]:
                    path.draw_path_bottom_right(screen)
                else:
                    path.draw_path_left_right(screen)
            else:
                if next_path_coords[0] > path_corner[0]:
                    path.draw_path_top_left(screen)
                elif next_path_coords[0] < path_corner[0]:
                    path.draw_path_top_right(screen)
                else:
                    path.draw_path_left_right(screen)
        elif path_num == path_length_minus_one:
            if path_corner[0] == 100:
                if path_corner[1] > prev_coords[1]:
                    path.draw_path_bottom_right(screen)
                elif path_corner[1] < prev_coords[1]:
                    path.draw_path_top_right(screen)
                else:
                    path.draw_path_top_bottom(screen)
            elif path_corner[0] == 460:
                if path_corner[1] > prev_coords[1]:
                    path.draw_path_bottom_left(screen)
                elif path_corner[1] < prev_coords[1]:
                    path.draw_path_top_left(screen)
                else:
                    path.draw_path_top_bottom(screen)
            elif path_corner[1] == 100:
                if  path_corner[0] < prev_coords[0]:
                    path.draw_path_bottom_left(screen)
                elif path_corner[0] > prev_coords[0]:
                    path.draw_path_bottom_right(screen)
                else:
                    path.draw_path_left_right(screen)
            else:
                if path_corner[0] < prev_coords[0]:
                    path.draw_path_top_left(screen)
                elif path_corner[0] > prev_coords[0]:
                    path.draw_path_top_right(screen)
                else:
                    path.draw_path_left_right(screen)
        else:
            next_path = path_grid[path_num+1]
            next_path_coords = next_path.top_left_corner_pos
            if prev_coords[0] < next_path_coords[0]:
                if prev_coords[1] < next_path_coords[1]:
                    if path_corner[1]>prev_coords[1]:
                        path.draw_path_bottom_left(screen)
                    else:
                        path.draw_path_top_right(screen)
                elif prev_coords[1] > next_path_coords[1]:
                    if path_corner[1]<prev_coords[1]:
                        path.draw_path_top_left(screen)
                    else:
                        path.draw_path_bottom_right(screen)
                else:
                    path.draw_path_top_bottom(screen)
            elif prev_coords[0] > next_path_coords[0]:
                if prev_coords[1] < next_path_coords[1]:
                    if path_corner[1]>prev_coords[1]:
                        path.draw_path_bottom_right(screen)
                    else:
                        path.draw_path_top_left(screen)
                elif prev_coords[1] > next_path_coords[1]:
                    if path_corner[1]<prev_coords[1]:
                        path.draw_path_top_right(screen)
                    else:
                        path.draw_path_bottom_left(screen)
                else:
                    path.draw_path_top_bottom(screen)
            else:
                path.draw_path_left_right(screen)

        prev_coords = path_corner
            


class enemy():
    def __init__(self,health,position,speed,size,goal,path):
        self.path = path
        self.health(health)
        self.position = position
        self.speed = speed
        self.goal = goal
        self.colour = "blue"
        self.size = size
        self.path = path
        self.counter = 0

    def move(self):
        self.position[0] = self.position[0]+self.speed[0]
        self.position[1] = self.position[1]+self.speed[1]
        if self.position == self.goal:
            self.find_new_speed()

    
    def find_new_speed(self):
        if self.counter == len(self.path):
            pass


    
    def draw(self,screen):
        pygame.draw.circle(screen,self.colour,self.position,self.size)
        


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
    round_number = 0
    font = pygame.font.SysFont('Arial',20)

    screen.fill("white")
    rectangle_grid_tuple = make_grid_rect(grid,square_size)
    rectangle_grid = rectangle_grid_tuple[0]
    path_grid = rectangle_grid_tuple[1]
    sorted_path_grid = sorted(path_grid,key=lambda x: x.order)

    print(sorted_path_grid)

    draw_rectangle(rectangle_grid,screen)
    draw_path(sorted_path_grid,screen)

    font_screen = font.render("Round:   "+str(round_number),True,"black")
    screen.blit(font_screen,(100,50))

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