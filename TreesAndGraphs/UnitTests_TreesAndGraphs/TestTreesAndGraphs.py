"""
Tests various  stack classes and methods
"""
import unittest
from TreesAndGraphs.TreesAndGraphs import *

class TestTreesAndGraphsQuestions(unittest.TestCase):
    """ Class for unit test methods """

    def test_AreNodesConnected(self):
        """ Test AreNodesConnected 
        :rtype: object
        """
        nodesInGraph = []
        for i in range(1, 10):
            nodesInGraph.append(GraphNode(i))

        # Create the connection points
        nodesInGraph[0].addAdjacentNode(nodesInGraph[1])
        nodesInGraph[0].addAdjacentNode(nodesInGraph[4])

        nodesInGraph[2].addAdjacentNode(nodesInGraph[5])
        nodesInGraph[2].addAdjacentNode(nodesInGraph[6])
        nodesInGraph[2].addAdjacentNode(nodesInGraph[1])
        nodesInGraph[2].addAdjacentNode(nodesInGraph[4])

        nodesInGraph[3].addAdjacentNode(nodesInGraph[7])
        nodesInGraph[3].addAdjacentNode(nodesInGraph[8])

        nodesInGraph[4].addAdjacentNode(nodesInGraph[2])
        nodesInGraph[4].addAdjacentNode(nodesInGraph[3])

        nodesInGraph[6].addAdjacentNode(nodesInGraph[2])


        # Create a graph
        graph = DirectedGraph(nodesInGraph)

        # Find the path from node 1 to node 9 (should be true)
        self.assertTrue(TreesAndGraphsQuestions.AreNodesConnected(nodesInGraph[0], nodesInGraph[8]))
        graph.clearVisited()

        # FInd the path from node 7 to node 1 (should be false)
        self.assertFalse(TreesAndGraphsQuestions.AreNodesConnected(nodesInGraph[6], nodesInGraph[0]))
        graph.clearVisited()

        # Find the path from node 8 to node 4 (should be false)
        self.assertFalse(TreesAndGraphsQuestions.AreNodesConnected(nodesInGraph[7], nodesInGraph[3]))
        graph.clearVisited()

        # Find the path from node 5 to node 6 (should be true)
        self.assertTrue(TreesAndGraphsQuestions.AreNodesConnected(nodesInGraph[4], nodesInGraph[5]))
        graph.clearVisited()

        # Find the path from node 7 to node 9 (should be true)
        self.assertTrue(TreesAndGraphsQuestions.AreNodesConnected(nodesInGraph[6], nodesInGraph[8]))
        graph.clearVisited()

        # Find the path from node 3 to node 7 (should be true)
        self.assertTrue(TreesAndGraphsQuestions.AreNodesConnected(nodesInGraph[2], nodesInGraph[6]))
        graph.clearVisited()




