#-*-coding=utf-8-*-
#/usr/bin/env python
from itertools import count
from heapq import heapify,heappush,heappop

def huffman(seq,frq):
    num = count()        #生成无限迭代器 1,2,3,....
    trees = list(zip(frq,num,seq))#zip()连接多个可迭代对象[(),(),()]
    heapify(trees)
    while len(trees)>1:
        fa,_,a = heappop(trees) #权值较小的两个节点
        fb,_,b = heappop(trees)
        n =next(num)
        heappush(trees,(fa+fb,n,[a,b]))#通过列表的嵌套表示树结构，生成新的节点
    return trees[0][-1]

def codes(tree,prefix=""):
    if len(tree)==1:              #递归基
        yield (tree,prefix)
        return
    for bit,child in zip("01",tree):
        for pair in codes(child,prefix+bit):
            yield pair

if __name__=="__main__":
    seq="abcdefghi"
    frq=[4,5,6,9,11,12,15,16,20]
    tree=huffman(seq,frq)
    print list(codes(tree))