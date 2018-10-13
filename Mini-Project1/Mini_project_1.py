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

Extracted_Puzzle = [1, 6, 3, 7, 5, 2, 0, 4, 9, 10, 11, 8]


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
	for i in range (0, len(Node.Board)):
		if (Node.Board[i] == 0):
			#print ("Position of 0 on board is", i)
			return i

def Move_Up(Node):
	Zero_Pos = Find_Zero_Index(Node)
	Row = Node.getBoard_Size[0]
	if Zero_Pos -  Row > 0:
		temp = Node.Board[Zero_Pos+Row]
		Node.Board[Zero_Pos+Row] = 0
		Node.Board[Zero_Pos] = temp
	return

def Move_Up_Right(Node):
	
	return

def Move_Right(Node):
	
	return

def Move_Down_Right(Node):
	
	return

def Move_Down(Node):
	
	return

def Move_Down_Left(Node):
	
	return

def Move_Left(Node):
	
	return

def Move_Up_Left(Node):
	
	return


# Depth-First Search 
SolutionNotFound = False
Col = 4
Row = 3
Root = Node(Board = Extracted_Puzzle, Board_Size = [Row, Col])
# Find_Zero_Index(Root)

print ("Board before moving\n", Root.getBoard_Position)

Move_Up(Root)

print ("Board before moving\n", Root.getBoard_Position)


#while SolutionNotFound == False:




#Output to puzzleDFS.txt




