# Chess Move

import sys
sys.path.append(".")
from board import *
from player import *
from pieces import *

# Begin Move Class ##########################################
#
class Move():
    # initialize both parameters are of Piece type
    # Begin Init ##################################
    def __init__(self, piece, dest, tpe, board):
        self.piece = piece
        self.dest = dest
        self.type = tpe
        self.board = board
        self.promoteID = 0
        self.checkPromote()
        # need special options for pawn promotion
        # special options for castling
    # End Init ####################################

    def checkPromote(self):
        from pieces import Pawn
        if(type(self.piece) == Pawn):
            if((self.piece.color == 'w' and self.piece.position[1] == 6) or (self.piece.color == 'b' and self.piece.position[1] == 1)):
                self.type = 'p'

    def execute(self):
        if(self.type == 'm'):
            self.move()
            return
        if(self.type == 'm2'):
            self.move2()
            return
        if(self.type == 'c'):
            self.capture()
            return
        if(self.type == 'ep'):
            self.enPassant()
            return
        if(self.type == 'cl'):
            self.castleLong()
            return
        if(self.type == 'cs'):
            self.castleShort()
            return
        if(self.type == 'p'):
            self.promote()
            return
        print(self.type)
        print("!!!!!!!!!!!!!!move type assignment error!!!!!!!!!!!!!!!!!!!")

    def move(self):
        position = self.piece.position
        self.piece.position = self.dest.position
        self.dest.position = position
        self.piece.hasMoved = True
        self.board.allocatePieces()

    def move2(self):
        self.move()
        self.piece.hasMoved2 = True

    def capture(self):
        from pieces import Empty
        position = self.piece.position
        self.piece.position = self.dest.position
        self.board.allPieces.remove(self.dest)
        self.board.allPieces.append(Empty(position))
        self.piece.hasMoved = True
        self.board.allocatePieces()

    def enPassant(self):
        from pieces import Empty
        position = self.dest.position
        if(self.piece.color == 'w'):
            dpos = tuple(map(sum, zip(position,(0,1))))
        else:
            dpos = tuple(map(sum, zip(position,(0,-1))))
        board.allPieces.remove(self.dest)
        board.allPieces.append(Empty(position))
        self.dest = self.board.findPiece(dpos)
        self.move()

    def castleLong(self):
        self.move()
        kpos = self.piece.position
        self.piece = self.board.findPiece(tuple(map(sum, zip(kpos,(-2,0)))))
        self.dest = self.board.findPiece(tuple(map(sum, zip(kpos,(1,0)))))
        self.move()

    def castleShort(self):
        self.move()
        kpos = self.piece.position
        self.piece = self.board.findPiece(tuple(map(sum, zip(kpos,(1,0)))))
        self.dest = self.board.findPiece(tuple(map(sum, zip(kpos,(-1,0)))))
        self.move()

    def promote(self):
        from pieces import Queen, Bishop, Knight, Rook, Empty
        while(True):
            newPiece = input('what piece would you like to promote your pawn to? [q = Queen, b = Bishop, n = Knight, r = rook] ')
            if(newPiece == 'q'):
                self.promotePiece = Queen(self.piece.color, self.dest.position, 1000+self.promoteID)
                break
            elif(newPiece == 'b'):
                self.promotePiece = Bishop(self.piece.color, self.dest.position, 1000+self.promoteID)
                break
            elif(newPiece == 'n'):
                self.promotePiece = Knight(self.piece.color, self.dest.position, 1000+self.promoteID)
                break
            elif(newPiece == 'r'):
                self.promotePiece = Rook(self.piece.color, self.dest.position, 1000+self.promoteID)
                break
            else:
                print('invalid input, try again...')
        position = self.piece.position
        self.board.allPieces.remove(self.piece)
        self.board.allPieces.remove(self.dest)
        self.board.allPieces.append(self.promotePiece)
        self.board.allPieces.append(Empty(position))
        self.board.allocatePieces()

    # display a move
    # Begin Display ##
    def display(self):
        print(self.piece.display(), self.piece.position, '|', self.dest.display(), self.dest.position, '|', self.type)
    # End Display ####

    def displayNice(self):
        print(self.piece.display(), self.piece.positionNice(), '|', self.dest.display(), self.dest.positionNice(), '|', self.type)
#
# End Move Class ############################################