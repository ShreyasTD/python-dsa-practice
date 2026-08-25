import pygame
import time
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE  = (50, 153, 213)

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock to control game speed
clock = pygame.time.Clock()

# Snake initial position and body
snake_pos = [100, 50]
snake_body = [[100, 50], [80, 50], [60, 50]]
snake_direction = "RIGHT"
change_to = snake_direction

# Food position
food_pos = [random.randrange(1, WIDTH // CELL_SIZE) * CELL_SIZE,
            random.randrange(1, HEIGHT // CELL_SIZE) * CELL_SIZE]
food_spawn = True

# Score
score = 0

# Function to display score
def show_score():
    font = pygame.font.SysFont("times new roman", 20)
    score_surface = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_surface, (10, 10))

# Game Over function
def game_over():
    font = pygame.font.SysFont("times new roman", 40)
    go_surface = font.render(f"Game Over! Score: {score}", True, RED)
    go_rect = go_surface.get_rect(center=(WIDTH/2, HEIGHT/2))
    screen.blit(go_surface, go_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()

# Main game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                change_to = "RIGHT"

    # Update direction
    snake_direction = change_to

    # Move snake
    if snake_direction == "UP":
        snake_pos[1] -= CELL_SIZE
    elif snake_direction == "DOWN":
        snake_pos[1] += CELL_SIZE
    elif snake_direction == "LEFT":
        snake_pos[0] -= CELL_SIZE
    elif snake_direction == "RIGHT":
        snake_pos[0] += CELL_SIZE

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Spawn new food
    if not food_spawn:
        food_pos = [random.randrange(1, WIDTH // CELL_SIZE) * CELL_SIZE,
                    random.randrange(1, HEIGHT // CELL_SIZE) * CELL_SIZE]
    food_spawn = True

    # Background
    screen.fill(BLACK)

    # Draw snake
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], CELL_SIZE, CELL_SIZE))

    # Draw food
    pygame.draw.rect(screen, BLUE, pygame.Rect(food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))

    # Check for collisions
    if (snake_pos[0] < 0 or snake_pos[0] >= WIDTH or
        snake_pos[1] < 0 or snake_pos[1] >= HEIGHT):
        game_over()

    for block in snake_body[1:]:
        if snake_pos == block:
            game_over()

    # Show score
    show_score()

    # Refresh game screen
    pygame.display.update()

    # Control speed
    clock.tick(10)


class Solution:
    def missingMultiple(self, nums, k):
        num_set = set(nums)
        multiple = k
        while multiple in num_set:
            multiple += k
        return multiple