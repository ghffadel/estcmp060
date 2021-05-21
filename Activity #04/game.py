import pygame

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

SCORE_MAX = 2

size = (1280, 720)
screen = pygame.display.set_mode(size)
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
scoring_sound_effect = pygame.mixer.Sound('assets/bleep.wav')

# player 1
player_1 = pygame.image.load("assets/player.png")
rect_player_1 = player_1.get_rect()
player_1_y = 300
rect_player_1 = rect_player_1.move(50, player_1_y)
player_1_move_up = False
player_1_move_down = False


# player 2 - robot
player_2 = pygame.image.load("assets/player.png")
rect_player_2 = player_2.get_rect()
player_2_y = 300
rect_player_2 = rect_player_2.move(1180, player_2_y)

# ball
ball = pygame.image.load("assets/ball.png")
rect_ball_ = ball.get_rect()
ball_x = 640
ball_y = 360
rect_ball = rect_ball_.move(ball_x, ball_y)
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
        if event.type == pygame.QUIT:
            game_loop = False

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

        # ball collision with the player 2 's paddle
        elif rect_ball.colliderect(rect_player_2) and ball_dx > 0:
            ball_dx *= -1
            if rect_player_2.bottom >= rect_ball.top > rect_player_2.centery + 30:
                if ball_dy == 0:
                    ball_dy = -5
                else:
                    ball_dy *= 1
            elif rect_player_2.top <= rect_ball.bottom < rect_player_2.centery - 30:
                if ball_dy == 0:
                    ball_dy = -5
                else:
                    ball_dy *= -1
                bounce_sound_effect.play()
            elif rect_player_2.centery + 30 >= rect_ball.centery > rect_player_2.centery - 30:
                ball_dy = 0

        # scoring points
        if rect_ball.x < -50:
            rect_ball.x = 640
            rect_ball.y = 360
            ball_dy *= -1
            ball_dx *= -1
            score_2 += 1
            scoring_sound_effect.play()
        elif rect_ball.x > 1320:
            rect_ball.x = 640
            rect_ball.y = 360
            ball_dy *= -1
            ball_dx *= -1
            score_1 += 1
            scoring_sound_effect.play()

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

        # player 2 "Artificial Intelligence"
        rect_player_2.y = rect_ball.y
        if rect_player_2.y <= 0:
            rect_player_2.y = 0
        elif rect_player_2.y >= 570:
            rect_player_2.y = 570

        # update score hud
        score_text = score_font.render(str(score_1) + ' x ' + str(score_2), True, COLOR_WHITE, COLOR_BLACK)

        # drawing objects
        screen.blit(ball, (rect_ball.x, rect_ball.y))
        screen.blit(player_1, (rect_player_1.x, rect_player_1.y))
        screen.blit(player_2, (rect_player_2.x, rect_player_2.y))
        screen.blit(score_text, score_text_rect)
    else:
        # drawing victory
        screen.fill(COLOR_BLACK)
        screen.blit(score_text, score_text_rect)
        screen.blit(victory_text, victory_text_rect)

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
