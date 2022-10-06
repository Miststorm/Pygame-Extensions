#This function automatically turns given rectangles into clickable buttons

#An example is shown below. It would also be fairly simple to replace the colorUp and colorDown values with your own images

def buttonLogic(button, colorUp, colorDown):
    global pushed
    
    mouse_pos = pygame.mouse.get_pos()
    rectCollider = button.collidepoint(mouse_pos)
    
    pygame.draw.rect(screen, colorUp, button)
    mouse_pressed = pygame.mouse.get_pressed()
    
        
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN and rectCollider:
            pushed = True

        if event.type == MOUSEBUTTONUP and rectCollider and pushed:
            pygame.draw.rect(screen, colorUp, button)
            return True
        
    if not rectCollider:
        pushed = False
        
        
    if rectCollider:
        if mouse_pressed[0]:
            if pushed:
                pygame.draw.rect(screen, colorDown, button)
                
#This is where the function ends and the example begins.

import pygame
pygame.init()
from pygame.locals import MOUSEBUTTONDOWN, MOUSEBUTTONUP

screenlength = 1960/2
screenheight = 1080/2
screen = pygame.display.set_mode((screenlength, screenheight))

running = True

button1 = pygame.Rect(300, 300, 300, 300)

while running:
  if buttonLogic(button1, RED, BLUE):
    print("button got pushed")
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
            
  pygame.display.flip()
