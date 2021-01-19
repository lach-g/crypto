import sys
sys.path.append("../assignment")

import unittest
from Graph_dsa import Graph, Vertex, Edge

class TestGraph(unittest.TestCase):

    def test_init(self):
        graph = Graph()
        self.assertEqual(graph.vert_count, 0,
                        "Count of vertices should begin at 0.")

    def test_vert_list(self):
        graph = Graph()
        graph.add_vertex("A", 1)
        vert_list = graph.vert_list()
        vert = vert_list.peek_first()
        self.assertEqual(vert.data, 1,
                    "Vert list returns the linked of vertices each with data.")

    def test_add_vertex(self):
        graph = Graph()
        graph.add_vertex("A", 1)
        self.assertTrue(graph.has_vertex("A"),
            "Graph should track all vertices added through add vertex.")

    def test_add_edge(self):
        graph = Graph()
        graph.add_vertex("A", 1)
        graph.add_vertex("B", 2)
        graph.add_edge("A", "B", "Strong")
        self.assertTrue(graph.points_to("A", "B"),
                    "The edge must have direction and be trackable through the vert links.")

    def test_get_vertex_count(self):
        graph = Graph()
        graph.add_vertex("A", 1)
        graph.add_vertex("B", 2)
        self.assertEqual(graph.get_vertex_count(), 2,
                    "Added to vertices should return a vertex count of 2.")

    def test_get_adjacent(self):
        graph = Graph()
        graph.add_vertex("A", 1)
        graph.add_vertex("B", 2)
        graph.add_edge("A", "B", "Strong")
        arcs_list = graph.get_adjacent("A")
        arc = arcs_list.peek_first()
        self.assertEqual(arc.end, "B",
                    "The only arc in the vert link should point to the only other vertex set up.")

    def test_bfs_shortest_path(self):
        graph = Graph()
        graph.add_vertex("A", 1)
        graph.add_vertex("B", 2)
        graph.add_vertex("C", 3)
        graph.add_vertex("D", 4)

        graph.add_edge("A", "B", None)
        graph.add_edge("A", "C", None)
        graph.add_edge("B", "C", None)
        graph.add_edge("C", "D", None)

        path = graph.bfs_shortest_path("A", "D")
        path_str = ""
        for i in path:
            path_str = path_str + i

        correct_path = "ACD"
        self.assertEqual(path_str, correct_path,
                    "BFS Path must find the shortest path regardless of edge weight")  

    def test_sort_edge_weight(self):
        graph = Graph()
        graph.add_vertex("A", 1)
        graph.add_vertex("B", 2)
        graph.add_vertex("C", 3)
        graph.add_vertex("D", 4)

        graph.add_edge("A", "B", 2)
        graph.add_edge("A", "C", 1)
        graph.add_edge("B", "C", None)
        graph.add_edge("C", "D", None)

        sorted_array_decreasing_val = graph.sort_edge_weight(graph.get_vertex("A").links)
        self.assertEqual(sorted_array_decreasing_val[0].end, "B")

    # def test_dfs_shortest_path(self):
    #     graph = Graph()
    #     graph.add_vertex("A", 1)
    #     graph.add_vertex("B", 2)
    #     graph.add_vertex("C", 3)
    #     graph.add_vertex("D", 4)

    #     graph.add_edge("A", "C", 1)
    #     graph.add_edge("A", "B", 3)
    #     graph.add_edge("B", "C", 4)
    #     graph.add_edge("C", "D", 2)

    #     path = graph.dfs_shortest_path("A", "D")
    #     path_str = ""
    #     for i in path:
    #         print(i)
    #         path_str = path_str + i

    #     correct_path = "ABCD"
    #     self.assertEqual(path_str, correct_path,
    #                 "DFS Path must find the shortest path based on edge weight")


    def test_linked_list_to_array_edges(self):
        graph = Graph()
        graph.add_vertex("A", 1)
        graph.add_vertex("B", 2)
        graph.add_vertex("C", 3)
        graph.add_vertex("D", 4)

        graph.add_edge("A", "B", None)
        graph.add_edge("A", "C", None)
        graph.add_edge("B", "C", None)
        graph.add_edge("C", "D", None)

        array = graph.linked_list_to_array_edges(graph.get_vertex("A").links)
        self.assertEqual(array[0].end, "B",
                        "Turns the given vertex name's edges to an array.")

    def test_clear(self):
        graph = Graph()
        graph.add_vertex("A", 1)
        graph.add_vertex("B", 2)
        graph.add_vertex("C", 3)
        graph.add_vertex("D", 4)

        graph.add_edge("A", "B", None)
        graph.add_edge("A", "C", None)
        graph.add_edge("B", "C", None)
        graph.add_edge("C", "D", None)

        vert = graph.get_vertex("A")
        vert.visited = True
        graph.clear()
        self.assertEqual(vert.visited, False,
                "The clear should reset all visited vertex variables to false")





if __name__ == "__main__":
    unittest.main()