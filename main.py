from pygame import *

#создаём окошко
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load("fonn.jpg"), (win_width, win_height))
clock = time.Clock()

class GameSprite(sprite.Sprite):
 #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
    
    
        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
    
    
        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    #метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
 
#класс главного игроков
class Player(GameSprite):
    #метод для управления спрайтом стрелками клавиатуры
    def updateR(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 65:
            self.rect.y += self.speed
    def updateL(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 65:
            self.rect.y += self.speed
    
class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        super.__init__(self, player_image, player_x, player_y, size_x, size_y, 3)
        self.speed_x = 5
        self.speed_y = 5
    def update(self, rect1, rect2):
        

player_l = Player("Lraket.jpg", 10, 250, 40, 100, 20)
player_r = Player("Lraket.jpg", 650, 250, 40, 100, 20)

Ball = 
run = True

while run:
    #событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(background, (0,0))
    player_l.updateL()
    player_r.updateR()

    player_l.reset()
    player_r.reset()

    display.update()
    clock.tick(60)