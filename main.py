import pygame
import spritesheet

pygame.init()
pygame.display.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BackgroundColor = (50, 50, 50)
color = (0, 0, 0)
color2 = (255, 255, 255)

BackgroundImage = pygame.image.load('Images/Sprite-0010-export.png')

Chicken1 = pygame.image.load('Images/Chicken.png')
Chicken1 = pygame.transform.scale_by(Chicken1, 0.5)
Chicken2 = pygame.image.load('Images/Chicken.png')
Chicken2 = pygame.transform.scale_by(Chicken2, 0.5)
Chicken3 = pygame.image.load('Images/Chicken.png')
Chicken3 = pygame.transform.scale_by(Chicken3, 0.5)
Chicken4 = pygame.image.load('Images/Chicken.png')
Chicken4 = pygame.transform.scale_by(Chicken4, 0.5)

Cannibal1 = pygame.image.load('Images/Cannibal.png')
Cannibal1 = pygame.transform.scale_by(Cannibal1, 0.5)
Cannibal2 = pygame.image.load('Images/Cannibal.png')
Cannibal2 = pygame.transform.scale_by(Cannibal2, 0.5)
Cannibal3 = pygame.image.load('Images/Cannibal.png')
Cannibal3 = pygame.transform.scale_by(Cannibal3, 0.5)
Cannibal4 = pygame.image.load('Images/Cannibal.png')
Cannibal4 = pygame.transform.scale_by(Cannibal4, 0.5)

Boat1 = pygame.image.load('Images/Boat2.png')
Boat1 = pygame.transform.scale_by(Boat1, 0.5)



pygame.display.set_caption("The Missionaries Trail")






BoatState = False # False means close shore, true means far shore
BoatFull = False
Boatcount = 0 # how many passengers are onboard

#Positions for Near saved
BoatFalseCannibal1PosBoat = (300, 300)
BoatFalseCannibal1PosLand = (10, 400)
BoatFalseCannibal2PosBoat = (300, 325)
BoatFalseCannibal2PosLand = (30, 400)
BoatFalseCannibal3PosBoat = (300, 350)
BoatFalseCannibal3PosLand = (50, 400)

BoatFalseChicken1PosBoat = (350, 300)
BoatFalseChicken1PosLand = (160, 340)
BoatFalseChicken2PosBoat = (350, 325)
BoatFalseChicken2PosLand = (180, 340)
BoatFalseChicken3PosBoat = (350, 350)
BoatFalseChicken3PosLand = (200, 340)

# To implement far positions
#Positions for Far saved
#BoatTrueCannibal1PosBoat = (x, y)
#BoatTrueCannibal1PosLand = (x, y)
#BoatTrueCannibal2PosBoat = (x, y)
#BoatTrueCannibal2PosLand = (x, y)
#BoatTrueCannibal3PosBoat = (x, y)
#BoatTrueCannibal3PosLand = (x, y)

#BoatTrueChicken1PosBoat = (x, y)
#BoatTrueChicken1PosLand = (x, y)
#BoatTrueChicken2PosBoat = (x, y)
#BoatTrueChicken2PosLand = (x, y)
#BoatTrueChicken3PosBoat = (x, y)
#BoatTrueChicken3PosLand = (x, y)


# b1  Near  /  b2  Far
# False == Land  /  True == Boat
b1_Cannibal1State = False
b1_Cannibal2State = False
b1_Cannibal3State = False
b1_Chicken1State = False
b1_Chicken2State = False
b1_Chicken3State = False

b2_Cannibal1State = False
b2_Cannibal2State = False
b2_Cannibal3State = False
b2_Chicken1State = False
b2_Chicken2State = False
b2_Chicken3State = False

# Make BackgroundColor (grey) on screen
screen.fill(BackgroundColor)

# Make BackgroundImage on screen
screen.blit(BackgroundImage, (0, 0))

# Boat
screen.blit(Boat1, (250, 250))

# Three Chickens
screen.blit(Chicken1, (160, 340))
screen.blit(Chicken2, (180, 340))
screen.blit(Chicken3, (200, 340))

# Three Cannibals
screen.blit(Cannibal1, (10, 400))
screen.blit(Cannibal2, (30, 400))
screen.blit(Cannibal3, (50, 400))

#Buttons

button = False  # used to negate double clicking button
font = pygame.font.Font('freesansbold.ttf', 32)

# Button for Cannibal

rect1 = pygame.Rect(0, 0, 80, 80)
rect11 = pygame.Rect(0, 0, 82, 82)

rect1.center = (80, 550)
rect11.center = (80, 550)

pygame.draw.rect(screen, color2, rect11)  # White outline
pygame.draw.rect(screen, color, rect1)  # Black Box
screen.blit(Cannibal4, (60, 516))  # Cannibal Image

# Button for Chicken

rect2 = pygame.Rect(0, 0, 80, 80)
rect22 = pygame.Rect(0, 0, 82, 82)

rect2.center = (200, 550)
rect22.center = (200, 550)

pygame.draw.rect(screen, color2, rect22)
pygame.draw.rect(screen, color, rect2)
screen.blit(Chicken4, (180, 516))

# Button for Boat

rect3 = pygame.Rect(0, 0, 160, 80)
rect33 = pygame.Rect(0, 0, 162, 82)

rect3.center = (500, 550)
rect33.center = (500, 550)

textBoat = font.render('Boat', True, color2)
textRect = textBoat.get_rect()
textRect.center = (500, 550)

pygame.draw.rect(screen, color2, rect33)
pygame.draw.rect(screen, color, rect3)
screen.blit(textBoat, textRect)

# Button for put back down











clock = pygame.time.Clock()

running = True



if __name__ == "__main__":
    while running:

        # More than 2 on board the Boat
        if Boatcount > 2:
            pygame.quit()
            quit()

        if Boatcount == 2:
            BoatState = True



        # event handler
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button.

                    if Boatcount == 2:
                        BoatFull = True

                    # Check if the rect collides with the mouse pos.
                    if rect1.collidepoint(pygame.mouse.get_pos()):

                        button = True  # so only once it is clicked
                        print('Cannibal clicked.')

                        # Check for boat state / Near or Far?

                        # False for Near
                        if BoatState == False and button == True:

                            button = False

                            # check if shore has cannibals
                            if (b1_Cannibal1State == False or
                                b1_Cannibal2State == False or
                                b1_Cannibal3State == False):

                                    # check if boat isnt full
                                    if BoatFull == False:

                                        # check which cannibal wants to get on the boat
                                        # Cannibal 1
                                        if b1_Cannibal1State == False:
                                            print('Cannibal 1 on Boat From Near.')
                                            b1_Cannibal1State = True
                                            Boatcount += 1
                                            screen.blit(Cannibal1, BoatFalseCannibal1PosBoat)
                                        # Cannibal 2
                                        elif b1_Cannibal2State == False:
                                            print('Cannibal 2 on Boat From Near.')
                                            b1_Cannibal2State = True
                                            Boatcount += 1
                                            screen.blit(Cannibal2, BoatFalseCannibal2PosBoat)
                                        # Cannibal 3
                                        elif b1_Cannibal3State == False:
                                            print('Cannibal 3 on Boat From Near.')
                                            b1_Cannibal3State = True
                                            Boatcount += 1
                                            screen.blit(Cannibal3, BoatFalseCannibal3PosBoat)

                        # True for Far
                        if BoatState == True and button == True:

                            button = False

                            # check if shore has cannibals
                            if (b2_Cannibal1State == False or
                                b2_Cannibal2State == False or
                                b2_Cannibal3State == False):

                                    # check if boat isnt full
                                    if BoatFull == False:

                                        # check which cannibal wants to get on the boat
                                        # Cannibal 1
                                        if b2_Cannibal1State == False:
                                            print('Cannibal 1 on Boat From Far.')
                                            b1_Cannibal1State = True
                                            Boatcount += 1
                                            # screen.blit(Cannibal1, BoatFalseCannibal1PosBoat)
                                        # Cannibal 2
                                        elif b2_Cannibal2State == False:
                                            print('Cannibal 2 on Boat From Fa.')
                                            b1_Cannibal2State = True
                                            Boatcount += 1
                                            # screen.blit(Cannibal2, BoatFalseCannibal2PosBoat)
                                        # Cannibal 3
                                        elif b2_Cannibal3State == False:
                                            print('Cannibal 3 on Boat From Fa.')
                                            b1_Cannibal3State = True
                                            Boatcount += 1
                                            # screen.blit(Cannibal3, BoatFalseCannibal3PosBoat)
                        # Change button
                        button = False

                    if rect2.collidepoint(pygame.mouse.get_pos()):

                        print('Chicken clicked.')
                        button = True  # so only once it is clicked

                        # Check for boat state / Near or Far?

                        # False for Near
                        if BoatState == False and button == True:

                            button = False

                            # check if shore has Chickens
                            if (b1_Chicken1State == False or
                                b1_Chicken2State == False or
                                b1_Chicken3State == False):

                                    # check if boat isnt full
                                    if BoatFull == False:

                                        # check which Chicken wants to get on the boat
                                        # Chicken 1
                                        if b1_Chicken1State == False:
                                            print('Chicken 1 on Boat From Near.')
                                            b1_Chicken1State = True
                                            Boatcount += 1
                                            screen.blit(Chicken1, BoatFalseChicken1PosBoat)
                                        # Chicken 2
                                        elif b1_Chicken2State == False:
                                            print('Chicken 2 on Boat From Near.')
                                            b1_Chicken2State = True
                                            Boatcount += 1
                                            screen.blit(Chicken2, BoatFalseChicken2PosBoat)
                                        # Chicken 3
                                        elif b1_Chicken3State == False:
                                            print('Chicken 3 on Boat From Near.')
                                            b1_Chicken3State = True
                                            Boatcount += 1
                                            screen.blit(Chicken3, BoatFalseChicken3PosBoat)

                        # True for Far
                        if BoatState == True and button == True:

                            button = False

                            # check if shore has cannibals
                            if (b2_Chicken1State == False or
                                b2_Chicken2State == False or
                                b2_Chicken3State == False):

                                    # check if boat isnt full
                                    if BoatFull == False:

                                        # check which Chicken wants to get on the boat
                                        # Chicken 1
                                        if b2_Chicken1State == False:
                                            print('Chicken 1 on Boat From Far.')
                                            b1_Chicken1State = True
                                            Boatcount += 1
                                            # screen.blit(Chicken1, BoatFalseChicken1PosBoat)
                                        # Chicken 2
                                        elif b2_Chicken2State == False:
                                            print('Chicken 2 on Boat From Fa.')
                                            b1_Chicken2State = True
                                            Boatcount += 1
                                            # screen.blit(Chicken2, BoatFalseCannibal2PosBoat)
                                        # Chicken 3
                                        elif b2_Chicken3State == False:
                                            print('Chicken 3 on Boat From Fa.')
                                            b1_Chicken3State = True
                                            # screen.blit(Chicken3, BoatFalseCannibal3PosBoat)
                                            Boatcount += 1


                    if rect3.collidepoint(pygame.mouse.get_pos()): # Boat
                        print('Boat clicked.')
                    # need remove button for both
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_paused = True
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

pygame.quit()
quit()
