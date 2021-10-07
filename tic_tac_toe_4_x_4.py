
# laura_tic_tac_toe.py

import pygame
import sys

# color definitions
red = (255,0,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

# define window size and line thickness
window_x = 600
window_y = 600
line_thickness = 4

# open pygame window
def open_window():
    screen = pygame.display.set_mode((window_x,window_y))
    pygame.display.set_caption('Tic-Tac-Toe')
    return screen


# create game board
def create_board(screen):
    screen.fill(white)
    pygame.draw.rect(screen, black, (0, 0, window_x, window_y), line_thickness*4)
    pygame.draw.rect(screen, black, (0, 0, window_x, window_y/4), line_thickness)
    pygame.draw.rect(screen, black, (0, 0, window_x, window_y*2/4), line_thickness)
    pygame.draw.rect(screen, black, (0, 0, window_x,window_y*3/4), line_thickness)
    pygame.draw.rect(screen, black, (0, 0, window_x/4, window_y), line_thickness)
    pygame.draw.rect(screen, black, (0, 0, window_x*2/4, window_y), line_thickness)
    pygame.draw.rect(screen, black, (0, 0, window_x*3/4,window_y), line_thickness)
    
    pygame.display.update()

# map mouse click to grid
def map_to_grid(pos):
    x = pos[0]
    y = pos[1]
    #print("x: " + str(x) )
    #print("y: " + str(y) )
    if x < window_x / 4:
        if y < window_y / 4:
            region = 0
        elif (window_y/4 < y) and (y < window_y*2/4):
            region = 4
        elif (window_y*2/4 < y) and (y < window_y*3/4):
            region = 8
        else:
            region = 12
    elif (window_x/4 < x) and (x < window_x*2/4):
        if y < window_y/4:
            region = 1
        elif (window_y/4 < y) and (y < window_y*2/4):
            region = 5
        elif (window_y*2/4 < y) and (y < window_y*3/4):
            region = 9
        else:
            region = 13
    elif (window_x*2/4 < x) and (x < window_x * 3 / 4):
        if y < window_y / 4:
            region = 2
        elif (window_y/4 < y) and (y < window_y*2/4):
            region = 6
        elif (window_y*2/4 < y) and (y< window_y*3/4):
            region = 10
        else:
            region = 14
    else:
        if y < window_y / 4:
            region = 3
        elif (window_y/4 < y) and (y < window_y*2/4):
            region = 7
        elif (window_y*2/4 < y) and (y < window_y*3/4):
            region = 11
        else:
            region = 15
    return region
    
# place marker on grid
def place_on_grid(screen, region, player):
    
    font_size = 180
    font_family = 'Calibri'

    if player == "X":
        color = red
        offset_x = 50
        offset_y = 10
    if player == "O":
        color = blue
        offset_x = 40
        offset_y = 15
    
    myfont = pygame.font.SysFont(font_family, font_size)
    textsurface = myfont.render(player, True, color) # text, anti-alias, color 
    
    if region == 0:
        pass
    if region == 1:
        offset_x = offset_x + window_x / 4
    if region == 2:
        offset_x = offset_x + window_x*2/4
    if region == 3:
        offset_x = offset_x + window_x*3/4
    if region == 4:
        offset_y = offset_y + window_y/4
    if region == 5:
        offset_x = offset_x + window_x/4
        offset_y = offset_y + window_y/4
    if region == 6:
        offset_x = offset_x + (window_x*2/4)
        offset_y = offset_y + window_y/4
    if region == 7:
        offset_x = offset_x + (window_x*3/4)
        offset_y = offset_y + window_y/4
    if region == 8:
        offset_y = offset_y + (window_y*2/4)
    if region == 9:
        offset_x = offset_x + window_x/4
        offset_y = offset_y + (window_y*2/4)
    if region == 10:
        offset_x = offset_x + (window_x*2/4)
        offset_y = offset_y + (window_y*2/4)
    if region == 11:
        offset_x = offset_x + (window_x*3/4)
        offset_y = offset_y + (window_y*2/4)
    if region == 12:
        offset_y = offset_y + (window_y*3/4)
    if region == 13:
        offset_x = offset_x + window_x/4
        offset_y = offset_y + (window_y*3/4)
    if region == 14:
        offset_x = offset_x + (window_x*2/4)
        offset_y = offset_y + (window_y*3/4)
    if region == 15:
        offset_x = offset_x + (window_x*3/4)
        offset_y = offset_y + (window_y*3/4)
        
    screen.blit(textsurface,(offset_x, offset_y))
    pygame.display.update() 

# return opponent's marker
def get_opponent(player):
    if player == "X":
        return "O"
    else:
        return "X"

# find empty regions
def find_empty_regions(state):
    empty_regions = []
    for i in range(0, len(state)):
        if (state[i] != "X") and (state[i] != "O"):
            empty_regions.append(state[i])
    return empty_regions

# search for terminal state
def terminal_test(state, player):
    empty_regions = find_empty_regions(state)
    if (state[0] == player and state[1] == player and state[2] == player and state[3] == player) or \
       (state[4] == player and state[5] == player and state[6] == player and state[7] == player) or \
       (state[8] == player and state[9] == player and state[10] == player and state[11] == player) or \
       (state[12] == player and state[13] == player and state[14] == player and state[15] == player) or \
       (state[0] == player and state[4] == player and state[8] == player and state[12] == player) or \
       (state[1] == player and state[5] == player and state[9] == player and state[13] == player) or \
       (state[2] == player and state[6] == player and state[10] == player and state[14] == player) or \
       (state[3] == player and state[7] == player and state[11] == player and state[15] == player) or \
       (state[0] == player and state[5] == player and state[10] == player and state[15] == player) or \
       (state[3] == player and state[6] == player and state[9] == player and state[12] == player):
        print("Game over! " + player + " wins!")
        return True
    elif len(empty_regions) == 0:
        print("Game over! Draw!")
        return True

def choose_ai():
    while True:
        sys.stdout.write("Choose AI. [1/2/3/4]\n1. Random\n2. Minimax\n3. Full Alpha-Beta\n4. Alpha-Beta with Cutoff\n> ")
        answer = input().lower()
        if answer == "1":
            return 1
        elif answer == "2":
            return 2
        elif answer == "3":
            return 3
        elif answer == "4":
            return 4
        else:
            sys.stdout.write("Please respond with '1', '2', '3', or '4'.\n")

# ask user if they'd like to play again
def play_again():
    while True:
        pygame.display.update()
        sys.stdout.write("Play again? [Y/N]\n> ")
        answer = input().lower()
        if (answer == "y"):
            terminal_state = True
            return terminal_state
        elif (answer == "n"):
            sys.exit(0)
        else:
            sys.stdout.write("Please respond with 'Y' or 'N'.\n")

