# Generic Tie Tac Toe library
**Python library for implementing any NxN Tic Tac Toe game**
### Usage:

**1) Setup the board:**

    from gttt.env import board	#import board object
    b = board(5)			#initialize a 5x5 board for the game

**2) Playing:**

    b.step(<playID>,<row>,<column>)

**Example:**

    b.step(0,1,0) #Puts an 0 at the position (1,0)
Step returns the flag of last move and current state of the board.
Flag is PlayID for win, -1 for no termination and -2 for draw. State of the board is NxN list of current board state.

 **3) Print State:**
 

    b.printState()
This function prints the existing state of the board.
**Example:**

    - - - O
    - - O X
    X O X -
    O X - -
