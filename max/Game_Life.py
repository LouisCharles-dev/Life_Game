import numpy as np
import time

class Game_Life:

    def __init__(self,grid):
        self.grid = np.pad(grid, 1, mode = 'constant')
        self.n = len(self.grid)

# """
# See if this generation of this cell is evolving
# """

    def generation(self,value,neig):
        # print('hit')
        if value == 1:
            # print('hit')
            if neig < 2:
                return False
            elif neig == 2 or neig == 3:
                # print("touch")
                return True
            elif neig > 3:
                return False

        else:

            if neig == 3:
                return True

# """
# Count the number of neighbour
# """

    def neighbour(self,value,row,column):
        m=0
        for i in range(3):
            for k in range(3):
                if 1 == self.grid[(row-1) + i][(column-1) + k]:
                    m += 1
        if self.grid[row][column] == 1:
            m-=1
        # print(m)
        return m

# """
# See if this generation of this cell is evolving
# """

    def test(self):

        neig = np.zeros((self.n - 2 , self.n - 2))

        for i in range(0,self.n - 2):
            for k in range(0,self.n - 2):
                v = self.grid[i][k]
                neig[i][k] = int(self.neighbour(v,i,k))
                # print(f"{i},{k},{v},{neig[i][k]}")


        for i in range(0,self.n - 2):
            for k in range(0,self.n - 2):

                if self.generation(self.grid[i][k],int(neig[i][k])):
                    self.grid[i][k] = 1
                else:
                    self.grid[i][k] = 0


        print(self.grid)
        time.sleep(0.1)
        # print(neig)
        self.test()



    # def retest(self):














        #
