class board:
    
    def __init__(self,bdim):
        bd=[]
        self.bdim=bdim
        for i in range(0,bdim): bd.append(['-']*bdim)
        self.brd=bd

    def checkDraw(self):
        for i in self.brd:
            if '-' in i:
                return 1
        return 0

    def checkTerm(self):
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
                return ini
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
                return ini
        #checkDiagonals
        score=0
        ini = self.brd[0][0]
        if ini != '-':
            for i in range(0,self.bdim):
                if ini == self.brd[i][i]:
                    score = score+1
        if score == self.bdim:
            return ini

        score=0
        ini = self.brd[0][self.bdim-1]
        if ini != '-':
            for i in range(0,self.bdim):
                if ini == self.brd[i][self.bdim-i-1]:
                    score = score+1
        if score == self.bdim:
            return ini
        if self.checkDraw() == 1:
            return -1
        else:
            return -2

    def step(self,plyID,x,y):
        if self.brd[x][y] == '-':
            self.brd[x][y] = plyID
            r = self.checkTerm()
            return r,self.brd

    def printState(self):
        for i in self.brd:
            print(i)