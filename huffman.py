
#/usr/bin/env python
from itertools import count
from heapq import heapify,heappush,heappop
def huffman(seq,freq):
    num = count()
    trees = list(zip(frq,num,seq))
    heapify(trees)
    while len(trees)>1:
        fa,_,a = heappop(trees)
        fb,_,b = heappop(trees)
        n =next(num)
        heappush(trees,(fa+fb,n,[a,b]))
    return trees[0][-1]

if __name__=="__main__":
    seq="abcdefghi"
    frq=[4,5,6,9,11,12,15,16,20]
    print huffman(seq,frq)