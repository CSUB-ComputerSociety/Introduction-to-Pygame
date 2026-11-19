import random  #for choosing random food positions
import pygame

#This script has been copied from https://coddy.tech/docs/pygame/pygame-examples
#Comments have been made for guide to workshop

pygame.init()
CELL, COLS, ROWS = 20, 24, 18
#For one line, Cell = 20 meaning it is 20 pixels wide and 20 pixels tall
#Cols = 24 columms
#Rows = 10 rows

screen = pygame.display.set_mode((CELL * COLS, CELL * ROWS)) #set the screen in respect to the CELL< COLS, Rows
pygame.display.set_caption("Snake") #set name for window
clock = pygame.time.Clock() #Set clock
font = pygame.font.Font(None, 30) #Set Font for text

#Create the snake as a list of (column, row) coordinate pairs.
# each pair represents one segment occupyting one grid cell
# (5,9) = the head stored at index 0
#(4,9) the next body segment) stored at 1
#(3,9) = the last segment or tail stored at index 2
snake = [(5, 9), (4, 9), (3, 9)]
direction = (1, 0) #initial movement to the right cell
food = (15, 9) #fist food placement
frame = 0 #counter that tracks how many frames have passed
alive = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            # Create a dictionary mapping arrow keys to movement directions.
            #
            # pygame.K_UP:    (0, -1) = move up one row.
            # pygame.K_DOWN:  (0, 1)  = move down one row.
            # pygame.K_LEFT:  (-1, 0) = move left one column.
            # pygame.K_RIGHT: (1, 0)  = move right one column.
            #
            # Each dictionary entry has the form key: value.
            # This statement continues onto the next line because
            # the dictionary's braces have not closed yet.
            turns = {pygame.K_UP: (0, -1), pygame.K_DOWN: (0, 1),
                     pygame.K_LEFT: (-1, 0), pygame.K_RIGHT: (1, 0)}

            # Look up the pressed key in the turns dictionary.
            # event.key identifies which key was pressed.
            # If it is an arrow key, new receives its direction tuple.
            # If the key is absent, .get(...) returns None.
            new = turns.get(event.key)
            # Accept the direction only if:
            #
            # 1. new has a value, meaning an arrow key was pressed.
            #
            # 2. The new direction is not exactly opposite the current one.
            #    new[0] = requested horizontal movement.
            #    new[1] = requested vertical movement.
            #    -direction[0] = opposite current horizontal movement.
            #    -direction[1] = opposite current vertical movement.
            #
            # The "or" means at least one component must differ from
            # the opposite direction. An exact reversal makes both
            # comparisons False, so the direction is rejected.
            #
            # Example when moving right, direction = (1, 0):
            # Request left, new = (-1, 0):
            # new and (-1 != -1 or 0 != 0)
            # -> new and (False or False)
            # -> False, so the turn is rejected.
            #
            # Request up, new = (0, -1):
            # new and (0 != -1 or -1 != 0)
            # -> new and (True or True)
            # -> True, so the turn is accepted.
            #
            # Python checks "new" first, avoiding indexing None.
            if new and (new[0] != -direction[0] or new[1] != -direction[1]):
                direction = new

    frame += 1
    # Move the snake only when both conditions are true:
    # alive = the snake has not collided with anything.
    # frame % 7 == 0 = the frame number is divisible by 7.
    #
    # % gives the remainder after division.
    # For example, 14 % 7 is 0, but 15 % 7 is 1.
    #
    # This updates the snake on frames 7, 14, 21, and so on.
    # At 60 frames per second, it moves about 60 / 7 = 8.57 cells per second.
    if alive and frame % 7 == 0:
        # Calculate the proposed position of the next head.
        #
        # snake[0] = the current head's (column, row) tuple.
        # snake[0][0] = the current head's column.
        # snake[0][1] = the current head's row.
        # direction[0] = horizontal change.
        # direction[1] = vertical change.
        #
        # Example:
        # If the head is (5, 9) and direction is (1, 0):
        # head = (5 + 1, 9 + 0) = (6, 9).
        #
        # This calculates a position without changing the snake list yet.
        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        if head in snake or not (0 <= head[0] < COLS and 0 <= head[1] < ROWS):
            alive = False
        else:
            snake.insert(0, head)
            if head == food:
                while food in snake:
                    # Generate a new random (column, row) position.
                    # random.randrange(COLS) chooses 0 through 23.
                    # random.randrange(ROWS) chooses 0 through 17.
                    # The upper limit is excluded in randrange(...).
                    food = (random.randrange(COLS), random.randrange(ROWS))
            else:
                snake.pop()

    screen.fill((20, 30, 20))
    pygame.draw.rect(screen, (240, 80, 80), (food[0] * CELL, food[1] * CELL, CELL, CELL), border_radius=6)
    for x, y in snake:
        pygame.draw.rect(screen, (110, 220, 110), (x * CELL + 1, y * CELL + 1, CELL - 2, CELL - 2), border_radius=4)
    screen.blit(font.render(f"Length {len(snake)}", True, "white"), (8, 8))
    if not alive:
        screen.blit(font.render("Game over", True, (255, 140, 140)), (190, 170))
    pygame.display.flip()
    clock.tick(60)
#improvements
# 1. add a restart control, either space key or not, see if you can
#	replicate the same logic from catch the coins
