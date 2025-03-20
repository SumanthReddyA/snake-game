import pygame
import random

# Button colors
button_color = (100, 100, 100)
button_hover_color = (150, 150, 150)

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
    global snake_speed, current_difficulty, game_state, game_close, x1, y1, x1_change, y1_change, snake_list, length_of_snake, food_x, food_y

    game_state = 'MENU'  # Initial game state
    game_over = False
    game_close = False

    # Menu UI elements
    menu_font = pygame.font.SysFont(None, 40)
    easy_button_rect = pygame.Rect(screen_width / 4, screen_height / 2, 100, 50)
    medium_button_rect = pygame.Rect(screen_width / 2, screen_height / 2, 100, 50)
    hard_button_rect = pygame.Rect(screen_width * 3 / 4, screen_height / 2, 100, 50)

    # Initial snake position and direction
    x1 = screen_width / 2
    y1 = screen_height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Food position
    food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    # Function to draw buttons
    def draw_button(rect, text, color, hover_color, action=None):
        mouse_pos = pygame.mouse.get_pos()
        clicked = False
        button_color = color
        if rect.collidepoint(mouse_pos):
            button_color = hover_color
            if pygame.mouse.get_pressed()[0] == 1:
                action()
                clicked = True

        pygame.draw.rect(screen, button_color, rect)
        text_surface = menu_font.render(text, True, black)
        text_rect = text_surface.get_rect(center=rect.center)
        screen.blit(text_surface, text_rect)
        return clicked

    def set_difficulty(difficulty):
        global current_difficulty, snake_speed, game_state
        current_difficulty = difficulty
        snake_speed = difficulty_presets[current_difficulty]
        game_state = 'PLAY'  # Transition to PLAY state
        reset_game_variables() # Reset game variables when difficulty is set

    def reset_game_variables():
        global x1, y1, x1_change, y1_change, snake_list, length_of_snake, food_x, food_y, game_close
        x1 = screen_width / 2
        y1 = screen_height / 2
        x1_change = 0
        y1_change = 0
        snake_list = []
        length_of_snake = 1
        food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
        food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
        game_close = False


    while not game_over:
        if game_state == 'MENU':
            screen.fill(black)
            title_font = pygame.font.SysFont(None, 60)
            title_text = title_font.render("Snake Game", True, white)
            title_rect = title_text.get_rect(center=(screen_width / 2, screen_height / 4))
            screen.blit(title_text, title_rect)

            easy_clicked = draw_button(easy_button_rect, "Easy", button_color, button_hover_color, action=lambda: set_difficulty("easy"))
            medium_clicked = draw_button(medium_button_rect, "Medium", button_color, button_hover_color, action=lambda: set_difficulty("medium"))
            hard_clicked = draw_button(hard_button_rect, "Hard", button_color, button_hover_color, action=lambda: set_difficulty("hard"))

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
        elif game_state == 'PLAY':
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
                            game_state = 'MENU'
                            game_close = False
                            reset_game_variables() # Reset variables before going to menu

                pygame.time.wait(100)


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


            x1 += x1_change
            y1 += y1_change
            screen.fill(black)
            pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])
            snake_head = [x1, y1]
            snake_list.append(snake_head)
            if len(snake_list) > length_of_snake:
                del snake_list[0]

            for segment in snake_list[:-1]:
                if segment == snake_head:
                    game_over_sound.play()
                    game_close = True

            draw_snake(snake_block, snake_list)
            display_score(length_of_snake - 1)
            pygame.display.update()

            if not game_close and x1 == food_x and y1 == food_y:
                food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
                food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
                length_of_snake += 1
                eat_sound.play()

            pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
