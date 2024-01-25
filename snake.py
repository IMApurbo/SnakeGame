import pygame
import time
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
SNAKE_SIZE = 20
FPS = 15

# Colors
WHITE = (255, 255, 255)
RED = (0, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Load snake images
head_image = pygame.image.load("/home/kali/Downloads/head.png")
head_image = pygame.transform.scale(head_image, (SNAKE_SIZE, SNAKE_SIZE))

body_image = pygame.image.load("/home/kali/Downloads/snake.png")
body_image = pygame.transform.scale(body_image, (SNAKE_SIZE, SNAKE_SIZE))

tail_image = pygame.image.load("/home/kali/Downloads/tail.png")
tail_image = pygame.transform.scale(tail_image, (SNAKE_SIZE, SNAKE_SIZE))

food_image = pygame.image.load("/home/kali/Downloads/abc.png")
food_image = pygame.transform.scale(food_image, (SNAKE_SIZE, SNAKE_SIZE))

# Initialize clock
clock = pygame.time.Clock()

# Initialize fonts
font = pygame.font.Font(None, 36)

# Function to display score
def display_score(score):
    score_text = font.render("Score: {}".format(score), True, WHITE)
    screen.blit(score_text, (10, 10))

# Function to run the game
def game_loop():
    snake = [
        (WIDTH / 2, HEIGHT / 2),
        (WIDTH / 2 - SNAKE_SIZE, HEIGHT / 2),
        (WIDTH / 2 - 2 * SNAKE_SIZE, HEIGHT / 2)
    ]
    snake_direction = (SNAKE_SIZE, 0)

    food_position = (random.randrange(0, WIDTH - SNAKE_SIZE, SNAKE_SIZE),
                     random.randrange(0, HEIGHT - SNAKE_SIZE, SNAKE_SIZE))

    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != (0, SNAKE_SIZE):
                    snake_direction = (0, -SNAKE_SIZE)
                elif event.key == pygame.K_DOWN and snake_direction != (0, -SNAKE_SIZE):
                    snake_direction = (0, SNAKE_SIZE)
                elif event.key == pygame.K_LEFT and snake_direction != (SNAKE_SIZE, 0):
                    snake_direction = (-SNAKE_SIZE, 0)
                elif event.key == pygame.K_RIGHT and snake_direction != (-SNAKE_SIZE, 0):
                    snake_direction = (SNAKE_SIZE, 0)

        # Move the snake
        new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])

        # Wrap around to the opposite side if the snake hits the border
        new_head = (new_head[0] % WIDTH, new_head[1] % HEIGHT)

        snake.insert(0, new_head)

        # Check for collision with itself
        if len(snake) > 1 and new_head in snake[1:]:
            game_over()

        # Check for collision with food
        if new_head == food_position:
            food_position = (random.randrange(0, WIDTH - SNAKE_SIZE, SNAKE_SIZE),
                             random.randrange(0, HEIGHT - SNAKE_SIZE, SNAKE_SIZE))
            score += 1
        else:
            snake.pop()

        # Draw everything
        screen.fill(RED)
        for i, segment in enumerate(snake):
            if i == 0:
                screen.blit(head_image, (segment[0], segment[1]))
            elif i == len(snake) - 1:
                screen.blit(tail_image, (segment[0], segment[1]))
            else:
                screen.blit(body_image, (segment[0], segment[1]))
        screen.blit(food_image, (food_position[0], food_position[1]))
        display_score(score)

        pygame.display.flip()

        # Control the frame rate
        clock.tick(FPS)

# Function to display game over screen
def game_over():
    screen.fill(RED)
    game_over_text = font.render("Game Over", True, WHITE)
    screen.blit(game_over_text, (WIDTH / 2 - 100, HEIGHT / 2 - 50))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

if __name__ == "__main__":
    game_loop()
