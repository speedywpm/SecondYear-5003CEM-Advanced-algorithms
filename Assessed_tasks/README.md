# Graph Algorithms Repository

This repository contains implementations of various graph **algorithms and data structures**, divided into two categories: **Standard** and **Advanced**. The code is in **Python**, and each file is labeled with a prefix: `STD` for Standard and `ADV` for Advanced.

## Table of Contents

* Standard
  - STD_1.py
  - STD_2.py
  - STD_3.py
  - STD_4.py
  - STD_5.py
* Advanced
  - ADV_1.py
  - ADV_2.py
  - ADV_3.py
* Conclusion

# Standard

The Standard section includes basic graph algorithms and data structures, such as:

1. **Adjacency Matrix**: A simple implementation of an adjacency matrix, allowing the user to interactively add vertices, add edges, remove edges, and display the matrix.
2. **Prim's Algorithm**: An implementation of Prim's Algorithm for finding the minimum spanning tree of a connected, undirected graph with weighted edges.
3. **Linked List**: A basic implementation of a singly linked list, including methods to insert nodes at the beginning, end, or after a specific node.

## STD_1.py

### Graph Data Structure

This file implements a simple Graph data structure that can store vertices and edges. The graph is represented using an adjacency list.

**Key Functions:**

* `addVertex(self, vertex)`: Adds a vertex to the graph.
* `addEdge(self, vertex1, vertex2)`: Adds an edge between two vertices.

## STD_2.py

### Breadth-First Search

This file demonstrates the Breadth-First Search (BFS) algorithm on a given graph. The BFS algorithm visits all the vertices of a graph in a breadthward motion, exploring all the neighbors of a vertex before moving on to the next level.

**Key Functions:**

`bfs(self, start_vertex)`: Performs Breadth-First Search starting from a given vertex.

## STD_3.py

### Adjacency Matrix

This file implements an adjacency matrix representation of a graph with additional user-interactive options. Users can add vertices, add edges (while checking for existing edges), remove edges (while checking for non-existing edges), and display the matrix.

**Key Classes and Functions:**

* `class Graph`: The main class representing the adjacency matrix.
  - `__init__(self, size)`: Initializes the matrix.
  - `addvertex(self, vert1)`: Adds vertices to the graph.
  - `addedge(self, vertx2, verty2)`: Adds an edge between two vertices.
  - `remove_edge(self, vertxx, vertyy)`: Removes an edge between two vertices.
  - `printmatrix(self)`: Displays the matrix.
  - `matrixselector(self)`: Allows the user to interact with the graph.

## STD_4.py

### Prim's Algorithm

This file implements Prim's Algorithm for finding the Minimum Spanning Tree (MST) of a connected, undirected graph. The algorithm works by incrementally building the MST, always choosing the edge with the minimum weight that connects a vertex in the MST to a vertex outside of it.

**Key Classes and Functions:**

* `class Graph`: The main class representing the graph.
  - `__init__(self, vertices)`: Initializes the graph as an adjacency matrix.
  - `printMST(self, parent)`: Prints the MST.
  - `minKey(self, key, mstSet)`: Finds the unreached node with the minimum cost.
  - `primMST(self)`: Computes the MST using Prim's Algorithm.

## STD_5.py

### Linked List

This file implements a singly linked list data structure. A linked list consists of nodes where each node contains a data field and a reference to the next node in the sequence.

**Key Classes and Functions:**

* `class Node`: Represents a node in the linked list.
* `__init__(self, dataval=None)`: Initializes a node with a given data value and a reference to the next node.
* `class SLinkedList`: Represents a singly linked list.
  - `__init__(self)`: Initializes an empty linked list with a head value set to None.
  - `listprint(self)`: Prints the linked list.
  - `AtBeginning(self, newdata)`: Adds a new node with the given data value at the beginning of the list.
  - `AtEnd(self, newdata)`: Adds a new node with the given data value at the end of the list.
  - `Insert(self, val_before, newdata)`: Inserts a new node with the given data value after the specified existing node in the list.

# Advanced

The Advanced section covers more complex graph algorithms, such as:

1. **Adjacency List**: An implementation of an adjacency list for an undirected graph, with functionality to add vertices, add edges, remove edges, and display the list.
2. **Dijkstra's Algorithm**: An implementation of Dijkstra's Algorithm for finding the shortest path from a source vertex to all other vertices in a weighted graph.

## ADV_1.py

### Dijkstra's Algorithm

This file implements Dijkstra's Algorithm for finding the shortest path between a source node and all other nodes in a weighted graph. The algorithm works by iteratively selecting the vertex with the smallest known distance from the source and updating its neighboring vertices' distances.

**Key Classes and Functions:**

* `class Graph`: The main class representing the graph.
  - `__init__(self, vertices)`: Initializes the graph as an adjacency matrix.
  - `printSolution(self, dist)`: Prints the shortest path distances.
  - `minDistance(self, dist, sptSet)`: Finds the vertex with the minimum distance value.
  - `dijkstra(self, src)`: Computes the shortest paths using Dijkstra's Algorithm.

## ADV_2.py

### Kruskal's Algorithm

This file implements Kruskal's Algorithm for finding the Minimum Spanning Tree (MST) of a connected, undirected graph. The algorithm works by sorting all the edges by their weights and iteratively adding the next smallest edge that does not form a cycle with the MST.

**Key Classes and Functions:**

* `class Graph`: The main class representing the graph.
  - `__init__(self, vertices)`: Initializes the graph.
  - `addEdge(self, u, v, w)`: Adds an edge between two vertices with a given weight.
  - `find(self, parent, i)`: Finds the set of an element i.
  - `union(self, parent, rank, x, y)`: Unites two sets x and y.
  - `KruskalMST(self)`: Computes the MST using Kruskal's Algorithm.

## ADV_3.py

### Bellman-Ford Algorithm

This file implements the Bellman-Ford Algorithm for finding the shortest path between a source node and all other nodes in a weighted graph. The algorithm iteratively updates the distances of all vertices, relaxing each edge |V|-1 times, where |V| is the number of vertices in the graph. The algorithm is capable of handling negative weight edges but not negative weight cycles.

**Key Classes and Functions:**

* `class Graph`: The main class representing the graph.
  - `__init__(self, vertices)`: Initializes the graph with a given number of vertices.
  - `addEdge(self, u, v, w)`: Adds an edge between two vertices with a given weight.
  - `printArr(self, dist)`: Prints the shortest path distances.
  - `BellmanFord(self, src)`: Computes the shortest paths using the Bellman-Ford Algorithm.

# Conclusion

These **algorithms and data structures** provide a **solid foundation** for working with graphs in **Python**. They can be easily adapted and extended to solve a wide range of graph-related problems. The repository includes comprehensive documentation and examples for each file, making it easy to understand and use these algorithms in your own projects.

