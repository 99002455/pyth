from toh import *
from tower import *
from TowerOfHanoi import *
import time
def run(self): 
    self.showtower()
    Stack_A, Stack_B, Stack_C = self.towers
    self.mdisk(Stack_A, Stack_B, Stack_C, self.numDisc)

def mdisk(self, Stack_A, Stack_B, Stack_C, n): 
    if n <= 0: 
        return
    self.mdisk(Stack_A, Stack_B, Stack_C, n - 1)
    self.n_move += 1
    time.sleep(2)
    print('moving  from {} to {}.'.format(Stack_A.name, Stack_B.name))
    disk = Stack_A.pop()
    Stack_B.push(disk)
    self.showtower()
    self.mdisk(Stack_C, Stack_B, Stack_A, n - 1)

def showtower(self): 
    for tower  in self.towers: 
        print(tower)
