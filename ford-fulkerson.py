def bfs(G, s, t, parent, weight):
    visited  = {vertex: False for vertex in G}

    queue = []
    queue.append(s)

    visited [s] = True

    while queue:
        node = queue.pop(0) #wyrzucanie 1 elem

        for neighbor in G[node]:
            if not visited [neighbor] and (node, neighbor) in weight and weight[(node, neighbor)] > 0:
                queue.append(neighbor)
                visited [neighbor] = True
                parent[neighbor] = node

    return True if visited [t] else False

def ford_fulkerson(G, s, t, weight):
    parent = {vertex: None for vertex in G}
    max_flow = 0
    paths = {}

    while bfs(G, s, t, parent, weight): #dopóki jest połącznie start-koniec
        path_flow = float("inf")
        w = t
        path = []  # lista na wierxxchołki

        # znajdź min wartość w ścieżce = maksymalna wartosc jaka mozemy przeslac tą ściażką
        while w != s:
            u = parent[w]
            path_flow = min(path_flow, weight[(u, w)])
            path.append(w)
            w = u

        path.append(s)  # dodaj wierzchołek źródłowy do ścieżki
        path.reverse()  # odwrócnie ścieżki, żebyt zaczynało się od wierzchołka start

        # + lub - przepływ w zależności od kierunku w ścieżce
        for i in range(len(path) - 1):
            u = path[i]
            v = path[i + 1]
            weight[(u, v)] -= path_flow
            if (v, u) in weight:
                weight[(v, u)] += path_flow
            else:
                weight[(v, u)] = path_flow
                G[v].append(u)  # dodaj krawędź zwrotną

        max_flow += path_flow
        paths[tuple(path)] = path_flow #append każdej z ścieżek

    return max_flow, path

if __name__ == "__main__":
    # graf
    G = {'S': ['A', 'E'], 'A': ['E', 'B'], 'B': ['T','E'], 'T': [], 'D': ['T', 'B'], 'E': ['D', 'A']}
    weight = {('S', 'A'): 16, ('S', 'E'): 13, ('A', 'E'): 10, ('A', 'B'): 12, ('B', 'T'): 20, ('B', 'E'): 9, ('D', 'T'): 4, ('D', 'B'): 7, ('E', 'D'): 14,('E', 'A'): 4 }
    s = 'S'  # start
    t = 'T'  # koniec

    max_flow, path = ford_fulkerson(G, s, t, weight)
    print("Maksymalny przepływ:", max_flow)
    print("Ścieżki (od punktu start do punktu koniec: MAX przepływ tej ścieżki)", path)