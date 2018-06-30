# Generic Tie Tac Toe library
**Python library for implementing any NxN Tic Tac Toe game**
### Usage:

**1) Setup the board:**

    from tictactoe import board #import board object
    b = board(5) #initialize a 5x5 board for the game

**2) Playing:**

    b.put(<class>,<row>,<column>)

Where:
 - class-1 denotes 'X'
- class-0 denotes 'O'

**Example:**

    b.put(0,1,0) #Puts an 'O' at the position (1,0)


   **3) Get State:**
   
    b.getState()
This function returns a 2D array of the current state of the board.

**4) Check Win:**

    flag,winner=b.checkWin()
   Winner contains the **class** of the player who has won.
   Flag denotes the end of the game where,
   

 - flag = 1 denotes Game Termination.
 - flag = -1 denotes Game Continuation.

 **5) Print State:**
 

    b.printState()
This function prints the existing state of the board.
**Example:**

    - - - O
    - - O X
    X O X -
    O X - -
**6) Reset Board**

    b.resetBoard()
   This function resets the board to start a new game.
