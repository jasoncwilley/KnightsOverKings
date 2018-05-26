import pygame
import board.chessBoard

#from board.move import Move
#from player.minimax import Minimax

pygame.init()
gameDisplay = pygame.display.set_mode((800, 800))
pygame.display.set_caption("PyChess")
clock = pygame.time.Clock()


chessBoard = board.chessBoard.Board()
chessBoard.createBoard()
chessBoard.printBoard()




quitGame = False

while not quitGame:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitGame = True
            pygame.quit()
            quit()




    pygame.display.update()
    clock.tick(60)
