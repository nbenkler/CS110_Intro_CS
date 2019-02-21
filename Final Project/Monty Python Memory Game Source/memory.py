#   Name:  Noam Benkler
#   Date:  March 14, 2018
#   File: memory.py
#   Description: This is the memory.py code which is holds the 'main' function
#      that calls upon the gameBoard and gameMusic classes to run the Monty Python
#      based memory card game in which players try to find matching pairs of cards.

import pygame, sys, os
from pygame.locals import *
from gameBoard import *
from gameMusic import *

TITLE_CAPTION = "Nobody Expects the Spanish Inquisition!"
WINDOW_WIDTH = 1280 
WINDOW_HEIGHT = 680 
NUM_PICS = 18 
NUM_PAIRS = 9 

def main():
    inGame = False
    numGuesses = 0
    numPairs = 0
    SELECTION_ONE = -1
    SELECTION_TWO = -1
    clock = pygame.time
    game_Board = GameBoard()
    game_Music = Music("intro.wav","inGame.ogg","card.ogg",
        "pair.ogg","win.ogg","gameOver.ogg","noPair.ogg","helpMusic.ogg")

    os.environ["SDL_VIDEO_CENTERED"] = '1' 
    game_Board.InitializeScreenSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    game_Board.SetGameTitle(TITLE_CAPTION)
    game_Board.InitializeGameData(NUM_PICS)
    game_Board.RandomizeGamePieces()

    game_Music.PlayIntro()

    while(not inGame):
        inGame = game_Board.DisplayStartScreen()
        clock.wait(70)

    game_Music.StopIntro()

    while(inGame):
        game_Board.DisplayIngameBackground(numGuesses, numPairs)
        game_Music.PlayInGame()

        if(numPairs < NUM_PAIRS):

            if(game_Board.NumPairs() < 1):
                game_Board.DisplayGameBoard()

            elif(game_Board.NumPairs() > 0):
                game_Board.DisplayGameBoard()
                pygame.display.update()

                if((SELECTION_ONE > -1) and (SELECTION_TWO > -1)):
                    clock.wait(1500)

                    for event in pygame.event.get():
                        if(event.type == MOUSEBUTTONUP):
                            continue

                    if(game_Board.IsPair(SELECTION_ONE, SELECTION_TWO)):
                        numPairs += 1
                        game_Music.PlayPairSoundFX()

                    else:
                        game_Music.PlayNoPairSoundFX()
                        game_Board.RemoveSelection()
                        game_Board.RemoveSelection()
                    SELECTION_ONE = -1
                    SELECTION_TWO = -1

            for event in pygame.event.get():
                if((event.type == QUIT) or (event.type == KEYUP and event.key == K_ESCAPE)):
                    print("EXITING..")
                    inGame = False

                if(event.type == MOUSEMOTION):
                    mouseX, mouseY = event.pos

                elif(event.type == MOUSEBUTTONUP):
                    mouseX, mouseY = event.pos

                    if(game_Board.GetSelection(mouseX, mouseY) == "help"):
                        game_Music.PauseInGame()
                        game_Music.PlayHelp()
                        inGame = game_Board.DisplayHelp()
                        game_Music.StopHelp()
                        game_Music.ResumeInGame()

                    elif((numGuesses % 2) == 0):
                        SELECTION_ONE = game_Board.GetSelection(mouseX, mouseY)
                        if(SELECTION_ONE > -1):
                            game_Music.PlayCardSoundFX()
                            game_Board.AppendSelection(SELECTION_ONE)
                            numGuesses += 1
                    else:
                        SELECTION_TWO = game_Board.GetSelection(mouseX, mouseY)
                        if(SELECTION_TWO > -1):
                            game_Music.PlayCardSoundFX()
                            game_Board.AppendSelection(SELECTION_TWO)
                            numGuesses += 1

        else:
            game_Board.DisplayGameBoard()
            pygame.display.update()
            clock.wait(2500)
            game_Music.StopInGame()
            game_Music.PlayWinSoundFX()
            game_Music.PlayGameOver()
            inGame = game_Board.GameOver(numGuesses)
            game_Music.StopGameOver()
            game_Board.DisplayBlackScreen()
            game_Board.ReInitializeBoard()
            numGuesses = 0
            numPairs = 0
        pygame.display.flip()
        clock.wait(70)

    print("\nThanks For Playing!!!")
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
