import pygame
import webbrowser
from sys import exit
import math
from pygame_button import *
from Scene_Changer import *
from DB import DB
from Localization import l

class Scene_Credits:
    mfont = pygame.font.Font("msjh.ttf", 24)
    mfont2 = pygame.font.Font("msjh.ttf", 18)
    graphics_bg = pygame.image.load("Graphics/bg_xfly.png")

    audio_bgm_filename = "Audio/BGM/credits.ogg"
    frame = 0
    WINDOWWIDTH = 800 # size of window's width in pixels
    WINDOWHEIGHT = 720 # size of windows' height in pixels
    
    def __init__(self):
        
        ####改解析度
        self.NewScreen = pygame.display.set_mode((self.WINDOWWIDTH,self.WINDOWHEIGHT), 0, 32)
        
        try:
            pygame.mixer.music.load(self.audio_bgm_filename)
            pygame.mixer.music.play(-1)
        except:
            pass

        self.img_logo = pygame.image.load("Graphics/logo.png").convert_alpha()
        
        self.button1_image = self.mfont.render("1104105348 謝政憲 a.k.a. xFly", 24, (255,255,255), True)
        self.button2_image = self.mfont.render("1104105340 謝宸豪", 24, (255,255,255), True)
        self.button3_image = self.mfont.render("1104105355 黃佳禾", 24, (255,255,255), True)

        self.text1 = self.mfont2.render(l("CREDITS_CLICKTOFB"), 14, (255,255,255), True)
        self.text2 = self.mfont2.render(l("CREDITS_PROJECTINFO"), 14, (255,255,255), True)
        
        self.button4_image = self.mfont2.render(l("CREDITS_M1_JOB"), 14, (255,255,255), True)
        self.button5_image = self.mfont2.render(l("CREDITS_M2_JOB"), 14, (255,255,255), True)
        self.button6_image = self.mfont2.render(l("CREDITS_M3_JOB"), 14, (255,255,255), True)

        self.button7_string = l("CREDITS_M1_COMM")
        
        kk = self.button7_string.split("\n")
        self.button7_images = []
        for i in kk:
            self.button7_images.append(self.mfont2.render(i, 14, (255,255,255), True))

        self.button8_string =l("CREDITS_M2_COMM")
        kk = self.button8_string.split("\n")
        self.button8_images = []
        for i in kk:
            self.button8_images.append(self.mfont2.render(i, 14, (255,255,255), True))

        self.button9_string = l("CREDITS_M3_COMM")
        kk = self.button9_string.split("\n")
        self.button9_images = []
        for i in kk:
            self.button9_images.append(self.mfont2.render(i, 14, (255,255,255), True))
            
        self.button1 = pyButton()
        self.button1.setImage(self.button1_image, True)
        self.button2 = pyButton()
        self.button2.setImage(self.button2_image, True)
        self.button3 = pyButton()
        self.button3.setImage(self.button3_image, True)

        self.button4 = pyButton()
        self.button4.setImage(self.button4_image, True)
        self.button5 = pyButton()
        self.button5.setImage(self.button5_image, True)
        self.button6 = pyButton()
        self.button6.setImage(self.button6_image, True)

        self.button7_s = []
        for i in self.button7_images:
            n = pyButton()
            n.setImage(i,True)
            self.button7_s.append(n)

        self.button8_s = []
        for i in self.button8_images:
            n = pyButton()
            n.setImage(i,True)
            self.button8_s.append(n)

        self.button9_s = []
        for i in self.button9_images:
            n = pyButton()
            n.setImage(i,True)
            self.button9_s.append(n)
            
        self.button1.rect.y = 240
        self.button4.rect.y = 264
        self.button2.rect.y = 360
        self.button5.rect.y = 384
        self.button3.rect.y = 480
        self.button6.rect.y = 504

        for i in range(len(self.button7_s)):
            self.button7_s[i].rect.y = 288+18*i

        for i in range(len(self.button8_s)):
            self.button8_s[i].rect.y = 408+18*i
            
        for i in range(len(self.button9_s)):
            self.button9_s[i].rect.y = 528+18*i
            
        self.ButtonGroup = pygame.sprite.Group()
        self.ButtonGroup.add([self.button1, self.button2, self.button3, self.button4, self.button5, self.button6])

        for i in self.button7_s:
            self.ButtonGroup.add(i)

        for i in self.button8_s:
            self.ButtonGroup.add(i)
            
        for i in self.button9_s:
            self.ButtonGroup.add(i)
            
    def update(self, screen):
        mouse1, mouse2, mouse3 = (False,False,False)
        
        # 退出事件處理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse1 = True
                if event.button == 3:
                    mouse3 = True
        
        cur_x, cur_y = pygame.mouse.get_pos()

        self.frame += 1

        if (self.frame%255 > 128):
            AAA = 51 - math.floor(self.frame%255/5)
        else:
            AAA = math.floor(self.frame%255/5)

        screen.blit(self.graphics_bg, (80,AAA))

        #LOGO
        screen.blit(self.img_logo,(self.WINDOWWIDTH-self.img_logo.get_width(),0))

        #按鈕繪製
        self.ButtonGroup.draw(screen)

        #TEXT
        screen.blit(self.text1,(0, self.WINDOWHEIGHT-self.text1.get_height()-32))
        screen.blit(self.text2,(self.WINDOWWIDTH-self.text2.get_width(), self.WINDOWHEIGHT-self.text2.get_height()))

        ####點擊判定
        if (self.frame%255 > 128):
            color = (255 - self.frame%255,255 - self.frame%255,255)
        else:
            color = (self.frame%255,self.frame%255,255)
            
        if (self.button1.rect.collidepoint(cur_x,cur_y)):
            nimg = self.mfont.render("1104105348 謝政憲 a.k.a. xFly", 24, color, True)
            self.button1.setImage(nimg)
            if (mouse1):
                webbrowser.open("https://www.facebook.com/xFly.Dragon", new=1, autoraise=True)
        else:
            self.button1.setImage(self.button1_image)

        if (self.button2.rect.collidepoint(cur_x,cur_y)):
            nimg = self.mfont.render("1104105340 謝宸豪", 24, color, True)
            self.button2.setImage(nimg)
            if (mouse1):
                webbrowser.open("https://www.facebook.com/xxyeadzt", new=1, autoraise=True)
        else:
            self.button2.setImage(self.button2_image)

        if (self.button3.rect.collidepoint(cur_x,cur_y)):
            nimg = self.mfont.render("1104105355 黃佳禾", 24, color, True)
            self.button3.setImage(nimg)
            if (mouse1):
                webbrowser.open("https://www.facebook.com/hjhwsx", new=1, autoraise=True)
        else:
            self.button3.setImage(self.button3_image)

        ####退出處理
        if (mouse3 == True):
            from Scene_Title import Scene_Title
            return Scene_Changer(Scene_Title(), screen)
