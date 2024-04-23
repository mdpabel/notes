---
title: Graph Data Structure
description: Implementations of graph data structures in Java
date: 03-24-2024
isPublished: false
priority: 1
---

In the Graph class, member variables such as nodes and adjacencyList are utilized to represent key aspects of the graph's structure. The nodes map, for instance, serves as a repository for the graph's nodes, with each node uniquely identified by its label. Similarly, the adjacencyList map embodies the essence of the graph's connectivity, mapping each node to its corresponding list of adjacent nodes

#### addNode()

The addNode() method creates a new node with the provided label and adds it to the nodes map if it doesn't already exist. Then, it initializes an empty adjacency list for the node in the adjacencyList map if it's not already present.

#### removeNode()

The removeNode() method removes a node from the graph along with its connections. It removes connections to the node from other nodes in the adjacency list, removes the node itself from the adjacency list, and finally removes the node from the nodes map.

#### addEdge()

The addEdge() method adds an edge between two nodes in the graph. It retrieves the corresponding nodes from the nodes map, ensures they are valid nodes, and then adds the second node to the adjacency list of the first node.

#### removeEdge()

The removeEdge() method removes an edge between two nodes in the graph. It retrieves the corresponding nodes from the nodes map, ensures they are valid nodes, and then removes the second node from the adjacency list of the first node.

#### dfs()

The dfs() method performs Depth-First Search (DFS) traversal starting from a given root node. It retrieves the node from the nodes map, ensures it's a valid node, and then calls the dfsHelper() method to perform the actual DFS traversal.

#### dfsHelper()

The dfsHelper() method is a helper method for recursive DFS traversal. It recursively explores the neighbors of a given node and marks them as visited, ensuring that each node is visited only once.

#### bfs()

The bfs() method performs Breadth-First Search (BFS) traversal starting from a given root node. It retrieves the node from the nodes map, ensures it's a valid node, and then uses a queue to visit all nodes in the graph level by level.

#### topologicalSort()

The topologicalSort() method performs topological sorting of the graph using Depth-First Search (DFS). It initializes a stack to store the sorted nodes and then calls the topologicalSortHelper() method for each node in the graph.

#### topologicalSortHelper()

The topologicalSortHelper() method is a helper method for topological sorting. It recursively explores the neighbors of a given node and adds the node to a stack after visiting all its neighbors, ensuring that nodes are added to the stack in topological order.

#### hasCycle()

The hasCycle() method detects cycles in the graph using Depth-First Search (DFS). It initializes sets to keep track of all nodes, currently visiting nodes, and visited nodes. Then, it iterates through all nodes in the graph and calls the hasCycleHelper() method for each unvisited node.

#### hasCycleHelper()

The hasCycleHelper() method is a helper method to detect cycles. It recursively explores the neighbors of a given node and checks for back edges, indicating the presence of a cycle in the graph.

```java
package graph;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;
import java.util.Stack;

public class Graph {

  // Internal class representing a Node in the graph
  private class Node {
    String label;

    public Node(String label) {
      this.label = label;
    }

    @Override
    public String toString() {
      return label;
    }
  }

  // Map to store nodes with their labels as keys
  private Map<String, Node> nodes = new HashMap<>();

  // Map to represent the adjacency list of each node in the graph
  private Map<Node, List<Node>> adjacencyList = new HashMap<>();

  // Method to add a node to the graph
  public void addNode(String label) {
    var node = new Node(label);
    nodes.putIfAbsent(label, node);
    adjacencyList.putIfAbsent(node, new ArrayList<>());
  }

  // Method to remove a node from the graph
  public void removeNode(String label) {
    var node = nodes.get(label);
    if (node == null)
      return;

    // Remove connections to the node
    for (var n : adjacencyList.keySet()) {
      adjacencyList.get(n).remove(node);
    }
    adjacencyList.remove(node);
    nodes.remove(label);
  }

  // Method to add an edge between two nodes in the graph
  public void addEdge(String from, String to) {
    var fromNode = nodes.get(from);
    var toNode = nodes.get(to);
    if (fromNode == null || toNode == null || from.equals(to))
      throw new IllegalArgumentException();

    adjacencyList.get(fromNode).add(toNode);
  }

  // Method to remove an edge between two nodes in the graph
  public void removeEdge(String from, String to) {
    var fromNode = nodes.get(from);
    var toNode = nodes.get(to);
    if (fromNode == null || toNode == null)
      return;

    adjacencyList.get(fromNode).remove(toNode);
  }

  // Depth-First Search traversal starting from a given root node
  public void dfs(String root) {
    var node = nodes.get(root);
    if (node == null)
      return;

    dfsHelper(node, new HashSet<>());
  }

  // Iterative Depth-First Search traversal starting from a given root node
  public void dfs(String root, boolean iterative) {
    var node = nodes.get(root);
    if (node == null)
      return;

    Set<Node> visited = new HashSet<>();
    Stack<Node> stack = new Stack<>();
    stack.push(node);

    while (!stack.isEmpty()) {
      var currentNode = stack.pop();

      if (visited.contains(currentNode))
        continue;

      System.out.println(currentNode);
      visited.add(currentNode);

      for (var neighbour : adjacencyList.get(currentNode)) {
        if (!visited.contains(neighbour)) {
          stack.push(neighbour);
        }
      }
    }
  }

  // Helper method for recursive Depth-First Search traversal
  private void dfsHelper(Node root, Set<Node> visited) {
    var edges = adjacencyList.get(root);

    System.out.println(root);
    visited.add(root);

    for (var node : edges) {
      if (!visited.contains(node)) {
        dfsHelper(node, visited);
      }
    }
  }

  // Breadth-First Search traversal starting from a given root node
  public void bfs(String root) {
    var node = nodes.get(root);
    if (node == null)
      return;

    Set<Node> visited = new HashSet<>();

    Queue<Node> queue = new ArrayDeque<>();
    queue.add(node);

    while (!queue.isEmpty()) {
      var currentNode = queue.remove();

      if (visited.contains(currentNode))
        continue;

      System.out.println(currentNode);
      visited.add(currentNode);

      for (var neighbour : adjacencyList.get(currentNode)) {
        if (!visited.contains(neighbour))
          queue.add(neighbour);
      }
    }
  }

  // Topological sorting of the graph
  public void topologicalSort() {
    Stack<Node> stack = new Stack<>();
    Set<Node> visited = new HashSet<>();

    for (var node : nodes.values()) {
      if (!visited.contains(node))
        topologicalSortHelper(node, visited, stack);
    }

    while (!stack.empty()) {
      System.out.println(stack.pop());
    }
  }

  // Helper method for topological sorting
  private void topologicalSortHelper(Node node, Set<Node> visited, Stack<Node> stack) {
    if (visited.contains(node))
      return;

    visited.add(node);

    for (var neighbour : adjacencyList.get(node)) {
      topologicalSortHelper(neighbour, visited, stack);
    }

    stack.push(node);
  }

  // Method to detect cycles in the graph
  public boolean hasCycle() {
    Set<Node> all = new HashSet<>(nodes.values());
    Set<Node> visiting = new HashSet<>();
    Set<Node> visited = new HashSet<>();

    while (!all.isEmpty()) {
      var node = all.iterator().next();
      if (hasCycleHelper(node, all, visiting, visited))
        return true;
    }

    return false;
  }

  // Helper method to detect cycles
  private boolean hasCycleHelper(Node node, Set<Node> all, Set<Node> visiting, Set<Node> visited) {
    all.remove(node);
    visiting.add(node);

    for (var neighbour : adjacencyList.get(node)) {
      if (visited.contains(neighbour))
        continue;

      if (visiting.contains(neighbour))
        return true;

      if (hasCycleHelper(neighbour, all, visiting, visited))
        return true;
    }

    visiting.remove(node);
    visited.add(node);

    return false;
  }

  // Method to print the graph
  public void print() {
    for (var vertex : adjacencyList.keySet()) {
      var connectedTo = adjacencyList.get(vertex);
      if (!connectedTo.isEmpty()) {
        System.out.println(vertex + " is connected to " + connectedTo);
      }
    }
  }

}
```
