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
            if event.type == run_game.ENDSONG_END:
                run_game.end_theme_done_playing = True
        
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

            if not run_game.game_has_ended:
                gui_.check_answer.button_blitting()
                
            if run_game.condition_include_duplicates:
                gui_.gameWindow.blit(gui_.show_condition_duplicates_included, (530, 25))
                
            if run_game.condition_include_holes:
                gui_.gameWindow.blit(gui_.show_condition_holes_included, (530, 50))

            if run_game.game_has_ended:
                x = 0
                for i in range(4):
                    x += 54
                    gui_.gameWindow.blit(run_game.the_code_visual[i], (208 + x, 30))
                
                if run_game.end_theme_done_playing:
                    gui_.back_to_main_menu_button.button_blitting()

        pygame.display.flip()
        fpsClock.tick(fps)
        