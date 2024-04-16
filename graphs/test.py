import unittest

from graph import Graph


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()

    def test_add_vertex(self):
        # Adding a new vertex
        self.assertTrue(self.graph.add_vertex('A'))
        self.assertIn('A', self.graph.adj_list)

        # Adding an existing vertex
        self.assertFalse(self.graph.add_vertex('A'))

    def test_add_edges(self):
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')

        # Adding edges between two vertices
        self.assertTrue(self.graph.add_edges('A', 'B'))
        self.assertIn('B', self.graph.adj_list['A'])
        self.assertIn('A', self.graph.adj_list['B'])

        # Adding edges with non-existent vertices
        self.assertFalse(self.graph.add_edges('A', 'C'))

    def test_print_graph(self):
        # Capturing stdout
        import io
        import sys
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.graph.add_edges('A', 'B')
        self.graph.print_graph()

        sys.stdout = sys.__stdout__
        output = capturedOutput.getvalue().strip()

        self.assertEqual(output, "A: B\nB: A")

    def test_remove_edge(self):
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.graph.add_edges('A', 'B')

        # Removing an existing edge
        self.assertTrue(self.graph.remove_edge('A', 'B'))
        self.assertNotIn('B', self.graph.adj_list['A'])
        self.assertNotIn('A', self.graph.adj_list['B'])

        # Removing a non-existent edge
        self.assertFalse(self.graph.remove_edge('A', 'B'))

    def test_remove_vertex(self):
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.graph.add_vertex('C')
        self.graph.add_edges('A', 'B')
        self.graph.add_edges('B', 'C')

        # Removing an existing vertex
        self.assertTrue(self.graph.remove_vertex('B'))
        self.assertNotIn('B', self.graph.adj_list)
        self.assertNotIn('B', self.graph.adj_list['A'])
        self.assertNotIn('B', self.graph.adj_list['C'])

        # Removing a non-existent vertex
        self.assertFalse(self.graph.remove_vertex('D'))

if __name__ == '__main__':
    unittest.main()