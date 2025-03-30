import math

import pygame

FRACTAL = "FT"
ALL_FRACTALS = ["ST", "FT"]
while FRACTAL == "LS":
    FRACTAL = input("What fractal would you like to see? (type ls to see list) ").upper()
    if FRACTAL == "LS":
        print("  - ST (Sierpinski Triangle)\n  - FT (Fractal Tree)\n")
    elif FRACTAL not in ALL_FRACTALS:
        print("Sorry, the fractal \"" + FRACTAL + "\" cannot be drawn. Make sure you have entered the abbreviated name.\n")
        FRACTAL = "LS"

# Initiate Pygame
pygame.init()

# Create Screen with specified dimensions (2 parentheses needed)
WIDTH = 960
HEIGHT = 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
SHORTEST_SIDE = min(WIDTH, HEIGHT)

# Initialize Offset Variables (add to x/y value to center in screen)
CENTER_X = WIDTH/2
CENTER_Y = HEIGHT/2

# Title
pygame.display.set_caption("Fractals")
pygame.display.update()

# Drawing functions
def draw_triangle (x1, y1, x2, y2, x3, y3, color):
    pygame.draw.line(SCREEN, color, (x1, y1), (x2, y2), width=1)
    pygame.draw.line(SCREEN, color, (x2, y2), (x3, y3), width=1)
    pygame.draw.line(SCREEN, color, (x1, y1), (x3, y3), width=1)

def draw_sierpinski_triangle (width, height, x, y, color, min_side):
    # Draw outer triangle
    draw_triangle(x, y+height, x+width/2, y, x+width, y+height, color)
    # Draw inner triangles
    if width/4 < min_side:
        return
    draw_sierpinski_triangle(width/2, height/2, x, y+height/2, color, min_side)
    draw_sierpinski_triangle(width/2, height/2, x+width/4, y, color, min_side)
    draw_sierpinski_triangle(width/2, height/2, x+width/2, y+height/2, color, min_side)

def draw_fractal_tree (x, y, branch_len, angle, branch_angle, shortening_factor, color, min_side):
    # Draw main line
    new_x = x+math.cos(angle)*branch_len
    new_y = y-math.sin(angle)*branch_len
    pygame.draw.line(SCREEN, color, (x, y), (new_x, new_y), width=1)
    # Draw branching lines
    if branch_len*shortening_factor < min_side:
        return
    draw_fractal_tree(new_x, new_y, branch_len * shortening_factor, angle - branch_angle, branch_angle,
                      shortening_factor, color, min_side)
    draw_fractal_tree(new_x, new_y, branch_len * shortening_factor, angle + branch_angle, branch_angle,
                      shortening_factor, color, min_side)

running = True
while running:

    # Update Screen Color
    SCREEN.fill((255, 255, 255))

    # Check for Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if FRACTAL == "ST":
        ST_WIDTH = SHORTEST_SIDE
        ST_HEIGHT = ST_WIDTH*math.sqrt(3)/2
        draw_sierpinski_triangle(ST_WIDTH, ST_HEIGHT, CENTER_X - ST_WIDTH/2, CENTER_Y - ST_HEIGHT/2, (0, 0, 0), 2)
    elif FRACTAL == "FT":
        draw_fractal_tree(CENTER_X, HEIGHT-50, 150, math.pi/2, math.pi/4, 0.75, (0, 0, 0), 4)

    # Update Display
    pygame.display.update()