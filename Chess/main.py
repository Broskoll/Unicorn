import unicornhat as unicorn
from functs import *
from classes import *

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

"""to invert intensities of several pieces
!!! call abstractPiece method invertIntensity()"""
def invertIntensities(pieces):
	for piece in pieces:
		piece.invertIntensity()

def freeCaseFilter(posToFiltrate):
	i = 0
	while i < len(posToFiltrate):
		if chessGrid[posToFiltrate[i][0]][posToFiltrate[i][1]] == None:
			i += 1
		else:
			posToFiltrate.remove(posToFiltrate[i])
	return posToFiltrate

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
		if getCase(select).player == "p1":
			selectedPiece = getCase(select)
			selectedPiece.invertIntensity()
			invertIntensities(P1)
			valid = not valid
		else:
			select = raw_input("Case invalide !\nSelectionner une case (A-H 1-8) :\n")
	valid = not valid

	selectedPiece.possiblePositions = freeCaseFilter(selectedPiece.possiblePositions)
	for possibility in selectedPiece.possiblePositions:
		unicorn.set_pixel(possibility[0],possibility[1],255,255,255)
	unicorn.show()
	sleep(4)
