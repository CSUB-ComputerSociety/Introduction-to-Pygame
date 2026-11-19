import random
import pygame

#This code has been copied from the pygame example website
# https://coddy.tech/docs/pygame/pygame-examples

pygame.init() #initialize a pygame instance
screen = pygame.display.set_mode((480, 360)) #parameters (height, width) for size 

pygame.display.set_caption("Catch") #sets the name of the window
clock = pygame.time.Clock() #initializes a clock 
font = pygame.font.Font(None, 32) #sets a font to use for the words
#32 is the size of the font for pixels

def new_game():
    return pygame.Rect(200, 330, 80, 16), [], 0, 3  #everytime a player dies, this is called to start a new game
#the parameters include creating a new rectangle for the basket (x,y, width in pixels, and height in pixel)
# [] empty list that holds the falling coins
# 0 the starting score
# 3 the starting number of lives 


basket, coins, score, lives = new_game()
playing = True #the game is active

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #crucial always in every pygame example
            raise SystemExit
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not playing:
            basket, coins, score, lives = new_game()
            playing = True	#essentially if player dies and hits the space key, a new_game is formed
#in the if statement, all conditions must be met to start a new game
#reset the basket,coins, score, lives to starting for new game
#Question for challenge: Can you add another key to take back to home screen
    if playing:
	#get keyboard state
        keys = pygame.key.get_pressed()
	#calculating method for moving the basket horizontally
	#keys[pygame.K_RIGHT] if true will act as 1, false will be 0
	#Strictly right (1-0) * 7 pixels
	#strictly left( (0-1) * 7 pixels , negative so opposite direction
        basket.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 7
        basket.clamp_ip(screen.get_rect()) 
	#strictly for keeping the basket inside the screen
        if random.random() < 0.03: #creating a random decimal between 0 and 1
# the 0.03 acts as 3% meaning there is a 3% chance of a coin spawning in
#pygame.Rect(x,y,width,height)
#random.randint(0,460) random left-edge x coordinate including both - and 460
#-20 is top edge y coordinate
#20 is coin width
#20 is coin height
            coins.append(pygame.Rect(random.randint(0, 460), -20, 20, 20))
        for coin in coins[:]:
#increase the coin's y-coordinate by 4 pixels
            coin.y += 4
            if coin.colliderect(basket):
                coins.remove(coin)
                score += 1
            elif coin.top > 360:
                coins.remove(coin)
                lives -= 1
        playing = lives > 0
#logic, if the coin is in bag, remove coin and add a point, else remove coin and remove a life
#paint the screen this color, can you add an image?
    screen.fill((25, 30, 55))
    for coin in coins: #drawing the coin
        pygame.draw.ellipse(screen, (255, 210, 60), coin)
    pygame.draw.rect(screen, (120, 200, 255), basket, border_radius=6)
    screen.blit(font.render(f"Score {score}   Lives {lives}", True, "white"), (10, 10))
    if not playing:
        msg = font.render("Game over. Press Space", True, (255, 120, 120))
        screen.blit(msg, msg.get_rect(center=(240, 180)))
    pygame.display.flip()
    clock.tick(60)
