import unicornhat as unicorn
from functions import *
from classes import *

unicorn.rotation(180)

# pieces of player 1 (tab[Objects])
P1 = [King(player = "p1", case = "A4"),
Queen(player = "p1", case = "A5"),
Bishop(player = "p1", case = "A3"),
Bishop(player = "p1", case = "A6"),
Knight(player = "p1", case = "A2"),
Knight(player = "p1", case = "A7"),
Rook(player = "p1", case = "A1"),
Rook(player = "p1", case = "A8")]

for i in range(8):
	P1.append(Pawn(player = "p1", case = "B" + str(i+1)))

# pieces of player 2 (tab[Objects])
P2 = [King(player = "p2", case = "H5"),
Queen(player = "p2", case = "H4"),
Bishop(player = "p2", case = "H3"),
Bishop(player = "p2", case = "H6"),
Knight(player = "p2", case = "H2"),
Knight(player = "p2", case = "H7"),
Rook(player = "p2", case = "H1"),
Rook(player = "p2", case = "H8")]

for i in range(8):
	P2.append(Pawn(player = "p2", case = "G" + str(i+1)))

# grid of the chessboard (tab[lines[Objects]])
chessGrid = [
[P1[6],P1[4],P1[2],P1[0],P1[1],P1[3],P1[5],P1[7]],
[P1[8],P1[9],P1[10],P1[11],P1[12],P1[13],P1[14],P1[15]],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[P2[8],P2[9],P2[10],P2[11],P2[12],P2[13],P2[14],P2[15]],
[P2[6],P2[4],P2[2],P2[0],P2[1],P2[3],P2[5],P2[7]]
]

"""argument:
		-case : case of intrest (String)
Return content of the case (None or pieceObject)"""
def getCase(case):
	coord = caseToPosition(case)
	return chessGrid[coord[0]][coord[1]]

def getPos(coord):
	if coord[0] < 0 or coord[0] > 7 or coord[1] < 0 or coord[1] > 7:
		return None 
	else:
		return chessGrid[coord[0]][coord[1]]

"""to invert intensities of several pieces
!!! call abstractPiece method invertIntensity()"""
def invertIntensities(pieces):
	for piece in pieces:
		piece.invertIntensity()

def possibleCases(position, player, pType, diagonal, horizVert, length):
	validPos = []
	
	if horizVert:
		i = 1
		positive = True
		negative = True

		while (positive or negative) and i <= length:
			if position[1]+i > 7:
				positive = False
			elif getPos([position[0],position[1]+i]) != None:
				if getPos([position[0],position[1]+i]).player != player and positive:
					validPos.append([position[0],position[1]+i])		
				positive = False
			elif positive:
				validPos.append([position[0],position[1]+i])
			
			if position[1]-i < 0:
				negative = False
			elif getPos([position[0],position[1]-i]) != None:
				if getPos([position[0],position[1]-i]).player != player and negative:
					validPos.append([position[0],position[1]-i])		
				negative = False
			elif negative:
				validPos.append([position[0],position[1]-i])
			i += 1

		i = 1
		positive = True
		negative = True

		while (positive or negative) and i <= length:
			if position[0]+i > 7:
				positive = False
			elif getPos([position[0]+i,position[1]]) != None:
				if getPos([position[0]+i,position[1]]).player != player and positive:
					validPos.append([position[0]+i,position[1]])		
				positive = False
			elif positive:
				validPos.append([position[0]+i,position[1]])
			
			if position[0]-i < 0:
				negative = False
			elif getPos([position[0]-i,position[1]]) != None:
				if getPos([position[0]-i,position[1]]).player != player and negative:
					validPos.append([position[0]-i,position[1]])		
				negative = False
			elif negative:
				validPos.append([position[0]-i,position[1]])
			i += 1

	if diagonal:
		i = 1
		positive = True
		negative = True
		while (positive or negative) and i <= length:

			if position[0]+i > 7 or position[1]+i > 7:
				positive = False
			elif getPos([position[0]+i,position[1]+i]) != None:
				if getPos([position[0]+i,position[1]+i]).player != player and positive:
					validPos.append([position[0]+i,position[1]+i])		
				positive = False
			elif positive:
				validPos.append([position[0]+i,position[1]+i])
			
			if position[0]-i < 0 or position[1]-i < 0:
				negative = False
			elif getPos([position[0]-i,position[1]-i]) != None:
				if getPos([position[0]-i,position[1]-i]).player != player and negative:
					validPos.append([position[0]-i,position[1]-i])		
				negative = False
			elif negative:
				validPos.append([position[0]-i,position[1]-i])
			i += 1

		i = 1
		positive = True
		negative = True

		while (positive or negative) and i <= length:
			if position[0]-i < 0 or position[1]+i > 7:
				positive = False
			elif getPos([position[0]-i,position[1]+i]) != None:
				if getPos([position[0]-i,position[1]+i]).player != player and positive:
					validPos.append([position[0]-i,position[1]+i])		
				positive = False
			elif positive:
				validPos.append([position[0]-i,position[1]+i])
			
			if position[0]+i > 7 or position[1]-i < 0:
				negative = False
			elif getPos([position[0]+i,position[1]-i]) != None:
				if getPos([position[0]+i,position[1]-i]).player != player and negative:
					validPos.append([position[0]+i,position[1]-i])		
				negative = False
			elif negative:
				validPos.append([position[0]+i,position[1]-i])
			i += 1

	if pType == "knight":
		i = 0
		validPos = [
		[position[0]-2,position[1]-1],
		[position[0]-2,position[1]+1],
		[position[0]-1,position[1]-2],
		[position[0]+1,position[1]-2],
		[position[0]+2,position[1]-1],
		[position[0]+2,position[1]+1],
		[position[0]-1,position[1]+2],
		[position[0]+1,position[1]+2]]
		validPos = limitFilter(validPos)
		while i < len(validPos):
			if getPos(validPos[i]) != None:
				if getPos(validPos[i]).player == player:
					validPos.remove(validPos[i])
				else:
					i += 1
			else:
				i += 1

	if pType == "pawn":
		if player == "p1":
			xInit = 1
			i = 1
		else:
			xInit = 6
			i = -1

		validPos = [[position[0]+i, position[1]]]
		if position[0] == xInit:
			validPos.append([position[0]+(2*i), position[1]])
		if getPos(validPos[0]) != None:
			validPos = []
		elif len(validPos) == 2:
			if getPos(validPos[1]) != None:
				validPos.remove(validPos[1])

		if getPos([position[0]+i, position[1]-1]) != None:
			validPos.append([position[0]+i, position[1]-1])

		if getPos([position[0]+i, position[1]+1]) != None:
			validPos.append([position[0]+i, position[1]+1])

	return validPos
	
# initialisation of unicornhat
for line in chessGrid:
	for piece in line:
		if piece:
			unicorn.set_pixel(piece.position[0],piece.position[1],piece.color[0],piece.color[1],piece.color[2])
unicorn.show()
print P2[6].possiblePositions
sleep(3)
valid = False

# main loop
while True:
	invertIntensities(P2)
	unicorn.show()
	
	select = raw_input("Selectionner une case (A-H 1-8) :\n")
	
	# choose piece to play
	while not valid: #loop until a valid choice
		if not bool(caseToPosition(select)) or getCase(select) == None or getCase(select).player == "p2":
			select = raw_input("Case invalide !\nSelectionner une case (A-H 1-8) :\n")
			
		else:
			selectedPiece = getCase(select)
			selectedPiece.invertIntensity()
			invertIntensities(P1)
			selectedPiece.possiblePositions = possibleCases(selectedPiece.position, selectedPiece.player, selectedPiece.type, selectedPiece.diagonal, selectedPiece.horizVert, selectedPiece.length)
			if bool(selectedPiece.possiblePositions):
				valid = not valid
			else:
				print("Aucun deplacement possible pour cette piece")
				for i in range(3):
					unicorn.set_pixel(selectedPiece.position[0], selectedPiece.position[1], selectedPiece.color[0], selectedPiece.color[1], selectedPiece.color[2])
					unicorn.show()
					sleep(0.2)
					unicorn.set_pixel(selectedPiece.position[0], selectedPiece.position[1],0,0,0)
					unicorn.show()
					sleep(0.2)
				selectedPiece.invertIntensity()
				invertIntensities(P1)
				select = raw_input("Selectionner une autre case:")
	valid = not valid

	
	for possibility in selectedPiece.possiblePositions:
		if getPos(possibility) != None:
			unicorn.set_pixel(possibility[0],possibility[1],0,128,128)	
		else:
			unicorn.set_pixel(possibility[0],possibility[1],255,255,255)
	unicorn.show()
	sleep(4)
