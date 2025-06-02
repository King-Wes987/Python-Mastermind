import pygame
import game_loop
import button_gui
import run_game

if __name__ == 'main':
    pygame.init()

    game_loop.GameLoop()

    pygame.mixer.music.unload()
    pygame.display.quit()
    pygame.quit()