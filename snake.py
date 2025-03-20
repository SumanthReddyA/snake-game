import pygame
import random

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Load sound files
eat_sound = pygame.mixer.Sound('eat.wav')
game_over_sound = pygame.mixer.Sound('game_over.wav')

# Screen dimensions
screen_width = 600
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake block size and speed
snake_block = 10
snake_speed = 15

# Difficulty settings
difficulty_presets = {
    "easy": 10,
    "medium": 15,
    "hard": 25
}
current_difficulty = "medium"  # Default difficulty

# Fonts
font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont(None, 35)


def display_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    screen.blit(value, [0, 0])


def draw_snake(snake_block, snake_list):
    for segment in snake_list:
        pygame.draw.rect(screen, green, [segment[0], segment[1], snake_block, snake_block])


def game_loop():
    global snake_speed, current_difficulty

    game_over = False
    game_close = False

    while True:
        difficulty = input("Choose difficulty (Easy, Medium, Hard): ").lower()
        if difficulty in difficulty_presets:
            current_difficulty = difficulty
            snake_speed = difficulty_presets[current_difficulty]
            break
        else:
            print("Invalid difficulty. Please choose from Easy, Medium, or Hard.")

    # Snake starting position
    x1 = screen_width / 2
    y1 = screen_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Food position
    food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(black)
            game_over_message = font_style.render("You Lost! Press C-Play Again or Q-Quit", True, red)
            text_rect = game_over_message.get_rect(center=(screen_width / 2, screen_height / 2))
            screen.blit(game_over_message, text_rect)
            display_score(length_of_snake - 1)
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
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_over_sound.play()
            game_close = True
        if game_close:
            continue

        x1 += x1_change
        y1 += y1_change
        screen.fill(black)
        pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        # Check for self-collision after adding new head
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over_sound.play()
                game_close = True
                break # Exit inner loop once collision is detected

        draw_snake(snake_block, snake_list)
        display_score(length_of_snake - 1)
        pygame.display.update()

        if not game_close and x1 == food_x and y1 == food_y: # Only play sound and increase length if game is not already closed
            food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            eat_sound.play()

        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
