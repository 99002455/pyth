class Tower: 
    def __init__(self, name, numDiscs = 0): 
        self.name = name
        self.disks = []
        for i in range(numDiscs, 0, -1): 
            self.push(str(i))
# Add push function --Koushik
    def push(self, disk): 
        self.disks.append(disk)
# Add pop function --Aman
    def pop(self): 
        return self.disks.pop()
# Declaration and representation of the object as a string --Aditya
    def __str__(self): 
        disks = ''.join('{:<2}'.format(d) for d in self.disks)
        return '{}: {}'.format(self.name, disks)