import copy

# These need to be modified here
#########################
Max_Depth = 40          #
Col = 4                 #
Row = 3                 #
#########################



print("Enter puzzle of 12 pieces, example of input: 0 1 2 3 4 5 6 7 8 9 10 11")
input_puzzle = input("Input the initial puzzle sequence\n")
type(input_puzzle)
print("this is the initial puzzle sequence that was inputted: ", input_puzzle)
Extracted_Puzzle = [int(s) for s in input_puzzle.split() if s.isdigit()]



# Node Class

class Node(object):

    def __init__(self, 
                 Heuristic      = 0, 
                 Board          = None,
                 Leaf_Nodes     = None,
                 Parent         = None,
                 Board_Size     = None,
                 Move           = None,
                 Depth          = 0,
                 Piece_Moved    = None):
        
        self.Heuristic      = Heuristic
        self.Board 	        = Board
        self.Leaf_Nodes     = Leaf_Nodes
        self.Parent         = Parent
        self.Board_Size     = Board_Size
        self.Move           = Move
        self.Depth          = Depth
        self.Piece_Moved    = Piece_Moved

    def setHeuristic(self, Heuristic):
        self.Heuristic = Heuristic

    def getHeuristic(self):
        return self.Heuristic


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
    

    def setMove(self, Move):
        self.Move = Move
    
    def getMove(self):
        return self.Move
    

    def setDepth(self, Depth):
        self.Depth = Depth
    
    def getDepth(self):
        return self.Depth


    def setPiece_Moved(self, Piece_Moved):
        self.Piece_Moved = Piece_Moved
    
    def getPiece_Moved(self):
        return self.Piece_Moved
    

### End Class NodeTree ###




# Move Functions #

def Find_Zero_Indexes(Node):
    Board_Size = Node.getBoard_Size()
    Row = Board_Size[0]  
    Col = Board_Size[1]

    for i in range (0, Row):
       for j in range (0, Col):
          if Node.Board[i][j] == 0:
            # print ("Position of 0 on board is", i, j)
            return i, j
		
	# for i in range (0, len(Node.Board)):
	# 	if (Node.Board[i] == 0):
	# 		print ("Position of 0 on board is", i)
	# 		return i

def Move_Up(Node):
    Zero_Pos                = Find_Zero_Indexes(Node)
    Zero_Row                = Zero_Pos[0]  
    Zero_Col                = Zero_Pos[1]
    Board                   = Node.getBoard_Position()
    Board_Size              = Node.getBoard_Size()
    Max_Row                 = Board_Size[0]
    Max_Col                 = Board_Size[1]
    Index_Of_Moving_Piece   = None
    # print(Zero_Pos)
    if Zero_Row - 1 >= 0:
        temp = Board[Zero_Row-1][Zero_Col]
        Index_Of_Moving_Piece = (Zero_Row-1)*Max_Col + Zero_Col
        Board[Zero_Row-1][Zero_Col] = 0
        Board[Zero_Row][Zero_Col] = temp
        Node.setPiece_Moved(Index_Of_Moving_Piece)
        Node.setBoard_Position(Board)
        # print ("Board from Move_up", Board)

    # if Zero_Pos -  Row > 0:
    # 	temp = Board[Zero_Pos+Row]
    # 	Board[Zero_Pos+Row] = 0
    # 	Board[Zero_Pos] = temp
    return

def Move_Up_Right(Node):
    Zero_Pos                = Find_Zero_Indexes(Node)
    Zero_Row                = Zero_Pos[0]  
    Zero_Col                = Zero_Pos[1]
    Board                   = Node.getBoard_Position()
    Board_Size              = Node.getBoard_Size()
    Max_Row                 = Board_Size[0]
    Max_Col                 = Board_Size[1]
    Index_Of_Moving_Piece   = None

    # print(Zero_Pos)
    if Zero_Row - 1 >= 0 and Zero_Col + 1 < Max_Col:
        temp = Board[Zero_Row-1][Zero_Col+1]
        Index_Of_Moving_Piece = (Zero_Row-1)*Max_Col + Zero_Col+1
        Board[Zero_Row-1][Zero_Col+1] = 0
        Board[Zero_Row][Zero_Col] = temp
        Node.setPiece_Moved(Index_Of_Moving_Piece)
        Node.setBoard_Position(Board)

        # print ("Board from Move_up_Right", Board)

    return

def Move_Right(Node):
    Zero_Pos                = Find_Zero_Indexes(Node)
    Zero_Row                = Zero_Pos[0]  
    Zero_Col                = Zero_Pos[1]
    Board                   = Node.getBoard_Position()
    Board_Size              = Node.getBoard_Size()
    Max_Row                 = Board_Size[0]
    Max_Col                 = Board_Size[1]
    Index_Of_Moving_Piece   = None
    # print(Zero_Pos)

    if Zero_Col + 1 < Max_Col:
        temp = Board[Zero_Row][Zero_Col+1]
        Index_Of_Moving_Piece = (Zero_Row)*Max_Col + Zero_Col+1
        Board[Zero_Row][Zero_Col+1] = 0
        Board[Zero_Row][Zero_Col] = temp
        Node.setPiece_Moved(Index_Of_Moving_Piece)
        Node.setBoard_Position(Board)

        # print ("Board from Move_Right", Board)

    return

def Move_Down_Right(Node):
    Zero_Pos                = Find_Zero_Indexes(Node)
    Zero_Row                = Zero_Pos[0]  
    Zero_Col                = Zero_Pos[1]
    Board                   = Node.getBoard_Position()
    Board_Size              = Node.getBoard_Size()
    Max_Row                 = Board_Size[0]
    Max_Col                 = Board_Size[1]
    Index_Of_Moving_Piece   = None
    # print(Zero_Pos)

    if Zero_Row + 1 < Max_Row and Zero_Col + 1 < Max_Col:
        temp = Board[Zero_Row+1][Zero_Col+1]
        Index_Of_Moving_Piece = (Zero_Row+1)*Max_Col + Zero_Col+1
        Board[Zero_Row+1][Zero_Col+1] = 0
        Board[Zero_Row][Zero_Col] = temp
        Node.setPiece_Moved(Index_Of_Moving_Piece)
        Node.setBoard_Position(Board)

        # print ("Board from Move_Down_Right", Board)

    return

def Move_Down(Node):
    Zero_Pos                = Find_Zero_Indexes(Node)
    Zero_Row                = Zero_Pos[0]  
    Zero_Col                = Zero_Pos[1]
    Board                   = Node.getBoard_Position()
    Board_Size              = Node.getBoard_Size()
    Max_Row                 = Board_Size[0]
    Max_Col                 = Board_Size[1]
    Index_Of_Moving_Piece   = None

    if Zero_Row + 1 < Max_Row:
        temp = Board[Zero_Row+1][Zero_Col]
        Index_Of_Moving_Piece = (Zero_Row+1)*Max_Col + Zero_Col
        Board[Zero_Row+1][Zero_Col] = 0
        Board[Zero_Row][Zero_Col] = temp
        Node.setPiece_Moved(Index_Of_Moving_Piece)
        Node.setBoard_Position(Board)

        # print ("Board from Move_Down", Board)

    return

def Move_Down_Left(Node):
    Zero_Pos                = Find_Zero_Indexes(Node)
    Zero_Row                = Zero_Pos[0]  
    Zero_Col                = Zero_Pos[1]
    Board                   = Node.getBoard_Position()
    Board_Size              = Node.getBoard_Size()
    Max_Row                 = Board_Size[0]
    Max_Col                 = Board_Size[1]
    Index_Of_Moving_Piece   = None

    if Zero_Row + 1 < Max_Row and Zero_Col - 1 >= 0:
        temp = Board[Zero_Row+1][Zero_Col-1]
        Index_Of_Moving_Piece = (Zero_Row+1)*Max_Col + Zero_Col-1
        Board[Zero_Row+1][Zero_Col-1] = 0
        Board[Zero_Row][Zero_Col] = temp
        Node.setPiece_Moved(Index_Of_Moving_Piece)
        Node.setBoard_Position(Board)

        # print ("Board from Move_Down_Left", Board)

    return

def Move_Left(Node):
    Zero_Pos                = Find_Zero_Indexes(Node)
    Zero_Row                = Zero_Pos[0]  
    Zero_Col                = Zero_Pos[1]
    Board                   = Node.getBoard_Position()
    Board_Size              = Node.getBoard_Size()
    Max_Row                 = Board_Size[0]
    Max_Col                 = Board_Size[1]
    Index_Of_Moving_Piece   = None

    if Zero_Col - 1 >= 0:
        temp = Board[Zero_Row][Zero_Col-1]
        Index_Of_Moving_Piece = (Zero_Row)*Max_Col + Zero_Col-1
        Board[Zero_Row][Zero_Col-1] = 0
        Board[Zero_Row][Zero_Col] = temp
        Node.setPiece_Moved(Index_Of_Moving_Piece)
        Node.setBoard_Position(Board)

        # print ("Board from Move_Left", Board)

    return

def Move_Up_Left(Node):
    Zero_Pos                = Find_Zero_Indexes(Node)
    Zero_Row                = Zero_Pos[0]  
    Zero_Col                = Zero_Pos[1]
    Board                   = Node.getBoard_Position()
    Board_Size              = Node.getBoard_Size()
    Max_Row                 = Board_Size[0]
    Max_Col                 = Board_Size[1]
    Index_Of_Moving_Piece   = None

    if Zero_Row - 1 >= 0 and Zero_Col - 1 >= 0:
        temp = Board[Zero_Row-1][Zero_Col-1]
        Index_Of_Moving_Piece = (Zero_Row-1)*Max_Col + Zero_Col-1
        Board[Zero_Row-1][Zero_Col-1] = 0
        Board[Zero_Row][Zero_Col] = temp
        Node.setPiece_Moved(Index_Of_Moving_Piece)
        Node.setBoard_Position(Board)

        # print ("Board from Move_Up_Left", Board)

    return




# used in the making of the output file
Pieces = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q"]

### Creating a 2D list to hold the board of the game ###
Board = [[i * j for j in range(Col)] for i in range(Row)]

k = 0
#Convert to 2D list
for i in range (0, Row):
    for j in range (0, Col):
        Board[i][j] = Extracted_Puzzle[k]
        #print (k)
        k = k + 1

### Building the Final Solution Board ###
Final_Solution = [[i * j for j in range(Col)] for i in range(Row)]
k = 1
#Convert to 2D list
for i in range (0, Row):
    for j in range (0, Col):
        if k == Row * Col:
            Final_Solution[i][j] = 0
        else:
            Final_Solution[i][j] = k
        k = k + 1

#print ("What Final Solution should look like", Final_Solution)




### Depth-First Search ### 
SolutionFound = False
Root = Node(Board = Board, Board_Size = [Row, Col], Depth=0)
#Find_Zero_Indexes(Root)

#print ("Board before moving\n", Root.getBoard_Position())

#Move_Down_Right(Root)

#print ("Board after moving\n", Root.getBoard_Position())
# Max_Depth = 10
#Final_Solution_Found = [[i * j for j in range(Col)] for i in range(Row)]
Final_Solution_Found = []
Reversed_Search_Path = []
Search_Path          = []
# print("Final_Solution_Found initialization ", Final_Solution_Found)


def Find_Search_Path(Node):
    global Search_Path
    if Node.getParent():
        Current_Move = []
        Index_of_Piece = Node.getPiece_Moved()
        Current_Move.append(Pieces[Index_of_Piece])
        Current_Move.append(Node.getBoard_Position())
        Reversed_Search_Path.append(Current_Move)
        Find_Search_Path(Node.getParent())

    else:
        Current_Move = []
        Current_Move.append("0")
        Current_Move.append(Node.getBoard_Position())
        Reversed_Search_Path.append(Current_Move)

    # Current_Move = Node.getMove()
    # if Current_Move == 0:

    # elif Current_Move == 1:
        
    # elif Current_Move == 2:
        
    # elif Current_Move == 3:
        
    # elif Current_Move == 4:
        
    # elif Current_Move == 5:
        
    # elif Current_Move == 6:
        
    # elif Current_Move == 7:




def Tree_Traversal(Current_Node):
    #print("Calling Tree_Traversal Fct")
    # print("Current_Node's depth", Current_Node.getDepth(),"move", Current_Node.getMove(), "Board", Current_Node.getBoard_Position())
    global Final_Solution_Found
    global SolutionFound
    global Type_Of_Search
    #while SolutionFound == False:
    if SolutionFound == False:

        if Current_Node.getBoard_Position() == Final_Solution:
            SolutionFound = True
            Final_Solution_Found = copy.deepcopy(Current_Node.getBoard_Position())
            # print("Current_Node's depth", Current_Node.getDepth(),"move", Current_Node.getMove(), "Board", Current_Node.getBoard_Position())
            Find_Search_Path(Current_Node)
            ### Call function to find Search Path to solution
            return
        elif Current_Node.getDepth() == Max_Depth:
            Final_Solution_Found =  copy.deepcopy(Current_Node.getBoard_Position())
            # Find_Search_Path(Current_Node)
            # print ("Final_Solution_Found for Max_Depth", Final_Solution_Found)
            return
        else:
            Zero_Pos    = Find_Zero_Indexes(Current_Node)
            Zero_Row    = Zero_Pos[0]  
            Zero_Col    = Zero_Pos[1]
            Board       = Current_Node.getBoard_Position()
            Board_Size  = Current_Node.getBoard_Size()
            Max_Row	    = Board_Size[0]
            Max_Col     = Board_Size[1]
            LeafNodes   = []

            if (Zero_Row - 1 >= 0) and (Current_Node.getMove() != 4): #Create node by moving Zero position up
                # print("Create Node for moving up")
                New_Node = Node(Board = copy.deepcopy(Board), Board_Size = Board_Size)
                Move_Up(New_Node)
                # print ("Showing board from 0", New_Node.getBoard_Position())
                # print("Showing Board of current_Node", Board)
                New_Node.setParent(Current_Node)
                New_Node.setMove(0)
                New_Node.setDepth(Current_Node.getDepth() + 1)
                LeafNodes.append(New_Node)

            if (Zero_Row - 1 >= 0 and Zero_Col + 1 < Max_Col) and (Current_Node.getMove() != 5): #Create node by moving Zero position Up-Right
                # print("Create Node for moving up right")
                New_Node = Node(Board = copy.deepcopy(Board), Board_Size = Board_Size)
                Move_Up_Right(New_Node)
                # print ("Showing board from 1", New_Node.getBoard_Position())
                # print("Showing Board of current_Node", Board)
                New_Node.setParent(Current_Node)
                New_Node.setMove(1)
                New_Node.setDepth(Current_Node.getDepth() + 1)
                LeafNodes.append(New_Node)

            if (Zero_Col + 1 < Max_Col) and (Current_Node.getMove() != 6): #Create node by moving Zero position Right
                # print("Create Node for moving right")
                New_Node = Node(Board = copy.deepcopy(Board), Board_Size = Board_Size)
                Move_Right(New_Node)
                # print ("Showing board from 2", New_Node.getBoard_Position())
                # print("Showing Board of current_Node", Board)
                New_Node.setParent(Current_Node)
                New_Node.setMove(2)
                New_Node.setDepth(Current_Node.getDepth() + 1)
                LeafNodes.append(New_Node)

            if (Zero_Row + 1 < Max_Row and Zero_Col + 1 < Max_Col) and (Current_Node.getMove() != 7): #Create node by moving Zero position Down-Right
                # print("Create Node for moving down right")
                New_Node = Node(Board = copy.deepcopy(Board), Board_Size = Board_Size)
                Move_Down_Right(New_Node)
                # print ("Showing board from 3", New_Node.getBoard_Position())
                # print("Showing Board of current_Node", Board)
                New_Node.setParent(Current_Node)
                New_Node.setMove(3)
                New_Node.setDepth(Current_Node.getDepth() + 1)
                LeafNodes.append(New_Node)

            if (Zero_Row + 1 < Max_Row) and (Current_Node.getMove() != 0): #Create node by moving Zero position Down
                # print("Create Node for moving down")
                New_Node = Node(Board = copy.deepcopy(Board), Board_Size = Board_Size)
                Move_Down(New_Node)
                # print ("Showing board from 4", New_Node.getBoard_Position())
                # print("Showing Board of current_Node", Board)
                New_Node.setParent(Current_Node)
                New_Node.setMove(4)
                New_Node.setDepth(Current_Node.getDepth() + 1)
                LeafNodes.append(New_Node)

            if (Zero_Row + 1 < Max_Row and Zero_Col - 1 >= 0) and (Current_Node.getMove() != 1): #Create node by moving Zero position Down-Left
                # print("Create Node for moving down left")
                New_Node = Node(Board = copy.deepcopy(Board), Board_Size = Board_Size)
                Move_Down_Left(New_Node)
                # print ("Showing board from 5", New_Node.getBoard_Position())
                # print("Showing Board of current_Node", Board)
                New_Node.setParent(Current_Node)
                New_Node.setMove(5)
                New_Node.setDepth(Current_Node.getDepth() + 1)
                LeafNodes.append(New_Node)

            if (Zero_Col - 1 >= 0) and (Current_Node.getMove() != 2): #Create node by moving Zero position Left
                # print("Create Node for moving left")
                New_Node = Node(Board = copy.deepcopy(Board), Board_Size = Board_Size)
                Move_Left(New_Node)
                # print ("Showing board from 6", New_Node.getBoard_Position())
                # print("Showing Board of current_Node", Board)
                New_Node.setParent(Current_Node)
                New_Node.setMove(6)
                New_Node.setDepth(Current_Node.getDepth() + 1)
                LeafNodes.append(New_Node)

            if (Zero_Row - 1 >= 0 and Zero_Col - 1 >= 0) and (Current_Node.getMove() != 3): #Create node by moving Zero position Up-Left
                # print("Create Node for moving up left")
                New_Node = Node(Board = copy.deepcopy(Board), Board_Size = Board_Size)
                Move_Up_Left(New_Node)
                # print ("Showing board from 7", New_Node.getBoard_Position())
                # print("Showing Board of current_Node", Board)
                New_Node.setParent(Current_Node)
                New_Node.setMove(7)
                New_Node.setDepth(Current_Node.getDepth() + 1)
                LeafNodes.append(New_Node)

            Current_Node.setLeaf_Nodes(LeafNodes)

            for j in range (0, len(LeafNodes)):
                Tree_Traversal(LeafNodes[j])


Tree_Traversal(Root)

### Reversing the Search Path List
for i in reversed(Reversed_Search_Path):
    Search_Path.append(i)

print("Final Solution found is:", Final_Solution_Found, "\n")
print("Number of moves needed: ", len(Search_Path) - 1)
# print("Search Path of Solution:\n", Search_Path)

### Outputing to a file ###
for j in Search_Path:
    print(j, file=open("puzzleDFS.txt", "a"))

#Output to puzzleDFS.txt




