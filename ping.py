from pygame import *
w = 600
h = 500
font.init()
font1=font.Font(None,36)
class GameSprite(sprite.Sprite):
   #class constructor
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       super().__init__()
       #every sprite must store the image property
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       #every sprite must have the rect property – the rectangle it is fitted in
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
class player(GameSprite):
   def update(self):
      keyp=key.get_pressed()
      if keyp[K_w] and self.rect.y>=0:
         self.rect.y-=self.speed
      if keyp[K_s] and self.rect.y<=435:
         self.rect.y+=self.speed
   def update1(self):
      keyp=key.get_pressed()
      if keyp[K_UP] and self.rect.y>=0:
         self.rect.y-=self.speed
      if keyp[K_DOWN] and self.rect.y<=435:
         self.rect.y+=self.speed


fps = 60
clock = time.Clock()

window = display.set_mode((w,h))
bg = (1,1,1)
window.fill(bg)
ball = GameSprite("m.jpg",280,210,60,60,5)
man1=player('man1.jpg',30,250,50,150,10)
man2=player('man2.jpg',550,250,50,150,10)
game = True
finish=False
speedx=3
speedy=3
win1=font1.render('p1 wins!!!!',True,(255,255,255))
win2=font1.render('p2 wins!!!!',True,(255,255,255))
while game:
   window.fill(bg)
   if finish!=True:
      ball.rect.x+=speedx
      ball.rect.y+=speedy
   if sprite.collide_rect(man1,ball) or sprite.collide_rect(man2,ball):
      speedx*=-1
   if ball.rect.y>=h-50 or ball.rect.y<=0:
      speedy*=-1
   if ball.rect.x>=w:
      finish=True
      window.blit(win1,(280,210))
   if ball.rect.x<=0:
      finish=True
      window.blit(win2,(280,210))
   for e in event.get():
      if e.type == QUIT:
         game = False
   ball.reset()
   man1.reset()
   man1.update()
   man2.reset()
   man2.update1()
   display.update()
   clock.tick(fps)