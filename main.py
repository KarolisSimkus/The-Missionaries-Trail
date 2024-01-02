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

Missionary1 = pygame.image.load('Images/Chicken.png')
Missionary1 = pygame.transform.scale_by(Missionary1, 0.5)
Missionary2 = pygame.image.load('Images/Chicken.png')
Missionary2 = pygame.transform.scale_by(Missionary2, 0.5)
Missionary3 = pygame.image.load('Images/Chicken.png')
Missionary3 = pygame.transform.scale_by(Missionary3, 0.5)
Missionary4 = pygame.image.load('Images/Chicken.png')
Missionary4 = pygame.transform.scale_by(Missionary4, 0.5)

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



rect1 = pygame.Rect(0, 0, 80, 80)
rect11 = pygame.Rect(0, 0, 82, 82)
rect2 = pygame.Rect(0, 0, 80, 80)
rect22 = pygame.Rect(0, 0, 82, 82)
rect3 = pygame.Rect(0, 0, 160, 80)
rect33 = pygame.Rect(0, 0, 162, 82)

rect1.center = (80, 550)
rect11.center = (80, 550)
rect2.center = (200, 550)
rect22.center = (200, 550)
rect3.center = (500, 550)
rect33.center = (500, 550)


font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Boat', True, color2)
textRect = text.get_rect()
textRect.center = (500, 550)

clock = pygame.time.Clock()

running = True

if __name__ == "__main__":
    while running:

        screen.fill(BackgroundColor)
        screen.blit(BackgroundImage, (0, 0))

        screen.blit(Boat1, (250, 250))

        screen.blit(Missionary1, (160, 340))
        screen.blit(Missionary2, (180, 340))
        screen.blit(Missionary3, (200, 340))


        screen.blit(Cannibal1, (10, 400))
        screen.blit(Cannibal2, (30, 400))
        screen.blit(Cannibal3, (50, 400))


        pygame.draw.rect(screen, color2, rect11)
        pygame.draw.rect(screen, color, rect1)
        pygame.draw.rect(screen, color2, rect22)
        pygame.draw.rect(screen, color, rect2)
        pygame.draw.rect(screen, color2, rect33)
        pygame.draw.rect(screen, color, rect3)
        screen.blit(text, textRect)
        screen.blit(Cannibal3, (60, 516))
        screen.blit(Missionary3, (180, 516))




        # pygame.display.flip()

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button.
                    # Check if the rect collides with the mouse pos.
                    if rect1.collidepoint(pygame.mouse.get_pos()):
                        print('Cannibal clicked.')
                        # check if free 1
                        # yes then blit it
                        # no? check if free 2
                        # yes then blit
                        # no? ignore
                    if rect2.collidepoint(pygame.mouse.get_pos()):
                        print('Chicken clicked.')
                        # check if free 1
                        # yes then blit it
                        # no? check if free 2
                        # yes then blit
                        # no? ignore
                    if rect3.collidepoint(pygame.mouse.get_pos()): # Ends turn
                        print('Boat clicked.')
                    # need undo button that removes all flag states
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_paused = True
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

pygame.quit()
quit()
