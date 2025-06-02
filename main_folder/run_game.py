import pygame
import random
import sys, os
pygame.init()

on_main_menu = bool(True)
gameWindow = pygame.display.set_mode((720, 720))

condition_include_duplicates = False
condition_include_holes = False

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def image_path_alpha(image_name):
    return pygame.image.load(resource_path("res/images/pins/" + str(image_name))).convert_alpha()

black_pin = image_path_alpha("PinBlack.png")
blue_pin = image_path_alpha("PinBlue.png")
green_pin = image_path_alpha("PinGreen.png")
orange_pin = image_path_alpha("PinOrange.png")
purple_pin = image_path_alpha("PinPurple.png")
red_pin = image_path_alpha("PinRed.png")
white_pin = image_path_alpha("PinWhite.png")
yellow_pin = image_path_alpha("PinYellow.png")
hole_pin = image_path_alpha("Hole.png")

alpha_black_pin = image_path_alpha("AlphaBlackPin.png")
alpha_blue_pin = image_path_alpha("AlphaBluePin.png")
alpha_green_pin = image_path_alpha("AlphaGreenPin.png")
alpha_orange_pin = image_path_alpha("AlphaOrangePin.png")
alpha_purple_pin = image_path_alpha("AlphaPurplePin.png")
alpha_red_pin = image_path_alpha("AlphaRedPin.png")
alpha_white_pin = image_path_alpha("AlphaWhitePin.png")
alpha_yellow_pin = image_path_alpha("AlphaYellowPin.png")

red_score_pin = image_path_alpha("PinScoreRed.png")
white_score_pin = image_path_alpha("PinScoreWhite.png")
score_hole_pin = image_path_alpha("ScorePinHole.png")

#Global variables
selected_pin = hole_pin
selected_pin_alpha = hole_pin
selected_pin_colour_value = 0
the_code = [0, 0, 0, 0]
active_guessing_row = 9
cursor_look = pygame.cursors.Cursor()

the_code_visual = [0, 0, 0, 0]
game_has_ended = False
end_theme_done_playing = False
ENDSONG_END = pygame.USEREVENT + 1

correct_colour_and_place = 0
correct_colour_not_place = 0

def select_pin(pin_name, alpha_pin_name, pin_colour_value):
    global selected_pin, selected_pin_alpha, selected_pin_colour_value

    selected_pin = pin_name
    selected_pin_alpha = alpha_pin_name
    selected_pin_colour_value = pin_colour_value

def generate_the_code():
    global the_code
    
    if not condition_include_duplicates and not condition_include_holes:

        while not ((the_code[0] != the_code[1] != the_code[2] != the_code[3]) and
                   (the_code[0] != the_code[3] != the_code[1]) and
                   (the_code[0] != the_code[2])):
            for i in range(4):
                the_code[i] = random.randint(1, 8)
            #print("Choice: " + str(the_code))
            
    elif condition_include_duplicates and not condition_include_holes:

        for i in range(4):
            the_code[i] = random.randint(1, 8)
        #print("Choice: " + str(the_code))

    elif not condition_include_duplicates and condition_include_holes:

        while not ((the_code[0] != the_code[1] != the_code[2] != the_code[3]) and
                   (the_code[0] != the_code[3] != the_code[1]) and
                   (the_code[0] != the_code[2])):
            for i in range(4):
                the_code[i] = random.randint(0, 8)
            #print("Choice: " + str(the_code))
                
    elif condition_include_duplicates and condition_include_holes:

        for i in range(4):
            the_code[i] = random.randint(0, 8)
        #print("Choice: " + str(the_code))

class RunGame():
    
    def new_game():
        global on_main_menu, selected_pin, selected_pin_alpha, selected_pin_colour_value, the_code, active_guessing_row

        selected_pin = hole_pin
        selected_pin_alpha = hole_pin
        selected_pin_colour_value = 0
        the_code = [0, 0, 0, 0]
        active_guessing_row = 9

        on_main_menu = False
        pin_creation()
        generate_the_code()

class Pins():
    def __init__(self, x, y, image, alpha_image, colour_value, colourSelectPin=False, scorePin=False):
        global the_code_visual, the_code
        self.x = x
        self.y = y
        self.image = image
        self.alpha_image = alpha_image
        self.colour_value = colour_value
        self.colourSelectPin = colourSelectPin
        self.scorePin = scorePin

        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.current_pin_image = self.image

        self.already_pressed = False

    def pin_blitting(self):
        global selected_pin, selected_pin_alpha, cursor_look

        for i in range(4):
            if the_code[i] == self.colour_value:
                the_code_visual[i] = self.image

        if (((not self.colourSelectPin and active_guessing_row == self.alpha_image) or
            (self.colourSelectPin)) and not self.scorePin):

            mousePos = pygame.mouse.get_pos()
            self.current_pin_image = self.image

            if self.buttonRect.collidepoint(mousePos):

                mouse_hovers(self)

                if pygame.mouse.get_pressed(num_buttons=3)[0]:

                    if not self.already_pressed:
                        mouse_left_clicks_on_pin(self)
                    else:
                        self.already_pressed = True

                if pygame.mouse.get_pressed(num_buttons=3)[2]:

                    if not self.already_pressed:
                        mouse_right_clicks_on_pin(self)
                    else:
                        self.already_pressed = True
        
        if self.scorePin:
            self.current_pin_image = self.image

        gameWindow.blit(self.current_pin_image, self.buttonRect)    

def mouse_hovers(self):
    if self.colourSelectPin:
                pygame.cursors.Cursor()
    if not self.colourSelectPin and self.image == hole_pin:
        self.current_pin_image = selected_pin_alpha

def mouse_left_clicks_on_pin(self):
    global selected_pin

    if self.colourSelectPin:

        select_pin(self.image, self.alpha_image, self.colour_value)
        cursor_look = pygame.cursors.Cursor((15, 15), self.image)
        pygame.mouse.set_cursor(cursor_look)
                        
    elif not self.colourSelectPin:

        if selected_pin != hole_pin:
            self.image = selected_pin
            self.colour_value = selected_pin_colour_value

        select_pin(hole_pin, hole_pin, 0)
        pygame.mouse.set_cursor(pygame.cursors.Cursor())

def mouse_right_clicks_on_pin(self):
    if not self.colourSelectPin:

        self.image = hole_pin
        self.colour_value = 0

#Pins

scoring_pin_grid = [[40, 39], [38, 37], [36, 35], [34, 33], [32, 31], [30, 29],
                    [28, 27], [26, 25], [24, 23], [22, 21], [20, 19], [18, 17], 
                    [16, 15], [14, 13], [12, 11], [10, 9], [8, 7], [6, 5],
                    [4, 3], [2, 1]]

pin_grid = [[37, 38, 39, 40],
            [33, 34, 35, 36],
            [29, 30, 31, 32],
            [25, 26, 27, 28],
            [21, 22, 23, 24],
            [17, 18, 19, 20],
            [13, 14, 15, 16],
            [9, 10 , 11, 12],
            [5, 6 ,7, 8],
            [1, 2, 3, 4]]

def pin_creation():
    #Normal Pins
    
    y_coordinate = 60
    row_in_matrix = -1

    for row in range(10):

        y_coordinate += 54
        x_coordinate = 245
        row_in_matrix += 1

        for col in range(4):

            x_coordinate += 54
            pin_grid[row][col] = Pins(x_coordinate, y_coordinate, hole_pin, row_in_matrix, 0)

    #Scoring Pins
    y_coordinate = 74
    row_in_matrix = -1

    for row in range(20):

        y_coordinate += 27
        x_coordinate = 189
        row_in_matrix += 1

        for col in range(2):

            x_coordinate += 27
            scoring_pin_grid[row][col] = Pins(x_coordinate, y_coordinate, score_hole_pin, row_in_matrix, -2, False, True)

black_pin_selector = Pins(635, 167, black_pin, alpha_black_pin, 1, True)
white_pin_selector = Pins(635, 218, white_pin, alpha_white_pin, 2, True)
red_pin_selector = Pins(635, 269, red_pin, alpha_red_pin, 3, True)
orange_pin_selector = Pins(635, 320, orange_pin, alpha_orange_pin, 4, True)
yellow_pin_selector = Pins(635, 371, yellow_pin, alpha_yellow_pin, 5, True)
green_pin_selector = Pins(635, 422, green_pin, alpha_green_pin, 6, True)
blue_pin_selector = Pins(635, 473, blue_pin, alpha_blue_pin, 7, True)
purple_pin_selector = Pins(635, 524, purple_pin, alpha_purple_pin, 8, True)

selector_pins = [black_pin_selector, white_pin_selector, red_pin_selector,
                 orange_pin_selector, yellow_pin_selector, green_pin_selector,
                 blue_pin_selector, purple_pin_selector]

class CheckAndGradeAnswer:
    def check_and_grade_answer():
        global active_guessing_row, game_has_ended, correct_colour_and_place, correct_colour_not_place, on_main_menu

        if game_has_ended:
            reset_game()
            return

        hole = [-1, -1, -1, -1]
        
        hole[0] = (pin_grid[active_guessing_row][0]).colour_value
        hole[1] = (pin_grid[active_guessing_row][1]).colour_value
        hole[2] = (pin_grid[active_guessing_row][2]).colour_value
        hole[3] = (pin_grid[active_guessing_row][3]).colour_value

        if validate_user_answer(hole[0], hole[1], hole[2], hole[3]) == "Valid":

            pygame.mixer.music.load(resource_path("res/sound/Score.ogg"))
            pygame.mixer.music.play(0, 0.0, 100)

            temp_code = [-2, -2, -2, -2]

            correct_colour_and_place, correct_colour_not_place = 0, 0

            for i in range(4):
                temp_code[i] = the_code[i]
        
            for i in range(4):
                if temp_code[i] == hole[i]:
                    correct_colour_and_place += 1
                    hole[i] = -1
                    temp_code[i] = -2

            for code_value in range(4):
                for hole_value in range(4):
                    if temp_code[code_value] == hole[hole_value]:
                        correct_colour_not_place += 1
                        hole[hole_value] = -1
                        temp_code[code_value] = -2

            if active_guessing_row > 0:
                
                """print("----")
                print("Row " + str(active_guessing_row) + ": ")
                print("Red: " + str(correct_colour_and_place))
                print("White " + str(correct_colour_not_place))
                """
                score_pin_logic()

                active_guessing_row -= 1

            elif active_guessing_row == 0:

                score_pin_logic()
                if not game_has_ended:
                    game_is_lost()

            else:
                game_is_lost()

        else:
            pygame.mixer.music.load(resource_path("res/sound/Warning.ogg"))
            pygame.mixer.music.play(0, 0.0, 100)

def validate_user_answer(hole_zero, hole_one, hole_two, hole_three):
    hole_test = [hole_zero, hole_one, hole_two, hole_three]

    if not condition_include_duplicates and not condition_include_holes:

        if ((hole_test[0] != hole_test[1] != hole_test[2] != hole_test[3]) and
            (hole_test[0] != hole_test[3] != hole_test[1]) and
            (hole_test[0] != hole_test[2])):

            for i in range(4):
                if hole_test[i] == 0:
                    return("Invalid")
            return("Valid")
            
        else:
            return("Invalid")
            
    elif condition_include_duplicates and not condition_include_holes:

        for i in range(4):
            if hole_test[i] == 0:
                return("Invalid")
        else:
            return("Valid")

    elif not condition_include_duplicates and condition_include_holes:

        if ((hole_test[0] != hole_test[1] != hole_test[2] != hole_test[3]) and
                   (hole_test[0] != hole_test[3] != hole_test[1]) and
                   (hole_test[0] != hole_test[2])):
            return("Valid")
        else:
            return("Invalid")   
                
    elif condition_include_duplicates and condition_include_holes:

        return("Valid")

def game_is_won():
    global game_has_ended

    """Pins.pin_blitting(scoring_pin_grid[active_guessing_row * 2][0])
    Pins.pin_blitting(scoring_pin_grid[active_guessing_row * 2][1])
    Pins.pin_blitting(scoring_pin_grid[active_guessing_row * 2 + 1][0])
    Pins.pin_blitting(scoring_pin_grid[active_guessing_row * 2 + 1][1])
    """
    game_has_ended = True

    pygame.display.set_caption("Python: Mastermind - - - CONGRATULATIONS! YOU HAVE FIGURED OUT THE CODE!")

    pygame.mixer.music.load(resource_path("res/sound/Victory.ogg"))
    pygame.mixer.music.set_endevent(ENDSONG_END)
    pygame.mixer.music.play(0, 0.0, 100)
    pygame.mixer.music.set_volume(0.5)
    
    pygame.mixer.music.queue(resource_path("res/sound/Title.ogg"), "", -1)

def game_is_lost():
    global game_has_ended

    game_has_ended = True

    pygame.display.set_caption("Python: Mastermind - - - OH DEAR! YOU FAILED TO FIGURE OUT THE CODE! Better luck next time!")

    pygame.mixer.music.load(resource_path("res/sound/Defeat.ogg"))
    pygame.mixer.music.set_endevent(ENDSONG_END)
    pygame.mixer.music.play(0, 0.0, 100)
    pygame.mixer.music.set_volume(0.5)

    pygame.mixer.music.queue(resource_path("res/sound/DownbeatTitle.ogg"), "", -1)

"""Due to the complexity of scoring in Mastermind,
   I decided to manually place the pins by finding
   the score scenario and then placing the pins.
"""
def score_pin_logic():
    global correct_colour_and_place, correct_colour_not_place
    
    if correct_colour_and_place == 0:

        if correct_colour_not_place == 1:
            scoring_pin_grid[active_guessing_row * 2][0].image = white_score_pin
        elif correct_colour_not_place == 2:
            scoring_pin_grid[active_guessing_row * 2][0].image = white_score_pin
            scoring_pin_grid[active_guessing_row * 2][1].image = white_score_pin
        elif correct_colour_not_place == 3:
            scoring_pin_grid[active_guessing_row * 2][0].image = white_score_pin
            scoring_pin_grid[active_guessing_row * 2][1].image = white_score_pin
            scoring_pin_grid[active_guessing_row * 2 + 1][0].image = white_score_pin
        elif correct_colour_not_place == 4:
            scoring_pin_grid[active_guessing_row * 2][0].image = white_score_pin
            scoring_pin_grid[active_guessing_row * 2][1].image = white_score_pin
            scoring_pin_grid[active_guessing_row * 2 + 1][0].image = white_score_pin
            scoring_pin_grid[active_guessing_row * 2 + 1][1].image = white_score_pin
                
    elif correct_colour_and_place == 1:

        scoring_pin_grid[active_guessing_row * 2][0].image = red_score_pin

        if correct_colour_not_place == 1:
            scoring_pin_grid[active_guessing_row * 2][1].image = white_score_pin
        elif correct_colour_not_place == 2:
            scoring_pin_grid[active_guessing_row * 2][1].image = white_score_pin
            scoring_pin_grid[active_guessing_row * 2 + 1][0].image = white_score_pin
        elif correct_colour_not_place == 3:
            scoring_pin_grid[active_guessing_row * 2][1].image = white_score_pin
            scoring_pin_grid[active_guessing_row * 2 + 1][0].image = white_score_pin
            scoring_pin_grid[active_guessing_row * 2 + 1][1].image = white_score_pin

    elif correct_colour_and_place == 2:

        scoring_pin_grid[active_guessing_row * 2][0].image = red_score_pin
        scoring_pin_grid[active_guessing_row * 2][1].image = red_score_pin

        if correct_colour_not_place == 1:
            scoring_pin_grid[active_guessing_row * 2 + 1][0].image = white_score_pin
        elif correct_colour_not_place == 2:
            scoring_pin_grid[active_guessing_row * 2 + 1][0].image = white_score_pin
            scoring_pin_grid[active_guessing_row * 2 + 1][1].image = white_score_pin

    elif correct_colour_and_place == 3:

        scoring_pin_grid[active_guessing_row * 2][0].image = red_score_pin
        scoring_pin_grid[active_guessing_row * 2][1].image = red_score_pin
        scoring_pin_grid[active_guessing_row * 2 + 1][0].image = red_score_pin

    elif correct_colour_and_place == 4:

        scoring_pin_grid[active_guessing_row * 2][0].image = red_score_pin
        scoring_pin_grid[active_guessing_row * 2][1].image = red_score_pin
        scoring_pin_grid[active_guessing_row * 2 + 1][0].image = red_score_pin
        scoring_pin_grid[active_guessing_row * 2 + 1][1].image = red_score_pin

        game_is_won()

def reset_game():
    global on_main_menu, game_has_ended, cursor_look, end_theme_done_playing

    on_main_menu = True
    game_has_ended = False
    end_theme_done_playing = False
    cursor_look = pygame.cursors.Cursor()
    pygame.display.set_caption("Python: Mastermind")
    
    pygame.mixer.music.fadeout(500)
    pygame.mixer.music.load(resource_path("res/sound/Title.ogg"))
    pygame.mixer.music.play(-1, 0.0, 1000)
    pygame.mixer.music.set_volume(0.5)