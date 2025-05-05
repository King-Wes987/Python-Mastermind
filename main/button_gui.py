import pygame
import run_game
pygame.init()

main_menu_buttons = []
game_buttons = []

condition_include_duplicates = False
condition_include_holes = False

screen_width, screen_height = 720, 720
gameWindow = pygame.display.set_mode((screen_width, screen_height))

pygame.mixer.music.load("../Python Mastermind/res/sound/Title.ogg")
pygame.mixer.music.play(-1, 0.0, 1000)
pygame.mixer.music.set_volume(0.5)

pygame.display.set_caption("Python: Mastermind")

def image_path(image_name):
    return pygame.image.load("../Python Mastermind/res/images/" + str(image_name)).convert_alpha()

backgroun_image_menu = image_path("OpeningScreen.png")
background_image_game = image_path("MasterMindBG2.png")

plain_start_button = image_path("PlainStart.png")
hover_start_button = image_path("HoverStart.png")
plain_duplicates_button = image_path("PlainDuplicates.png")
hover_duplicates_button = image_path("HoverDuplicates.png")
selected_duplicates_button = image_path("SelectedDuplicates.png")
plain_holes_included_button = image_path("PlainHolesIncluded.png")
hover_holes_included_button = image_path("HoverHolesIncluded.png")
selected_holes_included_button = image_path("SelectedHolesIncluded.png")

plain_back_to_main_menu = image_path("PlainBackToMainMenu.png")
hover_back_to_main_menu = image_path("HoverBackToMainMenu.png")

plain_check_answer = image_path("PlainScoreAnswerButton.png")
hover_check_answer = image_path("HoverScoreAnswerButton.png")
pressed_check_answer = image_path("PressedScoreAnswerButton.png")

show_condition_duplicates_included = image_path("SelectedDuplicatesSMALL.png")
show_condition_holes_included = image_path("SelectedHolesIncludedSMALL.png")

game_won = image_path("end_screen/WON.png")
game_lost = image_path("end_screen/LOST.png")

number_one = image_path("end_screen/one.png")
number_two = image_path("end_screen/two.png")
number_three = image_path("end_screen/three.png")
number_four = image_path("end_screen/four.png")
number_five = image_path("end_screen/five.png")
number_six = image_path("end_screen/six.png")
number_seven = image_path("end_screen/seven.png")
number_eight = image_path("end_screen/eight.png")
number_nine = image_path("end_screen/nine.png")
number_ten = image_path("end_screen/ten.png")

numbers = [number_ten, number_nine, number_eight, number_seven, number_six,
           number_five, number_four, number_three, number_two, number_one]

class Button():
    def __init__(self, x, y, plain_image_name, hover_image_name, selected_image_name, onclickFunction=None, isOnMainMenu=False):
        self.x = x
        self.y = y
        self.plain_image_name = plain_image_name
        self.hover_image_name = hover_image_name
        self.selected_image_name = selected_image_name
        self.onclickFunction = onclickFunction
        self.isOnMainMenu = isOnMainMenu

        self.width, self.height = self.plain_image_name.get_width(), self.plain_image_name.get_height()
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.current_button_image = self.plain_image_name
        
        self.button_states = {
            'plain': plain_image_name,
            'hover': hover_image_name,
            'selected': selected_image_name
        }

        self.alreadyPressed = False

        if self.isOnMainMenu:
            main_menu_buttons.append(self)
        else:
            game_buttons.append(self)

    def button_blitting(self):
        
        mousePos = pygame.mouse.get_pos()
        
        self.current_button_image = self.button_states['plain']
        if self.buttonRect.collidepoint(mousePos):

            self.current_button_image = self.button_states['hover']

            if pygame.mouse.get_pressed(num_buttons=3)[0]: 
                self.current_button_image = self.button_states['selected']
                
                if not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
                    if self == start_game_button: return
            else:
                self.alreadyPressed = False

        if condition_include_duplicates and self.plain_image_name == plain_duplicates_button:
            self.current_button_image = selected_duplicates_button
        if condition_include_holes and self.plain_image_name == plain_holes_included_button:
            self.current_button_image = selected_holes_included_button

        gameWindow.blit(self.current_button_image, self.buttonRect)
            

def main_start_button():
    run_game.RunGame.new_game()
    pygame.mixer.music.fadeout(3000)
    
def include_duplicates():
    global condition_include_duplicates
    condition_include_duplicates = not condition_include_duplicates
    #print("Duplicates Toggle")

def include_holes():
    global condition_include_holes
    condition_include_holes = not condition_include_holes
    #print("Holes Toggle")

#List of created buttons:

#Main menu:
start_game_button = Button((screen_width-412)/2, screen_height/2,
                            plain_start_button, hover_start_button,
                            hover_start_button, main_start_button, True)
with_duplicates = Button((screen_width-422)/2, 500,
                          plain_duplicates_button, hover_duplicates_button,
                          selected_duplicates_button, include_duplicates, True)
with_holes = Button((screen_width-488)/2, 550,
                     plain_holes_included_button, hover_holes_included_button,
                     selected_holes_included_button, include_holes, True)

#Not on main menu (Used in the game)
check_answer = Button(152, 660, plain_check_answer,
                      hover_check_answer, pressed_check_answer,
                      run_game.CheckAndGradeAnswer.check_and_grade_answer)
back_to_main_menu_button = Button(199, 650, plain_back_to_main_menu,
                                  hover_back_to_main_menu, plain_back_to_main_menu,
                                  run_game.reset_game)