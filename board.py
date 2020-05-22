def createBoard(n): 
	x = 0
	board = [[],[],[],[],[],[],[],[]]
 
	for i in range(n): 
		for j in range(n):
			board[i].append(x)
			x += 1
	return board

board = createBoard(8)
			          
def getX(input):
	return input // 8

def getY(input):
	return input % 8

def getMoves(n):
	i = getX(n)
	j = getY(n)
	moves = []
	offsets = [ (i-2,j-1), (i-2,j+1), (i-1,j-2), (i-1,j+2), (i+1,j-2), (i+1,j+2), (i+2,j-1), (i+2,j+1) ]
	for o in offsets:
		if o[0] > -1 and o[1] > -1:
			if validateMoveInRange(o):
				moves.append(board[o[0]][o[1]])
	return moves		

def validateMoveInRange(coords):
	try:
		return board[coords[0]][coords[1]]
	except IndexError:
		return False

counter = 1

def shortestPath(start):
	next = getMoves(start)
	while end not in next:
		for n in next:
			counter += 1
			shortestPath(n)
	return counter

start = 11
end = 

print(shortestPath(start))




def BFS(self, s): 
  
	visited = {}

	queue = [] 
 
	queue.append(s) 
	visited.add(s)

	while queue: 

	    s = queue.pop(0) 
	    print (s, end = " ") 

	    for i in self.graph[s]: 
	        if visited[i] == False: 
	            queue.append(i) 
	            visited[i] = True







