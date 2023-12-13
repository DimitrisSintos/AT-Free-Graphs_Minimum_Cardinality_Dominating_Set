from utilities import *
from graph import Graph
from itertools import combinations



class PolynomialTimeAlgorithm:
    def __init__(self,graph : Graph, weight : int):
        self.graph = graph
        self.weight = weight



    def mcdsw(self):
        """
        Returns a minimum cardinality dominating set of the graph.
        """
        D = self.graph.vertices
        for vertex in self.graph.vertices:
            H = self.graph.bfs_levels(vertex)
            l = len(H) - 1 
            i = 1
            
            print("BFS Levels of:",vertex,":\n" ,H)
            A1 = self.initialize_queue(vertex)
            print("Init queue of:",vertex,":\n" ,A1)
            A = { i : A1}

            while A and i < l:
                i = i + 1
                A[i] = []
                
                print("A:", A)
                for triple in A[i-1]:
                    print("Iner loop triple:", triple)
                    S = triple[0]
                    S_accent = triple[1]
                    val_S_accent = triple[2]
                    r = len(H[i])
                    for U in combinations(H,r):
                        print("Inner loop U:", U)
                        if len( S | set(U) ) <= self.weight:
                            print("U that make it:", U)
                            closed_neighborhood_of_S_and_U = self.graph.closed_neighborhood_of_set(S | set(U))
                            if closed_neighborhood_of_S_and_U.issuperset(H):
                                print("H is subset of closed_neighborhood_of_S_and_U")
                                R = ( S | set(U) ) - H[i-2]
                                R_accent = S_accent
                                val_R_accent = val_S_accent + len(U)
                                if not any(triple[0] == R for triple in A[i]):
                                    A[i].append((R, R_accent, val_R_accent))
                                #IF there is a triple (P; P_accent ; val_P_accent) in Ai such that P = R AND val_R_accent < val_P_accent
                                #THEN replace (P; P_accent ; val_P_accent) by (R; R_accent ; val_R_accent) in Ai ;
                                for index, triple in enumerate(A[i]):
                                    if triple[0] == R and val_R_accent < triple[2]:
                                        A[i][index] = (R, R_accent, val_R_accent)
            if A:
                # Find the triple with minimum val(S') in A[l] that satisfies H[l] ⊆ N[S]
                print("\nA[i]:", A[i-1])
                optimal_triple = min((triple for triple in A[i-1] if set(H[i-1]).issubset(self.graph.closed_neighborhood_of_set(triple[0]))), 
                                    key=lambda x: x[2], default=None)
                
                print("\noptimal_triple:", optimal_triple)
                
                if optimal_triple and optimal_triple[2] < len(D):
                    D = optimal_triple[1]  # Update D if a better solution is found
                    print("########\nD is updated to:", D)
        
        print("THE DOMINATION SET IS:", D)
        self.graph.domination_set = D
        self.graph.show()
                            
        return 
    
    def initialize_queue(self, vertex):
        queue = []
        for subset in self.generate_subsets(vertex):
            queue.append((subset, subset, len(subset)))
        return queue
    
    def generate_subsets(self, vertex):
        closed_nbhd = self.graph.closed_neighborhood(vertex)
        subsets = []
        for r in range(1, self.weight + 1):
            for subset in combinations(closed_nbhd, r):
                subsets.append(set(subset))
        return subsets

    
    
    def run(self):
        return self.mcdsw()