import pygame
import sys
import random

def game_floor():
    screen.blit(floor_base, (floor_x_pos, 0))
    screen.blit(floor_base, (floor_x_pos + 1790, 0))

def check_collision(clouds):
    for cloud in clouds:
        if plane_rect.colliderect(cloud):
            return False
    if plane_rect.bottom>=900 or plane_rect.top<=-200:
        return False
    return True


#nori
def create_cloud():
    random_cloud_pos=random.choice(cloud_height)
    main_cloud=cloud_surface.get_rect(midbottom=(2000, random_cloud_pos))
    return main_cloud


def move_clouds(clouds):
    for cloud in clouds:
        cloud.centerx -= 1
    return clouds

def draw_clouds(clouds):
    for cloud in clouds:
        screen.blit(cloud_surface,cloud)


pygame.init()

clock=pygame.time.Clock()
#variabile
gravity=0.02
plane_movement=0


screen=pygame.display.set_mode((1800,1000))
background=pygame.image.load("Background.jpg").convert()
background = pygame.transform.smoothscale(background, screen.get_size())
plane=pygame.image.load("avion negru.png").convert_alpha()
plane=pygame.transform.scale(plane, (300, 100))
plane_rect=plane.get_rect(center=(500,10))

floor_base=pygame.image.load("floor.png").convert_alpha()
floor_x_pos=0


message=pygame.image.load("Retry.png").convert_alpha()
game_over_rect=message.get_rect(center=(900,500))


#generare Pt nori Individuali
cloud_surface=pygame.image.load("1 cloud.png").convert_alpha()
#cloud_surface=pygame.transform.scale(cloud_surface, (100, 100))
cloud_list=[]
SPAWNCLOUD=pygame.USEREVENT
pygame.time.set_timer(SPAWNCLOUD, 3600)
cloud_height=[400, 500, 600, 700, 800, 300, 200, 100 , 0]


game_active=True
while True:
    #Sa se inchida cand se apasa pe buton
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and game_active:
                plane_movement=0
                plane_movement-=2
            if event.key==pygame.K_SPACE and game_active==False:
                plane_rect.center=(300,500)
                plane_movement=0
                game_active=True
        if event.type==SPAWNCLOUD and game_active:
            cloud_list.append(create_cloud())
    #pentru fundal
    screen.blit(background,(0,0))
    if game_active:
        plane_movement+=gravity
        plane_rect.centery+=plane_movement
        screen.blit(plane, plane_rect)

        cloud_list=move_clouds(cloud_list)
        draw_clouds(cloud_list)

        game_active=check_collision(cloud_list)
    else:
        screen.blit(message, game_over_rect)
    #pentru avion
    plane_movement+=gravity
    plane_rect.centery+=plane_movement
    screen.blit(plane, plane_rect)


    #Verificare daca Izbeste nori
    #game_active=check_collision()
    
    #resetare nori
    floor_x_pos-=1
    game_floor() 
    if floor_x_pos<=-1790:
        floor_x_pos=0

    pygame.display.update()
    #frame-uri
    clock.tick(120)