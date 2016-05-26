class SelfConjugatePartition:
    
    def __init__(self, partition):
        self.part = partition

    def conversion(self):
        con_part = []
        m = len(self.part)
        new_len = self.part[0]
        for i in range(new_len):
            con_part.append(1)
        for j in range(2,m+1):
            for i in range(1,self.part[j-1]+1):
                con_part[i-1] += 1
        return con_part
