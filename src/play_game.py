import pygame
import pygame.mixer
from src.snake import Snake
from src.food import Food
from src.constants import *

pygame.init()
pygame.mixer.init()

# Load sound files
eat_sound = pygame.mixer.Sound('assets/eat.wav')
game_over_sound = pygame.mixer.Sound('assets/game_over.wav')

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

def display_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    screen.blit(value, [0, 0])

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

def game_loop():
    game_state = 'MENU'
    game_over = False
    game_close = False
    score = 0

    snake = Snake(screen, snake_block)
    food = Food(screen, snake_block)

    # Menu UI elements
    easy_button_rect = pygame.Rect(screen_width / 4, screen_height / 2, 100, 50)
    medium_button_rect = pygame.Rect(screen_width / 2, screen_height / 2, 100, 50)
    hard_button_rect = pygame.Rect(screen_width * 3 / 4, screen_height / 2, 100, 50)

    def set_difficulty(difficulty):
        nonlocal game_state, score
        current_difficulty = difficulty
        snake_speed = difficulty_presets[current_difficulty]
        game_state = 'PLAY'
        snake.reset()
        food.respawn()
        score = 0

    while not game_over:
        if game_state == 'MENU':
            screen.fill(black)
            title_text = title_font.render("Snake Game", True, white)
            title_rect = title_text.get_rect(center=(screen_width / 2, screen_height / 4))
            screen.blit(title_text, title_rect)

            draw_button(easy_button_rect, "Easy", button_color, button_hover_color, action=lambda: set_difficulty("easy"))
            draw_button(medium_button_rect, "Medium", button_color, button_hover_color, action=lambda: set_difficulty("medium"))
            draw_button(hard_button_rect, "Hard", button_color, button_hover_color, action=lambda: set_difficulty("hard"))

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
                display_score(score)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            game_state = 'MENU'
                            game_close = False
                            snake.reset()
                            food.respawn()
                            score = 0

                pygame.time.wait(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        snake.update_direction("LEFT")
                    elif event.key == pygame.K_RIGHT:
                        snake.update_direction("RIGHT")
                    elif event.key == pygame.K_UP:
                        snake.update_direction("UP")
                    elif event.key == pygame.K_DOWN:
                        snake.update_direction("DOWN")

            snake.move()

            if snake.x >= screen_width or snake.x < 0 or snake.y >= screen_height or snake.y < 0:
                game_over_sound.play()
                game_close = True

            screen.fill(black)
            food.draw()
            snake.snake_list.append([snake.x, snake.y])
            if len(snake.snake_list) > snake.length:
                del snake.snake_list[0]

            for segment in snake.snake_list[:-1]:
                if segment == [snake.x, snake.y]:
                    game_over_sound.play()
                    game_close = True

            snake.draw()
            display_score(score)
            pygame.display.update()

            if not game_close and snake.x == food.x and snake.y == food.y:
                food.respawn()
                snake.grow()
                score += 1
                eat_sound.play()

            clock.tick(snake_speed)

    pygame.quit()
    quit()

if __name__ == '__main__':
    game_loop()
