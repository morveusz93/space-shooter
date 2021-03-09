import pygame
import random

width = 800
height = 800
pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("SpaceShooter by Morvy")

surface = pygame.Surface((800,800)) # creating surface to downscaling
bg_img = pygame.transform.scale(pygame.image.load('images\BG.jpg'), (surface.get_width(), surface.get_height()))
player_img = [pygame.transform.scale(pygame.image.load('images\player\player1.png'), (100,100)),
                pygame.transform.scale(pygame.image.load('images\player\player2.png'), (100,100))]

enemies_img = [pygame.transform.scale(pygame.image.load('images\enemies\green.png'),(70,70)), 
                pygame.transform.scale(pygame.image.load('images\enemies\grey.png'),(70,70)), 
                pygame.transform.scale(pygame.image.load('images\enemies\pink.png'),(70,70)), 
                pygame.transform.scale(pygame.image.load('images\enemies\yellow.png'),(70,70))]



i = 0  # for refresh animation (look draw_game)

def move_player(keys_pressed, player_position_x, player_position_y):
    if keys_pressed[pygame.K_LEFT] and player_position_x >= 0:
        player_position_x -=1
    if keys_pressed[pygame.K_RIGHT] and player_position_x < width - player_img[0].get_width():
        player_position_x +=1
    if keys_pressed[pygame.K_UP] and player_position_y >= 0:
        player_position_y -=1
    if keys_pressed[pygame.K_DOWN] and player_position_y < height - player_img[0].get_height() :
        player_position_y +=1    
    return player_position_x, player_position_y

def create_enemies(number_of_enemies):
    enemies_list = []
    for x in range (number_of_enemies):
        enemies_list.append(enemies_img[0])
    return enemies_list

def draw_enemies(enemies_list):
    for enemy in range (0, len(enemies_list)):
        surface.blit(enemies_list[enemy], (10 + 80* enemy, 50))
    pygame.display.update()

def draw_game(player_pos_x, player_pos_y, number_of_enemies):
    global i #for refresh animation 
    surface.blit(bg_img, (0,0))
    surface.blit(player_img[i//5], (player_pos_x, player_pos_y))
    i += 1 
    if i == 10:
        i = 0
    draw_enemies(create_enemies(number_of_enemies))
    pygame.transform.scale(surface, ((width//surface.get_width(), height//surface.get_height()))) # downscaling
    screen.blit(surface, (0, 0)) # downscaling
    pygame.display.flip()


def main():
    player_pos_x = width//2 - player_img[0].get_width()//2
    player_pos_y = height - player_img[0].get_height()
    play = True
    moving = ''
    number_of_enemies = 10
    enemies_list = []
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
        player_pos_x, player_pos_y = move_player(pygame.key.get_pressed(), player_pos_x, player_pos_y)
        draw_game(player_pos_x, player_pos_y, number_of_enemies)

    pygame.quit()
main()