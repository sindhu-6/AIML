def aStarAlgo(start_node,stop_node):
    open_set={start_node}
    closed_set=set()
    g={}
    parents={}
    g[start_node]=0
    parents[start_node]=start_node
    while open_set:
        n=None
        for v in open_set:
            if n is None or g[v]+heuristic(v)<g[n]+heuristic(n):
                n=v
        print(f"\nEvaluating node:{n}(g:{g[n]},h:{heuristic(n)},f:{g[n]+heuristic(n)})")
        print(f"Open Set:{open_set}")
        print(f"Closed Set:{closed_set}")
        if n==stop_node:
            path=[]
            while parents[n]!=n:
                path.append(n)
                n=parents[n]
            path.append(start_node)
            path.reverse()
            print('Path Found:{}'.format(path))
            return path
        print(f"Exploring neighbors of {n}:")
        for(m,weight)in get_neighbors(n):
            h_m=heuristic(m)
            print(f"Neighbor:{m} with weight:{weight} and h({m}):{h_m}")
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m]=n
                g[m]=g[n]+weight
                print(f"Added {m} to open set with g({m})={g[m]} and f({m})={g[m]+h_m}")
            else:
                if g[m]>g[n]+weight:
                    g[m]=g[n]+weight
                    parents[m]=n
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)
                        print(f" Updated{m} to have a shorter path with g({m})={g[m]+h_m}")
            open_set.remove(n)
            closed_set.add(n)
    print("Path does not exist!")
    return None
    
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    return[]

def heuristic(n):
    H_dist={'S':5,'A':3,'B':4,'C':2,'D':6,'G':0}
    return H_dist.get(n,0)
Graph_nodes={'S':[('A',1),('G',10)],
             'A':[('B',2),('C',1)],
             'S':[('D',5)],
             'C':[('D',3),('G',4)],
             'D':[('G',2)],
             }
aStarAlgo('S','G')
