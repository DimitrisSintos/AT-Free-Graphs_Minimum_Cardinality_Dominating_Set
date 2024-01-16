from graph import Graph
from polynomial_time_algorithm import PolynomialTimeAlgorithm
from graph_parser import GraphParser
from brute_force import BruteForce
import sys


def main(argv):
    file_path = None
    num_of_vertices = None
    num_of_edges = None
    edges = None
    at_free_graph = None

    if argv:
        file_path = argv[0]

    if file_path is None:
        num_of_vertices = 8
        num_of_edges = 11
        edges = [
            (0, 1),
            (1, 2),
            (1, 5),
            (1, 3),
            (1, 4),
            (2, 6),
            (3, 6),
            (3, 4),
            (4, 7),
            (6, 7),
            (5, 7)
        ]
        at_free_graph = Graph(num_of_vertices, num_of_edges, edges)
    else:
        at_free_graph = GraphParser.parse_graph_from_file(file_path)

    # at_free_graph.show()
    weight = 5
    algorithm = PolynomialTimeAlgorithm(at_free_graph,weight)
    algorithm.run()
    
    brute_force_algorithm = BruteForce(at_free_graph)
    brute_force_domintaion_set = brute_force_algorithm.run()
    print("brute_force_domintaion_set",brute_force_domintaion_set)
    print("brute_force_algorithm, minimum_domination_set_size:", len(brute_force_domintaion_set))
    at_free_graph.domination_set = brute_force_domintaion_set
    at_free_graph.show("brute_force_graph")

if __name__ == "__main__":
    main(argv=sys.argv[1:])
