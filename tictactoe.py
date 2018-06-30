class board:

    def __init__(self,bdim):
        bd=[]
        self.bdim=bdim
        for i in range(0,bdim): bd.append(['-']*bdim)
        self.brd=bd

    def printState(self):
        for i in range(0,self.bdim):
            print(' '.join(self.brd[i]))

    def getState(self):
        return(self.brd)

    def put(self,plyID,x,y):
        if plyID == 1:
            self.brd[x][y]='X'
        elif plyID == 0:
            self.brd[x][y]='O'

    def checkWin(self):
        #checkRow
        for x in range(0,self.bdim):
            score = 0
            ini = self.brd[x][0]
            if ini == '-':
                continue
            for y in range(0,self.bdim):
                if self.brd[x][y] == ini:
                    score = score+1
            if score == self.bdim:
                return 1,ini
        #checkColumn
        for y in range(0,self.bdim):
            score = 0
            ini = self.brd[0][y]
            if ini == '-':
                continue
            for x in range(0,self.bdim):
                if self.brd[x][y] == ini:
                    score = score+1
            if score == self.bdim:
                return 1,ini
        #checkDiagonals
        score=0
        ini = self.brd[0][0]
        if ini != '-':
            for i in range(0,self.bdim):
                if ini == self.brd[i][i]:
                    score = score+1
        if score == self.bdim:
            return 1,ini

        score=0
        ini = self.brd[0][self.bdim-1]
        if ini != '-':
            for i in range(0,self.bdim):
                if ini == self.brd[i][self.bdim-i-1]:
                    score = score+1
        if score == self.bdim:
            return 1,ini
       
        return -1,0
       
       
    def resetBoard(self):
        bdim = self.bdim
        bd = []
        for i in range(0,bdim): bd.append(['-']*bdim)
        self.brd=bd