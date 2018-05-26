import pygame
from board import tile
from board import move
#from player.minimax import minimax

pygame.init()
gameDisplay = pygame.display.set_mode((800,800))
pygame.display.set_caption("TheHive")
clock = pygame.time.Clock()

firstboard = tilemap.Board()
firstboard.createBoard()

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
    pygame.draw.rect(gameDisplay, color, [x, y, w, h])
    allTiles.append([color, [x, y, w, h]])

def drawChessPieces():
    xpos = 0
    ypos = 0
    color = 0
    width = 100
    height = 100
    black = (66,134,244)
    white = (143,155,175)
    number = 0
    for _ in range(20):
        for _ in range(20):
            if color % 2 == 0:
                squares(xpos, ypos, width, height, white)
                if not firstBoard.gameTiles[number].pieceOnTile.toString() == "-":
                    img = pygame.image.load("./ChessArt/" + firstBoard.gameTiles[number].pieceOnTile.alliance[0].upper() + firstBoard.gameTiles[
                        number].pieceOnTile.toString().upper() + ".png")
                    img = pygame.transform.scale(img, (100, 100))
                    allPieces.append([img, [xpos, ypos], firstBoard.gameTiles[number].pieceOnTile])
                xpos += 100
            else:
                squares(xpos, ypos, width, height, black)
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

def updateChessPieces():

    xpos = 0
    ypos = 0
    number = 0
    newPieces = []

    for _ in range(10):
        for _ in range(10):
            if not firstBoard.gameTiles[number].pieceOnTile.toString() == "-":

                img = pygame.image.load(
                    "./ChessArt/" + firstBoard.gameTiles[number].pieceOnTile.alliance[0].upper() + firstBoard.gameTiles[
                        number].pieceOnTile.toString().upper() + ".png")
                img = pygame.transform.scale(img, (100, 100))

                newPieces.append([img, [xpos, ypos], firstBoard.gameTiles[number].pieceOnTile])
            xpos += 100
            number += 1
        xpos = 0
        ypos += 100

    return newPieces


allSqParams = createSqParams()
drawChessPieces()

selectedImage = None
selectedLegals = None
resetColors = []
quitGame = False
mx, my = pygame.mouse.get_pos()
prevx, prevy = [0,0]

while not quitGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitGame = True
            pygame.quit()
            quit()

            pygame.display.update=()
            clock.tick(60)
