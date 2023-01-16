import pygame
from tkinter import *
from PIL import Image, ImageTk
import random
import time
import cv2
from cv2 import sqrt
import math
import easygui

pygame.init()

coord = []
f = open("coordonate.txt", "r")
lines = f.readline()
while lines:
    a=int(lines.split()[0])
    b=int(lines.split()[1])
    coord.append([a, b])
    lines = f.readline()
random.seed(None)
rand = random.randint(0,19)
x=coord[rand][0]
y=coord[rand][1]
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Map')
font = pygame.font.SysFont('Comic Sans MS', 40)
clock = pygame.time.Clock()
where = 0
open = 1
running = True
while running:

    if where == 0:
        bg = pygame.transform.scale(pygame.image.load("bg.jpg"), [SCREEN_WIDTH, SCREEN_HEIGHT])
        screen.blit(bg, (0, 0))
        wins = 0
        fails = 0
        buttonX = 200
        buttonY = 100
        button1 = pygame.draw.rect(screen, (20, 140, 90), ((SCREEN_WIDTH-buttonX)/2, (SCREEN_HEIGHT-4*buttonY)/2, buttonX, buttonY), 0, 20)
        button2 = pygame.draw.rect(screen, (20, 140, 90), ((SCREEN_WIDTH-buttonX)/2, (SCREEN_HEIGHT-buttonY)/2, buttonX, buttonY), 0, 20)
        button3 = pygame.draw.rect(screen, (20, 140, 90), ((SCREEN_WIDTH-buttonX)/2, (SCREEN_HEIGHT+2*buttonY)/2, buttonX, buttonY), 0, 20)

        text = font.render('Start', 1, (136, 255, 0))
        textRect = text.get_rect()
        textRect.center = (button1.x + buttonX/2, button1.y + buttonY/2)
        screen.blit(text, textRect)
        text = font.render('Help', 1, (136, 255, 0))
        textRect = text.get_rect()
        textRect.center = (button2.x + buttonX/2, button2.y + buttonY/2)
        screen.blit(text, textRect)
        text = font.render('Credits', 1, (136, 255, 0))
        textRect = text.get_rect()
        textRect.center = (button3.x + buttonX/2, button3.y + buttonY/2)
        screen.blit(text, textRect)

        mouse_position = pygame.mouse.get_pos()
        if mouse_position[0] > (SCREEN_WIDTH-buttonX)/2 and mouse_position[0] < (SCREEN_WIDTH-buttonX)/2 + buttonX:
            if mouse_position[1] > (SCREEN_HEIGHT-4*buttonY)/2 and mouse_position[1] < (SCREEN_HEIGHT-4*buttonY)/2 + buttonY:
                button1 = pygame.draw.rect(screen, (0,0,255), ((SCREEN_WIDTH-buttonX)/2, (SCREEN_HEIGHT-4*buttonY)/2, buttonX, buttonY), 0, 20)
                text = font.render('Start', 1, (136, 255, 0))
                textRect = text.get_rect()
                textRect.center = (button1.x + buttonX/2, button1.y + buttonY/2)
                screen.blit(text, textRect)
            elif mouse_position[1] > (SCREEN_HEIGHT-buttonY)/2 and mouse_position[1] < (SCREEN_HEIGHT-buttonY)/2 + buttonY:
                button2 = pygame.draw.rect(screen, (0,0,255), ((SCREEN_WIDTH-buttonX)/2, (SCREEN_HEIGHT-buttonY)/2, buttonX, buttonY), 0, 20)
                text = font.render('Help', 1, (136, 255, 0))
                textRect = text.get_rect()
                textRect.center = (button2.x + buttonX/2, button2.y + buttonY/2)
                screen.blit(text, textRect)
            elif mouse_position[1] > (SCREEN_HEIGHT+2*buttonY)/2 and mouse_position[1] < (SCREEN_HEIGHT+2*buttonY)/2 + buttonY:
                button3 = pygame.draw.rect(screen, (0,0,255), ((SCREEN_WIDTH-buttonX)/2, (SCREEN_HEIGHT+2*buttonY)/2, buttonX, buttonY), 0, 20)
                text = font.render('Credits', 1, (136, 255, 0))
                textRect = text.get_rect()
                textRect.center = (button3.x + buttonX/2, button3.y + buttonY/2)
                screen.blit(text, textRect)

        pygame.display.update()  

    elif where == 1:
        used = []
        bg = pygame.transform.scale(pygame.image.load("Romania.jpg"), [SCREEN_WIDTH, SCREEN_HEIGHT])
        screen.blit(bg, (0, 0))
        while where == 1:

            
            back = pygame.draw.rect(screen, (200, 10, 90), (0, 0, buttonX/4, buttonY/2), 0, 10, 0, 10, 10, 10)
            arrow = pygame.transform.scale(pygame.image.load("arrow.png"), [50, 50])
            screen.blit(arrow, (0, 0))
            if open==1:
                path = "Baza date/{}.jpg".format(rand+1)
                image = cv2.imread(path)
                window_name = 'Image'
                cv2.imshow(window_name, image)
                open = 0

            mouse_position = pygame.mouse.get_pos()
            if mouse_position[0] < buttonX/4 and mouse_position[1] < buttonY/2:
                back = pygame.draw.rect(screen, (200, 10, 250), (0, 0, buttonX/4, buttonY/2), 0, 10, 0, 10, 10, 10)
                arrow = pygame.transform.scale(pygame.image.load("arrow.png"), [50, 50])
                screen.blit(arrow, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mouse_position[0]<SCREEN_WIDTH-100 and mouse_position[0]>SCREEN_WIDTH-300 and mouse_position[1]>100 and mouse_position[1]<200:
                        if dist[0]<=20:
                            wins = wins + 1
                            easygui.msgbox("You guessed right!!! Congratulations!!!\nDistance = {}\nWins: {}\nFails: {}".format(dist[0], wins, fails), title="Result")
                            open = 1
                            rand = random.randint(0,19)

                            x=coord[rand][0]
                            y=coord[rand][1]
                        else:
                            fails = fails + 1
                            easygui.msgbox("You guessed WRONG!!!\nDistance = {}\nWins: {}\nFails: {}".format(dist[0], wins, fails), title="Result")
                    else:
                        mouse_position = pygame.mouse.get_pos()
                        dist=sqrt(pow((x - mouse_position[0]), 2) + pow((y - mouse_position[1]), 2))
                        print("dist:", dist[0])
                        
                        if mouse_position[0]>x:
                            if mouse_position[1]>y:
                                print("mai sus, stanga")
                            else:
                                print("mai jos, stanga")
                        else:
                            if mouse_position[1]>y:
                                print("mai sus, dreapta")
                            else:
                                print("mai jos, dreapta")
                        print(mouse_position)
                        print(x, y)
                        pin = pygame.transform.scale(pygame.image.load("pin.png"), [50, 50])
                        screen.blit(bg, (0, 0))
                        screen.blit(pin, (mouse_position[0]-25, mouse_position[1]-46))
                        confirm = pygame.draw.rect(screen, (125,0,125), (SCREEN_WIDTH-300, 100, buttonX, buttonY), 0, 20)
                        text = font.render('Confirm?', 1, (136, 255, 0))
                        textRect = text.get_rect()
                        textRect.center = (confirm.x + 100, confirm.y + 50)
                        screen.blit(text, textRect)
                        
                        if mouse_position[0] < buttonX/4 and mouse_position[1] < buttonY/2:
                            where = 0
                            open = 1
                            rand = random.randint(0,19)
                            x=coord[rand][0]
                            y=coord[rand][1]
                elif event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
            if fails>5:
                where = 4
                open = 1
                rand = random.randint(0,19)
                x=coord[rand][0]
                y=coord[rand][1]
            if wins >= 1:
                where = 5
                open = 1
                rand = random.randint(0,19)
                x=coord[rand][0]
                y=coord[rand][1]

            pygame.display.update()
        
        

          

    elif where == 2:
        bg = pygame.transform.scale(pygame.image.load("help.jpg"), [SCREEN_WIDTH, SCREEN_HEIGHT])
        screen.blit(bg, (0, 0))
        back = pygame.draw.rect(screen, (200, 10, 90), (0, 0, buttonX/4, buttonY/2), 0, 10, 0, 10, 10, 10)
        arrow = pygame.transform.scale(pygame.image.load("arrow.png"), [50, 50])
        screen.blit(arrow, (0, 0))
        mouse_position = pygame.mouse.get_pos()
        if mouse_position[0] < buttonX/4 and mouse_position[1] < buttonY/2:
            back = pygame.draw.rect(screen, (200, 10, 250), (0, 0, buttonX/4, buttonY/2), 0, 10, 0, 10, 10, 10)
            arrow = pygame.transform.scale(pygame.image.load("arrow.png"), [50, 50])
            screen.blit(arrow, (0, 0))
        help = pygame.draw.rect(screen, (0,0,0), (buttonY, buttonY, SCREEN_WIDTH-2*buttonY, SCREEN_HEIGHT-2*buttonY), 0, 30)
        credits = pygame.draw.rect(screen, (255,255,255), (buttonY, buttonY, SCREEN_WIDTH-3*buttonY/2, SCREEN_HEIGHT-3*buttonY/2), 0, 40)
        image = pygame.transform.scale(pygame.image.load("final_help.png"), [1000, 600])
        screen.blit(image, (100, 100))  
        text = font.render('Help', 1, (0, 0, 102))
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH/2, 3*buttonY/2)
        screen.blit(text, textRect)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if mouse_position[0] < buttonX/4 and mouse_position[1] < buttonY/2:
                    where = 0
            elif event.type == pygame.QUIT:
                running = False
                pygame.quit()

        pygame.display.update()  

    elif where == 3:
        bg = pygame.transform.scale(pygame.image.load("credits.jpg"), [SCREEN_WIDTH, SCREEN_HEIGHT])
        screen.blit(bg, (0, 0))
        back = pygame.draw.rect(screen, (200, 10, 90), (0, 0, buttonX/4, buttonY/2), 0, 10, 0, 10, 10, 10)
        arrow = pygame.transform.scale(pygame.image.load("arrow.png"), [50, 50])
        screen.blit(arrow, (0, 0))
        mouse_position = pygame.mouse.get_pos()
        if mouse_position[0] < buttonX/4 and mouse_position[1] < buttonY/2:
            back = pygame.draw.rect(screen, (200, 10, 250), (0, 0, buttonX/4, buttonY/2), 0, 10, 0, 10, 10, 10)
            arrow = pygame.transform.scale(pygame.image.load("arrow.png"), [50, 50])
            screen.blit(arrow, (0, 0))
        credits = pygame.draw.rect(screen, (255,255,255), (buttonY, buttonY, SCREEN_WIDTH-3*buttonY/2, SCREEN_HEIGHT-3*buttonY/2), 0, 40)
        image = pygame.transform.scale(pygame.image.load("credits_matei.jpg"), [1000, 600])
        screen.blit(image, (100, 100))  
        text = font.render('Credits', 1, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH/2, 3*buttonY/2)
        screen.blit(text, textRect) 
         

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if mouse_position[0] < buttonX/4 and mouse_position[1] < buttonY/2:
                    where = 0
            elif event.type == pygame.QUIT:
                running = False
                pygame.quit()

        pygame.display.update()

    elif where == 4:
        bg = pygame.transform.scale(pygame.image.load("lost.jpg"), [SCREEN_WIDTH, SCREEN_HEIGHT])
        screen.blit(bg, (0, 0))
        back = pygame.draw.rect(screen, (200, 10, 90), (0, 0, buttonX/4, buttonY/2), 0, 10, 0, 10, 10, 10)
        arrow = pygame.transform.scale(pygame.image.load("arrow.png"), [50, 50])
        screen.blit(arrow, (0, 0))
        mouse_position = pygame.mouse.get_pos()
        if mouse_position[0] < buttonX/4 and mouse_position[1] < buttonY/2:
            back = pygame.draw.rect(screen, (200, 10, 250), (0, 0, buttonX/4, buttonY/2), 0, 10, 0, 10, 10, 10)
            arrow = pygame.transform.scale(pygame.image.load("arrow.png"), [50, 50])
            screen.blit(arrow, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if mouse_position[0] < buttonX/4 and mouse_position[1] < buttonY/2:
                    where = 0
            elif event.type == pygame.QUIT:
                running = False
                pygame.quit() 

    elif where == 5:
        bg = pygame.transform.scale(pygame.image.load("win.jpg"), [SCREEN_WIDTH, SCREEN_HEIGHT])
        screen.blit(bg, (0, 0))
        back = pygame.draw.rect(screen, (200, 10, 90), (0, 0, buttonX/4, buttonY/2), 0, 10, 0, 10, 10, 10)
        arrow = pygame.transform.scale(pygame.image.load("arrow.png"), [50, 50])
        screen.blit(arrow, (0, 0))
        mouse_position = pygame.mouse.get_pos()
        if mouse_position[0] < buttonX/4 and mouse_position[1] < buttonY/2:
            back = pygame.draw.rect(screen, (200, 10, 250), (0, 0, buttonX/4, buttonY/2), 0, 10, 0, 10, 10, 10)
            arrow = pygame.transform.scale(pygame.image.load("arrow.png"), [50, 50])
            screen.blit(arrow, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if mouse_position[0] < buttonX/4 and mouse_position[1] < buttonY/2:
                    where = 0
            elif event.type == pygame.QUIT:
                running = False
                pygame.quit() 

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos[0] > (SCREEN_WIDTH-buttonX)/2 and mouse_pos[0] < (SCREEN_WIDTH-buttonX)/2 + buttonX:
                if mouse_pos[1] > (SCREEN_HEIGHT-4*buttonY)/2 and mouse_pos[1] < (SCREEN_HEIGHT-4*buttonY)/2 + buttonY:
                    where = 1
                elif mouse_pos[1] > (SCREEN_HEIGHT-buttonY)/2 and mouse_pos[1] < (SCREEN_HEIGHT-buttonY)/2 + buttonY:
                    where = 2
                elif mouse_pos[1] > (SCREEN_HEIGHT+2*buttonY)/2 and mouse_pos[1] < (SCREEN_HEIGHT+2*buttonY)/2 + buttonY:
                    where = 3
        elif event.type == pygame.QUIT:
            running = False
            pygame.quit()
    pygame.display.update()  
    clock.tick(60)
