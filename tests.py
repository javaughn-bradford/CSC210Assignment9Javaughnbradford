# tests.py
# Tests for your WeightedGraph.dijkstra(), edge_exists(), and path reconstruction.
# Do not modify the provided tests; add your own in the indicated section.
# Modified by: 

import unittest
from weighted_graph import WeightedGraph


def print_path(path):
    for i, x in enumerate(path):
        end = "" if i == len(path) - 1 else " -> "
        print(f"{x}", end=end)
    print()


class TestDijkstraCityGraph1(unittest.TestCase):
    # DO NOT MODIFY THIS TEST CASE
    def test_city_graph_1(self):
        g = WeightedGraph()
        g.add_edge("Seattle", "Chicago", 2097)
        g.add_edge("Seattle", "Denver", 1331)
        g.add_edge("Seattle", "San Francisco", 807)
        g.add_edge("San Francisco", "Denver", 1267)
        g.add_edge("San Francisco", "Los Angeles", 381)
        g.add_edge("Los Angeles", "Denver", 1015)
        g.add_edge("Los Angeles", "Kansas City", 1663)
        g.add_edge("Los Angeles", "Dallas", 1435)
        g.add_edge("Denver", "Chicago", 1003)
        g.add_edge("Denver", "Kansas City", 599)
        g.add_edge("Kansas City", "Chicago", 533)
        g.add_edge("Kansas City", "New York", 1260)
        g.add_edge("Kansas City", "Atlanta", 864)
        g.add_edge("Kansas City", "Dallas", 496)
        g.add_edge("Chicago", "Boston", 983)
        g.add_edge("Chicago", "New York", 787)
        g.add_edge("Boston", "New York", 214)
        g.add_edge("Atlanta", "New York", 888)
        g.add_edge("Atlanta", "Dallas", 781)
        g.add_edge("Atlanta", "Houston", 810)
        g.add_edge("Atlanta", "Miami", 661)
        g.add_edge("Houston", "Miami", 1187)
        g.add_edge("Houston", "Dallas", 239)

        print("------cityGraph1------")
        print(g)  # uses __str__

        parents, distances = g.dijkstra("New York")

        # Are the distances from New York correct?
        self.assertEqual(distances["San Francisco"], 3057)
        self.assertEqual(distances["Los Angeles"], 2805)
        self.assertEqual(distances["Seattle"], 2884)
        self.assertEqual(distances["Denver"], 1790)
        self.assertEqual(distances["Kansas City"], 1260)
        self.assertEqual(distances["Chicago"], 787)
        self.assertEqual(distances["Boston"], 214)
        self.assertEqual(distances["Atlanta"], 888)
        self.assertEqual(distances["Miami"], 1549)
        self.assertEqual(distances["Dallas"], 1669)
        self.assertEqual(distances["Houston"], 1698)
        self.assertEqual(distances["San Francisco"], 3057)

        path = g.path_map_to_path(parents, "San Francisco")
        print("------cityGraph1 path------")
        print_path(path)

        # Shortest path should be: New York -> Chicago -> Denver -> San Francisco
        self.assertEqual(len(path), 4)
        self.assertEqual(path[0], "New York")
        self.assertEqual(path[-1], "San Francisco")

        last = path[0]
        for current in path[1:]:
            self.assertTrue(g.edge_exists(last, current))
            last = current


class TestDijkstraCityGraph2(unittest.TestCase):
    # DO NOT MODIFY THIS TEST CASE
    def test_city_graph_2(self):
        g = WeightedGraph()
        g.add_edge("Seattle", "Chicago", 1737)
        g.add_edge("Seattle", "San Francisco", 678)
        g.add_edge("San Francisco", "Riverside", 386)
        g.add_edge("San Francisco", "Los Angeles", 348)
        g.add_edge("Los Angeles", "Riverside", 50)
        g.add_edge("Los Angeles", "Phoenix", 357)
        g.add_edge("Riverside", "Phoenix", 307)
        g.add_edge("Riverside", "Chicago", 1704)
        g.add_edge("Phoenix", "Dallas", 887)
        g.add_edge("Phoenix", "Houston", 1015)
        g.add_edge("Dallas", "Chicago", 805)
        g.add_edge("Dallas", "Atlanta", 721)
        g.add_edge("Dallas", "Houston", 225)
        g.add_edge("Houston", "Atlanta", 702)
        g.add_edge("Houston", "Miami", 968)
        g.add_edge("Atlanta", "Chicago", 588)
        g.add_edge("Atlanta", "Washington", 543)
        g.add_edge("Atlanta", "Miami", 604)
        g.add_edge("Miami", "Washington", 923)
        g.add_edge("Chicago", "Detroit", 238)
        g.add_edge("Detroit", "Boston", 613)
        g.add_edge("Detroit", "Washington", 396)
        g.add_edge("Detroit", "New York", 482)
        g.add_edge("Boston", "New York", 190)
        g.add_edge("New York", "Philadelphia", 81)
        g.add_edge("Philadelphia", "Washington", 123)

        print("------cityGraph2------")
        print(g)  # uses __str__

        parents, distances = g.dijkstra("Miami")

        # Are the distances from Miami correct?
        self.assertEqual(distances["Seattle"], 2929)
        self.assertEqual(distances["Chicago"], 1192)
        self.assertEqual(distances["Atlanta"], 604)
        self.assertEqual(distances["New York"], 1127)

        path = g.path_map_to_path(parents, "San Francisco")
        print("------cityGraph2 path------")
        print_path(path)

        # Shortest path should be:
        # Miami -> Houston -> Phoenix -> Riverside -> San Francisco
        self.assertEqual(len(path), 5)
        self.assertEqual(path[0], "Miami")
        self.assertEqual(path[-1], "San Francisco")

        last = path[0]
        for current in path[1:]:
            self.assertTrue(g.edge_exists(last, current))
            last = current


# YOUR CODE HERE
# ADD YOUR OWN TEST CASE
# Prove that dijkstra() works correctly in your own test case,
# using the methods of WeightedGraph.
# You should make up your own graph and test it. Do not reuse cityGraph1/2.
# Look at the prior two tests as examples.


if __name__ == "__main__":
    unittest.main()
