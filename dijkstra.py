from collections import defaultdict

topo3 = {    1: {1: 0,  2: 133, 3:float('inf'), 4: 64, 5:float('inf')},
             2: {1: 133, 2 : 0, 3: float('inf'), 4: float('inf'), 5: 64},
             3: {1: float('inf'), 2 : float('inf'), 3 : 0, 4 : 64, 5: 133},
             4: {1: 64, 2 : float('inf'), 3: 64, 4 : 0, 5: float('inf')},
             5: {1: float('inf'), 2: 64, 3: 133, 4: float('inf'), 5:0}
         }

topo1 = {
            1 : { 1: 0, 2: 10, 3: float('inf'), 4: float('inf'), 5 : float('inf'), 6: float('inf'),7: 64, 8 : 133, 9 : float('inf'), 10 : float('inf')},
            2 : { 1 : 10, 2 : 0, 3: 10, 4: float('inf'), 5: float('inf'), 6:  133, 7: 133, 8 : float('inf'), 9: float('inf'), 10 : float('inf')},
            3 : { 1 : float('inf'), 2: 10, 3: 0, 4: 64, 5: 64, 6: float('inf'), 7: float('inf'), 8 : float('inf'), 9 : float('inf'), 10 : float('inf')},
            4 : { 1 : float('inf'), 2: float('inf'), 3: 64, 4: 0, 5: 133, 6: 10, 7: float('inf'), 8 : float('inf'), 9 : float('inf'), 10 : float('inf')},
            5 : { 1 : float('inf'), 2: float('inf'), 3: 64, 4: 133, 5: 0, 6: float('inf'), 7 : float('inf'), 8 : float('inf'), 9 : float('inf'), 10 : 10},
            6 : { 1 : float('inf'), 2: 133, 3: float('inf'), 4: 10, 5: float('inf'), 6:  0, 7 : 64, 8 : float('inf'), 9 : float('inf'), 10 : float('inf')},
            7 : { 1 : 64, 2: 133, 3: float('inf'), 4: float('inf'), 5: float('inf'), 6: 64, 7 : 0, 8: 133, 9: 64, 10 : float('inf')},
            8 : { 1 : 133, 2: float('inf'), 3: float('inf'), 4: float('inf'), 5: float('inf'), 6: float('inf'), 7: 133, 8: 0, 9 : 64, 10 : float('inf')},
            9 : { 1 : float('inf'), 2: float('inf'), 3: float('inf'), 4: float('inf'), 5: float('inf'), 6: float('inf'), 7: 64, 8: 133, 9 : 0, 10: float('inf')},
            10: { 1 : float('inf'), 2: float('inf'), 3: float('inf'), 4: float('inf'), 5: 10, 6: float('inf'), 7 : float('inf'), 8 : float('inf'), 9 : float('inf'), 10 : 0}
        }

topo2 = {
            1 : { 1 : 0, 2: float('inf'), 3 : float('inf'), 4 : float('inf'), 5: 64, 6: 133, 7 : float('inf')},
            2 : { 1 : float('inf'), 2: 0, 3 : float('inf'), 4 : float('inf'),5: 64, 6 : float('inf'), 7: 133},
            3 : { 1 : float('inf'), 2: float('inf'), 3 : 0, 4: 133, 5 : float('inf'), 6: 64, 7: 10},
            4 : { 1 : float('inf'), 2 : float('inf'), 3: 133, 4 : 0, 5 : float('inf'), 6 : float('inf'), 7: 133},
            5 : { 1 : 64, 2: 64, 3 : float('inf'), 4 : float('inf'), 5 : 0, 6 : float('inf'), 7 : float('inf')},
            6 : { 1 : 133, 2 : float('inf'), 3: 64, 4 : float('inf'), 5 : float('inf'), 6 : 0, 7 : float('inf')},
            7 : { 1 : float('inf'), 2: 133, 3: 10, 4: 133, 5 : float('inf'), 6 : float('inf'), 7 : 0}
        }



adjacency=defaultdict(lambda:defaultdict(lambda:None))
switch=set(topo3)

def minimum_distance(Q, distance):
    min = float('inf')
    node = 0
    for v in Q:
        if distance[v] < min:
            min = distance[v]
            node = v
    return node

def dijkstra (graf, src, dst):
    Q=set(graf)
    distance = {}
    previous = {}


    for i in Q:
        distance[i] = float('Inf')
        previous[i] = None

    #Q.remove(src)
    distance[src]=0

    while len(Q)>0:
        u = minimum_distance(Q, distance)
        Q.remove(u)

        for p in Q:
          if graf[u][p] =! float('inf') #it means they're directly connected
            if distance[p] > distance[u] + graf[u][p]:
                distance[p] = distance[u] + graf[u][p]
                previous[p] = u
                #print "u: ",u, "p: ",p,"dist[u][p]",distance[u][p], "Q: ",Q,"dist G-u",G[src][u],"G u-p",G[u][p]
    r=[]
    p=dst
    r.append(p)
    q=previous[p]
    while q is not None:
        if q == src:
            r.append(q)
            break
        p=q
        r.append(p)
        q=previous[p]
    r.reverse()
    if src==dst:
        path=[src]
        distance[src]= graf[src][dst]
    else:
        path=r

    print "shortest path from ",src, "to ",dst, ": ",path, "cost= ",distance[dst]


def main():
    for src in switch:
        for dst in switch:
            dijkstra(topo3, src,dst)


if __name__ == "__main__":
    main()
