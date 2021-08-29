import pygame
import matplotlib.pyplot as plt
import numpy as np


class Node():


    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.c = 0
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    time = 0

    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    open_list = []
    closed_list = []

    open_list.append(start_node)

    while len(open_list) > 0:
        if time >= 5000:
            return -1
        time += 1

        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f <= current_node.f and item.c <= current_node.c + .5:
                current_node = item
                current_index = index


        open_list.pop(current_index)
        closed_list.append(current_node)


        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
                print(current_node.c, ' ', time)

            return path[::-1]


        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:  # Adjacent squares


            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])


            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (
                    len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                continue

            node_contage = current_node.c
            for x in range(-2, 2):
                for y in range(-2, 2):
                    if maze[node_position[0] + x][node_position[1] + y] != -1:
                        node_contage = + maze[node_position[0] + x][node_position[1] + y] * (
                                    1 / ((abs(x) ** 2 + abs(y) ** 2 + .01) ** (1 / 2)))

            if maze[node_position[0]][node_position[1]] >= 4 + (time / 100) or maze[node_position[0]][
                node_position[1]] == -1:
                continue
            if node_contage > 4 + (time / 100):
                continue

            new_node = Node(current_node, node_position)
            new_node.c = node_contage

            children.append(new_node)


        for child in children:

            for closed_child in closed_list:
                if child == closed_child:
                    continue

            child.g = current_node.g + 1
            child.c = node_contage
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                        (child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h + (node_contage)

            for open_node in open_list:
                if (child == open_node and child.g > open_node.g) and child.c < open_node.c:  # cambio
                    continue

            open_list.append(child)




def juegoPygame(grid, patha):
    pygame.init()
    # create a screen:
    screen = pygame.display.set_mode((600, 600))
    done = False
    a = [1, 10]
    b = [1, 11]
    # (red,green,blue)
    c = (255, 2, 2)

    # never ending loop now:
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        for x in range(0, 600, 50):
            pygame.draw.line(screen, c, (1, x), (600, x), 2)
            pygame.draw.line(screen, c, (x, 1), (x, 600), 2)


        for y in range(len(grid)):
                # esto imprime a las personas en el grid
            for x in range(len(grid)):
                if grid[x][y] != 0:
                    colorsito = 0
                    if grid[x][y] < 3 and grid[x][y] >= 0:

                        pygame.draw.circle(screen, (0, 255, 0), (x * 50 + 25, y * 50 + 25), 15)

                    elif grid[x][y] >= 3 and grid[x][y] < 7:

                        pygame.draw.circle(screen, (250, 147, 0), (x * 50 + 25, y * 50 + 25), 15)
                    else:

                        pygame.draw.circle(screen, (255, 0, 0), (x * 50 + 25, y * 50 + 25), 15)


        for x in range(len(pathf)):
            # print(grid[pathf[x][0]][pathf[x][1]])
            grid[pathf[x][0]][pathf[x][1]] = 10
            pygame.draw.circle(screen, (255,255,255), (pathf[x][0] * 50 + 25, pathf[x][1] * 50 + 25), 15)








        pygame.display.update()
#INICIO DEL PROGRAMA
grid = np.random.choice([1,0, 5,0,0,0,0,10,0,3,0,0, 0,0,0], size=(30, 30))
for x  in range(0,len(grid)):
  for y in range(0,len(grid)):
    count = 0
    for a in range(-2,2):
      for b in range(-2,2):
        if x+a < (len(grid) - 1) and x+a > 0 and y+b < (len(grid[0]) -1) and y+b > 0:
          if grid[x+a][y+b] == 0:
            count+=1
    if count == 0 :
        grid[x][y] = 0
for x in range(0,10):
  grid[x][29] = x

inicio = (0,0)
fin = (18,12)
fpath = np.zeros((30,30))
pathf = astar(grid,inicio, fin)
plt.matshow(grid)
print(pathf)
if pathf != None and pathf != -1:
  print(len(pathf))
  for x in range(len(pathf)):

    grid[pathf[x][0]][pathf[x][1]] = 10

plt.matshow(grid)
# plt.show()

print(grid)
juegoPygame(grid,pathf)