import pygame
import numpy as np

# Pygame başlangıcı
pygame.init()

# Ekran ayarları
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Araç sınıfı
class Car:
    def __init__(self):
        self.x = width // 2
        self.y = height // 2
        self.angle = 0
        self.speed = 0

    def update(self):
        self.x += self.speed * np.cos(np.radians(self.angle))
        self.y -= self.speed * np.sin(np.radians(self.angle))
        self.check_bounds()

    def check_bounds(self):
        if self.x < 0:
            self.x = 0
        elif self.x > width:
            self.x = width
        if self.y < 0:
            self.y = 0
        elif self.y > height:
            self.y = height

    def draw(self, screen):
        car_image = pygame.image.load('car.png')
        car_image = pygame.transform.rotate(car_image, self.angle)
        rect = car_image.get_rect(center=(self.x, self.y))
        screen.blit(car_image, rect.topleft)

# Oyun döngüsü
running = True
car = Car()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car.angle += 5
    if keys[pygame.K_RIGHT]:
        car.angle -= 5
    if keys[pygame.K_UP]:
        car.speed = 5
    elif keys[pygame.K_DOWN]:
        car.speed = -5
    else:
        car.speed = 0

    car.update()

    screen.fill((255, 255, 255))
    car.draw(screen)
    pygame.display.flip()

pygame.quit()
