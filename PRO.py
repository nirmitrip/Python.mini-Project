import random
import pygame
import time

pygame.init()

# Set up the display
width, height = 640, 480
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Set up game variables
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_position = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
food_spawned = True
direction = 'RIGHT'
change_to = direction
score = 0

# Game over function
def game_over():
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over! Try Again.", True, white)
    text_rect = text.get_rect()
    text_rect.center = (width // 2, height // 2)
    display.blit(text, text_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                change_to = 'RIGHT'
            elif event.key == pygame.K_a:
                change_to = 'LEFT'
            elif event.key == pygame.K_w:
                change_to = 'UP'
            elif event.key == pygame.K_s:
                change_to = 'DOWN'

    # Validate direction
    if change_to == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    elif change_to == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    elif change_to == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    elif change_to == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    # Update snake position
    if direction == 'RIGHT':
        snake_position[0] += 10
    elif direction == 'LEFT':
        snake_position[0] -= 10
    elif direction == 'UP':
        snake_position[1] -= 10
    elif direction == 'DOWN':
        snake_position[1] += 10

    # Snake body growth
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 1
        food_spawned = False
    else:
        snake_body.pop()

    # Spawn food
    if not food_spawned:
        food_position = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
    food_spawned = True

    # Update display
    display.fill(black)
    for pos in snake_body:
        pygame.draw.rect(display, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(display, white, pygame.Rect(food_position[0], food_position[1], 10, 10))

    # Game over conditions
    if snake_position[0] < 0 or snake_position[0] >= width or snake_position[1] < 0 or snake_position[1] >= height:
        game_over()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    pygame.display.flip()
    pygame.time.Clock().tick(30)
