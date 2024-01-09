import sys
import os
import pygame


# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")

# Load Background sprite
Background_image = pygame.image.load("Images/Background.png")
Background_rect = Background_image.get_rect()
Background_rect.topleft = (0,0)

# Load Buttons
ButtonChicken_image = pygame.image.load("Images/ChickenButton.png")
ButtonChicken_rect = ButtonChicken_image.get_rect()
ButtonChicken_rect.topleft = (20,500)
ButtonCannibal_image = pygame.image.load("Images/CannibalButton.png")
ButtonCannibal_rect = ButtonCannibal_image.get_rect()
ButtonCannibal_rect.topleft = (160,500)
Minus_image = pygame.image.load("Images/Minus.png")
Minus_rect = Minus_image.get_rect()
Minus_rect.topleft = (103,500)
Minus1_image = pygame.image.load("Images/Minus.png")
Minus1_rect = Minus1_image.get_rect()
Minus1_rect.topleft = (243,500)
Minus2_image = pygame.image.load("Images/Minus.png")
Minus2_rect = Minus1_image.get_rect()
Minus2_rect.topleft = (700,500)
Quit_image = pygame.image.load("Images/Button.png")
Quit_rect = Quit_image.get_rect()
Quit_rect.topleft = (550,545)
ButtonBoat_image = pygame.image.load("Images/BoatButton.png")
ButtonBoat_image = pygame.transform.scale(ButtonBoat_image, (ButtonBoat_image.get_width()*0.3, ButtonBoat_image.get_height()*0.3))
ButtonBoat_rect = ButtonBoat_image.get_rect()
ButtonBoat_rect.topleft = (300,500)

# Load Boat
Boat_image = pygame.image.load("Images/Boat.png")
Boat_image = pygame.transform.scale(Boat_image, (Boat_image.get_width()*0.4, Boat_image.get_height()*0.4))
Boat_rect = Boat_image.get_rect()
Boat_rect.topleft = (350,300)

# Load Chickens
Chicken_image = pygame.image.load("Images/Chicken.png")
Chicken_image = pygame.transform.scale(Chicken_image, (Chicken_image.get_width()*0.5, Chicken_image.get_height()*0.5))
Chicken_rect = Chicken_image.get_rect()
Chicken_rect.topleft = (100,360)
Chicken1_image = pygame.image.load("Images/Chicken.png")
Chicken1_image = pygame.transform.scale(Chicken1_image, (Chicken1_image.get_width()*0.5, Chicken1_image.get_height()*0.5))
Chicken1_rect = Chicken1_image.get_rect()
Chicken1_rect.topleft = (130,360)
Chicken2_image = pygame.image.load("Images/Chicken.png")
Chicken2_image = pygame.transform.scale(Chicken2_image, (Chicken2_image.get_width()*0.5, Chicken2_image.get_height()*0.5))
Chicken2_rect = Chicken2_image.get_rect()
Chicken2_rect.topleft = (160,360)

# Load Cannibals
Cannibal_image = pygame.image.load("Images/Cannibal.png")
Cannibal_image = pygame.transform.scale(Cannibal_image, (Cannibal_image.get_width()*0.5, Cannibal_image.get_height()*0.5))
Cannibal_rect = Cannibal_image.get_rect()
Cannibal_rect.topleft = (10, 400)
Cannibal1_image = pygame.image.load("Images/Cannibal.png")
Cannibal1_image = pygame.transform.scale(Cannibal1_image, (Cannibal1_image.get_width()*0.5, Cannibal1_image.get_height()*0.5))
Cannibal1_rect = Cannibal1_image.get_rect()
Cannibal1_rect.topleft = (40, 400)
Cannibal2_image = pygame.image.load("Images/Cannibal.png")
Cannibal2_image = pygame.transform.scale(Cannibal2_image, (Cannibal2_image.get_width()*0.5, Cannibal2_image.get_height()*0.5))
Cannibal2_rect = Cannibal2_image.get_rect()
Cannibal2_rect.topleft = (70, 400)



# SFX
pygame.mixer.init()
pygame.mixer.music.set_volume(0.1)

button_SFX = pygame.mixer.Sound(r"Sounds\Button.wav")
EndGame_SFX = pygame.mixer.Sound(r"Sounds\No.mp3")
EndGame1_SFX = pygame.mixer.Sound(r"Sounds\good.mp3")
EndGame2_SFX = pygame.mixer.Sound(r"Sounds\yippe.mp3")

playlist = list()

def addMusic(playlist):
    playlist.append ( r"Sounds\Music\Funk.mp3" )
    playlist.append ( r"Sounds\Music\Pox.mp3" )
    playlist.append ( r"Sounds\Music\Rains.mp3" )
    playlist.append ( r"Sounds\Music\Space.mp3" )
    playlist.append ( r"Sounds\Music\Spring.mp3" )

addMusic(playlist)
pygame.mixer.music.load(playlist[0])
playlist.pop(0)

pygame.mixer.music.play()

font = pygame.font.Font(None, 36)



# Menus
def start():

    Some_text = font.render(f" Press Anywhere to start ", True, (255,255,255))
    screen.blit(Some_text, (250, 300))
    pygame.display.update()

    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if pygame.mixer.music.get_busy() == False:
                print('music end event')
                if len(playlist) == 0:
                    addMusic(playlist)
                pygame.mixer.music.load(playlist[0])
                playlist.pop(0)
                pygame.mixer.music.play()

            if event.type == pygame.MOUSEBUTTONDOWN:
                button_SFX.play()
                return


def endWin():

    pygame.mixer.music.pause()

    EndGame2_SFX.play()
    EndGame1_SFX.play(-1)

    Win_image = pygame.image.load("Images/winBox.png")
    Win_rect = Win_image.get_rect()
    Win_rect.topleft = (0, 300)
    screen.blit(Win_image, Win_rect)

    Win_text = font.render(f" CONGRATULATIONS, YOU HAVE WON!!! ", True, (255,255,255))
    screen.blit(Win_text, (180, 335))
    pygame.display.update()

    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()



def endLose(TurnCounter):

    pygame.mixer.music.pause()

    EndGame_SFX.play()

    Sad_image = pygame.image.load("Images/unhappy.png")
    Sad_image = pygame.transform.scale(Sad_image, (Sad_image.get_width()*1.5, Sad_image.get_height()*4))
    Sad_rect = Sad_image.get_rect()
    Sad_rect.topleft = (0, 0)
    screen.blit(Sad_image, Sad_rect)

    Lose_image = pygame.image.load("Images/loseBox.png")
    Lose_rect = Lose_image.get_rect()
    Lose_rect.topleft = (0, 300)
    screen.blit(Lose_image, Lose_rect)

    Some_text = font.render(f" YOU FAILED, NOOOOOOO!!!!!! ", True, (255,255,255))
    Some_text1 = font.render(f" Taken Turns: {TurnCounter}", True, (200,0,200))
    screen.blit(Some_text, (200, 330))
    screen.blit(Some_text1, (200, 350))
    pygame.display.update()

    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()

def main_loop(Boat_image,Background_image,ButtonChicken_image,Minus_image,Minus1_image,Minus2_image,Quit_image,ButtonCannibal_image,ButtonBoat_image,Chicken_image,Chicken1_image,Chicken2_image,Cannibal_image,Cannibal1_image,Cannibal2_image):



    # Counters
    BoatCounter = 0
    TurnCounter = 1
    FChickenCounter = 3
    TChickenCounter = 0
    FCannibalCounter = 3
    TCannibalCounter = 0

    # Bool States
    isBoatFull = False
    isShoreState = False
    isFailState = False
    isWinState = False

    isChickenBoat, isChickenBoat1 = False, False
    isCannibalBoat, isCannibalBoat1 = False, False

    # Saved Positions
    posFCannibalLand = (10, 400)
    posFCannibal1Land = (40, 400)
    posFCannibal2Land = (70, 400)

    posFChickenLand = (100, 360)
    posFChicken1Land = (130, 360)
    posFChicken2Land = (160, 360)

    posFBoatChicken = (380,350)
    posFBoatChicken1 = (380,380)

    posFBoatCannibal = (400,350)
    posFBoatCannibal1 = (400,380)

    posTCannibalLand = (750, 340)
    posTCannibal1Land = (760, 340)
    posTCannibal2Land = (770, 340)

    posTChickenLand = (700, 350)
    posTChicken1Land = (710, 350)
    posTChicken2Land = (720, 350)

    posTBoatChicken = (615, 340)
    posTBoatChicken1 = (615, 350)

    posTBoatCannibal = (625,340)
    posTBoatCannibal1 = (625,350)

    while True:

        font = pygame.font.Font(None, 36)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.mixer.music.get_busy() == False:
                print('music end event')
                if len(playlist) == 0:
                    addMusic(playlist)
                pygame.mixer.music.load(playlist[0])
                playlist.pop(0)
                pygame.mixer.music.play()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("M1 Pressed")
                # CHICKENS
                if ButtonChicken_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Chicken Button Pressed")
                    button_SFX.play()
                    if isBoatFull == False and isChickenBoat == False and isShoreState == False:
                        if Chicken_rect.topleft == posFChickenLand:
                            Chicken_rect.topleft = posFBoatChicken
                            BoatCounter += 1
                            isChickenBoat = True
                            FChickenCounter -= 1
                        elif Chicken1_rect.topleft == posFChicken1Land:
                            Chicken1_rect.topleft = posFBoatChicken
                            BoatCounter += 1
                            isChickenBoat = True
                            FChickenCounter -= 1
                        elif Chicken2_rect.topleft == posFChicken2Land:
                            Chicken2_rect.topleft = posFBoatChicken
                            BoatCounter += 1
                            isChickenBoat = True
                            FChickenCounter -= 1
                        else:
                            print("you eff'd up")
                    elif isBoatFull == False and isChickenBoat1 == False and isShoreState == False:
                        if Chicken_rect.topleft == posFChickenLand:
                            Chicken_rect.topleft = posFBoatChicken1
                            BoatCounter += 1
                            isChickenBoat1 = True
                            FChickenCounter -= 1
                        elif Chicken1_rect.topleft == posFChicken1Land:
                            Chicken1_rect.topleft = posFBoatChicken1
                            BoatCounter += 1
                            isChickenBoat1 = True
                            FChickenCounter -= 1
                        elif Chicken2_rect.topleft == posFChicken2Land:
                            Chicken2_rect.topleft = posFBoatChicken1
                            BoatCounter += 1
                            isChickenBoat1 = True
                            FChickenCounter -= 1
                        else:
                            print("you eff'd up")
                    if isBoatFull == False and isChickenBoat == False and isShoreState == True:
                        if Chicken_rect.topleft == posTChickenLand:
                            Chicken_rect.topleft = posTBoatChicken
                            BoatCounter += 1
                            isChickenBoat = True
                            TChickenCounter -= 1
                        elif Chicken1_rect.topleft == posTChicken1Land:
                            Chicken1_rect.topleft = posTBoatChicken
                            BoatCounter += 1
                            isChickenBoat = True
                            TChickenCounter -= 1
                        elif Chicken2_rect.topleft == posTChicken2Land:
                            Chicken2_rect.topleft = posTBoatChicken
                            BoatCounter += 1
                            isChickenBoat = True
                            TChickenCounter -= 1
                        else:
                            print("you eff'd up")
                    elif isBoatFull == False and isChickenBoat1 == False and isShoreState == True:
                        if Chicken_rect.topleft == posTChickenLand:
                            Chicken_rect.topleft = posTBoatChicken1
                            BoatCounter += 1
                            isChickenBoat1 = True
                            TChickenCounter -= 1
                        elif Chicken1_rect.topleft == posTChicken1Land:
                            Chicken1_rect.topleft = posTBoatChicken1
                            BoatCounter += 1
                            isChickenBoat1 = True
                            TChickenCounter -= 1
                        elif Chicken2_rect.topleft == posTChicken2Land:
                            Chicken2_rect.topleft = posTBoatChicken1
                            BoatCounter += 1
                            isChickenBoat1 = True
                            TChickenCounter -= 1
                        else:
                            print("you eff'd up")
                # CANNIBALS
                if ButtonCannibal_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Cannibal Button Pressed")
                    button_SFX.play()
                    if isBoatFull == False and isCannibalBoat == False and isShoreState == False:
                        if Cannibal_rect.topleft == posFCannibalLand:
                            Cannibal_rect.topleft = posFBoatCannibal
                            BoatCounter += 1
                            isCannibalBoat = True
                            FCannibalCounter -= 1
                        elif Cannibal1_rect.topleft == posFCannibal1Land:
                            Cannibal1_rect.topleft = posFBoatCannibal
                            BoatCounter += 1
                            isCannibalBoat = True
                            FCannibalCounter -= 1
                        elif Cannibal2_rect.topleft == posFCannibal2Land:
                            Cannibal2_rect.topleft = posFBoatCannibal
                            BoatCounter += 1
                            isCannibalBoat = True
                            FCannibalCounter -= 1
                        else:
                            print("you eff'd up")
                    elif isBoatFull == False and isCannibalBoat1 == False and isShoreState == False:
                        if Cannibal_rect.topleft == posFCannibalLand:
                            Cannibal_rect.topleft = posFBoatCannibal1
                            BoatCounter += 1
                            isCannibalBoat1 = True
                            FCannibalCounter -= 1
                        elif Cannibal1_rect.topleft == posFCannibal1Land:
                            Cannibal1_rect.topleft = posFBoatCannibal1
                            BoatCounter += 1
                            isCannibalBoat1 = True
                            FCannibalCounter -= 1
                        elif Cannibal2_rect.topleft == posFCannibal2Land:
                            Cannibal2_rect.topleft = posFBoatCannibal1
                            BoatCounter += 1
                            isCannibalBoat1 = True
                            FCannibalCounter -= 1
                        else:
                            print("you eff'd up")
                    if isBoatFull == False and isCannibalBoat == False and isShoreState == True:
                        if Cannibal_rect.topleft == posTCannibalLand:
                            Cannibal_rect.topleft = posTBoatCannibal
                            BoatCounter += 1
                            isCannibalBoat = True
                            TCannibalCounter -= 1
                        elif Cannibal1_rect.topleft == posTCannibal1Land:
                            Cannibal1_rect.topleft = posTBoatCannibal
                            BoatCounter += 1
                            isCannibalBoat = True
                            TCannibalCounter -= 1
                        elif Cannibal2_rect.topleft == posTCannibal2Land:
                            Cannibal2_rect.topleft = posTBoatCannibal
                            BoatCounter += 1
                            isCannibalBoat = True
                            TCannibalCounter -= 1
                        else:
                            print("you eff'd up")
                    elif isBoatFull == False and isCannibalBoat1 == False and isShoreState == True:
                        if Cannibal_rect.topleft == posTCannibalLand:
                            Cannibal_rect.topleft = posTBoatCannibaln1
                            BoatCounter += 1
                            isCannibalBoat1 = True
                            TCannibalCounter -= 1
                        elif Cannibal1_rect.topleft == posTCannibal1Land:
                            Cannibal1_rect.topleft = posTBoatCannibal1
                            BoatCounter += 1
                            isCannibalBoat1 = True
                            TCannibalCounter -= 1
                        elif Cannibal2_rect.topleft == posTCannibal2Land:
                            Cannibal2_rect.topleft = posTBoatCannibal1
                            BoatCounter += 1
                            isCannibalBoat1 = True
                            TCannibalCounter -= 1
                        else:
                            print("you eff'd up")
                if ButtonBoat_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Boat Button Pressed")
                    button_SFX.play()
                    if FCannibalCounter > FChickenCounter and FChickenCounter != 0:
                        endLose(TurnCounter)
                    if TCannibalCounter > TChickenCounter and TChickenCounter != 0:
                        endLose(TurnCounter)

                    if TCannibalCounter == 3 and TChickenCounter == 3:
                        endWin()

                    if isShoreState == False and BoatCounter > 0:
                        isShoreState = True
                        Boat_image = pygame.transform.scale(Boat_image, (Boat_image.get_width()*0.4, Boat_image.get_height()*0.4))
                        Boat_rect.topleft = (600, 320)
                        TurnCounter += 1

                        # Chickens
                        if Chicken_rect.topleft == posFBoatChicken:
                            Chicken_image = pygame.transform.scale(Chicken_image, (Chicken_image.get_width()*0.4, Chicken_image.get_height()*0.4))
                            Chicken_rect.topleft = posTBoatChicken
                        elif Chicken_rect.topleft == posFBoatChicken1:
                            Chicken_image = pygame.transform.scale(Chicken_image, (Chicken_image.get_width()*0.4, Chicken_image.get_height()*0.4))
                            Chicken_rect.topleft = posTBoatChicken1
                        if Chicken1_rect.topleft == posFBoatChicken:
                            Chicken1_image = pygame.transform.scale(Chicken1_image, (Chicken1_image.get_width()*0.4, Chicken1_image.get_height()*0.4))
                            Chicken1_rect.topleft = posTBoatChicken
                        elif Chicken1_rect.topleft == posFBoatChicken1:
                            Chicken1_image = pygame.transform.scale(Chicken1_image, (Chicken1_image.get_width()*0.4, Chicken1_image.get_height()*0.4))
                            Chicken1_rect.topleft = posTBoatChicken1
                        if Chicken2_rect.topleft == posFBoatChicken:
                            Chicken2_image = pygame.transform.scale(Chicken2_image, (Chicken2_image.get_width()*0.4, Chicken2_image.get_height()*0.4))
                            Chicken2_rect.topleft = posTBoatChicken
                        elif Chicken2_rect.topleft == posFBoatChicken1:
                            Chicken2_image = pygame.transform.scale(Chicken2_image, (Chicken2_image.get_width()*0.4, Chicken2_image.get_height()*0.4))
                            Chicken2_rect.topleft = posTBoatChicken1
                        # Cannibals
                        if Cannibal_rect.topleft == posFBoatCannibal:
                            Cannibal_image = pygame.transform.scale(Cannibal_image, (Cannibal_image.get_width()*0.4, Cannibal_image.get_height()*0.4))
                            Cannibal_rect.topleft = posTBoatCannibal
                        elif Cannibal_rect.topleft == posFBoatCannibal1:
                            Cannibal_image = pygame.transform.scale(Cannibal_image, (Cannibal_image.get_width()*0.4, Cannibal_image.get_height()*0.4))
                            Cannibal_rect.topleft = posTBoatCannibal1
                        if Cannibal1_rect.topleft == posFBoatCannibal:
                            Cannibal1_image = pygame.transform.scale(Cannibal1_image, (Cannibal1_image.get_width()*0.4, Cannibal1_image.get_height()*0.4))
                            Cannibal1_rect.topleft = posTBoatCannibal
                        elif Cannibal1_rect.topleft == posFBoatCannibal1:
                            Cannibal1_image = pygame.transform.scale(Cannibal1_image, (Cannibal1_image.get_width()*0.4, Cannibal1_image.get_height()*0.4))
                            Cannibal1_rect.topleft = posTBoatCannibal1
                        if Cannibal2_rect.topleft == posFBoatCannibal:
                            Cannibal2_image = pygame.transform.scale(Cannibal2_image, (Cannibal2_image.get_width()*0.4, Cannibal2_image.get_height()*0.4))
                            Cannibal2_rect.topleft = posTBoatCannibal
                        elif Cannibal2_rect.topleft == posFBoatCannibal1:
                            Cannibal2_image = pygame.transform.scale(Cannibal2_image, (Cannibal2_image.get_width()*0.4, Cannibal2_image.get_height()*0.4))
                            Cannibal2_rect.topleft = posTBoatCannibal1

                    elif isShoreState == True and BoatCounter > 0:
                        isShoreState = False
                        Boat_image = pygame.image.load("Images/Boat.png")
                        Boat_image = pygame.transform.scale(Boat_image, (Boat_image.get_width()*0.4, Boat_image.get_height()*0.4))
                        Boat_rect.topleft = (350,300)
                        TurnCounter += 1

                        #Chickens
                        if Chicken_rect.topleft == posTBoatChicken:
                            Chicken_image = pygame.image.load("Images/Chicken.png")
                            Chicken_image = pygame.transform.scale(Chicken_image, (Chicken_image.get_width()*0.5, Chicken_image.get_height()*0.5))
                            Chicken_rect.topleft = posFBoatChicken
                        elif Chicken_rect.topleft == posTBoatChicken1:
                            Chicken_image = pygame.image.load("Images/Chicken.png")
                            Chicken_image = pygame.transform.scale(Chicken_image, (Chicken_image.get_width()*0.5, Chicken_image.get_height()*0.5))
                            Chicken_rect.topleft = posFBoatChicken1
                        if Chicken1_rect.topleft == posTBoatChicken:
                            Chicken1_image = pygame.image.load("Images/Chicken.png")
                            Chicken1_image = pygame.transform.scale(Chicken1_image, (Chicken1_image.get_width()*0.5, Chicken1_image.get_height()*0.5))
                            Chicken1_rect.topleft = posFBoatChicken
                        elif Chicken1_rect.topleft == posTBoatChicken1:
                            Chicken1_image = pygame.image.load("Images/Chicken.png")
                            Chicken1_image = pygame.transform.scale(Chicken1_image, (Chicken1_image.get_width()*0.5, Chicken1_image.get_height()*0.5))
                            Chicken1_rect.topleft = posFBoatChicken1
                        if Chicken2_rect.topleft == posTBoatChicken:
                            Chicken2_image = pygame.image.load("Images/Chicken.png")
                            Chicken2_image = pygame.transform.scale(Chicken2_image, (Chicken2_image.get_width()*0.5, Chicken2_image.get_height()*0.5))
                            Chicken2_rect.topleft = posFBoatChicken
                        elif Chicken2_rect.topleft == posTBoatChicken1:
                            Chicken2_image = pygame.image.load("Images/Chicken.png")
                            Chicken2_image = pygame.transform.scale(Chicken2_image, (Chicken2_image.get_width()*0.5, Chicken2_image.get_height()*0.5))
                            Chicken2_rect.topleft = posFBoatChicken1
                        # Cannibals
                        if Cannibal_rect.topleft == posTBoatCannibal:
                            Cannibal_image = pygame.image.load("Images/Cannibal.png")
                            Cannibal_image = pygame.transform.scale(Cannibal_image, (Cannibal_image.get_width()*0.5, Cannibal_image.get_height()*0.5))
                            Cannibal_rect.topleft = posFBoatCannibal
                        elif Cannibal_rect.topleft == posTBoatCannibal1:
                            Cannibal_image = pygame.image.load("Images/Cannibal.png")
                            Cannibal_image = pygame.transform.scale(Cannibal_image, (Cannibal_image.get_width()*0.5, Cannibal_image.get_height()*0.5))
                            Cannibal_rect.topleft = posFBoatCannibal1
                        if Cannibal1_rect.topleft == posTBoatCannibal:
                            Cannibal1_image = pygame.image.load("Images/Cannibal.png")
                            Cannibal1_image = pygame.transform.scale(Cannibal1_image, (Cannibal1_image.get_width()*0.5, Cannibal1_image.get_height()*0.5))
                            Cannibal1_rect.topleft = posFBoatCannibal
                        elif Cannibal1_rect.topleft == posTBoatCannibal1:
                            Cannibal1_image = pygame.image.load("Images/Cannibal.png")
                            Cannibal1_image = pygame.transform.scale(Cannibal1_image, (Cannibal1_image.get_width()*0.5, Cannibal1_image.get_height()*0.5))
                            Cannibal1_rect.topleft = posFBoatCannibal1
                        if Cannibal2_rect.topleft == posTBoatCannibal:
                            Cannibal2_image = pygame.image.load("Images/Cannibal.png")
                            Cannibal2_image = pygame.transform.scale(Cannibal2_image, (Cannibal2_image.get_width()*0.5, Cannibal2_image.get_height()*0.5))
                            Cannibal2_rect.topleft = posFBoatCannibal
                        elif Cannibal2_rect.topleft == posTBoatCannibal1:
                            Cannibal2_image = pygame.image.load("Images/Cannibal.png")
                            Cannibal2_image = pygame.transform.scale(Cannibal2_image, (Cannibal2_image.get_width()*0.5, Cannibal2_image.get_height()*0.5))
                            Cannibal2_rect.topleft = posFBoatCannibal1


                if Minus_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Minus Chicken Button Pressed")
                    button_SFX.play()
                    if isShoreState == False:
                        if Chicken_rect.topleft == posFBoatChicken:
                            Chicken_rect.topleft = posFChickenLand
                            isChickenBoat = False
                            BoatCounter -= 1
                            FChickenCounter += 1
                        elif Chicken_rect.topleft == posFBoatChicken1:
                            Chicken_rect.topleft = posFChickenLand
                            isChickenBoat1 = False
                            BoatCounter -= 1
                            FChickenCounter += 1
                        elif Chicken1_rect.topleft == posFBoatChicken:
                            Chicken1_rect.topleft = posFChicken1Land
                            isChickenBoat = False
                            BoatCounter -= 1
                            FChickenCounter += 1
                        elif Chicken1_rect.topleft == posFBoatChicken1:
                            Chicken1_rect.topleft = posFChicken1Land
                            isChickenBoat1 = False
                            BoatCounter -= 1
                            FChickenCounter += 1
                        elif Chicken2_rect.topleft == posFBoatChicken:
                            Chicken2_rect.topleft = posFChicken2Land
                            isChickenBoat = False
                            BoatCounter -= 1
                            FChickenCounter += 1
                        elif Chicken2_rect.topleft == posFBoatChicken1:
                            Chicken2_rect.topleft = posFChicken2Land
                            isChickenBoat1 = False
                            BoatCounter -= 1
                            FChickenCounter += 1
                    elif isShoreState == True:
                        if Chicken_rect.topleft == posTBoatChicken:
                            Chicken_rect.topleft = posTChickenLand
                            isChickenBoat = False
                            BoatCounter -= 1
                            TChickenCounter += 1
                        elif Chicken_rect.topleft == posTBoatChicken1:
                            Chicken_rect.topleft = posTChickenLand
                            isChickenBoat1 = False
                            BoatCounter -= 1
                            TChickenCounter += 1
                        elif Chicken1_rect.topleft == posTBoatChicken:
                            Chicken1_rect.topleft = posTChicken1Land
                            isChickenBoat = False
                            BoatCounter -= 1
                            TChickenCounter += 1
                        elif Chicken1_rect.topleft == posTBoatChicken1:
                            Chicken1_rect.topleft = posTChicken1Land
                            isChickenBoat1 = False
                            BoatCounter -= 1
                            TChickenCounter += 1
                        elif Chicken2_rect.topleft == posTBoatChicken:
                            Chicken2_rect.topleft = posTChicken2Land
                            isChickenBoat = False
                            BoatCounter -= 1
                            TChickenCounter += 1
                        elif Chicken2_rect.topleft == posTBoatChicken1:
                            Chicken2_rect.topleft = posTChicken2Land
                            isChickenBoat1 = False
                            BoatCounter -= 1
                            TChickenCounter += 1
                if Minus1_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Minus Cannibal Button Pressed")
                    button_SFX.play()
                    if isShoreState == False:
                        if Cannibal_rect.topleft == posFBoatCannibal:
                            Cannibal_rect.topleft = posFCannibalLand
                            isCannibalBoat = False
                            BoatCounter -= 1
                            FCannibalCounter += 1
                        elif Cannibal_rect.topleft == posFBoatCannibal1:
                            Cannibal_rect.topleft = posFCannibalLand
                            isCannibalBoat1 = False
                            BoatCounter -= 1
                            FCannibalCounter += 1
                        elif Cannibal1_rect.topleft == posFBoatCannibal:
                            Cannibal1_rect.topleft = posFCannibal1Land
                            isCannibalBoat = False
                            BoatCounter -= 1
                            FCannibalCounter += 1
                        elif Cannibal1_rect.topleft == posFBoatCannibal1:
                            Cannibal1_rect.topleft = posFCannibal1Land
                            isCannibalBoat1 = False
                            BoatCounter -= 1
                            FCannibalCounter += 1
                        elif Cannibal2_rect.topleft == posFBoatCannibal:
                            Cannibal2_rect.topleft = posFCannibal2Land
                            isCannibalBoat = False
                            BoatCounter -= 1
                            FCannibalCounter += 1
                        elif Cannibal2_rect.topleft == posFBoatCannibal1:
                            Cannibal2_rect.topleft = posFCannibal2Land
                            isCannibalBoat1 = False
                            BoatCounter -= 1
                            FCannibalCounter += 1
                    elif isShoreState == True:
                        if Cannibal_rect.topleft == posTBoatCannibal:
                            Cannibal_rect.topleft = posTCannibalLand
                            isCannibalBoat = False
                            BoatCounter -= 1
                            TCannibalCounter += 1
                        elif Cannibal_rect.topleft == posTBoatCannibal1:
                            Cannibal_rect.topleft = posTCannibalLand
                            isCannibalBoat1 = False
                            BoatCounter -= 1
                            TCannibalCounter += 1
                        elif Cannibal1_rect.topleft == posTBoatCannibal:
                            Cannibal1_rect.topleft = posTCannibal1Land
                            isCannibalBoat = False
                            BoatCounter -= 1
                            TCannibalCounter += 1
                        elif Cannibal1_rect.topleft == posTBoatCannibal1:
                            Cannibal1_rect.topleft = posTCannibal1Land
                            isCannibalBoat1 = False
                            BoatCounter -= 1
                            TCannibalCounter += 1
                        elif Cannibal2_rect.topleft == posTBoatCannibal:
                            Cannibal2_rect.topleft = posTCannibal2Land
                            isCannibalBoat = False
                            BoatCounter -= 1
                            TCannibalCounter += 1
                        elif Cannibal2_rect.topleft == posTBoatCannibal1:
                            Cannibal2_rect.topleft = posTCannibal2Land
                            isCannibalBoat1 = False
                            BoatCounter -= 1
                            TCannibalCounter += 1

                if Minus2_rect.collidepoint(pygame.mouse.get_pos()):
                    button_SFX.play()
                    print("isBoatFull", isBoatFull)
                    print("isCannibalBoat", isCannibalBoat)
                    print("isCannibalBoat1", isCannibalBoat1)
                    print("isChickenBoat", isChickenBoat)
                    print("isChickenBoat1", isChickenBoat1)
                    print("BoatCounter", BoatCounter)
                    print("TurnCounter", TurnCounter)
                    print("Cannibal", Cannibal_rect.topleft)
                    print("Cannibal1", Cannibal1_rect.topleft)
                    print("Cannibal2", Cannibal2_rect.topleft)
                    print("Chicken", Chicken_rect.topleft)
                    print("Chicken1", Chicken1_rect.topleft)
                    print("Chicken2", Chicken2_rect.topleft)
                    print("FChickenCounter", FChickenCounter)
                    print("TChickenCounter", TChickenCounter)
                    print("FCannibalCounter", FCannibalCounter)
                    print("TCannibalCounter", TCannibalCounter)

                if Quit_rect.collidepoint(pygame.mouse.get_pos()):
                    button_SFX.play()
                    pygame.quit()
                    sys.exit()

        # Clear the screen
        screen.fill((50, 50, 50))

        # Draw the character
        screen.blit(Background_image, Background_rect)
        screen.blit(ButtonChicken_image, ButtonChicken_rect)
        screen.blit(Minus_image, Minus_rect)
        screen.blit(Minus1_image, Minus1_rect)
        screen.blit(Minus2_image, Minus2_rect)
        screen.blit(Quit_image, Quit_rect)
        screen.blit(ButtonCannibal_image, ButtonCannibal_rect)
        screen.blit(ButtonBoat_image, ButtonBoat_rect)
        screen.blit(Boat_image, Boat_rect)
        screen.blit(Chicken_image, Chicken_rect)
        screen.blit(Chicken1_image, Chicken1_rect)
        screen.blit(Chicken2_image, Chicken2_rect)
        screen.blit(Cannibal_image, Cannibal_rect)
        screen.blit(Cannibal1_image, Cannibal1_rect)
        screen.blit(Cannibal2_image, Cannibal2_rect)

        #DEBUG
        #print("isBoatFull", isBoatFull)
        #print("isCannibalBoat", isCannibalBoat)
        #print("isCannibalBoat", isCannibalBoat1)
        #print("isChickenBoat", isChickenBoat)
        #print("isChickenBoat1", isChickenBoat1)
        #print("BoatCounter", BoatCounter)









        score_text = font.render(f"Turns: {TurnCounter}", True, (255,255,255))
        screen.blit(score_text, (500, 500))
        Quit_text = font.render(f" Quit ", True, (255,255,255))
        screen.blit(Quit_text, (565, 560))

        if BoatCounter == 2:
            isBoatFull = True
        if BoatCounter < 2:
            isBoatFull = False

        if TCannibalCounter == 3 and TChickenCounter == 3:
            endWin()

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        pygame.time.Clock().tick(30)


if __name__ == "__main__":
    start()
    main_loop(Boat_image,
        Background_image,
        ButtonChicken_image,
        Minus_image,
        Minus1_image,
        Minus2_image,
        Quit_image,
        ButtonCannibal_image,
        ButtonBoat_image,
        Chicken_image,
        Chicken1_image,
        Chicken2_image,
        Cannibal_image,
        Cannibal1_image,
        Cannibal2_image)
