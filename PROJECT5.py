import pygame

pygame.init()
width = 700
height = 400
screen = pygame.display.set_mode((width, height))
running = True

print("Start -->")

# Picture
img = pygame.image.load('img.png')
img = pygame.transform.scale(img, (200, 200))

x = 250
y = 100

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    screen.blit(img, (x, y)) 
    pygame.display.update()
pygame.quit() 
print("End -->")
          