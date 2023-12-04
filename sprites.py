import pygame as pg
import random



player_image = pg.image.load("DemonSlug-Sheet.png")
player_image_up = pg.image.load("DemonSlug-Sheet up.png")
player_image_down = pg.image.load("DemonSlug-Sheet down.png")
player_image_left = pg.image.load("DemonSlug-Sheet left.png")
swing_image1 = pg.image.load("swing1.png")
swing_image2 = pg.image.load("swing2.png")
swing_image3 = pg.image.load("swing3.png")
swing_image4 = pg.image.load("swing4.png")
swing_image5 = pg.image.load("swing5.png")
swing_image6 = pg.image.load("swing6.png")
swing_image7 = pg.image.load("swing7.png")
swing_image8 = pg.image.load("swing8.png")
swing_image9 = pg.image.load("swing9.png")
swing_image10 = pg.image.load("swing10.png")


enemy_image = pg.image.load("enemy.png")
projectile_image = pg.image.load("bullet1_strip.png")
enemy_image = pg.transform.scale(enemy_image,(100,100))

class Player(pg.sprite.Sprite):
    def __init__(self, all_sprites, enemies):
        pg.sprite.Sprite.__init__(self)
        
        self.image = player_image
        self.rect = self.image.get_rect()
        self.pos_x = 50
        self.pos_y = 400
        self.speed = 5
        self.hp = 100
        self.all_sprites = all_sprites
        self.enemies = enemies  
        self.attack_cooldown = 0
        self.attacking = True



    def take_dmg(self,dmg):
          self.hp -= dmg
          if self.hp <= 0:
               pg.quit()
   

    def attack(self):
          projectile = Ranged_attack(self.pos_x+10, self.pos_y, self.enemies)
          self.all_sprites.add(projectile)
          print("attacked")

    def melee(self):
          if self.attack_cooldown ==0:
               self.attack_cooldown =30
               print("melee")
               melee = MeleeAttack(self.rect.center)
               self.all_sprites.add(melee)

    def update(self):
            
            if self.attack_cooldown > 0:
                 self.attack_cooldown -=1


            self.rect.centerx = self.pos_x 
            self.rect.centery = self.pos_y 

            if self.pos_x > 900:
                 self.kill()

            keys = pg.key.get_pressed()
            if keys[pg.K_w]:
                 self.pos_y -= self.speed
                 self.image = player_image_up

            if keys[pg.K_s]:
                 self.pos_y += self.speed
                 self.image = player_image_down

            if keys[pg.K_a]:
                 self.pos_x -= self.speed
                 self.image = player_image_left


            if keys[pg.K_d]:
                 self.pos_x += self.speed
                 self.image = player_image

            if keys[pg.K_SPACE]:
                 self.attack()

            if keys[pg.K_x]:
                 self.melee()     
                      



class Enemy(pg.sprite.Sprite):
     def __init__(self):
          pg.sprite.Sprite.__init__(self)
          self.image = enemy_image
          self.rect = self.image.get_rect()
          self.pos_x = 900
          self.pos_y = random.randint(0,600)
          self.speed = random.randint(1,10)

     def update(self):
         

         self.rect.centerx = self.pos_x 
         self.rect.centery = self.pos_y 

         self.pos_x -= self.speed

         if self.pos_x < -100:
              self.kill() 

class Ranged_attack(pg.sprite.Sprite):
     def __init__(self,x,y,enemies):
          pg.sprite.Sprite.__init__(self)
          self.image = projectile_image
          self.rect = self.image.get_rect()
          self.image.set_colorkey((255,255,255))
          self.enemies = enemies

          self.pos_x=x
          self.pos_y=y
          self.speed=10

          self.rect.x=self.pos_x
          self.rect.y=self.pos_y

     def update(self):
          self.rect.x=self.pos_x
          self.rect.y=self.pos_y

          self.pos_x+=self.speed  

          hit = pg.sprite.spritecollide(self, self.enemies, True )


        


class MeleeAttack(pg.sprite.Sprite):
     def __init__(self,position):
          super().__init__()
          self.image = swing_image1
          self.rect = self.image.get_rect(center=position)
          self.rect.center = position
          self.lifetime = 10
          self.attacking_frames = [swing_image1,swing_image2,swing_image3,swing_image4,swing_image5,swing_image6,swing_image7,swing_image8,swing_image9,swing_image10]
          self.current_frame = 0   # lag denne variabelen for player spriten
          self.last_update = 0
          self.pos = position


     def update(self):
          self.animate()
          self.rect.center = self.pos

          self.lifetime -= 1
          if  self.lifetime <= 0:
               self.kill()     

     def animate(self):
          now = pg.time.get_ticks()   # på starten av animate henter vi hvilken "tick" eller frame vi er på 1 tick er 1 FPS
          print("animated")
           # vis vi står stille, altså dette er animasjonen vi vil kjøre om vi status for player er "standing"         
          if now - self.last_update > 2:   # her sørger vi for at vi bytte bilde kun hver 350 tick, lavere tall animerer fortere
               self.last_update = now
               self.current_frame = (self.current_frame + 1) % len(self.attacking_frames)
               self.image = self.attacking_frames[self.current_frame]
               self.rect = self.image.get_rect()
               print("anim")

          



         








               
            

           
