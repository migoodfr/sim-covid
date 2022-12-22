import pygame
import random

from circle import Circle

# constants
WIDTH = 1270
HEIGHT = 720
FPS = 60
BACKGROUND_COLOR = (255, 255, 255)
NBR_CIRCLE = 50


# setup pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sim Covid")
clock = pygame.time.Clock()



# objects declaration
c_group = []
i_group = []

# create all circle not infected and put them in the group of sprite circle
for circle in range(NBR_CIRCLE):
    x = random.randint(5, (WIDTH - 40)) 
    y = random.randint(5, (HEIGHT - 40))
    c_group.append(Circle(x, y, infected=False))



# create the first infected of the game and put it in the group of sprite infected
i_group.append(Circle(x=random.randint(5, (WIDTH - 40)), y=random.randint(5, (HEIGHT - 40)), infected=True))

# main function
def update(screen):
    circle_touched = 0
    touched = False
    
    # update all the circles 
    for c in c_group:
        c.update(screen)
        c.check_collision(WIDTH, HEIGHT)

    for i in i_group:
        i.update(screen)
        i.check_collision(WIDTH, HEIGHT)

    

    # get the circle who is infected
    for c in c_group:
        for i in i_group:
        
            if i.check_infection(i.x, i.y, c.x, c.y):
                circle_touched = c_group.index(c)
                touched = True
                break

    # infect the circle
    if (touched):
        i_group.append(c_group[circle_touched])
        c_group[circle_touched].infected = True
        c_group[circle_touched].image = pygame.image.load('infected.png')
        c_group.pop(circle_touched)
                
    
    
        
                

    pygame.display.flip()
    screen.fill(BACKGROUND_COLOR)
    clock.tick(FPS)

running = True
while running:

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
            pygame.quit()
    
    update(screen)
    

