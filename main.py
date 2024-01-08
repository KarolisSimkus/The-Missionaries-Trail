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

# Bool States
isBoatFull = False
isBoatBoarded = False
isShoreState = False
isFailState = False

# Saved Positions
posFCannibalLand = (10, 400)
posFCannibal1Land = (40, 400)
posFCannibal2Land = (70, 400)

posFChickenLand = (100, 360)
posFChicken1Land = (130, 360)
posFChicken2Land = (160, 360)

posFBoatChicken = (380,350)
posFBoatChicken1 = (380,380)

posFBoatCannibal = (380,350)
posFBoatCannibal1 = (380,380)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("M1 Pressed")
            if ButtonChicken_rect.collidepoint(pygame.mouse.get_pos()):
                Chicken_rect.topleft = posFBoatChicken
                Chicken1_rect.topleft = posFBoatChicken1
                print("Chicken Button Pressed")
            if ButtonCannibal_rect.collidepoint(pygame.mouse.get_pos()):
                Cannibal_rect.topleft = (410, 350)
                print("Cannibal Button Pressed")
            if ButtonBoat_rect.collidepoint(pygame.mouse.get_pos()):
                print("Boat Button Pressed")
                if isBoatBoarded == False and isShoreState == False:
                    isShoreState = True
                    Boat_image = pygame.transform.scale(Boat_image, (Boat_image.get_width()*0.4, Boat_image.get_height()*0.4))
                    Boat_rect.topleft = (600, 320)
                elif isBoatBoarded == False and isShoreState == True:
                    isShoreState = False
                    Boat_image = pygame.image.load("Images/Boat.png")
                    Boat_image = pygame.transform.scale(Boat_image, (Boat_image.get_width()*0.4, Boat_image.get_height()*0.4))
                    Boat_rect.topleft = (350,300)
            if Minus_rect.collidepoint(pygame.mouse.get_pos()):
                print("Minus Chicken Button Pressed")
                if isShoreState == False:
                    if Chicken_rect.topleft == posFBoatChicken or Chicken_rect.topleft == posFBoatChicken1:
                        Chicken_rect.topleft = posFChickenLand
                    elif Chicken1_rect.topleft == posFBoatChicken or Chicken1_rect.topleft == posFBoatChicken1:
                        Chicken1_rect.topleft = posFChicken1Land
                    elif Chicken2_rect.topleft == posFBoatChicken or Chicken2_rect.topleft == posFBoatChicken1:
                        Chicken2_rect.topleft = posFChicken2Land
            if Minus1_rect.collidepoint(pygame.mouse.get_pos()):
                print("Minus Cannibal Button Pressed")

            #nothing

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

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(30)
