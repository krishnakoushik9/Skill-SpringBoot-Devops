![[Pasted image 20250714142914.png]]
![[Pasted image 20250714163616.png]]
![[Pasted image 20250714164014.png]]
![[Pasted image 20250714170435.png]]
![[Pasted image 20250714170441.png]]
![[Pasted image 20250714170448.png]]

---
## Lets Deep Dive into the Code in C then
```
#include <stdio.h>
#include <limits.h>

#define V 6
#define INF INT_MAX

int main() {
    int graph[V][V] = {
        {0, 2, 4, 0, 0, 0},
        {0, 0, 3, 1, 5, 0},
        {0, 0, 0, 2, 0, 0},
        {0, 0, 0, 0, 1, 4},
        {0, 0, 0, 0, 0, 2},
        {0, 0, 0, 0, 0, 0}
    };

    int distance[V], visited[V] = {0}, parent[V];

    for (int node = 0; node < V; node++) {
        distance[node] = INF;
        parent[node] = -1;
    }
    distance[0] = 0;

    for (int step = 0; step < V - 1; step++) {
        int current = -1;
        int shortest = INF;

        for (int node = 0; node < V; node++) {
            if (!visited[node] && distance[node] < shortest) {
                shortest = distance[node];
                current = node;
            }
        }

        if (current == -1) break;
        visited[current] = 1;

        for (int neighbor = 0; neighbor < V; neighbor++) {
            if (graph[current][neighbor] && distance[current] + graph[current][neighbor] < distance[neighbor]) {
                distance[neighbor] = distance[current] + graph[current][neighbor];
                parent[neighbor] = current;
            }
        }
    }

    for (int target = 0; target < V; target++) {
        printf("Path to %c: ", 'A' + target);
        int path[10], index = 0, node = target;
        while (node != -1) {
            path[index++] = node;
            node = parent[node];
        }
        for (int i = index - 1; i >= 0; i--) {
            printf("%c", 'A' + path[i]);
            if (i != 0) printf(" -> ");
        }
        printf(" (Dist: %d)\n", distance[target]);
    }
}
```
![[Pasted image 20250714174718.png]]
