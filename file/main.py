import pygame
from fighter import Fighter
from pygame import mixer_music, mixer
import sys

pygame.init()
mixer.init()
#xaxi patohana sarqum

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Game')


clock = pygame.time.Clock()
FPS = 60

WARRIOR_SIZE = 127
WARRIOR_SCALE = 4.2
WARRIOR_OFFSET = [40, 90]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
GIRL_WARRIOR_SIZE = 80
GIRL_WARRIOR_SCALE = 5.1
GIRL_OFFSET = [20, 50]
GIRL_WARRIOR_DATA = [GIRL_WARRIOR_SIZE, GIRL_WARRIOR_SCALE, GIRL_OFFSET]
#guyner
WHITE = (255,255,255)
PINK = (194, 52, 132)
PURPLE = (209, 25, 209)
BLACK = (13, 12, 12)
YELLOW = (215, 247, 5)
BLUE = (5, 170, 247)
RED = (214, 13, 33)


intro = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0] #p1, p2
round_over = False
ROUND_OVER_COOLDOWN = 2000
WINNING_SCORE = 3



crag = "C:\\Users\\Asus\\Desktop\\xpoci_game\\file\\audio\\bolorselcragravoroxenq.mp3"
# crag = "C:\\Users\\Asus\\Desktop\\xpoci_game\\file\\audio\\esAlbertnem.mp3"

# mixer.music.set_volume(0.5)


game_music_path = "C:\\Users\\Asus\\Desktop\\xpoci_game\\file\\audio\\mixkit-medieval-show-fanfare-announcement-226.mp3"
# pygame.mixer.music.set_volume(0.1)
# pygame.mixer.music.play(-1, 0.0,5000)
# pygame.mixer.music.load("C\\Users\\Asus\\Desktop\\xpoci_game\\file\\audio\\taxemgluxd.mp3")
# pygame.mixer.music.load("C:\\Users\\Asus\\Desktop\\xpoci_game\\file\\audio\\chechecheno.mp3")
cheche = pygame.mixer.Sound("C:\\Users\\Asus\\Desktop\\xpoci_game\\file\\audio\\checheno.wav")
cheche.set_volume(1)

death_sound = mixer.Sound("C:\\Users\\Asus\\Desktop\\xpoci_game\\file\\audio\\taxemgluxdwav.wav")
victory_sound = mixer.Sound("C:\\Users\\Asus\\Desktop\\xpoci_game\\file\\audio\\winning.wav")  # Add your victory sound path

# taxemgluxd = pygame.mixer.Sound("C:\\Users\\Asus\\Desktop\\xpoci_game\\file\\audio\\taxemgluxdwav.wav")
# taxemgluxd.set_volume(0.5)

tebekrishka = pygame.mixer.Sound("C:\\Users\\Asus\\Desktop\\xpoci_game\\file\\audio\\krishkaaa.wav")
tebekrishka.set_volume(1)


# hit_sound = mixer.Sound("C:\\Users\\Asus\\Desktop\\xpoci_game\\file\\audio\\chechechenowav.wav")
# death_sound = mixer.Sound("C:\\Users\\Asus\\Desktop\\xpoci_game\\file\\audio\\taxemgluxdwav.wav")
#hetevi nkar
bg_image = pygame.image.load("back.jpg").convert_alpha()
warrior_sheet = pygame.image.load("C:\\Users\\Asus\\Desktop\\xpoci_game\\file\\new\\Necromancer_creativekind-Sheet.png").convert_alpha()
girl_warrior_sheet = pygame.image.load("C:\\Users\\Asus\\Desktop\\xpoci_game\\file\\nightborn\\NightBorne.png").convert_alpha()



victory1_img = pygame.image.load("C:\\Users\\Asus\\Desktop\\xpoci_game\\file\\nkarner\\victoryy.jpg.png").convert_alpha()
wasted_img = pygame.image.load("C:\\Users\\Asus\\Desktop\\xpoci_game\\file\\nkarner\\wasted.jpg.png").convert_alpha()




WARRIOR_ANIMATION_STEPS = [8, 8, 13, 13, 17, 5, 9]
GIRL_WARRIOR_STEPS = [9, 6, 12, 5, 23]
#vor nkary baci

count_font = pygame.font.Font("C:\\Users\\Asus\\Desktop\\xpoci_game\\file\\counter\\Turok.ttf", 150)
score_font = pygame.font.Font("C:\\Users\\Asus\\Desktop\\xpoci_game\\file\\counter\\Turok.ttf", 30)

cragravorox = pygame.mixer.Sound("C:\\Users\\Asus\\Desktop\\xpoci_game\\file\\audio\\bolorselcragravoroxenq.mp3")
cragravorox.set_volume(0.5)

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))


def draw_bg():
    popoxvac_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(popoxvac_bg, (0, 0))


def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 5, y - 5, 507, 50))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 500 * ratio, 40))

def draw_start_button():
    text_surface = count_font.render('Start', True, WHITE)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text_surface, text_rect)
    return text_rect

def is_start_button_clicked(pos, button_rect):
    return button_rect.collidepoint(pos)


def menu():
    mixer.music.load(crag)
    mixer.music.play(-1)
    while True:
        screen.fill(BLACK)
        start_button_rect = draw_start_button()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if is_start_button_clicked(event.pos, start_button_rect):
                    mixer.music.stop()
                    return  # Exit the menu loop and start the game

        pygame.display.flip()


def game():
    global intro, last_count_update, round_over, score, fighter_1, fighter_2

    mixer.music.load(game_music_path)
    mixer.music.play(-1)

    fighter_1 = Fighter(1, 500, 410, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, cheche)
    fighter_2 = Fighter(2, 900, 410, True, GIRL_WARRIOR_DATA, girl_warrior_sheet, GIRL_WARRIOR_STEPS, tebekrishka)

    run = True
    while run:
        clock.tick(FPS)
        draw_bg()

        draw_health_bar(fighter_1.health, 20, 20)
        draw_health_bar(fighter_2.health, 980, 20)
        draw_text('PLAYER 1: ' + str(score[0]), score_font, YELLOW, 20, 70)
        draw_text('PLAYER 2: ' + str(score[1]), score_font, YELLOW, 1000, 70)

        if intro <= 0:
            fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, round_over)
            fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, round_over)
        else:
            draw_text(str(intro), count_font, BLACK, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
            if (pygame.time.get_ticks() - last_count_update) >= 1000:
                intro -= 1
                last_count_update = pygame.time.get_ticks()
                print(intro)

        fighter_1.update()
        fighter_2.update()

        fighter_1.draw(screen)
        fighter_2.draw(screen)

        if not round_over:
            if not fighter_1.alive:
                score[1] += 1
                round_over = True
                round_over_time = pygame.time.get_ticks()
                death_sound.play()  # Play death sound
                if score[1] == WINNING_SCORE:
                    victory_sound.play()  # Play victory sound
                    draw_text("PLAYER 2 WINS!", count_font, YELLOW, SCREEN_WIDTH / 2 - 300, SCREEN_HEIGHT / 2 - 50)
                    pygame.display.update()
                    pygame.time.delay(2000)
                    run = False
            elif not fighter_2.alive:
                score[0] += 1
                round_over = True
                round_over_time = pygame.time.get_ticks()
                death_sound.play()  # Play death sound
                if score[0] == WINNING_SCORE:
                    victory_sound.play()  # Play victory sound
                    draw_text("PLAYER 1 WINS!", count_font, YELLOW, SCREEN_WIDTH / 2 - 300, SCREEN_HEIGHT / 2 - 50)
                    pygame.display.update()
                    pygame.time.delay(23000)
                    run = False
        else:
            if score[0] < WINNING_SCORE and score[1] < WINNING_SCORE:
                screen.blit(victory1_img, (590, 100))
                if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
                    round_over = False
                    intro = 3
                    
                    fighter_1 = Fighter(1, 500, 410, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, cheche)
                    fighter_2 = Fighter(2, 900, 410, True, GIRL_WARRIOR_DATA, girl_warrior_sheet, GIRL_WARRIOR_STEPS, tebekrishka)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()


menu()
game()
#--------------------------------------------------------------------------------------------------------------------------------------------

# import pygame
# from fighter import Fighter

# pygame.init()

# # Screen dimensions
# SCREEN_WIDTH = 1500
# SCREEN_HEIGHT = 800

# # Initialize screen
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption('Game')

# clock = pygame.time.Clock()
# FPS = 60

# # Colors
# WHITE = (255, 255, 255)
# PINK = (194, 52, 132)
# PURPLE = (209, 25, 209)
# BLACK = (13, 12, 12)
# YELLOW = (215, 247, 5)
# BLUE = (5, 170, 247)
# RED = (214, 13, 33)

# # Load background image
# bg_image = pygame.image.load("back.jpg").convert_alpha()

# # Draw background
# def draw_bg():
#     # Resize background image to fit screen
#     resized_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
#     screen.blit(resized_bg, (0, 0))

# # Draw health bar
# def draw_health_bar(health, x, y):
#     ratio = health / 100
#     pygame.draw.rect(screen, WHITE, (x - 5, y - 5, 510, 50))  # Border
#     pygame.draw.rect(screen, RED, (x, y, 500, 40))  # Background
#     pygame.draw.rect(screen, YELLOW, (x, y, 500 * ratio, 40))  # Health

# # Initialize fighters
# fighter_1 = Fighter(500, 410)
# fighter_2 = Fighter(900, 410)

# # Game loop
# run = True
# while run:
#     clock.tick(FPS)

#     # Draw background
#     draw_bg()

#     # Draw health bars
#     draw_health_bar(fighter_1.health, 20, 20)
#     draw_health_bar(fighter_2.health, 980, 20)

#     # Move fighters
#     fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
#     fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1)

#     # Draw fighters
#     fighter_1.draw(screen)
#     fighter_2.draw(screen)

#     # Event handling
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#     # Update display
#     pygame.display.update()

# # Quit pygame
# pygame.quit()
#--------------------------------------------------------------------------------------------------------------------------------------------

# import pygame
# from fighter import Fighter

# pygame.init()

# # Screen dimensions
# SCREEN_WIDTH = 1500
# SCREEN_HEIGHT = 800

# # Initialize screen
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption('Game')

# clock = pygame.time.Clock()
# FPS = 60

# # Colors
# WHITE = (255, 255, 255)
# PINK = (194, 52, 132)
# PURPLE = (209, 25, 209)
# BLACK = (13, 12, 12)
# YELLOW = (215, 247, 5)
# BLUE = (5, 170, 247)
# RED = (214, 13, 33)

# # Load background image
# bg_image = pygame.image.load("back.jpg").convert_alpha()

# # Draw background
# def draw_bg():
#     # Resize background image to fit screen
#     resized_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
#     screen.blit(resized_bg, (0, 0))

# # Draw health bar
# def draw_health_bar(health, x, y):
#     ratio = health / 100
#     pygame.draw.rect(screen, WHITE, (x - 5, y - 5, 510, 50))  # Border
#     pygame.draw.rect(screen, RED, (x, y, 500, 40))  # Background
#     pygame.draw.rect(screen, YELLOW, (x, y, 500 * ratio, 40))  # Health

# # Initialize fighters
# fighter_1 = Fighter(500, 410)
# fighter_2 = Fighter(900, 410)

# # Game loop
# run = True
# while run:
#     clock.tick(FPS)

#     # Draw background
#     draw_bg()

#     # Draw health bars
#     draw_health_bar(fighter_1.health, 20, 20)
#     draw_health_bar(fighter_2.health, 980, 20)

#     # Move fighters
#     fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
#     fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1)

#     # Draw fighters
#     fighter_1.draw(screen)
#     fighter_2.draw(screen)

#     # Event handling
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#     # Update display
#     pygame.display.update()

# # Quit pygame
# pygame.quit()
