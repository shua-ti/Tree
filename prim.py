#-*-coding=utf-8-*-
#/usr/bin/env python
"最小生成树p算法"

from heapq import heappop,heappush
N = {
    'a':{'a':float('inf'),'b':2,'c':float('inf'),'d':4,'e':5,'f':float('inf')},
    'b':{'a':2,'b':float('inf'),'c':4,'d':float('inf'),'e':10,'f':float('inf')},
    'c':{'a':float('inf'),'b':4,'c':float('inf'),'d':20,'e':6,'f':float('inf')},
    'd':{'a':4,'b':float('inf'),'c':20,'d':float('inf'),'e':float('inf'),'f':float('inf')},
    'e':{'a':5,'b':10,'c':6,'d':float('inf'),'e':float('inf'),'f':5,},
    'f':{'a':float('inf'),'b':float('inf'),'c':float('inf'),'d':float('inf'),'e':5,'f':float('inf')}
}
# 将节点分成两个集合 S1,S2
#(到达选定节点的距离，选定节点，选定节点的邻居节点)
# Q中存放着各个节点到S1集合各点的距离，heappop()选出距离最近的节点
def prim(G,s):
    P ,Q = {},[(0,None,s)]#自选定一起始节点
    idx=0
    while Q:
        _,p,u = heappop(Q)
        if u in P:continue#判断当前节点是否在选定节点集中
        P[u]=p
        idx+=1
        if idx==len(G):break
        for v,w in G[u].items():
            heappush(Q,(w,u,v))
    return P

if __name__=="__main__":
    print prim(N,'a')
