import pygame as pg
import random

from sprites import *
pg.init() # starter pygame modul

player_image = pg.image.load("DemonSlug-Sheet.png")

#screen.blit(player_images)
 
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)
 
screen = pg.display.set_mode((800,600)) # lager spill vindu, 800x600
clock = pg.time.Clock()

font_cs30 = pg.font.SysFont("Comic Sans",30)
font_times40 = pg.font.SysFont("Times New Roman",40)

all_sprites = pg.sprite.Group()
enemies = pg.sprite.Group()


player = Player(all_sprites,enemies) 
all_sprites.add(player)

i = 0
playing = True
while playing: # game loop
    clock.tick(120)
    #print("FPS: ", i)
    i += 1
    for event in pg.event.get():
        if event.type == pg.QUIT: # hvis vi trykker på krysset i spillvinduet
            playing = False
            pg.quit()

    if len(enemies) < 10:
        new_enemy = Enemy()
        all_sprites.add(new_enemy)
        enemies.add(new_enemy)

    all_sprites.update()

    hits = pg.sprite.spritecollide(player, enemies, True)
    if hits:
        player.take_dmg(10)
        print(player.hp)

    hp_text = font_times40.render(f"HP: {player.hp}", False,(RED))              
    

    screen.fill(BLACK)
    all_sprites.draw(screen)

    screen.blit(hp_text,(10,10))
 
    pg.display.update()