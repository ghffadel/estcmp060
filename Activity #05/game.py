import pygame

import sys

from pygame.locals import *

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

SCORE_MAX = 2

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MENU")
font = pygame.font.SysFont("pressstart2pregular", 40, False, False)

pause = False


# creating main menu
def main_menu():
    background_menu = pygame.image.load("assets/main_menu_pong.jpg")
    click = False
    menu_button_play = pygame.Rect(size[0] / 2 - 165, size[1] / 2 - 40, 300, 50)
    menu_button_credits = pygame.Rect(size[0] / 2 - 165, size[1] / 2 + 20, 300, 50)
    menu_button_quit = pygame.Rect(size[0] / 2 - 165, size[1] / 2 + 80, 300, 50)
    menu_button_color = (139, 0, 139)

    while True:
        screen.blit(background_menu, (0, 0))
        message_play = f'PLAY'
        message_credits = f'CREDITS'
        message_quit = f'QUIT'

        txt_screen_play = font.render(message_play, True, COLOR_BLACK)
        txt_screen_credits = font.render(message_credits, True, COLOR_BLACK)
        txt_screen_quit = font.render(message_quit, True, COLOR_BLACK)
        pygame.draw.rect(screen, menu_button_color, menu_button_play)
        pygame.draw.rect(screen, menu_button_color, menu_button_credits)
        pygame.draw.rect(screen, menu_button_color, menu_button_quit)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if click:
            if menu_button_play.collidepoint(mouse_x, mouse_y):
                game()
            if menu_button_credits.collidepoint(mouse_x, mouse_y):
                credits_game()
            if menu_button_quit.collidepoint(mouse_x, mouse_y):
                pygame.quit()
                sys.exit()

        screen.blit(txt_screen_play, (550, 328))
        screen.blit(txt_screen_credits, (487, 388))
        screen.blit(txt_screen_quit, (550, 448))
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
    background_game_pause = pygame.image.load("assets/game_pause.jpg")
    click = False
    menu_button_resume = pygame.Rect(size[0] / 2 - 165, size[1] / 2 - 40, 300, 50)
    menu_button_restart = pygame.Rect(size[0] / 2 - 165, size[1] / 2 + 20, 300, 50)
    menu_button_menu = pygame.Rect(size[0] / 2 - 165, size[1] / 2 + 80, 300, 50)
    menu_button_color = (139, 0, 139)

    while pause:
        screen.blit(background_game_pause, (0, 0))
        message_resume = f'RESUME'
        message_restart = f'RESTART'
        message_menu = f'MENU'

        txt_screen_resume = font.render(message_resume, True, COLOR_BLACK)
        txt_screen_restart = font.render(message_restart, True, COLOR_BLACK)
        txt_screen_menu = font.render(message_menu, True, COLOR_BLACK)
        pygame.draw.rect(screen, menu_button_color, menu_button_resume)
        pygame.draw.rect(screen, menu_button_color, menu_button_restart)
        pygame.draw.rect(screen, menu_button_color, menu_button_menu)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if click:
            if menu_button_resume.collidepoint(mouse_x, mouse_y):
                unpause()
            if menu_button_restart.collidepoint(mouse_x, mouse_y):
                game()
            if menu_button_menu.collidepoint(mouse_x, mouse_y):
                main_menu()

        screen.blit(txt_screen_resume, (508, 328))
        screen.blit(txt_screen_restart, (490, 388))
        screen.blit(txt_screen_menu, (546, 448))
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
    menu_button_color = (139, 0, 139)
    button_menu = pygame.Rect(size[0] / 2 - 630, size[1] / 2 - 350, 230, 50)
    background_credits = pygame.image.load("assets/credits_pong.jpg")
    pygame.display.set_caption("CREDITS")
    click = False

    while True:
        screen.blit(background_credits, (0, 0))

        message_button_menu = f'MENU'
        pygame.draw.rect(screen, menu_button_color, button_menu)
        txt_screen_back = font.render(message_button_menu, True, COLOR_BLACK)

        screen.blit(txt_screen_back, (size[0] / 2 - 598, size[1] / 2 - 343))

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

    pygame.display.set_caption("MyPong - PyGame Edition - 2021.01.30")

    # score text
    score_font = pygame.font.Font('assets/PressStart2P.ttf', 44)
    score_text = score_font.render('00 x 00', True, COLOR_WHITE, COLOR_BLACK)
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (680, 50)

    # victory text
    victory_font = pygame.font.Font('assets/PressStart2P.ttf', 100)
    victory_text = victory_font .render('VICTORY', True, COLOR_WHITE, COLOR_BLACK)
    victory_text_rect = score_text.get_rect()
    victory_text_rect.center = (450, 350)

    # sound effects
    bounce_sound_effect = pygame.mixer.Sound('assets/bounce.wav')
    scoring_sound_effect = pygame.mixer.Sound('assets/258020__kodack__arcade-bleep-sound.wav')

    # player 1
    player_1 = pygame.image.load("assets/player.png")
    player_1_y = 300
    player_1_move_up = False
    player_1_move_down = False

    # player 2 - robot
    player_2 = pygame.image.load("assets/player.png")
    player_2_y = 300

    # ball
    ball = pygame.image.load("assets/ball.png")
    ball_x = 640
    ball_y = 360
    ball_dx = 5
    ball_dy = 5

    # score
    score_1 = 0
    score_2 = 0

    # game loop
    game_loop = True
    game_clock = pygame.time.Clock()

    while game_loop:

        for event in pygame.event.get():

            # quit for main menu
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause = True
                    game_pause()

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            #  keystroke events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_1_move_up = True
                if event.key == pygame.K_DOWN:
                    player_1_move_down = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player_1_move_up = False
                if event.key == pygame.K_DOWN:
                    player_1_move_down = False

        # checking the victory condition
        if score_1 < SCORE_MAX and score_2 < SCORE_MAX:

            # clear screen
            screen.fill(COLOR_BLACK)

            # ball collision with the wall
            if ball_y > 700:
                ball_dy *= -1
                bounce_sound_effect.play()
            elif ball_y <= 0:
                ball_dy *= -1
                bounce_sound_effect.play()

            # ball collision with the player 1 's paddle
            if ball_x < 100:
                if player_1_y < ball_y + 25:
                    if player_1_y + 150 > ball_y:
                        ball_dx *= -1
                        bounce_sound_effect.play()

            # ball collision with the player 2 's paddle
            if ball_x > 1160:
                if player_2_y < ball_y + 25:
                    if player_2_y + 150 > ball_y:
                        ball_dx *= -1
                        bounce_sound_effect.play()

            # scoring points
            if ball_x < -50:
                ball_x = 640
                ball_y = 360
                ball_dy *= -1
                ball_dx *= -1
                score_2 += 1
                scoring_sound_effect.play()
            elif ball_x > 1320:
                ball_x = 640
                ball_y = 360
                ball_dy *= -1
                ball_dx *= -1
                score_1 += 1
                scoring_sound_effect.play()

            # ball movement
            ball_x = ball_x + ball_dx
            ball_y = ball_y + ball_dy

            # player 1 up movement
            if player_1_move_up:
                player_1_y -= 5
            else:
                player_1_y += 0

            # player 1 down movement
            if player_1_move_down:
                player_1_y += 5
            else:
                player_1_y += 0

            # player 1 collides with upper wall
            if player_1_y <= 0:
                player_1_y = 0

            # player 1 collides with lower wall
            elif player_1_y >= 570:
                player_1_y = 570

            # player 2 "Artificial Intelligence"
            player_2_y = ball_y
            if player_2_y <= 0:
                player_2_y = 0
            elif player_2_y >= 570:
                player_2_y = 570

            # update score hud
            score_text = score_font.render(str(score_1) + ' x ' + str(score_2), True, COLOR_WHITE, COLOR_BLACK)

            # drawing objects
            screen.blit(ball, (ball_x, ball_y))
            screen.blit(player_1, (50, player_1_y))
            screen.blit(player_2, (1180, player_2_y))
            screen.blit(score_text, score_text_rect)
        else:
            # drawing victory
            screen.fill(COLOR_BLACK)
            screen.blit(score_text, score_text_rect)
            screen.blit(victory_text, victory_text_rect)

        # update screen
        pygame.display.update()
        game_clock.tick(60)


main_menu()
pygame.display.update()
pygame.quit()
