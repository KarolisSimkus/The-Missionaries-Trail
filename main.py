import sys
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

# Counters
BoatCounter = 0
TurnCounter = 0

# Bool States
isBoatFull = False
isShoreState = False
isFailState = False

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

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("M1 Pressed")
            # CHICKENS
            if ButtonChicken_rect.collidepoint(pygame.mouse.get_pos()):
                print("Chicken Button Pressed")
                if isBoatFull == False and isChickenBoat == False and isShoreState == False:
                    if Chicken_rect.topleft == posFChickenLand:
                        Chicken_rect.topleft = posFBoatChicken
                        BoatCounter += 1
                        isChickenBoat = True
                    elif Chicken1_rect.topleft == posFChicken1Land:
                        Chicken1_rect.topleft = posFBoatChicken
                        BoatCounter += 1
                        isChickenBoat = True
                    elif Chicken2_rect.topleft == posFChicken2Land:
                        Chicken2_rect.topleft = posFBoatChicken
                        BoatCounter += 1
                        isChickenBoat = True
                    else:
                        print("you eff'd up")
                elif isBoatFull == False and isChickenBoat1 == False and isShoreState == False:
                    if Chicken_rect.topleft == posFChickenLand:
                        Chicken_rect.topleft = posFBoatChicken1
                        BoatCounter += 1
                        isChickenBoat1 = True
                    elif Chicken1_rect.topleft == posFChicken1Land:
                        Chicken1_rect.topleft = posFBoatChicken1
                        BoatCounter += 1
                        isChickenBoat1 = True
                    elif Chicken2_rect.topleft == posFChicken2Land:
                        Chicken2_rect.topleft = posFBoatChicken1
                        BoatCounter += 1
                        isChickenBoat1 = True
                    else:
                        print("you eff'd up")
                if isBoatFull == False and isChickenBoat == False and isShoreState == True:
                    if Chicken_rect.topleft == posTChickenLand:
                        Chicken_rect.topleft = posTBoatChicken
                        BoatCounter += 1
                        isChickenBoat = True
                    elif Chicken1_rect.topleft == posTChicken1Land:
                        Chicken1_rect.topleft = posTBoatChicken
                        BoatCounter += 1
                        isChickenBoat = True
                    elif Chicken2_rect.topleft == posTChicken2Land:
                        Chicken2_rect.topleft = posTBoatChicken
                        BoatCounter += 1
                        isChickenBoat = True
                    else:
                        print("you eff'd up")
                elif isBoatFull == False and isChickenBoat1 == False and isShoreState == True:
                    if Chicken_rect.topleft == posTChickenLand:
                        Chicken_rect.topleft = posTBoatChicken1
                        BoatCounter += 1
                        isChickenBoat1 = True
                    elif Chicken1_rect.topleft == posTChicken1Land:
                        Chicken1_rect.topleft = posTBoatChicken1
                        BoatCounter += 1
                        isChickenBoat1 = True
                    elif Chicken2_rect.topleft == posTChicken2Land:
                        Chicken2_rect.topleft = posTBoatChicken1
                        BoatCounter += 1
                        isChickenBoat1 = True
                    else:
                        print("you eff'd up")
            # CANNIBALS
            if ButtonCannibal_rect.collidepoint(pygame.mouse.get_pos()):
                print("Cannibal Button Pressed")
                if isBoatFull == False and isCannibalBoat == False and isShoreState == False:
                    if Cannibal_rect.topleft == posFCannibalLand:
                        Cannibal_rect.topleft = posFBoatCannibal
                        BoatCounter += 1
                        isCannibalBoat = True
                    elif Cannibal1_rect.topleft == posFCannibal1Land:
                        Cannibal1_rect.topleft = posFBoatCannibal
                        BoatCounter += 1
                        isCannibalBoat = True
                    elif Cannibal2_rect.topleft == posFCannibal2Land:
                        Cannibal2_rect.topleft = posFBoatCannibal
                        BoatCounter += 1
                        isCannibalBoat = True
                    else:
                        print("you eff'd up")
                elif isBoatFull == False and isCannibalBoat1 == False and isShoreState == False:
                    if Cannibal_rect.topleft == posFCannibalLand:
                        Cannibal_rect.topleft = posFBoatCannibaln1
                        BoatCounter += 1
                        isCannibalBoat1 = True
                    elif Cannibal1_rect.topleft == posFCannibal1Land:
                        Cannibal1_rect.topleft = posFBoatCannibal1
                        BoatCounter += 1
                        isCannibalBoat1 = True
                    elif Cannibal2_rect.topleft == posFCannibal2Land:
                        Cannibal2_rect.topleft = posFBoatCannibal1
                        BoatCounter += 1
                        isCannibalBoat1 = True
                    else:
                        print("you eff'd up")
                if isBoatFull == False and isCannibalBoat == False and isShoreState == True:
                    if Cannibal_rect.topleft == posTCannibalLand:
                        Cannibal_rect.topleft = posTBoatCannibal
                        BoatCounter += 1
                        isCannibalBoat = True
                    elif Cannibal1_rect.topleft == posTCannibal1Land:
                        Cannibal1_rect.topleft = posTBoatCannibal
                        BoatCounter += 1
                        isCannibalBoat = True
                    elif Cannibal2_rect.topleft == posTCannibal2Land:
                        Cannibal2_rect.topleft = posTBoatCannibal
                        BoatCounter += 1
                        isCannibalBoat = True
                    else:
                        print("you eff'd up")
                elif isBoatFull == False and isCannibalBoat1 == False and isShoreState == True:
                    if Cannibal_rect.topleft == posTCannibalLand:
                        Cannibal_rect.topleft = posTBoatCannibaln1
                        BoatCounter += 1
                        isCannibalBoat1 = True
                    elif Cannibal1_rect.topleft == posTCannibal1Land:
                        Cannibal1_rect.topleft = posTBoatCannibal1
                        BoatCounter += 1
                        isCannibalBoat1 = True
                    elif Cannibal2_rect.topleft == posTCannibal2Land:
                        Cannibal2_rect.topleft = posTBoatCannibal1
                        BoatCounter += 1
                        isCannibalBoat1 = True
                    else:
                        print("you eff'd up")
            if ButtonBoat_rect.collidepoint(pygame.mouse.get_pos()):
                print("Boat Button Pressed")
                if isShoreState == False:
                    isShoreState = True
                    Boat_image = pygame.transform.scale(Boat_image, (Boat_image.get_width()*0.4, Boat_image.get_height()*0.4))
                    Boat_rect.topleft = (600, 320)
                    BoatCounter += 1

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

                elif isShoreState == True:
                    isShoreState = False
                    Boat_image = pygame.image.load("Images/Boat.png")
                    Boat_image = pygame.transform.scale(Boat_image, (Boat_image.get_width()*0.4, Boat_image.get_height()*0.4))
                    Boat_rect.topleft = (350,300)

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
                    if Chicken1_rect.topleft == posTBoatCannibal:
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
                if isShoreState == False:
                    if Chicken_rect.topleft == posFBoatChicken:
                        Chicken_rect.topleft = posFChickenLand
                        isChickenBoat = False
                        BoatCounter -= 1
                    elif Chicken_rect.topleft == posFBoatChicken1:
                        Chicken_rect.topleft = posFChickenLand
                        isChickenBoat1 = False
                        BoatCounter -= 1
                    elif Chicken1_rect.topleft == posFBoatChicken:
                        Chicken1_rect.topleft = posFChicken1Land
                        isChickenBoat = False
                        BoatCounter -= 1
                    elif Chicken1_rect.topleft == posFBoatChicken1:
                        Chicken1_rect.topleft = posFChicken1Land
                        isChickenBoat1 = False
                        BoatCounter -= 1
                    elif Chicken2_rect.topleft == posFBoatChicken:
                        Chicken2_rect.topleft = posFChicken2Land
                        isChickenBoat = False
                        BoatCounter -= 1
                    elif Chicken2_rect.topleft == posFBoatChicken1:
                        Chicken2_rect.topleft = posFChicken2Land
                        isChickenBoat1 = False
                        BoatCounter -= 1
                elif isShoreState == True:
                    if Chicken_rect.topleft == posTBoatChicken:
                        Chicken_rect.topleft = posTChickenLand
                        isChickenBoat = False
                        BoatCounter -= 1
                    elif Chicken_rect.topleft == posTBoatChicken1:
                        Chicken_rect.topleft = posTChickenLand
                        isChickenBoat1 = False
                        BoatCounter -= 1
                    elif Chicken1_rect.topleft == posTBoatChicken:
                        Chicken1_rect.topleft = posTChicken1Land
                        isChickenBoat = False
                        BoatCounter -= 1
                    elif Chicken1_rect.topleft == posTBoatChicken1:
                        Chicken1_rect.topleft = posTChicken1Land
                        isChickenBoat1 = False
                        BoatCounter -= 1
                    elif Chicken2_rect.topleft == posTBoatChicken:
                        Chicken2_rect.topleft = posTChicken2Land
                        isChickenBoat = False
                        BoatCounter -= 1
                    elif Chicken2_rect.topleft == posTBoatChicken1:
                        Chicken2_rect.topleft = posTChicken2Land
                        isChickenBoat1 = False
                        BoatCounter -= 1
            if Minus1_rect.collidepoint(pygame.mouse.get_pos()):
                print("Minus Cannibal Button Pressed")
                if isShoreState == False:
                    if Cannibal_rect.topleft == posFBoatCannibal:
                        Cannibal_rect.topleft = posFCannibalLand
                        isCannibalBoat = False
                        BoatCounter -= 1
                    elif Cannibal_rect.topleft == posFBoatCannibal1:
                        Cannibal_rect.topleft = posFCannibalLand
                        isCannibalBoat1 = False
                        BoatCounter -= 1
                    elif Cannibal1_rect.topleft == posFBoatCannibal:
                        Cannibal1_rect.topleft = posFCannibal1Land
                        isCannibalBoat = False
                        BoatCounter -= 1
                    elif Cannibal1_rect.topleft == posFBoatCannibal1:
                        Cannibal1_rect.topleft = posFCannibal1Land
                        isCannibalBoat1 = False
                        BoatCounter -= 1
                    elif Cannibal2_rect.topleft == posFBoatCannibal:
                        Cannibal2_rect.topleft = posFCannibal2Land
                        isCannibalBoat = False
                        BoatCounter -= 1
                    elif Cannibal2_rect.topleft == posFBoatCannibal1:
                        Cannibal2_rect.topleft = posFCannibal2Land
                        isCannibalBoat1 = False
                        BoatCounter -= 1
                elif isShoreState == True:
                    if Cannibal_rect.topleft == posTBoatCannibal:
                        Cannibal_rect.topleft = posTCannibalLand
                        isCannibalBoat = False
                        BoatCounter -= 1
                    elif Cannibal_rect.topleft == posTBoatCannibal1:
                        Cannibal_rect.topleft = posTCannibalLand
                        isCannibalBoat1 = False
                        BoatCounter -= 1
                    elif Cannibal1_rect.topleft == posTBoatCannibal:
                        Cannibal1_rect.topleft = posTCannibal1Land
                        isCannibalBoat = False
                        BoatCounter -= 1
                    elif Cannibal1_rect.topleft == posTBoatCannibal1:
                        Cannibal1_rect.topleft = posTCannibal1Land
                        isCannibalBoat1 = False
                        BoatCounter -= 1
                    elif Cannibal2_rect.topleft == posTBoatCannibal:
                        Cannibal2_rect.topleft = posTCannibal2Land
                        isCannibalBoat = False
                        BoatCounter -= 1
                    elif Cannibal2_rect.topleft == posTBoatCannibal1:
                        Cannibal2_rect.topleft = posTCannibal2Land
                        isCannibalBoat1 = False
                        BoatCounter -= 1

    # Clear the screen
    screen.fill((50, 50, 50))

    # Draw the character
    screen.blit(Background_image, Background_rect)
    screen.blit(ButtonChicken_image, ButtonChicken_rect)
    screen.blit(Minus_image, Minus_rect)
    screen.blit(Minus1_image, Minus1_rect)
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


    if BoatCounter == 2:
        isBoatFull = True
    if BoatCounter < 2:
        isBoatFull = False

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(30)
