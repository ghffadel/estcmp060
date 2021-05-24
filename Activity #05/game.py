import pygame
import sys

# Importing the components
from ball import Ball
from brick import Brick
from paddle import Paddle
from pygame.locals import *

pygame.init()

# Defining colors
BLACK = (0, 0, 0)
DARK_BLUE = (36, 90, 190)
GREEN = (0, 127, 0)
LIGHT_BLUE = (0, 176, 240)
ORANGE = (255, 100, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
size = (800, 600)
screen = pygame.display.set_mode(size)
font = pygame.font.Font("assets/PressStart2P.ttf", 24)
pause = False


# creating main menu
def main_menu():
    pygame.display.set_caption("MENU")
    background_menu = pygame.image.load("assets/main_menu_breakout.jpg")
    background_menu = pygame.transform.scale(background_menu, (1000, 600))
    click = False
    menu_button_play = pygame.Rect(size[0] / 2 - 165, size[1] / 2 - 40, 300, 50)
    menu_button_credits = pygame.Rect(size[0] / 2 - 165, size[1] / 2 + 20, 300, 50)
    menu_button_quit = pygame.Rect(size[0] / 2 - 165, size[1] / 2 + 80, 300, 50)
    while True:
        screen.blit(background_menu, (-100, 0))
        txt_screen_play = font.render("PLAY", True, BLACK)
        txt_screen_credits = font.render("CREDITS", True, BLACK)
        txt_screen_quit = font.render("QUIT", True, BLACK)
        pygame.draw.rect(screen, RED, menu_button_play)
        pygame.draw.rect(screen, RED, menu_button_credits)
        pygame.draw.rect(screen, RED, menu_button_quit)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if click:
            if menu_button_play.collidepoint(mouse_x, mouse_y):
                game()
            if menu_button_credits.collidepoint(mouse_x, mouse_y):
                credits_game()
            if menu_button_quit.collidepoint(mouse_x, mouse_y):
                pygame.quit()
                sys.exit()
        screen.blit(txt_screen_play, (340, 275))
        screen.blit(txt_screen_credits, (310, 335))
        screen.blit(txt_screen_quit, (340, 395))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


# function unpause
def unpause():
    global pause
    pause = False


# creating a pause menu
def game_pause():
    background_game_pause = pygame.image.load("assets/game_pause_breakout.jpg")
    background_game_pause = pygame.transform.scale(background_game_pause, (1000, 600))
    click = False
    menu_button_resume = pygame.Rect(size[0] / 2 - 165, size[1] / 2 - 40, 300, 50)
    menu_button_restart = pygame.Rect(size[0] / 2 - 165, size[1] / 2 + 20, 300, 50)
    menu_button_menu = pygame.Rect(size[0] / 2 - 165, size[1] / 2 + 80, 300, 50)
    while pause:
        screen.blit(background_game_pause, (-100, 0))
        txt_screen_resume = font.render("RESUME", True, BLACK)
        txt_screen_restart = font.render("RESTART", True, BLACK)
        txt_screen_menu = font.render("MENU", True, BLACK)
        pygame.draw.rect(screen, RED, menu_button_resume)
        pygame.draw.rect(screen, RED, menu_button_restart)
        pygame.draw.rect(screen, RED, menu_button_menu)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if click:
            if menu_button_resume.collidepoint(mouse_x, mouse_y):
                unpause()
            if menu_button_restart.collidepoint(mouse_x, mouse_y):
                game()
            if menu_button_menu.collidepoint(mouse_x, mouse_y):
                main_menu()
        screen.blit(txt_screen_resume, (320, 275))
        screen.blit(txt_screen_restart, (310, 335))
        screen.blit(txt_screen_menu, (340, 395))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


# creating the credits
def credits_game():
    button_menu = pygame.Rect(size[0] / 2 - 350, size[1] / 2 - 275, 150, 50)
    background_credits = pygame.image.load("assets/credits_breakout.jpg")
    background_credits = pygame.transform.scale(background_credits, (900, 600))
    pygame.display.set_caption("CREDITS")
    click = False
    while True:
        screen.blit(background_credits, (-10, 0))
        pygame.draw.rect(screen, RED, button_menu)
        txt_screen_back = font.render("MENU", True, BLACK)
        screen.blit(txt_screen_back, (size[0] / 2 - 325, size[1] / 2 - 260))
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if click:
            if button_menu.collidepoint(mouse_x, mouse_y):
                main_menu()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()


def game():
    global pause
    # sound effects
    bounce_sound_effect = pygame.mixer.Sound("assets/bounce.wav")
    scoring_sound_effect = pygame.mixer.Sound("assets/bleep.wav")
    score = 0
    lives = 3
    pygame.display.set_caption("BREAKOUT")
    bricks_list = pygame.sprite.Group()
    sprites_list = pygame.sprite.Group()
    paddle = Paddle(LIGHT_BLUE, 100, 10)
    paddle.rect.x = 350
    paddle.rect.y = 560
    ball = Ball(WHITE, 10, 10)
    ball.rect.x = 345
    ball.rect.y = 240
    ball.velocity = [3, 3]

    # Adding the bricks with different colors
    for i in range(7):
        brick = Brick(RED, 80, 30)
        brick.rect.x = 100 * i + 60
        brick.rect.y = 80
        sprites_list.add(brick)
        bricks_list.add(brick)
    for i in range(7):
        brick = Brick(ORANGE, 80, 30)
        brick.rect.x = 100 * i + 60
        brick.rect.y = 120
        sprites_list.add(brick)
        bricks_list.add(brick)
    for i in range(7):
        brick = Brick(YELLOW, 80, 30)
        brick.rect.x = 100 * i + 60
        brick.rect.y = 160
        sprites_list.add(brick)
        bricks_list.add(brick)
    for i in range(7):
        brick = Brick(GREEN, 80, 30)
        brick.rect.x = 100 * i + 60
        brick.rect.y = 200
        sprites_list.add(brick)
        bricks_list.add(brick)
    sprites_list.add(ball)
    sprites_list.add(paddle)
    game_clock = pygame.time.Clock()
    game_loop = True
    while game_loop:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # Handling ESC Button
                if event.key == K_ESCAPE:
                    pause = True
                    game_pause()

            if event.type == pygame.QUIT:
                game_loop = False
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        # Paddle movement
        if keys[pygame.K_LEFT]:
            paddle.move_left(5)

        if keys[pygame.K_RIGHT]:
            paddle.move_right(5)

        sprites_list.update()

        # Left / right wall collision
        if ball.rect.x <= 0 or ball.rect.x >= 790:
            ball.velocity[0] *= -1
            bounce_sound_effect.play()

        # Top / bottom wall collision
        if ball.rect.y < 65 or ball.rect.y > 590:
            ball.velocity[1] *= -1
            bounce_sound_effect.play()

            # Decreasing lives if collides with bottom wall
            if ball.rect.y > 590:
                lives -= 1
                ball.rect.x = 345
                ball.rect.y = 240
                ball.velocity = [3, 3]

                # Displaying Game Over for 3 seconds
                if lives == 0:
                    fonts = pygame.font.Font("assets/PressStart2P.ttf", 64)
                    text = font.render("GAME OVER", 1, WHITE)
                    screen.blit(text, (300, 300))
                    pygame.display.flip()
                    pygame.time.wait(3000)

                    game_loop = False
                    main_menu()

        # Collision with paddle
        if pygame.sprite.collide_mask(ball, paddle):
            ball.rect.x -= ball.velocity[0]
            ball.rect.y -= ball.velocity[1]
            ball.collision()
            bounce_sound_effect.play()

        collision_list = pygame.sprite.spritecollide(ball, bricks_list, False)

        # Collision with bricks
        for brick in collision_list:
            ball.collision()
            brick.kill()
            score += 1
            scoring_sound_effect.play()

            # Displaying Level Completed for 3 seconds
            if len(bricks_list) == 0:
                fonts = pygame.font.Font("assets/PressStart2P.ttf", 64)
                text = font.render("LEVEL COMPLETED", 1, WHITE)
                screen.blit(text, (250, 300))
                pygame.display.flip()
                pygame.time.wait(3000)

                game_loop = False
                main_menu()

        screen.fill(DARK_BLUE)
        pygame.draw.line(screen, WHITE, (0, 58), (800, 58), 2)
        font = pygame.font.Font("assets/PressStart2P.ttf", 24)
        score_text = font.render("Score: %d" % score, 1, WHITE)
        screen.blit(score_text, (20, 15))
        lives_text = font.render("Lives: %d" % lives, 1, WHITE)
        screen.blit(lives_text, (575, 15))
        sprites_list.draw(screen)
        pygame.display.flip()
        game_clock.tick(60)


main_menu()
pygame.display.update()
pygame.quit()