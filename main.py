import pygame
import sys

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Set up the display
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Practice Clicker Game")
clock = pygame.time.Clock()
FPS = 30

#Set Colors
CLEAR = (0,0,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
LIBLUE=(0,128,255)

#Main Variables
titlestring = 'The Clicker Game'
text_font = pygame.font.Font(None, 50)
introstring = 'Welcome to Clicker.Cafe! Enjoy.'
introstring = text_font.render(str(introstring), True, WHITE)  # rendering text as object/image
introtext_rect = introstring.get_rect(
    center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))  # gets rect of the text shape, placed centered at a location
state = 'INTRO'
promptnumber = -1
money = 0
mouseclick = 0
circlecoordinates = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
circleradius = 50
circlecolor = RED

tuttext = ['Click the circle to gain $1', 'Your money is shown here',
           'When your finger gets tired,', 'after a long days work,', 'return to town here']

tuttext_locations = [(WINDOW_WIDTH/2,WINDOW_HEIGHT-150),
                     (160,WINDOW_HEIGHT-110),
                     (WINDOW_WIDTH/2,WINDOW_HEIGHT-150),
                     (WINDOW_WIDTH/2,WINDOW_HEIGHT-150),
                     (WINDOW_WIDTH-150,WINDOW_HEIGHT-110)]

#Make Money
def make_click_money(money):
    money+=1
    return money

#Next Button
nextbuttontext = 'Next'
nexttext_font = pygame.font.Font(None, 40)
nextbuttonstring = nexttext_font.render(str(nextbuttontext), True, WHITE)  # rendering text as object/image
nextbuttontext_rect = nextbuttonstring.get_rect(
    center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50))  # gets rect of the text shape, placed centered at a location
nextbuttontext_rect.inflate_ip(nextbuttontext_rect.width*1.2,nextbuttontext_rect.height*1.2)
newtextspot = nextbuttonstring.get_rect(center = nextbuttontext_rect.center)

homepath=r'C:\Users\Kyle\Pictures\PyGame Assets'
workpath=r'C:\Users\kcwalina\Documents\PyGameLocalAssets'
path=''

#Background Images
quainttownimage = pygame.image.load(r'QuaintTownSquare.png')
forestsceneimage = pygame.image.load(r'ForestScene.png')

#Icon Images
towniconimage = pygame.image.load(r'TownIcon.png')
forestsceneiconimage = pygame.image.load(r'ForestScene.png')


# Drawing scene backgrounds
def draw_background(locationimage):
    background_image = pygame.transform.scale(locationimage, (WINDOW_HEIGHT,WINDOW_HEIGHT))
    background_rect = background_image.get_rect(center=(WINDOW_WIDTH/2,WINDOW_HEIGHT/2))
    screen.blit(background_image,background_rect)

#Drawing location icons
def draw_location_icon(locationiconimage):
    location_icon_image = pygame.transform.scale(locationiconimage,(90,90))
    screen.blit(location_icon_image,icon_rect)

def draw_intro():
    if state == 'INTRO':
        screen.blit(introstring, introtext_rect)  # blits the rendered text onto the rectangle that is at a location
        draw_next_button()

def draw_moneyicon():
    money_font = pygame.font.Font(None, 50)
    money_string = '$ '+ str(money)
    money_text = money_font.render(money_string, True, WHITE)
    moneyrect = money_text.get_rect(center=(45,570))
    screen.blit(money_text,moneyrect)

def draw_mainclicktarget(circlecolor):
    pygame.draw.circle(screen, circlecolor, circlecoordinates,circleradius)

def draw_text_box(drawntext,fontsize,textlocation):
    boxtext = drawntext
    boxtextfont = pygame.font.Font(None,fontsize)
    renderedtext = boxtextfont.render(str(boxtext),True,WHITE)
    renderedrect = renderedtext.get_rect(center=textlocation) #width/2, height/2 ie.
    renderedrect.inflate_ip(renderedrect.width,renderedrect.height)
    newrenderedrect = renderedtext.get_rect(center = renderedrect.center)
    screen.blit(renderedtext,newrenderedrect)

def draw_next_button():
    pygame.draw.rect(screen, RED, nextbuttontext_rect)
    screen.blit(nextbuttonstring, newtextspot)

### SCENES
def draw_tutorial(circlecolor):
    if state == 'TUTORIAL':
        if promptnumber < len(tuttext):
            draw_text_box(tuttext[promptnumber],35,tuttext_locations[promptnumber])
        draw_next_button()
        draw_location_icon(towniconimage)
        draw_moneyicon()
        draw_mainclicktarget(circlecolor)

def draw_practice(circlecolor):
    if state == 'PRACTICE':
        draw_background(forestsceneimage)
        draw_moneyicon()
        draw_mainclicktarget(circlecolor)
        draw_location_icon(towniconimage)

def draw_town():
    if state == 'TOWN':
        draw_background(quainttownimage)
        draw_moneyicon()
        draw_location_icon(forestsceneiconimage)

# Stage Icon Rect. May expand, idk
def set_stage_icon_rects(state):
    icon_rect = pygame.Rect((WINDOW_WIDTH-95,WINDOW_HEIGHT-95),(90,90)) #location, size
    icon_rect = pygame.draw.rect(screen,CLEAR,icon_rect)
    return icon_rect

mouse_pos = pygame.mouse.get_pos()
Donetutorial=False

# Game loop
running = True
while running:
    # Event handling
    clock.tick(FPS)
    icon_rect = set_stage_icon_rects(state) #equal to the Return value of function
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #should be the only IF, so the game will always close first. i think
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if nextbuttontext_rect.collidepoint(event.pos) and (state == 'INTRO' or state == 'TUTORIAL'):
                state = 'TUTORIAL'
                promptnumber += 1
                if promptnumber >= len(tuttext):
                    state = 'PRACTICE'
                    circlecolor = BLUE
            if (event.pos[0] - circlecoordinates[0]) ** 2 + (event.pos[1] - circlecoordinates[1]) ** 2 <= 50 ** 2 and (state == 'TUTORIAL' or state == 'PRACTICE'):
                money = make_click_money(money)
            if icon_rect.collidepoint(event.pos) and state == 'PRACTICE':
                state = 'TOWN'
            elif icon_rect.collidepoint(event.pos) and state == 'TOWN':
                state = 'PRACTICE'

    # Clear the screen
    screen.fill(BLACK) # Passively fills all blank space with white. Shouldn't do much

    draw_intro()
    draw_tutorial(circlecolor)
    draw_practice(circlecolor)
    draw_town()
    if pygame.mouse.get_pressed()[0]:
         if ((mouse_pos[0] - circlecoordinates[0]) ** 2 + (mouse_pos[1] - circlecoordinates[1]) ** 2 <= 50 ** 2) and state == 'PRACTICE':
            draw_mainclicktarget(LIBLUE)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
