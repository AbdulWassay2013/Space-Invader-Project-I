import pygame
import math
import random
pygame.init()
SCREEN_WIDTH,SCREEN_HEIGHT = 800,500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
background = pygame.image.load("download.png")
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("download (1).png")
pygame.display.set_icon(icon)
player_img = pygame.image.load("player.png")
player_X = PLAYER_START_X
player_Y = PLAYER_START_Y
player_X_change = 0
enemy_img = []
enemy_X = []
enemy_Y = []
enemy_X_change = []
enemy_Y_change = []
num_of_enemy = 6
for _i in range(num_of_enemy):
    enemy_img.append(pygame.image.load("enemy.png")) 
    enemy_X.append(random.randint(0,SCREEN_WIDTH - 64))
    enemy_Y.append(random.randint(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX))
    enemy_X_change.append(ENEMY_SPEED_X)
    enemy_Y_change.append(ENEMY_SPEED_Y)
bullet_img = pygame.image.load("bullet.png")
bullet_X = 0
bullet_Y = PLAYER_START_Y
bullet_X_change = 0
bullet_Y_change = BULLET_SPEED_Y
bullet_state = "ready"
score_value = 0
font = pygame.font.Font("freesansbold.ttf",32)
text_X = 10
text_Y = 10
over_font = pygame.font.Font("freesansbold.ttf",64)
def show_score(x,y):
    score = font.render("Score " + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
def game_over_text():
    over_text = over_font.render("Game Over",True,(255,255,255))
    screen.blit(over_text,(200,250)) 