'''This is a simple spaceship  and enemy shooter game project
in python'''

import pygame
import random

# Initialize pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Player spaceship class
class Spaceship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.Surface((32, 32))
        self.image.fill(white)  # Replace with actual spaceship image
        self.speed = 5

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def shoot(self):
        # Create a new projectile object and add it to a projectile list
        pass  # Implement projectile creation logic

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# Enemy class
class Enemy:
    def __init__(self):
        self.x = random.randrange(0, screen_width - 32)  # Spawn within screen width
        self.y = -64  # Start off-screen above
        self.image = pygame.Surface((20, 20))
        self.image.fill(red)  # Replace with actual enemy image
        self.speed = 3

    def move(self):
        self.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# Game loop
running = True
clock = pygame.time.Clock()
score = 0
enemies = []  # List to store enemy objects

# Create initial spaceship object
spaceship = Spaceship(screen_width // 2, screen_height - 50)

# Spawn some initial enemies
for _ in range(5):
    enemies.append(Enemy())

while running:
    # Handle events (keyboard input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        spaceship.move_left()
    if keys[pygame.K_RIGHT]:
        spaceship.move_right()
    if keys[pygame.K_SPACE]:
        spaceship.shoot()  # Call shoot method on key press

    # Update game objects
    # - Move spaceship based on input
    # - Move enemies down
    # - Check for collisions between spaceship/projectiles and enemies
    #   - Update score on enemy hit
    #   - Remove destroyed enemies from the list
    #   - Implement logic for handling spaceship getting hit (if applicable)

    # Clear the screen
    screen.fill(black)

    # Draw game objects
    spaceship.draw(screen)
    for enemy in enemies:
        enemy.move()
        enemy.draw(screen)

    # Update the display
    pygame.display.flip()

    # Set frame rate
    clock.tick(60)  # Update 60 times per second

# Quit pygame
pygame.quit()
