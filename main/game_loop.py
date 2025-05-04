import pygame
import button_gui as gui_
import run_game
pygame.init()

game_running = True

fps = 60
fpsClock = pygame.time.Clock()

class GameLoop():

    while game_running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
        
        if run_game.on_main_menu:
            gui_.gameWindow.blit(gui_.backgroun_image_menu, (0, 0))
            for object in gui_.main_menu_buttons:
                if run_game.on_main_menu:
                    object.button_blitting()

        else:

            gui_.gameWindow.blit(gui_.background_image_game, (0,0))

            for row in run_game.pin_grid:
                for col in row:
                    col.pin_blitting()

            for row in run_game.scoring_pin_grid:
                for col in row:
                    col.pin_blitting()

            for object in run_game.selector_pins:
                object.pin_blitting()

            for object in gui_.game_buttons:
                object.button_blitting()

            if gui_.condition_include_duplicates:
                gui_.gameWindow.blit(gui_.show_condition_duplicates_included, (530, 25))
                
            if gui_.condition_include_holes:
                gui_.gameWindow.blit(gui_.show_condition_holes_included, (530, 50))

            if run_game.game_has_ended:
                x = 0
                for i in range(4):
                    x += 54
                    gui_.gameWindow.blit(run_game.the_code_visual[i], (208 + x, 30))

        pygame.display.flip()
        fpsClock.tick(fps)
        