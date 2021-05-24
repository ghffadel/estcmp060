import pygame

import sys

from pygame.locals import *

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (189, 16, 0)

SCORE_MAX = 2

size = (1280, 720)
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont("pressstart2pregular", 40, False, False)

pause = False


# creating main menu
def main_menu():
    pygame.display.set_caption("MENU")
    background_menu = pygame.image.load("assets/main_menu_breakout.jpg")
    click = False
    menu_button_play = pygame.Rect(size[0] / 2 - 165, size[1] / 2 - 40, 300, 50)
    menu_button_credits = pygame.Rect(size[0] / 2 - 165, size[1] / 2 + 20, 300, 50)
    menu_button_quit = pygame.Rect(size[0] / 2 - 165, size[1] / 2 + 80, 300, 50)

    while True:
        screen.blit(background_menu, (0, 0))

        txt_screen_play = font.render("PLAY", True, COLOR_BLACK)
        txt_screen_credits = font.render("CREDITS", True, COLOR_BLACK)
        txt_screen_quit = font.render("QUIT", True, COLOR_BLACK)
        pygame.draw.rect(screen, COLOR_RED, menu_button_play)
        pygame.draw.rect(screen, COLOR_RED, menu_button_credits)
        pygame.draw.rect(screen, COLOR_RED, menu_button_quit)

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
        screen.blit(txt_screen_credits, (486, 388))
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
    background_game_pause = pygame.image.load("assets/game_pause_breakout.jpg")
    click = False
    menu_button_resume = pygame.Rect(size[0] / 2 - 165, size[1] / 2 - 40, 300, 50)
    menu_button_restart = pygame.Rect(size[0] / 2 - 165, size[1] / 2 + 20, 300, 50)
    menu_button_menu = pygame.Rect(size[0] / 2 - 165, size[1] / 2 + 80, 300, 50)

    while pause:
        screen.blit(background_game_pause, (0, 0))

        txt_screen_resume = font.render("RESUME", True, COLOR_BLACK)
        txt_screen_restart = font.render("RESTART", True, COLOR_BLACK)
        txt_screen_menu = font.render("MENU", True, COLOR_BLACK)
        pygame.draw.rect(screen, COLOR_RED, menu_button_resume)
        pygame.draw.rect(screen, COLOR_RED, menu_button_restart)
        pygame.draw.rect(screen, COLOR_RED, menu_button_menu)

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
        screen.blit(txt_screen_menu, (548, 448))
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
    button_menu = pygame.Rect(size[0] / 2 - 630, size[1] / 2 - 350, 230, 50)
    background_credits = pygame.image.load("assets/credits_breakout.jpg")
    pygame.display.set_caption("CREDITS")
    click = False

    while True:
        screen.blit(background_credits, (0, 0))

        pygame.draw.rect(screen, COLOR_RED, button_menu)
        txt_screen_back = font.render("MENU", True, COLOR_BLACK)

        screen.blit(txt_screen_back, (size[0] / 2 - 593, size[1] / 2 - 343))

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

    pygame.display.set_caption("BREAKOUT")

    # score text
    score_font = pygame.font.Font("assets/PressStart2P.ttf", 44)
    score_text = score_font.render("00", True, COLOR_WHITE, COLOR_BLACK)
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (680, 50)

    # victory text
    victory_font = pygame.font.Font("assets/PressStart2P.ttf", 100)
    victory_text = victory_font .render("VICTORY", True, COLOR_WHITE, COLOR_BLACK)
    victory_text_rect = score_text.get_rect()
    victory_text_rect.center = (450, 350)

    # sound effects
    bounce_sound_effect = pygame.mixer.Sound("assets/bounce.wav")
    scoring_sound_effect = pygame.mixer.Sound("assets/bleep.wav")

    # player 1
    player_1 = pygame.image.load("assets/player.png")
    player_1 = pygame.transform.rotate(player_1, 90)
    rect_player_1 = player_1.get_rect()
    player_1_y = 500
    rect_player_1 = rect_player_1.move(50, player_1_y)
    player_1_move_up = False
    player_1_move_down = False

    # ball
    ball = pygame.image.load("assets/ball.png")
    rect_ball_ = ball.get_rect()
    ball_x = 0
    ball_y = 0
    rect_ball = rect_ball_.move(ball_x, ball_y)
    ball_dx = 5
    ball_dy = 5

    # score
    score = 0

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
        if score < SCORE_MAX:

            # clear screen
            screen.fill(COLOR_BLACK)

            # ball collision with the wall
            if rect_ball.y > 700:
                ball_dy *= -1
                bounce_sound_effect.play()
            elif rect_ball.y <= 0:
                ball_dy *= -1
                bounce_sound_effect.play()

            # ball collision with the player 1 's paddle
            if rect_ball.colliderect(rect_player_1) and ball_dx < 0:
                ball_dx *= -1
                if rect_player_1.bottom >= rect_ball.top > rect_player_1.centery + 30:
                    if ball_dy == 0:
                        ball_dy = 5
                    else:
                        ball_dy *= 1

                elif rect_player_1.top <= rect_ball.bottom < rect_player_1.centery - 30:
                    if ball_dy == 0:
                        ball_dy = 5
                    else:
                        ball_dy *= -1
                    bounce_sound_effect.play()
                elif rect_player_1.centery + 30 >= rect_ball.centery > rect_player_1.centery - 30:
                    ball_dy = 0

            # # scoring points
            # if rect_ball.x < -50:
            #     rect_ball.x = 640
            #     rect_ball.y = 360
            #     ball_dy *= -1
            #     ball_dx *= -1
            #     score_2 += 1
            #     scoring_sound_effect.play()
            # elif rect_ball.x > 1320:
            #     rect_ball.x = 640
            #     rect_ball.y = 360
            #     ball_dy *= -1
            #     ball_dx *= -1
            #     score_1 += 1
            #     scoring_sound_effect.play()

            # ball movement
            rect_ball.x = rect_ball.x + ball_dx
            rect_ball.y = rect_ball.y + ball_dy

            # player 1 up movement
            if player_1_move_up:
                rect_player_1.y -= 5
            else:
                rect_player_1.y += 0

            # player 1 down movement
            if player_1_move_down:
                rect_player_1.y += 5
            else:
                rect_player_1.y += 0

            # player 1 collides with upper wall
            if rect_player_1.y <= 0:
                rect_player_1.y = 0

            # player 1 collides with lower wall
            elif rect_player_1.y >= 570:
                rect_player_1.y = 570

            # update score hud
            score_text = score_font.render(str(score), True, COLOR_WHITE, COLOR_BLACK)

            # drawing objects
            screen.blit(ball, (rect_ball.x, rect_ball.y))
            screen.blit(player_1, (rect_player_1.x, rect_player_1.y))
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