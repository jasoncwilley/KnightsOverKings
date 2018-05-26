import pygame
from os import path
from board import chessBoard


img_dir = path.join(path.dirname( __file__), 'ChessAry')


#from board.move import Move
#from player.minimax import Minimax

pygame.init()
gameDisplay = pygame.display.set_mode((800, 800))
pygame.display.set_caption("PyChess")
clock = pygame.time.Clock()

firstBoard = chessBoard.Board()
firstBoard.createBoard()
firstBoard.printBoard()

allTiles = []
allPieces = []
currentPlayer = firstBoard.currentPlayer



def createSqParams():
    allSqRanges = []
    xMin = 0
    xMax = 100
    yMin = 0
    yMax = 100
    for _ in range(8):
        for _ in range(8):
            allSqRanges.append([xMin, xMax, yMin, yMax])
            xMin += 100
            xMax += 100
        xMin = 0
        xMax = 100
        yMin += 100
        yMax += 100
    return allSqRanges

def squares(x, y, w, h, color):
    pygame.draw.rect(gameDisplay, color, [x,y,w,h])
    allTiles.append([color, [x,y,w,h]])

def drawChessPieces():
    xpos = 0
    ypos = 0
    color = 0
    width = 100
    heigth = 100
    black = (0,0,0)
    white = (255,255,255)
    number = 0


    for _ in range(8):
        for _ in range(8):
            if color % 2 == 0:
                squares(xpos, ypos, width, heigth, white)
                if not firstBoard.gameTiles[number].pieceOnTile.toString() == "-":
                    img = pygame.image.load("./ChessArt/" + firstBoard.gameTiles[number].pieceOnTile.alliance[0].upper() + firstBoard.gameTiles[
                        number].pieceOnTile.toString().upper() + ".png")
                    img = pygame.transform.scale(img, (100, 100))
                    allPieces.append([img, [xpos, ypos], firstBoard.gameTiles[number].pieceOnTile])
                xpos += 100
            else:
                squares(xpos, ypos, width, heigth, black)
                if not firstBoard.gameTiles[number].pieceOnTile.toString() == "-":
                    img = pygame.image.load("./ChessArt/" + firstBoard.gameTiles[number].pieceOnTile.alliance[0].upper() + firstBoard.gameTiles[
                        number].pieceOnTile.toString().upper() + ".png")
                    img = pygame.transform.scale(img, (100, 100))
                    allPieces.append([img, [xpos, ypos], firstBoard.gameTiles[number].pieceOnTile])
                xpos += 100

            color += 1
            number += 1
        color += 1
        xpos = 0
        ypos += 100

drawChessPieces()

quitGame = False

while not quitGame:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitGame = True
            pygame.quit()
            quit()


    gameDisplay.fill((255, 255, 255))

    for info in allTiles:
        pygame.draw.rect(gameDisplay, info[0], info[1])

    for img in allPieces:
        gameDisplay.blit(img[0], img[1])


    pygame.display.update()
    clock.tick(60)
