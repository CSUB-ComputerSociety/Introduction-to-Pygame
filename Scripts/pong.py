import pygame

#This script has been copied from
#https://coddy.tech/docs/pygame/pygame-examples
#Comments have been made to help understand code

pygame.init()
screen = pygame.display.set_mode((480, 320))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 48)

player = pygame.Rect(16, 130, 10, 60) #pygame.Rect(left, top, width, height)
cpu = pygame.Rect(454, 130, 10, 60) #computer paddle
ball = pygame.Rect(234, 154, 12, 12)
velocity = pygame.Vector2(4, 3) #two component vector that stores ball's movement per frame
#4 = horizontal movement: positve values move to the right
#3 move vertically, positve values move down
#negative x moves left, and negative y moves up
score = [0, 0]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit

    keys = pygame.key.get_pressed()
#move the players paddle vertically 
#the true behaves as 1 and false as 0
    player.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 6
    player.clamp_ip(screen.get_rect())
#keep paddle in window
#check the paddles center
    if cpu.centery < ball.centery - 10:
        cpu.y += 4
    elif cpu.centery > ball.centery + 10:
        cpu.y -= 4
    cpu.clamp_ip(screen.get_rect())

    ball.x += velocity.x
    ball.y += velocity.y
    if ball.top <= 0 or ball.bottom >= 320:
        velocity.y = -velocity.y
    if ball.colliderect(player) and velocity.x < 0:
        velocity.x = -velocity.x * 1.05
    if ball.colliderect(cpu) and velocity.x > 0:
        velocity.x = -velocity.x * 1.05
    if ball.right < 0 or ball.left > 480:
        score[ball.left > 480] += 1
        ball.center = (240, 160)
        velocity.update(4 if ball.left > 480 else -4, 3)

    screen.fill((15, 15, 25))
    pygame.draw.line(screen, (60, 60, 80), (240, 0), (240, 320), 2)
    for paddle in (player, cpu):
        pygame.draw.rect(screen, "white", paddle)
    pygame.draw.ellipse(screen, (255, 220, 90), ball)
    screen.blit(font.render(f"{score[0]}   {score[1]}", True, "white"), (196, 10))
    pygame.display.flip()
    clock.tick(60)
