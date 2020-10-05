from maze import *
from gui_fx import *

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
DENSITY = 10
clock = pygame.time.Clock()

# gui will be our graphics manager
gui = GUI(WINDOW_WIDTH, WINDOW_HEIGHT, DENSITY)
gui.generateBackground()

while gui.state:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        gui.state = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                        # 1 is the left mouse button, 2 is middle, 3 is right.
                        if event.button == 1:
                                # `event.pos` is the mouse position.
                                if gui.whichButton(event.pos) == 0:
                                        pygame.display.flip()
                                elif gui.whichButton(event.pos) == 1:
                                        gui.state = False
        pygame.display.flip()