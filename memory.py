
import pygame, sys, os, random
from pygame.locals import *

TITLE_CAPTION = "Memory Lane"
WINDOW_WIDTH = 760
WINDOW_HEIGHT = 600
NUM_PICS = 6
NUM_PAIRS = 4




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



class GameBoard(object):
    
    def __init__(self):
        self.GAME_TITLE = "Memory Lane"
        self.TITLE_CAPTION = "Ahmad's Memory Game"
        self.ROW_ONE = 100
        self.ROW_TWO = 250
        self.ROW_THREE = 400
        self.WINDOW_WIDTH = 740
        self.WINDOW_HEIGHT = 600
        self.NUM_PICS = 8
        self.NUM_CARDS = 20
        self.NUM_PAIRS = 4
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
        self.startScreenButton = ""
        self.startScreenButton2 = ""
        self.change3 = ""
        self.change2 = ""
        self.change = ""
        self.level1 = ""
        self.level2 = ""
        self.level3 = ""
        self.level4 = ""
        self.level5 = ""
        self.level6 = ""
        self.difficulty = ""
        self.Instructions = ""
        self.startScreenLogo = ""
        self.clock = pygame.time

    def InitializeScreenSize(self, width, height):
        self.WINDOW_WIDTH = width
        self.WINDOW_HEIGHT = height
        self.SCREEN = pygame.display.set_mode((self.WINDOW_WIDTH,
            self.WINDOW_HEIGHT));



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
        self.change = pygame.image.load(os.path.join("data/img/","desertglow.png"))
        self.level1 = pygame.image.load(os.path.join("data/img/","1red.png"))
        self.difficulty = pygame.image.load(os.path.join("data/img/","words.png"))
        self.level2 = pygame.image.load(os.path.join("data/img/","circle2.png"))
        self.level3 = pygame.image.load(os.path.join("data/img/","circle3.png"))
        self.level4 = pygame.image.load(os.path.join("data/img/","circle4.png"))
        self.level5 = pygame.image.load(os.path.join("data/img/","circle5.png"))
        self.level6 = pygame.image.load(os.path.join("data/img/","circle6.png"))
        self.change2 = pygame.image.load(os.path.join("data/img/","city.png"))
        self.change3 = pygame.image.load(os.path.join("data/img/","jungle.png"))
        self.Instructions = pygame.image.load(os.path.join("data/img/","instructions.png"))
        self.startScreenButton = pygame.image.load(os.path.join("data/img/","button.png"))
        self.startScreenButton2 = pygame.image.load(os.path.join("data/img/","button2.png"))
        self.startScreenLogo = pygame.image.load(os.path.join("data/img/","logo.png"))
        self.directionsFont = pygame.font.Font(os.path.join("data/fnt/","scribble.TTF"),30)
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



        self.SCREEN.blit(self.background_Image,(0,0))
        self.SCREEN.blit(self.startScreenCards,(70,250))
        self.SCREEN.blit(self.startScreenButton,(410,360))
        self.SCREEN.blit(self.startScreenButton2,(410,440))
        self.SCREEN.blit(self.startScreenLogo,(170,80))
        self.SCREEN.blit(self.change,(20,20))
        self.SCREEN.blit(self.level1,(335,550))
        self.SCREEN.blit(self.level2,(380,550))
        self.SCREEN.blit(self.level3,(425,550))
        self.SCREEN.blit(self.level4,(470,550))
        self.SCREEN.blit(self.level5,(515,550))
        self.SCREEN.blit(self.level6,(560,550))
        self.SCREEN.blit(self.difficulty,(85,550))
        self.SCREEN.blit(self.change2,(20,100))
        self.SCREEN.blit(self.change3,(20,180))

        corner1 = (410,360)
        corner2 = (410,440)
        corner3 = (20,20)
        corner4 = (20,100)
        corner5 = (20,180)

        corner6 = (335,550)
        corner7 = (380,550)
        corner8 = (425,550)
        corner9 = (470,550)
        corner10 = (515,550)
        corner11 = (560,550)

        

        lengyy = 50
        highh = 50

        image_length = 247
        image_height = 75

        lengthy = 130
        heighty = 81


        for event in pygame.event.get():
            if((event.type == QUIT) or (event.type == KEYUP and event.key == K_ESCAPE)):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_xxxxx, mouse_yyyyy = event.pos
                if (mouse_xxxxx >= corner1[0]) and (mouse_xxxxx <= corner1[0]+image_length) and (mouse_yyyyy >= corner1[1]) and (mouse_yyyyy <= corner1[1]+image_height):
                    self.DisplaySettings()
                    pygame.display.flip()
                    return True
            if event.type == MOUSEBUTTONDOWN:
                mouse_xxxxx, mouse_yyyyy = event.pos
                if (mouse_xxxxx >= corner3[0]) and (mouse_xxxxx <= corner3[0]+lengthy) and (mouse_yyyyy >= corner3[1]) and (mouse_yyyyy <= corner3[1]+heighty):
                    self.background_Image = pygame.image.load(os.path.join("data/img/","back.png"))
                    self.change = pygame.image.load(os.path.join("data/img/","desertglow.png"))
                    self.change2 = pygame.image.load(os.path.join("data/img/","city.png"))
                    self.change3 = pygame.image.load(os.path.join("data/img/","jungle.png"))
            if event.type == MOUSEBUTTONDOWN:
                mouse_xxxxx, mouse_yyyyy = event.pos
                if (mouse_xxxxx >= corner4[0]) and (mouse_xxxxx <= corner4[0]+lengthy) and (mouse_yyyyy >= corner4[1]) and (mouse_yyyyy <= corner4[1]+heighty):
                    self.background_Image = pygame.image.load(os.path.join("data/img/","city.jpg"))
                    self.change = pygame.image.load(os.path.join("data/img/","desert.png"))
                    self.change2 = pygame.image.load(os.path.join("data/img/","cityglow.png"))
                    self.change3 = pygame.image.load(os.path.join("data/img/","jungle.png"))
            if event.type == MOUSEBUTTONDOWN:
                mouse_xxxxx, mouse_yyyyy = event.pos
                if (mouse_xxxxx >= corner5[0]) and (mouse_xxxxx <= corner5[0]+lengthy) and (mouse_yyyyy >= corner5[1]) and (mouse_yyyyy <= corner5[1]+heighty):
                    self.background_Image = pygame.image.load(os.path.join("data/img/","jungle.jpg"))
                    self.change = pygame.image.load(os.path.join("data/img/","desert.png"))
                    self.change2 = pygame.image.load(os.path.join("data/img/","city.png"))
                    self.change3 = pygame.image.load(os.path.join("data/img/","jungleglow.png"))
            if event.type == MOUSEBUTTONDOWN:
                mouse_xxxxx, mouse_yyyyy = event.pos
                if (mouse_xxxxx >= corner6[0]) and (mouse_xxxxx <= corner6[0]+lengyy) and (mouse_yyyyy >= corner6[1]) and (mouse_yyyyy <= corner6[1]+highh): 
                    self.level1 = pygame.image.load(os.path.join("data/img/","1red.png"))
                    self.level2 = pygame.image.load(os.path.join("data/img/","circle2.png"))
                    self.level3 = pygame.image.load(os.path.join("data/img/","circle3.png"))
                    self.level4 = pygame.image.load(os.path.join("data/img/","circle4.png"))
                    self.level5 = pygame.image.load(os.path.join("data/img/","circle5.png"))
                    self.level6 = pygame.image.load(os.path.join("data/img/","circle6.png"))
                    self.NUM_PAIRS = 4
                    NUM_PAIRS = 4
                    NUM_PICS = 6
                    
            if event.type == MOUSEBUTTONDOWN:
                mouse_xxxxx, mouse_yyyyy = event.pos
                if (mouse_xxxxx >= corner7[0]) and (mouse_xxxxx <= corner7[0]+lengyy) and (mouse_yyyyy >= corner7[1]) and (mouse_yyyyy <= corner7[1]+highh): 
                    self.level1 = pygame.image.load(os.path.join("data/img/","circle.png"))
                    self.level2 = pygame.image.load(os.path.join("data/img/","2red.png"))
                    self.level3 = pygame.image.load(os.path.join("data/img/","circle3.png"))
                    self.level4 = pygame.image.load(os.path.join("data/img/","circle4.png"))
                    self.level5 = pygame.image.load(os.path.join("data/img/","circle5.png"))
                    self.level6 = pygame.image.load(os.path.join("data/img/","circle6.png"))
                    self.NUM_PAIRS = 5
                    NUM_PAIRS = 5
                    NUM_PICS = 8
            if event.type == MOUSEBUTTONDOWN:
                mouse_xxxxx, mouse_yyyyy = event.pos
                if (mouse_xxxxx >= corner8[0]) and (mouse_xxxxx <= corner8[0]+lengyy) and (mouse_yyyyy >= corner8[1]) and (mouse_yyyyy <= corner8[1]+highh): 
                    self.level1 = pygame.image.load(os.path.join("data/img/","circle.png"))
                    self.level2 = pygame.image.load(os.path.join("data/img/","circle2.png"))
                    self.level3 = pygame.image.load(os.path.join("data/img/","3red.png"))
                    self.level4 = pygame.image.load(os.path.join("data/img/","circle4.png"))
                    self.level5 = pygame.image.load(os.path.join("data/img/","circle5.png"))
                    self.level6 = pygame.image.load(os.path.join("data/img/","circle6.png"))
                    self.NUM_PAIRS = 6
                    NUM_PAIRS = 6
                    NUM_PICS = 9
            if event.type == MOUSEBUTTONDOWN:
                mouse_xxxxx, mouse_yyyyy = event.pos
                if (mouse_xxxxx >= corner9[0]) and (mouse_xxxxx <= corner9[0]+lengyy) and (mouse_yyyyy >= corner9[1]) and (mouse_yyyyy <= corner9[1]+highh): 
                    self.level1 = pygame.image.load(os.path.join("data/img/","circle.png"))
                    self.level2 = pygame.image.load(os.path.join("data/img/","circle2.png"))
                    self.level3 = pygame.image.load(os.path.join("data/img/","circle3.png"))
                    self.level4 = pygame.image.load(os.path.join("data/img/","4red.png"))
                    self.level5 = pygame.image.load(os.path.join("data/img/","circle5.png"))
                    self.level6 = pygame.image.load(os.path.join("data/img/","circle6.png"))
                    self.NUM_PAIRS = 7
                    NUM_PAIRS = 7
                    NUM_PICS = 9
            if event.type == MOUSEBUTTONDOWN:
                mouse_xxxxx, mouse_yyyyy = event.pos
                if (mouse_xxxxx >= corner10[0]) and (mouse_xxxxx <= corner10[0]+lengyy) and (mouse_yyyyy >= corner10[1]) and (mouse_yyyyy <= corner10[1]+highh): 
                    self.level1 = pygame.image.load(os.path.join("data/img/","circle.png"))
                    self.level2 = pygame.image.load(os.path.join("data/img/","circle2.png"))
                    self.level3 = pygame.image.load(os.path.join("data/img/","circle3.png"))
                    self.level4 = pygame.image.load(os.path.join("data/img/","circle4.png"))
                    self.level5 = pygame.image.load(os.path.join("data/img/","5red.png"))
                    self.level6 = pygame.image.load(os.path.join("data/img/","circle6.png"))
                    self.NUM_PAIRS = 8
                    NUM_PAIRS = 8
                    NUM_PICS = 10
            if event.type == MOUSEBUTTONDOWN:
                mouse_xxxxx, mouse_yyyyy = event.pos
                if (mouse_xxxxx >= corner11[0]) and (mouse_xxxxx <= corner11[0]+lengyy) and (mouse_yyyyy >= corner11[1]) and (mouse_yyyyy <= corner11[1]+highh): 
                    self.level1 = pygame.image.load(os.path.join("data/img/","circle.png"))
                    self.level2 = pygame.image.load(os.path.join("data/img/","circle2.png"))
                    self.level3 = pygame.image.load(os.path.join("data/img/","circle3.png"))
                    self.level4 = pygame.image.load(os.path.join("data/img/","circle4.png"))
                    self.level5 = pygame.image.load(os.path.join("data/img/","circle5.png"))
                    self.level6 = pygame.image.load(os.path.join("data/img/","6red.png"))
                    self.NUM_PAIRS = 9
                    NUM_PAIRS = 9
                    NUM_PICS = 12
            if event.type == MOUSEBUTTONDOWN:
                mouse_xxxxx, mouse_yyyyy = event.pos
                if (mouse_xxxxx >= corner2[0]) and (mouse_xxxxx <= corner2[0]+image_length) and (mouse_yyyyy >= corner2[1]) and (mouse_yyyyy <= corner2[1]+image_height):
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()
            return False


    def DisplaySettings(self):



        self.SCREEN.blit(self.background_Image,(0,0))
        self.SCREEN.blit(self.startScreenButton,(410,360))
        self.SCREEN.blit(self.startScreenButton2,(410,440))
        self.SCREEN.blit(self.change,(20,20))
        self.SCREEN.blit(self.level1,(335,550))
        self.SCREEN.blit(self.level2,(380,550))
        self.SCREEN.blit(self.level3,(425,550))
        self.SCREEN.blit(self.level4,(470,550))
        self.SCREEN.blit(self.level5,(515,550))
        self.SCREEN.blit(self.level6,(560,550))
        self.SCREEN.blit(self.difficulty,(85,550))
        self.SCREEN.blit(self.change2,(20,100))
        self.SCREEN.blit(self.change3,(20,180))

        corner1 = (410,360)
        corner2 = (410,440)
        corner3 = (20,20)
        corner4 = (20,100)
        corner5 = (20,180)

        corner6 = (335,550)
        corner7 = (380,550)
        corner8 = (425,550)
        corner9 = (470,550)
        corner10 = (515,550)
        corner11 = (560,550)

        

        lengyy = 50
        highh = 50

        image_length = 247
        image_height = 75

        lengthy = 130
        heighty = 81


        for event in pygame.event.get():
            if((event.type == QUIT) or (event.type == KEYUP and event.key == K_ESCAPE)):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_xxxxx, mouse_yyyyy = event.pos
                if (mouse_xxxxx >= corner1[0]) and (mouse_xxxxx <= corner1[0]+image_length) and (mouse_yyyyy >= corner1[1]) and (mouse_yyyyy <= corner1[1]+image_height):
                    self.DisplayWhiteScreen()
                    pygame.display.flip()
                    return True
            if event.type == MOUSEBUTTONDOWN:
                mouse_xxxxx, mouse_yyyyy = event.pos
                if (mouse_xxxxx >= corner3[0]) and (mouse_xxxxx <= corner3[0]+lengthy) and (mouse_yyyyy >= corner3[1]) and (mouse_yyyyy <= corner3[1]+heighty):
                    self.background_Image = pygame.image.load(os.path.join("data/img/","back.png"))
                    self.change = pygame.image.load(os.path.join("data/img/","desertglow.png"))
                    self.change2 = pygame.image.load(os.path.join("data/img/","city.png"))
                    self.change3 = pygame.image.load(os.path.join("data/img/","jungle.png"))
            if event.type == MOUSEBUTTONDOWN:
                mouse_xxxxx, mouse_yyyyy = event.pos
                if (mouse_xxxxx >= corner4[0]) and (mouse_xxxxx <= corner4[0]+lengthy) and (mouse_yyyyy >= corner4[1]) and (mouse_yyyyy <= corner4[1]+heighty):
                    self.background_Image = pygame.image.load(os.path.join("data/img/","city.jpg"))
                    self.change = pygame.image.load(os.path.join("data/img/","desert.png"))
                    self.change2 = pygame.image.load(os.path.join("data/img/","cityglow.png"))
                    self.change3 = pygame.image.load(os.path.join("data/img/","jungle.png"))
            if event.type == MOUSEBUTTONDOWN:
                mouse_xxxxx, mouse_yyyyy = event.pos
                if (mouse_xxxxx >= corner5[0]) and (mouse_xxxxx <= corner5[0]+lengthy) and (mouse_yyyyy >= corner5[1]) and (mouse_yyyyy <= corner5[1]+heighty):
                    self.background_Image = pygame.image.load(os.path.join("data/img/","jungle.jpg"))
                    self.change = pygame.image.load(os.path.join("data/img/","desert.png"))
                    self.change2 = pygame.image.load(os.path.join("data/img/","city.png"))
                    self.change3 = pygame.image.load(os.path.join("data/img/","jungleglow.png"))
            if event.type == MOUSEBUTTONDOWN:
                mouse_xxxxx, mouse_yyyyy = event.pos
                if (mouse_xxxxx >= corner6[0]) and (mouse_xxxxx <= corner6[0]+lengyy) and (mouse_yyyyy >= corner6[1]) and (mouse_yyyyy <= corner6[1]+highh): 
                    self.level1 = pygame.image.load(os.path.join("data/img/","1red.png"))
                    self.level2 = pygame.image.load(os.path.join("data/img/","circle2.png"))
                    self.level3 = pygame.image.load(os.path.join("data/img/","circle3.png"))
                    self.level4 = pygame.image.load(os.path.join("data/img/","circle4.png"))
                    self.level5 = pygame.image.load(os.path.join("data/img/","circle5.png"))
                    self.level6 = pygame.image.load(os.path.join("data/img/","circle6.png"))
                    self.NUM_PAIRS = 6
            if event.type == MOUSEBUTTONDOWN:
                mouse_xxxxx, mouse_yyyyy = event.pos
                if (mouse_xxxxx >= corner7[0]) and (mouse_xxxxx <= corner7[0]+lengyy) and (mouse_yyyyy >= corner7[1]) and (mouse_yyyyy <= corner7[1]+highh): 
                    self.level1 = pygame.image.load(os.path.join("data/img/","circle.png"))
                    self.level2 = pygame.image.load(os.path.join("data/img/","2red.png"))
                    self.level3 = pygame.image.load(os.path.join("data/img/","circle3.png"))
                    self.level4 = pygame.image.load(os.path.join("data/img/","circle4.png"))
                    self.level5 = pygame.image.load(os.path.join("data/img/","circle5.png"))
                    self.level6 = pygame.image.load(os.path.join("data/img/","circle6.png"))
                    self.NUM_PAIRS = 8
            if event.type == MOUSEBUTTONDOWN:
                mouse_xxxxx, mouse_yyyyy = event.pos
                if (mouse_xxxxx >= corner8[0]) and (mouse_xxxxx <= corner8[0]+lengyy) and (mouse_yyyyy >= corner8[1]) and (mouse_yyyyy <= corner8[1]+highh): 
                    self.level1 = pygame.image.load(os.path.join("data/img/","circle.png"))
                    self.level2 = pygame.image.load(os.path.join("data/img/","circle2.png"))
                    self.level3 = pygame.image.load(os.path.join("data/img/","3red.png"))
                    self.level4 = pygame.image.load(os.path.join("data/img/","circle4.png"))
                    self.level5 = pygame.image.load(os.path.join("data/img/","circle5.png"))
                    self.level6 = pygame.image.load(os.path.join("data/img/","circle6.png"))
                    self.NUM_PAIRS = 10
            if event.type == MOUSEBUTTONDOWN:
                mouse_xxxxx, mouse_yyyyy = event.pos
                if (mouse_xxxxx >= corner9[0]) and (mouse_xxxxx <= corner9[0]+lengyy) and (mouse_yyyyy >= corner9[1]) and (mouse_yyyyy <= corner9[1]+highh): 
                    self.level1 = pygame.image.load(os.path.join("data/img/","circle.png"))
                    self.level2 = pygame.image.load(os.path.join("data/img/","circle2.png"))
                    self.level3 = pygame.image.load(os.path.join("data/img/","circle3.png"))
                    self.level4 = pygame.image.load(os.path.join("data/img/","4red.png"))
                    self.level5 = pygame.image.load(os.path.join("data/img/","circle5.png"))
                    self.level6 = pygame.image.load(os.path.join("data/img/","circle6.png"))
                    self.NUM_PAIRS = 12
            if event.type == MOUSEBUTTONDOWN:
                mouse_xxxxx, mouse_yyyyy = event.pos
                if (mouse_xxxxx >= corner10[0]) and (mouse_xxxxx <= corner10[0]+lengyy) and (mouse_yyyyy >= corner10[1]) and (mouse_yyyyy <= corner10[1]+highh): 
                    self.level1 = pygame.image.load(os.path.join("data/img/","circle.png"))
                    self.level2 = pygame.image.load(os.path.join("data/img/","circle2.png"))
                    self.level3 = pygame.image.load(os.path.join("data/img/","circle3.png"))
                    self.level4 = pygame.image.load(os.path.join("data/img/","circle4.png"))
                    self.level5 = pygame.image.load(os.path.join("data/img/","5red.png"))
                    self.level6 = pygame.image.load(os.path.join("data/img/","circle6.png"))
                    self.NUM_PAIRS = 14
            if event.type == MOUSEBUTTONDOWN:
                mouse_xxxxx, mouse_yyyyy = event.pos
                if (mouse_xxxxx >= corner11[0]) and (mouse_xxxxx <= corner11[0]+lengyy) and (mouse_yyyyy >= corner11[1]) and (mouse_yyyyy <= corner11[1]+highh): 
                    self.level1 = pygame.image.load(os.path.join("data/img/","circle.png"))
                    self.level2 = pygame.image.load(os.path.join("data/img/","circle2.png"))
                    self.level3 = pygame.image.load(os.path.join("data/img/","circle3.png"))
                    self.level4 = pygame.image.load(os.path.join("data/img/","circle4.png"))
                    self.level5 = pygame.image.load(os.path.join("data/img/","circle5.png"))
                    self.level6 = pygame.image.load(os.path.join("data/img/","6red.png"))
                    self.NUM_PAIRS = 16
            if event.type == MOUSEBUTTONDOWN:
                mouse_xxxxx, mouse_yyyyy = event.pos
                if (mouse_xxxxx >= corner2[0]) and (mouse_xxxxx <= corner2[0]+image_length) and (mouse_yyyyy >= corner2[1]) and (mouse_yyyyy <= corner2[1]+image_height):
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()
            return False






    


    def DisplayIngameBackground(self,numGuesses,numPairs):
        self.SCREEN.blit(self.background_Image,(0,0))
        self.SCREEN.blit(self.helpButton,(684,30))
        displayScore = self.currentScoreFont.render("Number of Guesses: %d" %
            int(numGuesses/2), True, (255,255,255))
        pairs = self.currentScoreFont.render("Number of Pairs: (%d / %d)" %
            (numPairs, self.NUM_PAIRS), True, (255,255,255))
        self.SCREEN.blit(displayScore,(230,35))
        self.SCREEN.blit(pairs,(210,535))



    def NumPairs(self):
        return len(self.pairs)


    def RemoveSelection(self):
        self.pairs.pop()


    def AppendSelection(self, userSelection):
        self.pairs.append(userSelection)


    def IsPair(self, SELECTION_ONE, SELECTION_TWO):
        return (self.gamePieces[SELECTION_ONE] == self.gamePieces[SELECTION_TWO])


    def DisplayGameBoard(self):

        if (self.NumPairs() >= 1):
            width = 80
            for row1 in range(0, 6):
                if(self.IsSelectedImage(row1)):

                    self.SCREEN.blit(self.gamePieces[row1],(width, self.ROW_ONE))
                else:

                    self.SCREEN.blit(self.cardCover[row1],(width, self.ROW_ONE))
                width += 100

            width = 80
            for row2 in range(6, 12):
                if(self.IsSelectedImage(row2)):
                    self.SCREEN.blit(self.gamePieces[row2],(width, self.ROW_TWO))
                else:
                    self.SCREEN.blit(self.cardCover[row2],(width, self.ROW_TWO))
                width += 100

            width = 80
            for row3 in range(12, 18):
                if(self.IsSelectedImage(row3)):
                    self.SCREEN.blit(self.gamePieces[row3],(width,self.ROW_THREE))
                else:
                    self.SCREEN.blit(self.cardCover[row3],(width,self.ROW_THREE))
                width += 100


        else:
            width = 80
            for row1 in range(0, 6):
                self.SCREEN.blit(self.cardCover[row1],(width,self.ROW_ONE))
                width += 100
            width = 80

            for row2 in range(6, 12):
                self.SCREEN.blit(self.cardCover[row2],(width,self.ROW_TWO))
                width += 100

            width = 80
            for row3 in range(12, 18):
                self.SCREEN.blit(self.cardCover[row3],(width,self.ROW_THREE))
                width += 100


    def IsSelectedImage(self, checkMatch):
        for item in self.pairs:
            if(int(checkMatch) == int(item)):
                return True
        return False


    def GameOver(self,numGuesses):
        inGame = False
        width = 220
        height = 215
        bull = 3
        donkey = 2
        cat = 1
        fish = 0
        numGuesses = int(numGuesses/2)
        self.SCREEN.blit(self.background_Image,(0,0))
        displayScore = self.currentScoreFont.render("Number of Guesses: %d" %
            (numGuesses), True, (255,255,255))
        resumeGame = self.directionsFont.render("Click Anywhere To Continue!",
            True, (255,255,255))
            
        if(numGuesses >= 25):
            self.SCREEN.blit(self.ranks[bull],(width,height))
            desc = self.currentScoreFont.render("Rank: PENGUIN (Bad)",
                True, (255,255,255))
            desc2 = self.currentScoreFont.render("---->Better Luck Next Time "
                "Loser!!!<----", True, (255,255,255))
            self.SCREEN.blit(desc,(180,95))
            self.SCREEN.blit(desc2,(15,145))

        elif(numGuesses >= 21):
            self.SCREEN.blit(self.ranks[donkey],(width,height))
            desc = self.currentScoreFont.render("Memory Rank: DONKEY (Average)",
                True, (255,255,255))
            desc2 = self.currentScoreFont.render("You worked Your Way "
                "To Completion", True, (255,255,255))
            self.SCREEN.blit(desc,(180,95))
            self.SCREEN.blit(desc2,(105,145))

        elif(numGuesses >= 17):
            self.SCREEN.blit(self.ranks[cat],(width,height))
            desc = self.currentScoreFont.render("Memory Rank: CAT (Smart)", True,
                (255,255,255))
            desc2 = self.currentScoreFont.render("You Cautiously Played Your Way "
                "To Completion", True, (255,255,255))
            self.SCREEN.blit(desc,(190,95))
            self.SCREEN.blit(desc2,(90,145))

        else:
            self.SCREEN.blit(self.ranks[fish],(width,height))
            desc = self.currentScoreFont.render("Memory Rank: FISH (Genius)",
                True, (255,255,255))
            desc2 = self.currentScoreFont.render("You Were As Fast "
                "As A Fish In Water", True, (255,255,255))
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
        #t1 = "Ahmads's Memory Lane is a mind stimulating educational"
        #t2 = "card game in which an assortment of cards are laid face "
        #t3 = "down on a surface, and the player tries to uncover two"
        #t4 = "identical pairs. If the two cards match, the player"
        #t5 = "will have to answer a math problem. If they do not"
        #t6 = "match, the cards are turned back over."
        #t7 = "This game is made for the benefit of KS2 children"
        screenTitle = "About"

        self.SCREEN.blit(self.background_Image,(0,0))
        self.SCREEN.blit(self.Instructions,(0,0))
        
        

        while(not inGame):
            self.clock.wait(70)
            resumeGame = self.directionsFont.render("Click Anywhere To Continue!", True, (255,255,255))
            BG = (0,0,0)
            FG = (255,255,0)
            #t1BG = self.helpDescrFont.render(t1, True, (BG))
            #t1FG = self.helpDescrFont.render(t1, True, (FG))
            #t2BG = self.helpDescrFont.render(t2, True, (BG))
            #t2FG = self.helpDescrFont.render(t2, True, (FG))
            #t3BG = self.helpDescrFont.render(t3, True, (BG))
            #t3FG = self.helpDescrFont.render(t3, True, (FG))
            #t4BG = self.helpDescrFont.render(t4, True, (BG))
            #t4FG = self.helpDescrFont.render(t4, True, (FG))
            #t5BG = self.helpDescrFont.render(t5, True, (BG))
            #t5FG = self.helpDescrFont.render(t5, True, (FG))
            #t6BG = self.helpDescrFont.render(t6, True, (BG))
            #t6FG = self.helpDescrFont.render(t6, True, (FG))

            #t7BG = self.helpDescrFont.render(t7, True, (BG))
            #t7FG = self.helpDescrFont.render(t7, True, (FG))


            #width = 40
            #height = 140
            #offset = 3
##            newLine = 35
##            self.SCREEN.blit(t1BG,(width,height))
##            self.SCREEN.blit(t1FG,(width-offset,height-offset))
##            self.SCREEN.blit(t2BG,(width,height+newLine))
##            self.SCREEN.blit(t2FG,(width-offset,(height+newLine)-offset))
##            self.SCREEN.blit(t3BG,(width,height+(newLine*2)))
##            self.SCREEN.blit(t3FG,(width-offset,(height+(newLine*2))-offset))
##            self.SCREEN.blit(t4BG,(width,height+(newLine*3)))
##            self.SCREEN.blit(t4FG,(width-offset,(height+(newLine*3))-offset))
##            self.SCREEN.blit(t5BG,(width,height+(newLine*4)))
##            self.SCREEN.blit(t5FG,(width-offset,(height+(newLine*4))-offset))
##            self.SCREEN.blit(t6BG,(width,height+(newLine*5)))
##            self.SCREEN.blit(t6FG,(width-offset,(height+(newLine*5))-offset))
##            self.SCREEN.blit(t7BG,(width,height+(newLine*6)))
##            self.SCREEN.blit(t7FG,(width-offset,(height+(newLine*6))-offset))
            self.SCREEN.blit(resumeGame,(90,550))
            pygame.display.flip()

            for event in pygame.event.get():
                if((event.type == QUIT) or (event.type == KEYUP and event.key == K_ESCAPE)):
                    return False
                elif(event.type == MOUSEBUTTONUP):
                    self.DisplayWhiteScreen()
                    pygame.display.flip()
                    return True


    def GetSelection(self, mouseX, mouseY):

        if((mouseY <= 60 and mouseY >= 33)and(mouseX <= 713 and mouseX >= 687)):
            return "help"
        

        elif((mouseY <= 190) and (mouseY >= 80)):

            if((mouseX <= 170) and (mouseX >=80)):
                if(self.IsSelectedImage(0) == False):
                    return 0 
            elif((mouseX <= 270) and (mouseX >= 180)):
                if(self.IsSelectedImage(1) == False):
                    return 1
            elif((mouseX <= 370) and (mouseX >= 280)):
                if(self.IsSelectedImage(2) == False):
                    return 2
            elif((mouseX <= 470) and (mouseX >= 380)):
                if(self.IsSelectedImage(3) == False):
                    return 3
            elif((mouseX <= 570) and (mouseX >= 480)):
                if(self.IsSelectedImage(4) == False):
                    return 4
            elif((mouseX <= 670) and (mouseX >= 580)):
                if(self.IsSelectedImage(5) == False):
                    return 5

        elif((mouseY <= 340) and (mouseY >= 250)):

            if((mouseX <= 170) and (mouseX >= 80)):
                if(self.IsSelectedImage(6) == False):
                    return 6
            elif((mouseX <= 270) and (mouseX >= 180)):
                if(self.IsSelectedImage(7) == False):
                    return 7
            elif((mouseX <= 370) and (mouseX >= 280)):
                if(self.IsSelectedImage(8) == False):
                    return 8
            elif((mouseX <= 470) and (mouseX >= 380)):
                if(self.IsSelectedImage(9) == False):
                    return 9
            elif((mouseX <= 570) and (mouseX >= 480)):
                if(self.IsSelectedImage(10) == False):
                    return 10
            elif((mouseX <= 670) and (mouseX >= 580)):
                if(self.IsSelectedImage(11) == False):
                    return 11

        elif((mouseY <= 490) and (mouseY >= 400)):

            if((mouseX <= 170) and (mouseX >= 80)):
                if(self.IsSelectedImage(12) == False):
                    return 12
            elif((mouseX <= 270) and (mouseX >= 180)):
                if(self.IsSelectedImage(13) == False):
                    return 13
            elif((mouseX <= 370) and (mouseX >= 280)):
                if(self.IsSelectedImage(14) == False):
                    return 14
            elif((mouseX <= 470) and (mouseX >= 380)):
                if(self.IsSelectedImage(15) == False):
                    return 15
            elif((mouseX <= 570) and (mouseX >= 480)):
                if(self.IsSelectedImage(16) == False):
                    return 16
            elif((mouseX <= 670) and (mouseX >= 580)):
                if(self.IsSelectedImage(17) == False):
                    return 17
        return -1

    def DisplayWhiteScreen(self):
        self.SCREEN.fill((255,255,255,255))



def main():
    inGame = False
    numGuesses = 0
    numPairs = 0
    SELECTION_ONE = -1
    SELECTION_TWO = -1
    clock = pygame.time
    game_Board = GameBoard()
    game_Music = Music("intro.ogg","inGame.ogg","card.ogg",
        "pair.ogg","win.ogg","gameOver.ogg","noPair.ogg","helpMusic.ogg")


    os.environ["SDL_VIDEO_CENTERED"] = '1'
    game_Board.InitializeScreenSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    game_Board.InitializeGameData(NUM_PICS)
    game_Board.RandomizeGamePieces()


    game_Music.PlayIntro()




        
    while(not inGame):
        inGame = game_Board.DisplayStartScreen()


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
            game_Board.DisplayWhiteScreen()
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
