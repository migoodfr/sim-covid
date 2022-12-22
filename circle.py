import pygame
import random

class Circle(pygame.sprite.Sprite):
    """
    Class of the circle, move around the screen, check the collision and if is infected, infecte the other circle
    """

    def __init__(self, x: int, y: int ,infected: bool): 
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.infected = infected
        self.dirx = random.uniform(-1, 1)
        self.diry = random.uniform(-1, 1)
        self.speed = 2
        self.counter = random.randint(60, 180)
        self.radius = 40


        # load image and get surface of the circle
        if (self.infected):
            self.image = pygame.image.load('infected.png').convert_alpha()
        else:
            self.image = pygame.image.load('circle.png').convert_alpha()

        self.rect = self.image.get_rect(center=(self.x, self.y))
        
   

    def update(self, surface):
        self.move()
        self.draw(surface)
    
    
    def check_infection(self, ax: int, ay: int, bx: int, by: int) -> bool:
        if (abs(ax - bx) < 40) and (abs(ay - by) < 40): 
            return True

        return False
            




    def check_collision(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        
        # Check collision with the borders of the screen
        if (self.x < 0) or (self.x > SCREEN_WIDTH - 40):
            self.dirx = -self.dirx

        if (self.y < 0) or (self.y > SCREEN_HEIGHT - 40):
            self.diry = -self.diry

    def move(self):

        if self.counter == 0:
            self.dirx = random.uniform(-1, 1)
            self.diry = random.uniform(-1, 1)
            self.counter = random.randint(60, 180)

        self.x = self.x + self.dirx * self.speed
        self.y = self.y + self.diry * self.speed
        self.counter -= 1

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

