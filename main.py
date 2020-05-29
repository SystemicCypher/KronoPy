import sys, pygame
pygame.init()

screen = pygame.display.set_mode((1280, 760))
clock = pygame.time.Clock()
done = False

x = 30
y = 30

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            done = True
            sys.exit()
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3

    screen.fill((128, 0, 0))
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x, y,  60, 60))
    pygame.display.flip()
    clock.tick(60)