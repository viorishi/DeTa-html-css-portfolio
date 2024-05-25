import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Car Racing Game")

# Set up colors
WHITE = (255, 255, 255)

# Set up the player (car)
car_image = pygame.image.load("car.png")  # Load car image
car_width = 80
car_height = 160
car_x = screen_width // 2 - car_width // 2
car_y = screen_height - 200
car_speed = 5

# Set up cows (obstacles)
cow_width = 100
cow_height = 80
cow_speed = 5
cows = []

# Load cow image
cow_image = pygame.image.load("cow.png")

# Function to create new cow
def create_cow():
    x = random.randint(0, screen_width - cow_width)
    y = -cow_height
    cows.append(pygame.Rect(x, y, cow_width, cow_height))

# Main game loop
clock = pygame.time.Clock()
score = 0
game_over = False

while not game_over:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= car_speed
    if keys[pygame.K_RIGHT]:
        car_x += car_speed

    # Move cows and check collision with car
    for cow in cows:
        cow.y += cow_speed
        screen.blit(cow_image, cow)
        if cow.colliderect(pygame.Rect(car_x, car_y, car_width, car_height)):
            game_over = True

    # Remove cows that have gone off-screen
    cows = [cow for cow in cows if cow.y < screen_height]

    # Create new cows
    if random.randint(0, 100) < 2:
        create_cow()

    # Draw the car
    screen.blit(car_image, (car_x, car_y))

    # Display score
    score += 1
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Game over screen
font = pygame.font.Font(None, 72)
text = font.render("Game Over", True, (0, 0, 0))
text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
screen.blit(text, text_rect)
pygame.display.flip()

# Wait for a moment before quitting
pygame.time.wait(2000)
pygame.quit()
sys.exit()
