import numpy as np
import svgwrite

def manhattan_convex_hull(grid_set):
    min_x = float('inf')
    max_x = float('-inf')
    min_y = float('inf')
    max_y = float('-inf')
    for x in grid_set:
        min_x = min(min_x,x[0])
        max_x = max(max_x,x[0]+1)
        min_y = min(min_y,x[1])
        max_y = max(max_y,x[1]+1)
    return (min_x,min_y,max_x-min_x,max_y-min_y)
grid = np.zeros((10,4))
GRID_SPACING = 10
GRID_OFFSET = 8
mapping = {'#':{(0,x) for x in range(10)},
           'S':{(1,0),(2,0)},
           'T':{(1,1)},
           'P':{(2,1)},
           'H':{(1,3)},
           'K':{(2,1)},
           'W':{(2,2)},
           'R':{(2,3)},
           '*':{(1,4),(2,4)},
           'A':{(3,2)},
           'O':{(3,3)},
           'F':{(1,5)},
           'r':{(2,5)},
           'p':{(1,6)},
           'B':{(2,6)},
           'L':{(1,7)},
           'G':{(2,7)},
           't':{(1,8)},
           'D':{(1,9)},
           's':{(2,8)},
           'Z':{(2,9)},
           'E':{(3,5)},
           'U':{(3,6)}}
for key in mapping:
    mapping[key] = {(x[1],x[0]) for x in mapping[key]}
def write_svg(filename='chorda.svg', chord=''):
    dwg = svgwrite.Drawing(filename, profile='tiny')
    for key in mapping:
        hull = manhattan_convex_hull(mapping[key])
        color = 'white'
        if key in chord:
            color = 'black'
        dwg.add(dwg.rect(insert=(hull[0]*GRID_SPACING+GRID_OFFSET,
          hull[1]*GRID_SPACING+GRID_OFFSET),size=(hull[2]*GRID_SPACING,
          hull[3]*GRID_SPACING), stroke=svgwrite.rgb(10, 10, 16, '%'),
          fill=color))
    dwg.save()
write_svg(chord='KEB')
