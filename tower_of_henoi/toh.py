from tower import *
from TowerOfHanoi import *
TOTAL_DISK = 4
def main(): 
    print('Starting the execution of the Towers of Henoi')

    toh = TowerOfHanoi(TOTAL_DISK)
    toh.run()
    print('Finished the execution of the Tower of Henoi')