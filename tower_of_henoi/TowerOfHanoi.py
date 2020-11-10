from tower import *
from functions import *
class TowerOfHanoi:  
#constructor __init__
    def __init__(self, numDisc): 
        self.numDisc = numDisc
        self.n_move = 0
        self.prepare_towers()

    def prepare_towers(self): 
        Stack_A = Tower('Stack A', self.numDisc)
        Stack_B = Tower('Stack B')
        Stack_C = Tower('Stack C')

        self.towers = [Stack_A, Stack_B, Stack_C] 
#should add functions here 
    def run(self): 
        self.showtower()
        Stack_A, Stack_B, Stack_C = self.towers
        self.mdisk(Stack_A, Stack_B, Stack_C, self.numDisc)

    def mdisk(self, Stack_A, Stack_B, Stack_C, n): 
        if n <= 0: 
            return

        self.mdisk(Stack_A, Stack_C, Stack_B, n - 1)
        self.n_move += 1
        print('moved from {} to {}.'.format( Stack_A.name, Stack_B.name))
        disk = Stack_A.pop()
        Stack_B.push(disk)
        self.showtower()
        self.mdisk(Stack_C, Stack_B, Stack_A, n - 1)

    def showtower(self): 
        for tx in self.towers: 
            print(tx)