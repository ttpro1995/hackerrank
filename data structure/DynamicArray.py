
class Container():
    def __init__(self, N):
        self.seq = []
        self.lastAnswer = 0
        for i in range(N):
            self.seq.append([])
    def solveQuery(self, t, x, y):
        t = int(t)
        x = int(x)
        y = int(y)
        if t == 1:
            # query 1 x y
            # find seq at index (x^lastAnswer)%N
            seqidx = (x^self.lastAnswer)%N
            self.seq[seqidx].append(y)
        elif t == 2:
            seqidx = (x^self.lastAnswer)%N
            size = len(self.seq[seqidx])
            idx = y%size
            l = self.seq[seqidx][idx]
            self.lastAnswer = l
            print (self.lastAnswer)

if __name__ == '__main__':
    x = raw_input()
    N, Q = x.split()
    N = int(N)
    Q = int(Q)
    obj = Container(N)
    for i in range(Q):
        t, x, y = raw_input().split()
        obj.solveQuery(t, x, y)
    
