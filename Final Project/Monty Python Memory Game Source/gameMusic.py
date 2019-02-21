#   Name:  Noam Benkler
#   Date:   March 14, 2018
#   File: gameMusic.py
#   Description: This is the gameMusic.py class that sets up the sounds
#      and music you hear during the game. This class reads the .ogg and .wav 
#      files from the "snd" directory to use during the program.

import pygame, os
from pygame.locals import *

class Music(object):
    def __init__(self, intro, game, card, pair, win, over, noPair, help):
        pygame.mixer.pre_init(44100, -16, 2)
        pygame.init()
        self.introMusic = pygame.mixer.Sound(os.path.join("data/snd/",intro))
        self.gameMusic = pygame.mixer.Sound(os.path.join("data/snd/",game))
        self.cardSoundFX = pygame.mixer.Sound(os.path.join("data/snd/",card))
        self.pairSoundFX = pygame.mixer.Sound(os.path.join("data/snd/",pair))
        self.winSoundFX = pygame.mixer.Sound(os.path.join("data/snd/",win))
        self.gameOverMusic = pygame.mixer.Sound(os.path.join("data/snd/",over))
        self.noPairSoundFX = pygame.mixer.Sound(os.path.join("data/snd/",noPair))
        self.helpMusic = pygame.mixer.Sound(os.path.join("data/snd/",help))
        self.semaphore = True 
        self.clock = pygame.time

    def PlayIntro(self):
        if(self.semaphore):
            self.introMusic.play(-1)
            self.semaphore = False

    def StopIntro(self):
        self.introMusic.stop()
        self.semaphore = True

    def PlayInGame(self):
        if(self.semaphore):
            self.gameMusic.play(-1)
            self.semaphore = False

    def PauseInGame(self):
        pygame.mixer.pause()
        self.semaphore = True

    def ResumeInGame(self):
        pygame.mixer.unpause()
        self.semaphore = False

    def StopInGame(self):
        self.gameMusic.stop()
        self.semaphore = True

    def PlayCardSoundFX(self):
        self.cardSoundFX.play()

    def PlayPairSoundFX(self):
        self.pairSoundFX.play()

    def PlayNoPairSoundFX(self):
        self.noPairSoundFX.play()

    def PlayWinSoundFX(self):
        self.winSoundFX.play()

    def PlayGameOver(self):
        if(self.semaphore):
            self.gameOverMusic.play(-1)
            self.semaphore = False

    def StopGameOver(self):
        self.gameOverMusic.stop()
        self.semaphore = True

    def PlayHelp(self):
        if(self.semaphore):
            self.helpMusic.play(-1)
            self.semaphore = False

    def StopHelp(self):
        self.helpMusic.stop()
        self.semaphore = True