import unicornhat as unicorn
from functions import *


class AbstractPiece :

	def __init__(self, player, case):
		self.type = ""
		self.color = [0,0,0]
		self.player = player
		self.case = case
		self.position = caseToPosition(self.case)
		self.possiblePositions = []

	def invertIntensity(self):
		for i in range(3):
			if self.color[i] > 100:
				self.color[i] = self.color[i]/2 
			else:
				self.color[i] = self.color[i]*2
		unicorn.set_pixel(self.position[0],self.position[1],self.color[0],self.color[1],self.color[2])

class King(AbstractPiece):
	
	def __init__(self, player, case):
		AbstractPiece.__init__(self, player, case)
		self.type = "king"
		self.color = [128, 0, 0]
		self.diagonal = True
		self.horizVert = True
		self.length = 1
		
	def move(self, case):
		self.case = case
		self.position = caseToPosition(self.case)		
		print("move")

class Queen(AbstractPiece):
	
	def __init__(self, player, case):
		AbstractPiece.__init__(self, player, case)
		self.type = "queen"
		self.color = [0, 128, 0]
		self.diagonal = True
		self.horizVert = True
		self.length = 7

	def move():
		print("move")

class Bishop(AbstractPiece):
	
	def __init__(self, player, case):
		AbstractPiece.__init__(self, player, case)
		self.type = "bishop"
		self.color = [0, 0, 128]
		self.diagonal = True
		self.horizVert = False
		self.length = 7
		
	def move():
		print("move")

class Knight(AbstractPiece):
	
	def __init__(self, player, case):
		AbstractPiece.__init__(self, player, case)
		self.type = "knight"
		self.color = [128, 0, 128]
		self.diagonal = False
		self.horizVert = False
		self.length = 0
		self.possiblePositions = [
		[self.position[0]-2,self.position[1]-1],
		[self.position[0]-2,self.position[1]+1],
		[self.position[0]-1,self.position[1]-2],
		[self.position[0]+1,self.position[1]-2],
		[self.position[0]+2,self.position[1]-1],
		[self.position[0]+2,self.position[1]+1],
		[self.position[0]-1,self.position[1]+2],
		[self.position[0]+1,self.position[1]+2]]
		self.possiblePositions = limitFilter(self.possiblePositions)

	def move():
		print("move")

class Rook(AbstractPiece):

	def __init__(self, player, case):
		AbstractPiece.__init__(self, player, case)
		self.type = "rook"
		self.color = [128, 128, 0]
		self.diagonal = False
		self.horizVert = True
		self.length = 7

	def move():
		print("move")

class Pawn(AbstractPiece):

	def __init__(self, player, case):
		AbstractPiece.__init__(self, player, case)
		self.type = "pawn"
		self.color = [128, 128, 128]
		self.diagonal = False
		self.horizVert = False
		self.length = 0
		if self.player == "p1":
			self.possiblePositions = [
			[self.position[0]+1,self.position[1]],
			[self.position[0]+2,self.position[1]]]
		else:
			self.possiblePositions = [
			[self.position[0]-1,self.position[1]],
			[self.position[0]-2,self.position[1]]]

	def move():
		print("move")
