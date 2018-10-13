#
#
#
# 1) Depth-First Search
# 2) Best-First Search
# 3) A* Algorithm
#
#
#
#   [	a,   b,   c,   d    ]
# 	[	e,   f,   g,   h    ]
# 	[	i,   j,   k,   l    ]
# 
#   There are 8 possible moves: (Also Order of Preference if there are ties) 
# 		- up
# 		- Up-Right
# 		- Right
# 		- Down-Right
# 		- Down
# 		- Down-Left
# 		- Left
# 		- Up-Left
#		



# print("Example of input: 0 1 2 3 4 5 6 7 8 9 10 11")
# input_string = input("Input the initial puzzle sequence\n")
# type(input_string)

# print("this is the initial puzzle sequence that was inputted: ", input_string)

# Extracted_Puzzle = [int(s) for s in input_string.split() if s.isdigit()]

# print (Extracted_Puzzle)


#Check for errors in initial puzzle



# Node Class

class Node(object):

    def __init__(self, 
                 Heuristic 		= 0, 
                 Board 			= None,
                 Leaf_Nodes 	= None,
                 Parent 		= None,
                 Board_Size 	= None):
        
        self.Heuristic		= Heuristic
        self.Board 			= Board
        self.Leaf_Nodes 	= Leaf_Nodes
        self.Parent 		= Parent
        self.Board_Size 		= Board_Size

    def setHeuristic(self, Heuristic):
        self.Heurisitc = Heurisitc

    def getHeuristic(self):
        return self.Heurisitic


    def setBoard_Position(self, Board):
        self.Board = Board

    def getBoard_Position(self):
        return self.Board


    def setLeaf_Nodes(self, Leaf_Nodes):
        self.Leaf_Nodes = Leaf_Nodes

    def getLeaf_Nodes(self):
        return self.Leaf_Nodes


    def setParent(self, Parent):
        self.Parent = Parent

    def getParent(self):
        return self.Parent

    def setBoard_Size(self, Board_Size):
        self.Board_Size = Board_Size
    
    def getBoard_Size(self):
        return self.Board_Size
    


### End Class NodeTree ###




# Move Functions #

def Find_Zero_Index(Node):
	Board_Size = Node.getBoard_Size()
	Row = Board_Size[0]  
	Col = Board_Size[1]

	for i in range (0, Row):
		for j in range (0, Col):
			if Node.Board[i][j] == 0:
				#print ("Position of 0 on board is", i, j)
				return i, j
		
	# for i in range (0, len(Node.Board)):
	# 	if (Node.Board[i] == 0):
	# 		print ("Position of 0 on board is", i)
	# 		return i

def Move_Up(Node):
	Zero_Pos = Find_Zero_Index(Node)
	Zero_Row = Zero_Pos[0]  
	Zero_Col = Zero_Pos[1]
	Board 	 = Node.getBoard_Position()

	if Zero_Row - 1 >= 0:
		temp = Board[Zero_Row-1][Zero_Col]
		Board[Zero_Row-1][Zero_Col] = 0
		Board[Zero_Row][Zero_Col] = temp

		#print ("Board from Move_up", Board)

	Node.setBoard_Position(Board)
		 
	# if Zero_Pos -  Row > 0:
	# 	temp = Board[Zero_Pos+Row]
	# 	Board[Zero_Pos+Row] = 0
	# 	Board[Zero_Pos] = temp
	return

def Move_Up_Right(Node):
	Zero_Pos 	= Find_Zero_Index(Node)
	Zero_Row 	= Zero_Pos[0]  
	Zero_Col 	= Zero_Pos[1]
	Board 	 	= Node.getBoard_Position()
	Board_Size 	= Node.getBoard_Size()
	Max_Row		= Board_Size[0]
	Max_Col  	= Board_Size[1]

	if Zero_Row - 1 >= 0 and Zero_Row + 1 <= Max_Col:
		temp = Board[Zero_Row-1][Zero_Col+1]
		Board[Zero_Row-1][Zero_Col+1] = 0
		Board[Zero_Row][Zero_Col] = temp

		#print ("Board from Move_up_Right", Board)

	Node.setBoard_Position(Board)
	return

def Move_Right(Node):
	Zero_Pos 	= Find_Zero_Index(Node)
	Zero_Row 	= Zero_Pos[0]  
	Zero_Col 	= Zero_Pos[1]
	Board 	 	= Node.getBoard_Position()
	Board_Size 	= Node.getBoard_Size()
	Max_Row		= Board_Size[0]
	Max_Col  	= Board_Size[1]

	if Zero_Col + 1 <= Max_Col:
		temp = Board[Zero_Row][Zero_Col+1]
		Board[Zero_Row][Zero_Col+1] = 0
		Board[Zero_Row][Zero_Col] = temp

		#print ("Board from Move_up", Board)

	Node.setBoard_Position(Board)
	return

def Move_Down_Right(Node):
	Zero_Pos 	= Find_Zero_Index(Node)
	Zero_Row 	= Zero_Pos[0]  
	Zero_Col 	= Zero_Pos[1]
	Board 	 	= Node.getBoard_Position()
	Board_Size 	= Node.getBoard_Size()
	Max_Row		= Board_Size[0]
	Max_Col  	= Board_Size[1]

	if Zero_Row + 1 <= Max_Row and Zero_Row + 1 <= Max_Col:
		temp = Board[Zero_Row+1][Zero_Col+1]
		Board[Zero_Row+1][Zero_Col+1] = 0
		Board[Zero_Row][Zero_Col] = temp

		#print ("Board from Move_up_Right", Board)

	Node.setBoard_Position(Board)
	return

def Move_Down(Node):
	Zero_Pos = Find_Zero_Index(Node)
	Zero_Row = Zero_Pos[0]  
	Zero_Col = Zero_Pos[1]
	Board 	 = Node.getBoard_Position()
	Board_Size 	= Node.getBoard_Size()
	Max_Row		= Board_Size[0]
	Max_Col  	= Board_Size[1]

	if Zero_Row + 1 <= Max_Row:
		temp = Board[Zero_Row+1][Zero_Col]
		Board[Zero_Row+1][Zero_Col] = 0
		Board[Zero_Row][Zero_Col] = temp

		#print ("Board from Move_up", Board)

	Node.setBoard_Position(Board)
	return

def Move_Down_Left(Node):
	Zero_Pos 	= Find_Zero_Index(Node)
	Zero_Row 	= Zero_Pos[0]  
	Zero_Col 	= Zero_Pos[1]
	Board 	 	= Node.getBoard_Position()
	Board_Size 	= Node.getBoard_Size()
	Max_Row		= Board_Size[0]
	Max_Col  	= Board_Size[1]

	if Zero_Row + 1 <= Max_Row and Zero_Row - 1 >= 0:
		temp = Board[Zero_Row+1][Zero_Col-1]
		Board[Zero_Row+1][Zero_Col-1] = 0
		Board[Zero_Row][Zero_Col] = temp

		#print ("Board from Move_up_Right", Board)

	Node.setBoard_Position(Board)
	return

def Move_Left(Node):
	Zero_Pos 	= Find_Zero_Index(Node)
	Zero_Row 	= Zero_Pos[0]  
	Zero_Col 	= Zero_Pos[1]
	Board 	 	= Node.getBoard_Position()

	if Zero_Col - 1 >= 0:
		temp = Board[Zero_Row][Zero_Col-1]
		Board[Zero_Row][Zero_Col-1] = 0
		Board[Zero_Row][Zero_Col] = temp

		#print ("Board from Move_up", Board)

	Node.setBoard_Position(Board)
	return

def Move_Up_Left(Node):
	Zero_Pos 	= Find_Zero_Index(Node)
	Zero_Row 	= Zero_Pos[0]  
	Zero_Col 	= Zero_Pos[1]
	Board 	 	= Node.getBoard_Position()
	Board_Size 	= Node.getBoard_Size()

	if Zero_Row - 1 >= 0 and Zero_Row - 1 >= 0:
		temp = Board[Zero_Row-1][Zero_Col-1]
		Board[Zero_Row-1][Zero_Col-1] = 0
		Board[Zero_Row][Zero_Col] = temp

		#print ("Board from Move_up_Right", Board)

	Node.setBoard_Position(Board)
	return


# Depth-First Search 
SolutionNotFound = False
Col = 4
Row = 3

Extracted_Puzzle = [1, 6, 3, 7, 5, 2, 0, 4, 9, 10, 11, 8]
Board = [[i * j for j in range(Col)] for i in range(Row)]
k = 0
#Convert to 2D list
for i in range (0, Row):
	for j in range (0, Col):
		Board[i][j] = Extracted_Puzzle[k]
		k = k + 1

print (Board)



Root = Node(Board = Board, Board_Size = [Row, Col])
Find_Zero_Index(Root)

print ("Board before moving\n", Root.getBoard_Position())

Move_Down_Right(Root)

print ("Board after moving\n", Root.getBoard_Position())


#while SolutionNotFound == False:




#Output to puzzleDFS.txt




