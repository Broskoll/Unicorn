import unicornhat as unicorn
from time import sleep
 
def setGrid(liste):
    for y in range(8):
            for x in range(8):
                    a = liste[y][x][0]
                    b = liste[y][x][1]
                    c = liste[y][x][2]
                    unicorn.set_pixel(y, x, a, b, c)
    unicorn.show()
    sleep(0.1)

""" Take a case (String) in argument like "A3"
Return a tuple x/y like [3,4] """
def caseToPosition(case):
        listComb = [["A","B","C","D","E","F","G","H"],["1","2","3","4","5","6","7","8"]]
        listXY = []
        for i in listComb:
                for j in i:
                        if case[listComb.index(i):listComb.index(i)+1] == j:
                                listXY.append(i.index(j))
        if len(listXY) == 2: 
        	return listXY
        else:
        	return False

""" Take a tuple x/y like [3,4] in argument
Return a case (String) like "A3" """
def positionToCase(position):
	listComb = [["A","B","C","D","E","F","G","H"],["1","2","3","4","5","6","7","8"]]
	case = listComb[0][position[0]]+listComb[1][position[1]]
	return case	

""" Specific to Object pieces
argument:
	-posToFiltrate : potential positions to filtrate (tab of tuple[[],...,[]])

Return positions minus out of limit positions"""
def limitFilter(posToFiltrate):
	i = 0
	while i < len(posToFiltrate):
		if (posToFiltrate[i][0] < 0 or posToFiltrate[i][0] > 7) or (posToFiltrate[i][1] < 0 or posToFiltrate[i][1] > 7):
			posToFiltrate.remove(posToFiltrate[i])
		else:
			i += 1
	return posToFiltrate
