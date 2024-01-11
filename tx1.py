import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((600,300))
pygame.display.set_caption("create by thinh")
RED = (178,34,34)
ti_me = 18
clock = pygame.time.Clock()
running = True
hienthixx = False
dk_dat = False
font = pygame.font.SysFont('sans', 50)
font1 = pygame.font.SysFont('sans', 20)
font2 = pygame.font.SysFont('sans', 40)
tiendat = 0
datcuoc = 0
dat_ben_nao = ""
kqtx = ""
kq = 0
tkc = 50000
RED = (165,42,42)
CL1 = (178,34,34)  
CL2 = (255,165,0)
CL3 = (255,255,255)
CL4 = (218,165,32)
CL5 = (205,133,63)
CL6 = (255,255,0)
CL7 = (128,0,0) 
tai = font.render('-Tài-', True, CL2)
xiu = font.render('-Xiu-', True, CL2)
b1 = font1.render('1k', True, CL3)
b5 = font1.render('5k', True, CL3)
b10 = font1.render('10k', True, CL3)
b20 = font1.render('20k', True, CL3)
b50 = font1.render('50k', True, CL3)
b100 = font1.render('100k', True, CL3)
b200 = font1.render('200k', True, CL3)
dtai = font1.render('Đăt Tài', True, CL3)
dxiu = font1.render('Đăt Xiu', True, CL3)
sound1 = pygame.mixer.Sound('y2meta.com-Nhạc-Nền-OB1-_-Free-Fire_-Cuộc-Chiến-Sinh-Tồn-_240p_.wav')
pygame.mixer.Sound.play(sound1)
def xucxac():
    x1 = pygame.image.load('xx1.png').convert()
    x2 = pygame.image.load('xx2.png').convert()
    x3 = pygame.image.load('xx3.png').convert()
    x4 = pygame.image.load('xx4.png').convert()
    x5 = pygame.image.load('xx5.png').convert()
    x6 = pygame.image.load('xx6.png').convert()
    
    tkc = 50000
    xx1 = random.randint(1, 6)
    xx2 = random.randint(1, 6)
    xx3 = random.randint(1, 6)
    global kq
    kq = xx1+xx2+xx3
    if kq <= 10:
        pygame.draw.circle(screen,CL6, (490, 110), 50)
    else:
        pygame.draw.circle(screen,CL6, (70, 110), 50)
    
    if xx1 == 1:
        xx1 = x1
    if xx2 == 1:
        xx2 = x1
    if xx3 == 1:
        xx3 = x1
    
    if xx1 == 2:
        xx1 = x2
    if xx2 == 2:
        xx2 = x2
    if xx3 == 2:
        xx3 = x2

    if xx1 == 3:
        xx1 = x3
    if xx2 == 3:
        xx2 = x3
    if xx3 == 3:
        xx3 = x3

    if xx1 == 4:
        xx1 = x4
    if xx2 == 4:
        xx2 = x4
    if xx3 == 4:
        xx3 = x4

    if xx1 == 5:
        xx1 = x5
    if xx2 == 5:
        xx2 = x5
    if xx3 == 5:
        xx3 = x5

    if xx1 == 6:
        xx1 = x6
    if xx2 == 6:
        xx2 = x6
    if xx3 == 6:
        xx3 = x6
    screen.blit(xx1, (240, 89))
    screen.blit(xx2, (289, 89))
    screen.blit(xx3, (263, 130))
    
while running:
    mouse_x,mouse_y = pygame.mouse.get_pos()
    clock.tick(1)
    screen.fill(RED)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if (50<mouse_x<95) and (240<mouse_y<280):
                    tkc -= 1000
                    tiendat += 1000
                if (120<mouse_x<165) and (240<mouse_y<280):
                    tkc -=5000
                    tiendat += 5000
                if (190<mouse_x<235) and (240<mouse_y<280):
                    tkc -= 10000
                    tiendat += 10000
                if (260<mouse_x<305) and (240<mouse_y<280):
                    tkc -= 20000
                    tiendat += 20000
                if (330<mouse_x<375) and (240<mouse_y<280):
                    tkc -= 50000
                    tiendat += 50000
                if (400<mouse_x<445) and (240<mouse_y<280):
                    tkc -= 100000
                    tiendat += 100000
                if (470<mouse_x<515) and (240<mouse_y<280):
                    tkc -= 200000
                    tiendat += 200000
                if (29<mouse_x<118) and (160<mouse_y<190):#tai
                    dat_ben_nao = 1
                    datcuoc = tiendat
                if (449<mouse_x<538) and (160<mouse_y<190):#xiu
                    dat_ben_nao = 2
                    datcuoc = tiendat
    pygame.draw.circle(screen,CL7, (285,120), 70)
    pygame.draw.rect(screen,CL5, (50,240,45,40))#1k
    pygame.draw.rect(screen,CL5, (120,240,45,40))#5k
    pygame.draw.rect(screen,CL5, (190,240,45,40))#10k
    pygame.draw.rect(screen,CL5, (260,240,45,40))#20k
    pygame.draw.rect(screen,CL5, (330,240,45,40))#50k
    pygame.draw.rect(screen,CL5, (400,240,45,40))#100k
    pygame.draw.rect(screen,CL5, (470,240,45,40))#200k
    pygame.draw.rect(screen, CL2, (29,160,89,30))#dat tai
    pygame.draw.rect(screen, CL2, (449,160,89,30))#dat xiu
    screen.blit(b1, (50,240))
    screen.blit(b5, (120,240))
    screen.blit(b10, (190,240))
    screen.blit(b20, (260,240))
    screen.blit(b50, (330,240))
    screen.blit(b100, (400,240))
    screen.blit(b200, (470,240))
    screen.blit(dtai, (53,165))
    screen.blit(dxiu, (453,165))
    if kq <= 10:
        kqtx = 2
    else:
        kqtx = 1
    ti_me -=1
    if ti_me == 0:
        hienthixx = True
    if ti_me == -1:
        hienthixx = False
        ti_me +=18
        time.sleep(5)
    if hienthixx == True:
        xucxac()
    if kqtx == dat_ben_nao and hienthixx == True:
        tkc+=(tiendat*2)
    screen.blit(tai, (30,80))
    screen.blit(xiu, (450,80))
    tkc_ht = font1.render('TK chính: '+str(tkc), True, CL3)
    screen.blit(tkc_ht, (10,10))
    tiendat_ht = font1.render('Tiên đăt: '+str(tiendat), True, CL3)
    screen.blit(tiendat_ht, (250,200))
    
    
    if dat_ben_nao == 1:
        datcuoc_ht = font1.render(str(tiendat), True, CL3)
        screen.blit(datcuoc_ht, (53, 200))
    if dat_ben_nao == 2:
        datcuoc_ht = font1.render(str(tiendat), True, CL3)
        screen.blit(datcuoc_ht, (453, 200))
    

    if ti_me == 16:
        dat_ben_nao = 0
        tiendat = 0
    
    text_time = font2.render(str(ti_me),True,CL3)
    screen.blit(text_time, (275,10))
    pygame.display.flip()
    
pygame.quit()

