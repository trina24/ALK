class PartitionGenerator(object):

    def __init__(self, n):
        self.n = n
        self.partitions = []
        self.temp_part = [None for i in range(n)]

    def part(self, n, b, m):
        if (n == 0):
            temp = self.prepare_partition(m)
            self.partitions.append(temp)
        else:
            for i in range(1,min(b,n)+1):
                self.temp_part[m] = i
                self.part(n-i,i,m+1)

    def prepare_partition(self, m):
        return self.temp_part[:m]

    def generate_partitions(self):
        if (self.n == 0):
            return [[0]]
        else:
            self.part(self.n,self.n,0)
            return self.partitions
