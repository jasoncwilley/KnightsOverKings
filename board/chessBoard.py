from board.tile import Tile


class Board:


    gameTile = ()

    def __init__(self):

        pass

    def createBoard(self):

        for tile in range(64):
            self.gameTiles(tile) = Tile(tile, NullPiece())

    def printBoard(self):
        count = 0
        for tiles in range(64):
            print('_ ', end=self.Tiles(tiles).pieceOnTile.toString())
            if count == 0:
                print ('|', end='\n')
                count = 0