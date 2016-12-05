#-*-coding=utf-8-*-
#/usr/bin/env python
"最小生成树k算法"
N = {
    'a':{'a':float('inf'),'b':2,'c':1,'d':3,'e':9,'f':4,'g':float('inf'),'h':float('inf')},
    'b':{'a':float('inf'),'b':float('inf'),'c':4,'d':float('inf'),'e':3,'f':float('inf'),'g':float('inf'),'h':float('inf')},
    'c':{'a':float('inf'),'b':float('inf'),'c':float('inf'),'d':8,'e':float('inf'),'f':float('inf'),'g':float('inf'),'h':float('inf')},
    'd':{'a':float('inf'),'b':float('inf'),'c':float('inf'),'d':float('inf'),'e':7,'f':float('inf'),'g':float('inf'),'h':float('inf')},
    'e':{'a':float('inf'),'b':float('inf'),'c':float('inf'),'d':float('inf'),'e':float('inf'),'f':5,'g':float('inf'),'h':float('inf')},
    'f':{'a':float('inf'),'b':float('inf'),'c':2,'d':float('inf'),'e':float('inf'),'f':float('inf'),'g':2,'h':2},
    'g':{'a':float('inf'),'b':float('inf'),'c':float('inf'),'d':float('inf'),'e':float('inf'),'f':1,'g':float('inf'),'h':6},
    'h':{'a':float('inf'),'b':float('inf'),'c':float('inf'),'d':float('inf'),'e':float('inf'),'f':9,'g':8,'h':float('inf')}
}
def find(C,u):
    if C[u]!=u:
        C[u]=find(C,C[u])
    return C[u]

def union(C,R,u,v):
    u=find(C,u);v=find(C,v)
    if R[u] > R[v]:
        C[v]=u
    else:
        C[u]=v
    if R[u]==R[v]:
        R[v]+=1

def Kruskal(G):
    E = [(G[u][v],u,v) for u in G for v in G]   #（权值,u,v）
    T = set()
    C,R = {u:u for u in G},{u:0 for u in G}
    for _,u,v in sorted(E):
        if find(C,u) != find(C,v):
            T.add((u,v))
            union(C,R,u,v)
    return T

if __name__=="__main__":
    print Kruskal(N)
