import pygame
import random

width = 600
height = 800
pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("SpaceShooter by Morvy")
icon = pygame.image.load('images\Space Shooter - 1\HUD\LifeIcon.png')
pygame.display.set_icon(icon)

surface = pygame.Surface((600,800)) # creating surface to downscaling
bg_img = pygame.transform.scale(pygame.image.load('shooter\images\BG.jpg'), (surface.get_width(), surface.get_height()))
player_img = pygame.transform.scale(pygame.image.load('shooter\images\player\player.png'), (125,125))


def main():
    player_position_x = width//2 - player_img.get_width()//2
    player_position_y = height - player_img.get_height()
    play = True
    moving = ''
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            player_position_x -=1
        if keys_pressed[pygame.K_RIGHT]:
            player_position_x +=1
        if keys_pressed[pygame.K_UP]:
            player_position_y -=1
        if keys_pressed[pygame.K_DOWN]:
            player_position_y +=1
            

        surface.blit(bg_img, (0,0))
        surface.blit(player_img, (player_position_x, player_position_y))



        pygame.transform.scale(surface, ((width//surface.get_width(), height//surface.get_height()))) # downscaling
        screen.blit(surface, (0, 0)) # downscaling
        pygame.display.flip()
    pygame.quit()
    

main()