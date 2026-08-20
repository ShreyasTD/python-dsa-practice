import pygame # type: ignore
import time
import random
# Initialize Pygame
pygame.init()
# Screen dimensions and colors
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
# Game settings
SNAKE_BLOCK = 10
SNAKE_SPEED = 15
# Initialize display and clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
# Fonts for score and messages
font_style = pygame.font.SysFont("bahnschrift", 25)
# Functions to display score and draw snake
def display_score(score):
   value = font_style.render(f"Your Score: {score}", True, WHITE)
   screen.blit(value, [0, 0])
def draw_snake(block_size, snake_list):
   for block in snake_list:
       pygame.draw.rect(screen, GREEN, [block[0], block[1], block_size, block_size])
# Main game loop function
def game_loop():
   game_over = False
   game_close = False
   x1, y1 = WIDTH // 2, HEIGHT // 2
   x1_change, y1_change = 0, 0
   snake_list = []
   snake_length = 1
   food_x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
   food_y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
   while not game_over:
       while game_close:
           screen.fill(BLACK)
           message = font_style.render("Game Over! Press Q-Quit or C-Play Again", True, RED)
           screen.blit(message, [WIDTH / 6, HEIGHT / 3])
           display_score(snake_length - 1)
           pygame.display.update()
           for event in pygame.event.get():
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_q:
                       game_over = True
                       game_close = False
                   if event.key == pygame.K_c:
                       game_loop()
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               game_over = True
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:
                   x1_change = -SNAKE_BLOCK
                   y1_change = 0
               elif event.key == pygame.K_RIGHT:
                   x1_change = SNAKE_BLOCK
                   y1_change = 0
               elif event.key == pygame.K_UP:
                   y1_change = -SNAKE_BLOCK
                   x1_change = 0
               elif event.key == pygame.K_DOWN:
                   y1_change = SNAKE_BLOCK
                   x1_change = 0
       if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
           game_close = True
       x1 += x1_change
       y1 += y1_change
       screen.fill(BLACK)
       pygame.draw.rect(screen, BLUE, [food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK])
       snake_head = [x1, y1]
       snake_list.append(snake_head)
       if len(snake_list) > snake_length:
           del snake_list[0]
       for block in snake_list[:-1]:
           if block == snake_head:
               game_close = True
       draw_snake(SNAKE_BLOCK, snake_list)
       display_score(snake_length - 1)
       pygame.display.update()
       if x1 == food_x and y1 == food_y:
           food_x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
           food_y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
           snake_length += 1
       clock.tick(SNAKE_SPEED)
   pygame.quit()
   quit()
# Start the game loop
game_loop()
