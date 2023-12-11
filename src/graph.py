from utilities import *
from itertools import combinations
from pyvis.network import Network


class Graph:
    show_count = 0  # Class-level variable to keep track of show calls

    def __init__(self, num_of_vertices, num_of_edges, edges, vertices=None):
        self.num_of_vertices = num_of_vertices
        self.num_of_edges = num_of_edges
        self.vertices = set(str(i) for i in range(num_of_vertices)) if vertices is None else vertices
        self.edges = set((str(u), str(v)) for u, v in edges)
        self.adjacency_list = {str(vertex): set() for vertex in self.vertices}
        for edge in self.edges:
            u, v = edge
            self.adjacency_list[u].add(v)
            self.adjacency_list[v].add(u)
            
    def bfs_levels(self, source):
        source = str(source)
        if source not in self.vertices:
            raise ValueError(f"Vertex {source} is not in the graph")

        visited = {vertex: False for vertex in self.vertices}
        level = {vertex: None for vertex in self.vertices}
        queue = []

        # Start from the source
        visited[source] = True
        level[source] = 0
        queue.append(source)

        levels = {}

        while queue:
            vertex = queue.pop(0)
            current_level = level[vertex]

            if current_level not in levels:
                levels[current_level] = set()
            levels[current_level].add(vertex)

            for neighbor in self.adjacency_list[vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    level[neighbor] = current_level + 1

        return levels
    
   

    def delete_vertices(self, vertices_to_delete):
        """
        Delete a set of vertices from the graph.
        
        :param vertices_to_delete: set of vertices to delete
        :return: A new Graph instance with the vertices deleted.
        """
        new_vertices = set(self.vertices - vertices_to_delete)
        print('new_vertices:', new_vertices)
        new_edges = set(
            e for e in self.edges if e[0] not in vertices_to_delete and e[1] not in vertices_to_delete)  # TODO
        print("new_edges:", new_edges)
        return Graph(len(new_vertices), len(new_edges), new_edges, new_vertices)

    def edge_exists(self, u, v):
        return (u, v) in self.edges or (v, u) in self.edges

    def copy(self):
        return Graph(self.num_of_vertices, self.num_of_edges, self.edges, self.vertices)

    def show(self, graph_name='graph'):
        Graph.show_count += 1
        print("Showing graph:", Graph.show_count)
        net = Network(height="500px", width="100%", bgcolor="#222222", font_color="white")

        for vertex in self.vertices:
            net.add_node(vertex)

        for edge in self.edges:
            u, v = edge
            net.add_edge(u, v, color="white")

        file_name = f"../output-graphs/{graph_name}-{Graph.show_count}.html"
        net.show(file_name)
