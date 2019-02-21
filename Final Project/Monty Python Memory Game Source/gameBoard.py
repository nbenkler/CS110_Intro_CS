#   Name:  Noam Benkler
#   Date:   March 14, 2018
#   File: gameBoard.py
#   Description: This is the gameBoard.py class that sets up the board
#      and cards for the main function in memory.py. This class reads 
#      the images and fonts files from the "img" & "fnt "directory to use
#      in the program.

import random, pygame, sys, os
from pygame.locals import *

class GameBoard(object):
    def __init__(self):
        self.GAME_TITLE = "Nobody Expects *oh,bugger*"
        self.TITLE_CAPTION = "by Noam Benkler"
        self.ROW_ONE = 50
        self.ROW_TWO = 255
        self.ROW_THREE = 460
        self.WINDOW_WIDTH = 1250
        self.WINDOW_HEIGHT = 680
        self.NUM_PICS = 18
        self.NUM_CARDS = 18
        self.NUM_PAIRS = 9
        self.NUM_RANKS = 4
        self.images = []
        self.gamePieces = []
        self.cardCover = []
        self.pairs = []
        self.ranks = []
        self.titleFont = ""
        self.directionsFont = ""
        self.helpFont = ""
        self.background_Image = ""
        self.helpButton = ""
        self.startScreenCards = ""
        self.clock = pygame.time

    def InitializeScreenSize(self, width, height):
        self.WINDOW_WIDTH = width
        self.WINDOW_HEIGHT = height
        self.SCREEN = pygame.display.set_mode((self.WINDOW_WIDTH,
            self.WINDOW_HEIGHT));

    def SetGameTitle(self, title):
        self.TITLE_CAPTION = title
        pygame.display.set_caption(self.TITLE_CAPTION)

    def InitializeGameData(self, totalPics):
        self.NUM_PICS = totalPics

        for x in range(self.NUM_PICS):
            self.images.append(pygame.image.load(os.path.join("data/img/",
                "img%d.png" % (x+1))))
        for x in range(self.NUM_RANKS):
            self.ranks.append(pygame.image.load(os.path.join("data/img/",
                "rank%d.png" % (x+1))))
        for x in range(self.NUM_CARDS):
            self.cardCover.append(pygame.image.load(os.path.join("data/img/",
                "card.png")))

        self.startScreenCards = pygame.image.load(os.path.join("data/img/","cards2.png"))
        self.titleFont = pygame.font.Font(os.path.join("data/fnt/","KLEPTOMA.TTF"),50)
        self.directionsFont = pygame.font.Font(os.path.join("data/fnt/","scribble.TTF"),30)
        self.jokeFont = pygame.font.Font(os.path.join("data/fnt/","scribble.TTF"),28)
        self.helpFont = pygame.font.Font(os.path.join("data/fnt/","scribble.TTF"),14)
        self.helpDescrFont = pygame.font.Font(os.path.join("data/fnt/","ShakeThatBooty.ttf"),30)
        self.currentScoreFont = pygame.font.Font(os.path.join("data/fnt/","ShakeThatBooty.ttf"),30)
        self.background_Image = pygame.image.load(os.path.join("data/img/","back.png"))
        self.helpButton = pygame.image.load(os.path.join("data/img/","Help_Turquoise.png"))

    def ReInitializeBoard(self):
        del self.pairs[:]
        del self.gamePieces[:]
        self.RandomizeGamePieces()

    def RandomizeGamePieces(self):
        random.shuffle(self.images)
        random.shuffle(self.images)
        for x in range(self.NUM_PAIRS):
            self.gamePieces.append(self.images[x])

        random.shuffle(self.gamePieces)

        for x in range(self.NUM_PAIRS, self.NUM_CARDS):
            self.gamePieces.append(self.gamePieces[x-self.NUM_PAIRS])

        random.shuffle(self.gamePieces)

    def DisplayStartScreen(self):
        titleHeight = 100
        titleWidth = 150
        titleBG = self.titleFont.render(self.GAME_TITLE, True, (0,0,0))
        titleFG = self.titleFont.render(self.GAME_TITLE, True, (225,225,0))
        directions = self.directionsFont.render("Welcome to Noam Benkler's Monty Python Memory Game! ",
            True, (255,255,255))
        directions2 = self.directionsFont.render("This game tests how well you can learn and remember",
            True, (255,255,255))
        directions3 = self.directionsFont.render("8...*eh*... 9 elements of the terrible Spanish Inquisition's",
            True, (255,255,255))
        directions4 = self.directionsFont.render("weaponry and heretical deeds! Just click on the cards and",
            True, (255,255,255))
        directions5 = self.directionsFont.render("remember, in case of emergency to... AAAARGH!!!!!...",
            True, (255,255,255))
        directions6 = self.directionsFont.render("...we regret to inform you that the programmer has just ",
            True, (255,255,255))
        directions7 = self.directionsFont.render("suffered a fatal heart attack. Please Click Once To Begin!",
            True, (255,255,255))
        joke = self.jokeFont.render(                                                                                                                                          "Type --  Wenn ist das Nunstuck git und Slotermeyer? Ja! ... ",
            True, (255,255,255))
        joke2 = self.jokeFont.render(                                                                                                                                          "Beiherhund das Oder die Flipperwaldt gersput. -- into Google Translate",
            True, (255,255,255))
        joke3 = self.jokeFont.render( 																																			"...you will not be dissappointed. Google still has a sense of humor",
            True, (255, 255, 255))
        author = self.directionsFont.render("By Noam Benkler", True,
            (255,255,255))

        self.SCREEN.blit(self.background_Image,(0,0))
        self.SCREEN.blit(titleBG,(titleHeight-4,titleWidth-4))
        self.SCREEN.blit(titleFG,(titleHeight,titleWidth))
        self.SCREEN.blit(author,(titleHeight+150,titleWidth+50))
        self.SCREEN.blit(directions,(titleHeight-20,titleWidth+280))
        self.SCREEN.blit(directions2,(titleHeight-20,titleWidth+305))
        self.SCREEN.blit(directions3,(titleHeight-20,titleWidth+330))
        self.SCREEN.blit(directions4,(titleHeight-20,titleWidth+355))
        self.SCREEN.blit(directions5,(titleHeight-20,titleWidth+380))
        self.SCREEN.blit(directions6,(titleHeight-20,titleWidth+450))
        self.SCREEN.blit(directions7,(titleHeight-20,titleWidth+475))
        self.SCREEN.blit(self.startScreenCards,(70,210))

        for event in pygame.event.get():
            if((event.type == QUIT) or (event.type == KEYUP and event.key == K_ESCAPE)):
                pygame.quit()
                sys.exit()
            elif(event.type == MOUSEBUTTONUP):
                self.DisplayBlackScreen()
                pygame.display.flip()
                return True
        pygame.display.flip()
        return False

    def DisplayIngameBackground(self,numGuesses,numPairs):
        self.SCREEN.blit(self.background_Image,(0,0))
        displayScore = self.currentScoreFont.render("Number of Guesses: %d" %
            int(numGuesses/2), True, (255,255,255))
        pairs = self.currentScoreFont.render("Number of Pairs: (%d / %d)" %
            (numPairs, self.NUM_PAIRS), True, (255,255,255))
        self.SCREEN.blit(displayScore,(450,15))
        self.SCREEN.blit(pairs,(450,595))

    def NumPairs(self):
        return len(self.pairs)

    def RemoveSelection(self):
        self.pairs.pop()

    def AppendSelection(self, userSelection):
        self.pairs.append(userSelection)

    def IsPair(self, SELECTION_ONE, SELECTION_TWO):
        return (self.gamePieces[SELECTION_ONE] == self.gamePieces[SELECTION_TWO])

    def DisplayGameBoard(self):
        self.SCREEN.blit(self.helpButton,(1180,15))
        if (self.NumPairs() >= 1):
            width = 80 
            for row1 in range(0, 6):
                if(self.IsSelectedImage(row1)):
                    self.SCREEN.blit(self.gamePieces[row1],(width, self.ROW_ONE))
                else:
                    self.SCREEN.blit(self.cardCover[row1],(width, self.ROW_ONE))
                width += 200

            width = 80
            for row2 in range(6, 12):
                if(self.IsSelectedImage(row2)):
                    self.SCREEN.blit(self.gamePieces[row2],(width, self.ROW_TWO))
                else:
                    self.SCREEN.blit(self.cardCover[row2],(width, self.ROW_TWO))
                width += 200

            width = 80
            for row3 in range(12, 18):
                if(self.IsSelectedImage(row3)):
                    self.SCREEN.blit(self.gamePieces[row3],(width,self.ROW_THREE))
                else:
                    self.SCREEN.blit(self.cardCover[row3],(width,self.ROW_THREE))
                width += 200

        else:
            width = 80
            for row1 in range(0, 6):
                self.SCREEN.blit(self.cardCover[row1],(width,self.ROW_ONE))
                width += 200

            width = 80
            for row2 in range(6, 12):
                self.SCREEN.blit(self.cardCover[row2],(width,self.ROW_TWO))
                width += 200

            width = 80
            for row3 in range(12, 18):
                self.SCREEN.blit(self.cardCover[row3],(width,self.ROW_THREE))
                width += 200

    def IsSelectedImage(self, checkMatch):
        for item in self.pairs:
            if(int(checkMatch) == int(item)):
                return True
        return False

    def GameOver(self,numGuesses):
        inGame = False
        width = 220
        height = 215
        scott = 3
        kngt = 2
        arch = 1
        lady = 0
        numGuesses = int(numGuesses/2)
        self.SCREEN.blit(self.background_Image,(0,0))
        displayScore = self.currentScoreFont.render("Number of Guesses: %d" %
            (numGuesses), True, (255,255,255))
        resumeGame = self.directionsFont.render("Click Anywhere To Continue!",
            True, (255,255,255))

        if(numGuesses >= 22):
            self.SCREEN.blit(self.ranks[scott],(width,height))
            desc = self.currentScoreFont.render("Rank: Kamikaze Scottsman (Worst)",
                True, (255,255,255))
            desc2 = self.currentScoreFont.render("You May Need to Rethink "
                "Your Strategy of Attack", True, (255,255,255))
            self.SCREEN.blit(desc,(180,95))
            self.SCREEN.blit(desc2,(15,145))

        elif(numGuesses >= 19):
            self.SCREEN.blit(self.ranks[kngt],(width,height))
            desc = self.currentScoreFont.render("Rank: The Black Knight (Average)",
                True, (255,255,255))
            desc2 = self.currentScoreFont.render("You Appear Formidable but May "
                "Need to Find Your Legs Before Another Attempt ", True, (255,255,255))
            self.SCREEN.blit(desc,(180,95))
            self.SCREEN.blit(desc2,(105,145))

        elif(numGuesses >= 15):
            self.SCREEN.blit(self.ranks[arch],(width,height))
            desc = self.currentScoreFont.render("Memory Rank: Archimedes (Smart)", True,
                (255,255,255))
            desc2 = self.currentScoreFont.render("Eurika!!! "
                "You're Beginning to Figure it Out", True, (255,255,255))
            self.SCREEN.blit(desc,(190,95))
            self.SCREEN.blit(desc2,(90,145))

        else:
            self.SCREEN.blit(self.ranks[lady],(width,height))
            desc = self.currentScoreFont.render("Memory Rank: Old Woman (Genius)",
                True, (255,255,255))
            desc2 = self.currentScoreFont.render("You're Unbeatable! The Tortures "
                "of The Inquisition Hold no Fear for You", True, (255,255,255))
            self.SCREEN.blit(desc,(180,95))
            self.SCREEN.blit(desc2,(25,145))

        self.SCREEN.blit(displayScore,(230,35))
        self.SCREEN.blit(resumeGame,(90,515))

        while(not inGame):
            self.clock.wait(70)
            pygame.display.flip()
            for event in pygame.event.get():
                if((event.type == QUIT) or (event.type == KEYUP and event.key == K_ESCAPE)):
                    return False
                elif(event.type == MOUSEBUTTONUP):
                    return True

    def DisplayHelp(self):
        inGame = False
        titleHeight = 100
        titleWidth = 150
        t1 = "Welcome to Noam Benkler's Monty Python Memory Game! "
        t2 = "This game tests how well you can learn and remember "
        t3 = "8...*uh*... 9 elements of the terrible Spanish  "
        t4 = "Inquisition's weaponry and deeds of which you have "
        t5 = "been charged! To do this, click on the back of the cards "
        t6 = "each card will turn over to reveal a weapon or deed. "
        t7 = "match each wepon with its pair to fully identify it "
        t8 = "and longer evade the clutches of cardinal fang."
        t9 = "Depending on how well you do you will be given a rank"
        t10 = "describing how well you did."
        screenTitle = "About"

        self.SCREEN.blit(self.background_Image,(115,0))

        while(not inGame):
            self.clock.wait(70)
            titleBG = self.titleFont.render(screenTitle, True, (0,0,0))
            titleFG = self.titleFont.render(screenTitle, True, (225,225,0))
            resumeGame = self.directionsFont.render("Click Anywhere To Continue!", True, (255,255,255))
            BG = (0,0,0)
            FG = (255,255,0)
            t1BG = self.helpDescrFont.render(t1, True, (BG))
            t1FG = self.helpDescrFont.render(t1, True, (FG))
            t2BG = self.helpDescrFont.render(t2, True, (BG))
            t2FG = self.helpDescrFont.render(t2, True, (FG))
            t3BG = self.helpDescrFont.render(t3, True, (BG))
            t3FG = self.helpDescrFont.render(t3, True, (FG))
            t4BG = self.helpDescrFont.render(t4, True, (BG))
            t4FG = self.helpDescrFont.render(t4, True, (FG))
            t5BG = self.helpDescrFont.render(t5, True, (BG))
            t5FG = self.helpDescrFont.render(t5, True, (FG))
            t6BG = self.helpDescrFont.render(t6, True, (BG))
            t6FG = self.helpDescrFont.render(t6, True, (FG))

            t7BG = self.helpDescrFont.render(t7, True, (BG))
            t7FG = self.helpDescrFont.render(t7, True, (FG))
            t8BG = self.helpDescrFont.render(t8, True, (BG))
            t8FG = self.helpDescrFont.render(t8, True, (FG))
            t9BG = self.helpDescrFont.render(t9, True, (BG))
            t9FG = self.helpDescrFont.render(t9, True, (FG))
            t10BG = self.helpDescrFont.render(t10, True, (BG))
            t10FG = self.helpDescrFont.render(t10, True, (FG))

            width = 40
            height = 140
            offset = 3
            newLine = 35
            self.SCREEN.blit(t1BG,(width,height))
            self.SCREEN.blit(t1FG,(width-offset,height-offset))
            self.SCREEN.blit(t2BG,(width,height+newLine))
            self.SCREEN.blit(t2FG,(width-offset,(height+newLine)-offset))
            self.SCREEN.blit(t3BG,(width,height+(newLine*2)))
            self.SCREEN.blit(t3FG,(width-offset,(height+(newLine*2))-offset))
            self.SCREEN.blit(t4BG,(width,height+(newLine*3)))
            self.SCREEN.blit(t4FG,(width-offset,(height+(newLine*3))-offset))
            self.SCREEN.blit(t5BG,(width,height+(newLine*4)))
            self.SCREEN.blit(t5FG,(width-offset,(height+(newLine*4))-offset))
            self.SCREEN.blit(t6BG,(width,height+(newLine*5)))
            self.SCREEN.blit(t6FG,(width-offset,(height+(newLine*5))-offset))
            self.SCREEN.blit(t7BG,(width,height+(newLine*6)))
            self.SCREEN.blit(t7FG,(width-offset,(height+(newLine*6))-offset))
            self.SCREEN.blit(t8BG,(width,height+(newLine*7)))
            self.SCREEN.blit(t8FG,(width-offset,(height+(newLine*7))-offset))
            self.SCREEN.blit(t9BG,(width,height+(newLine*8)))
            self.SCREEN.blit(t9FG,(width-offset,(height+(newLine*8))-offset))
            self.SCREEN.blit(t10BG,(width,height+(newLine*9)))
            self.SCREEN.blit(t10FG,(width-offset,(height+(newLine*9))-offset))

            self.SCREEN.blit(titleBG,(75-4,45-4))
            self.SCREEN.blit(titleFG,(75,45))
            self.SCREEN.blit(resumeGame,(90,515))
            pygame.display.flip()

            for event in pygame.event.get():
                if((event.type == QUIT) or (event.type == KEYUP and event.key == K_ESCAPE)):
                    return False
                elif(event.type == MOUSEBUTTONUP):
                    self.DisplayBlackScreen()
                    pygame.display.flip()
                    return True

    def GetSelection(self, mouseX, mouseY):
        if((mouseY <= 45 and mouseY >= 15)and(mouseX <= 1212 and mouseX >= 1183)):
            return "help"
        elif((mouseY <= 180) and (mouseY >= 30)):
            if((mouseX <= 210) and (mouseX >=80)):
                if(self.IsSelectedImage(0) == False):
                    return 0 
            elif((mouseX <= 410) and (mouseX >= 280)):
                if(self.IsSelectedImage(1) == False):
                    return 1 
            elif((mouseX <= 610) and (mouseX >= 480)):
                if(self.IsSelectedImage(2) == False):
                    return 2  
            elif((mouseX <= 810) and (mouseX >= 680)):
                if(self.IsSelectedImage(3) == False):
                    return 3  
            elif((mouseX <= 1010) and (mouseX >= 880)):
                if(self.IsSelectedImage(4) == False):
                    return 4  
            elif((mouseX <= 1210) and (mouseX >= 1080)):
                if(self.IsSelectedImage(5) == False):
                    return 5  
        elif((mouseY <= 385) and (mouseY >= 255)):
            if((mouseX <= 210) and (mouseX >=80)):
                if(self.IsSelectedImage(6) == False):
                    return 6  
            elif((mouseX <= 410) and (mouseX >= 280)):
                if(self.IsSelectedImage(7) == False):
                    return 7  
            elif((mouseX <= 610) and (mouseX >= 480)):
                if(self.IsSelectedImage(8) == False):
                    return 8  
            elif((mouseX <= 810) and (mouseX >= 680)):
                if(self.IsSelectedImage(9) == False):
                    return 9  
            elif((mouseX <= 1010) and (mouseX >= 880)):
                if(self.IsSelectedImage(10) == False):
                    return 10   
            elif((mouseX <= 1210) and (mouseX >= 1080)):
                if(self.IsSelectedImage(11) == False):
                    return 11 
        elif((mouseY <= 590) and (mouseY >= 460)):
            if((mouseX <= 210) and (mouseX >=80)):
                if(self.IsSelectedImage(12) == False):
                    return 12  
            elif((mouseX <= 410) and (mouseX >= 280)):
                if(self.IsSelectedImage(13) == False):
                    return 13  
            elif((mouseX <= 610) and (mouseX >= 480)):
                if(self.IsSelectedImage(14) == False):
                    return 14  
            elif((mouseX <= 810) and (mouseX >= 680)):
                if(self.IsSelectedImage(15) == False):
                    return 15 
            elif((mouseX <= 1010) and (mouseX >= 880)):
                if(self.IsSelectedImage(16) == False):
                    return 16  
            elif((mouseX <= 1210) and (mouseX >= 1080)):
                if(self.IsSelectedImage(17) == False):
                    return 17
        return -1

    def DisplayBlackScreen(self):
        self.SCREEN.fill((0,0,0,0))
