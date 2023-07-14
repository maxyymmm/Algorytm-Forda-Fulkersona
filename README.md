# Algorytm-Forda-Fulkersona
Algorytm ten służy do znajdowania maksymalnego przepływu w sieci przepływowej, która jest skierowanym grafem z przypisanymi pojemnościami krawędzi.

Główne funkcje w tej implementacji to **bfs(G, s, t, parent, weight)** i **ford_fulkerson(G, s, t, weight)**.

**bfs(G, s, t, parent, weight)** to pomocnicza funkcja, która wykonuje przeszukiwanie wszerz **(BFS)** w celu znalezienia ścieżki od wierzchołka źródłowego **s** do wierzchołka ujściowego **t**. Przyjmuje ona następujące parametry:<br />
**G**: Słownik reprezentujący graf, gdzie klucze to wierzchołki, a wartości to listy sąsiednich wierzchołków.<br />
**s**: Wierzchołek źródłowy.<br />
**t**: Wierzchołek ujściowy.<br />
**parent**: Słownik służący do przechowywania rodzica dla każdego wierzchołka w przeszukiwaniu BFS.<br />
**weight**: Słownik reprezentujący pojemności krawędzi, gdzie klucze to krotki **(u, v)** reprezentujące krawędź między wierzchołkami **u** i **v**, a wartości to odpowiadające im pojemności.<br />
<br />
<br />
**ford_fulkerson(G, s, t, weight)** to główna funkcja implementująca algorytm Forda-Fulkersona. Przyjmuje ona następujące parametry:<br />
**G**: Słownik reprezentujący graf.<br />
**s**: Wierzchołek źródłowy.<br />
**t**: Wierzchołek ujściowy.<br />
**weight**: Słownik reprezentujący pojemności krawędzi.<br />
<br />
<br />
Algorytm działa w następujący sposób:<br />
1) Inicjalizuje słownik **parent** do przechowywania rodzica dla każdego wierzchołka w ścieżkach powiększających i ustawia maksymalny przepływ **max_flow** na 0.<br />
2) Powtarza wywołania funkcji **bfs**, aby znaleźć ścieżkę powiększającą od wierzchołka źródłowego **s** do wierzchołka ujściowego **t**.<br />
3) Jeśli nie ma ścieżki powiększającej, algorytm kończy działanie i zwraca maksymalny przepływ oraz ścieżki.<br />
4) Jeśli znaleziono ścieżkę powiększającą, oblicza maksymalny przepływ, który może być przesłany przez tę ścieżkę, znajdując minimalną pojemność wzdłuż ścieżki.<br />
5) Aktualizuje przepływ wzdłuż ścieżki, odejmując przepływ od krawędzi przekierowanych i dodając przepływ do krawędzi zwrotnych.<br />
6) Aktualizuje maksymalny przepływ, dodając przepływ bieżącej ścieżki.<br />
7) Przechowuje bieżącą ścieżkę i jej maksymalny przepływ w słowniku **paths**.<br />
8) Kroki 2-7 są powtarzane, dopóki nie można znaleźć kolejnej ścieżki powiększającej.<br />
<br />
<br />
W podanym przykładzie algorytm jest zastosowany do grafu **G** z odpowiadającymi mu pojemnościami krawędzi **weight**, rozpoczynając od wierzchołka źródłowego **S** i kończąc na wierzchołku ujściowym **T**. Maksymalny przepływ oraz ścieżki wraz z ich maksymalnym przepływem są wyświetlane.
![f1](https://github.com/maxyymmm/Algorytm-Forda-Fulkersona/assets/120425774/02d1a76f-9442-417e-bfc6-991f15f12a00)
![f2](https://github.com/maxyymmm/Algorytm-Forda-Fulkersona/assets/120425774/52bf4f9b-0ceb-4e38-8e3c-82fd43264e1a)

