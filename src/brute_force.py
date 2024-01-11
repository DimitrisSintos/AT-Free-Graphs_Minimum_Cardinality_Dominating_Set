from graph import Graph

class BruteForce:
    def __init__(self, graph: Graph):
        self.graph = graph
        
    def is_domination_set(self, vertices_set):
        dominated = set(vertices_set)
        for vertex in vertices_set:
            dominated.update(self.graph.adjacency_list[vertex])
        return dominated == self.graph.vertices

    def minimum_domination_set(self):
        min_size = self.graph.num_of_vertices  # Start with the largest possible size
        min_domination_set = set()
        for i in range(1, 2 ** self.graph.num_of_vertices):
            subset = set()
            for j in range(self.graph.num_of_vertices):
                if i & (1 << j):
                    subset.add(str(j))
            if self.is_domination_set(subset):
                min_size = min(min_size, len(subset))
                if min_size == len(subset):
                    min_domination_set = subset
                
        return min_domination_set
    
    def run(self):
        return self.minimum_domination_set()