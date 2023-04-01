import pygame # Импорт модуля пайгейм
import random
pygame.init()
ping = pygame.mixer.Sound
width = 1366
height = 768
fps = 60
gameName = 'First Project'
pygame.mixer.music.load('8bit.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
screen = pygame.display.set_mode((width, height)) # Создание экрана с заданными

BLACK = '#000000'
WHITE = '#FFFFFF'
RED = '#FF0000'
GREEN = '#008000'
BLUE = '#0000FF'
CYAN = '#00FFFF'

Ball1 = ball.Ball()
Ball2 = ball.Ball()
Ball3 = ball.Ball()

balls = [Ball1, Ball2, Ball3]

img = pygame.image.load('img.png')
img = pygame.transform.scale(img, (60, 50))
img_rect = img.get_rect()
score = 0
def draw_text(screen,text,size,x,y,color):
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font('score', 40)
    text_image = font.rect(draw_text, True, BLACK)
    text_rect =text_image.get_rect()
    text_rect.center = (0,0)
    screen.bilt(text_image, text_rect)

import pygame

pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

X = 400
Y = 400

display_surface = pygame.display.set_mode((X, Y))

pygame.display.set_caption('Show Text')

font = pygame.font.Font('freesansbold.ttf', 32)

text = font.render('GeeksForGeeks', True, green, blue)

textRect = text.get_rect()

textRect.center = (X // 2, Y // 2)


while True:

    display_surface.fill(white)

    display_surface.blit(text, textRect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            quit()

        pygame.display.update()
platform = pygame.image.load('platform.png')
platform_rect = platform.get_rect()

platform_rect.x = width / 2 - platform.get_width() / 2
platform_rect.y = height - 60
speedX = 10
speedY = 10


clock = pygame.time.Clock()
run = True
while run:
    clock.tick(fps)
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()

    screen.fill(CYAN)
    for ball in balls:
        ball.update(width, screen)
        if platform_rect.celliderect(ball.rect):
            score += 1
            ball.speed[1] = -ball.speed[1]
        if ball.rect.bottom > height:
            rounds -= 1
            if rounds <= 0
                run = False
            ball.respawn(width)


    screen.blit(img, img_rect)
    screen.blit(platform, platform_rect)
    pygame.display.update()
    img_rect.x += speedX
    img_rect.y += speedY


    if img_rect.top < 0:
     ping.play()
    if img_rect.left < 0:
     ping.play(0)
    if img_rect.right > width:
     ping.play( )

    if img_rect.top < 0:
        speedY = -speedY
    if img_rect.left < 0:
        speedX = -speedX
    if img_rect.right > width:
        speedX = -speedX

    if key[pygame.K_LEFT] and platform_rect.left > 0:
        platform_rect.x -= 10
    if key[pygame.K_RIGHT] and platform_rect.right < width:
        platform_rect.x += 10

    if img_rect.colliderect(platform_rect):
        speedY = -speedY

    if img_rect.top < 0:
     ping.play()
    if img_rect.left < 0:
     ping.play(0)
    if img_rect.right > width:
     ping.play( )

    if img_rect.top < 0:
        speedY = -speedY
    if img_rect.left < 0:
        speedX = -speedX
    if img_rect.right > width:
        speedX = -speedX


