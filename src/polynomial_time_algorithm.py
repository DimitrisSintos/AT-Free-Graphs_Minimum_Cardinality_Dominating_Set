from utilities import *
from graph import Graph
from itertools import combinations



class PolynomialTimeAlgorithm:
    def __init__(self,graph : Graph):
        self.graph = graph
        self.is_recursive_call = False
        self.graph_snapshots = []
        self.contracted_vertex = None

        self.previous_triangle = None

    def mcdsw(self):
        """
        Returns a minimum cardinality dominating set of the graph.
        """
        for vertex in self.graph.vertices:
            bfs_levels = self.graph.bfs_levels(vertex)
            print(bfs_levels)
        
        return 

    
    
    def run(self):
        return self.mcdsw()