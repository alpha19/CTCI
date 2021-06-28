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

        nodesInGraph = []
        for i in range(1, 10):
            nodesInGraph.append(GraphNode(i))

        graph = DirectedGraph(nodesInGraph)

        # Create the connection points
        nodesInGraph[0].addAdjacentNode(nodesInGraph[1])
        nodesInGraph[0].addAdjacentNode(nodesInGraph[3])

        nodesInGraph[1].addAdjacentNode(nodesInGraph[2])
        nodesInGraph[1].addAdjacentNode(nodesInGraph[4])
        nodesInGraph[1].addAdjacentNode(nodesInGraph[5])

        nodesInGraph[2].addAdjacentNode(nodesInGraph[8])

        nodesInGraph[3].addAdjacentNode(nodesInGraph[0])
        nodesInGraph[3].addAdjacentNode(nodesInGraph[5])

        nodesInGraph[4].addAdjacentNode(nodesInGraph[6])

        nodesInGraph[5].addAdjacentNode(nodesInGraph[4])

        nodesInGraph[6].addAdjacentNode(nodesInGraph[7])

        nodesInGraph[7].addAdjacentNode(nodesInGraph[6])
        nodesInGraph[7].addAdjacentNode(nodesInGraph[8])

        nodesInGraph[8].addAdjacentNode(nodesInGraph[7])

        # Find the path from node 3 to node 9 (should be true)
        self.assertTrue(TreesAndGraphsQuestions.AreNodesConnected(nodesInGraph[2], nodesInGraph[8]))
        graph.clearVisited()

        # Find the path from node 1 to node 9 (should be true)
        self.assertTrue(TreesAndGraphsQuestions.AreNodesConnected(nodesInGraph[0], nodesInGraph[8]))
        graph.clearVisited()

        # Find the path from node 7 to node 9 (should be true)
        self.assertTrue(TreesAndGraphsQuestions.AreNodesConnected(nodesInGraph[6], nodesInGraph[8]))
        graph.clearVisited()

        # Find the path from node 9 to node 7 (should be true)
        self.assertTrue(TreesAndGraphsQuestions.AreNodesConnected(nodesInGraph[8], nodesInGraph[6]))
        graph.clearVisited()

        # Find the path from node 8 to node 1 (should be false)
        self.assertFalse(TreesAndGraphsQuestions.AreNodesConnected(nodesInGraph[8], nodesInGraph[0]))
        graph.clearVisited()

        # Find the path from node 3 to node 6 (should be false)
        self.assertFalse(TreesAndGraphsQuestions.AreNodesConnected(nodesInGraph[2], nodesInGraph[5]))
        graph.clearVisited()

        # Find the path from node 6 to node 2 (should be false)
        self.assertFalse(TreesAndGraphsQuestions.AreNodesConnected(nodesInGraph[5], nodesInGraph[1]))
        graph.clearVisited()

        # Find the path from node 3 to node 7 (should be true)
        self.assertTrue(TreesAndGraphsQuestions.AreNodesConnected(nodesInGraph[2], nodesInGraph[6]))
        graph.clearVisited()

        # Find the path from node 6 to node 9 (should be true)
        self.assertTrue(TreesAndGraphsQuestions.AreNodesConnected(nodesInGraph[5], nodesInGraph[8]))
        graph.clearVisited()

        # Find the path from node 4 to node 3 (should be true)
        self.assertTrue(TreesAndGraphsQuestions.AreNodesConnected(nodesInGraph[3], nodesInGraph[2]))
        graph.clearVisited()

    def test_ArryToBSTWithMinimalHeight(self):
        arry = [1, 2, 3]
        node = TreesAndGraphsQuestions.ArrayToBST(arry)

        self.assertEquals(node.getHeight(), 2)
        self.assertTrue(TreeAndGraphsHelpers.isBST(node))

        # TODO: More test cases!!!
        arry = [1, 2, 3, 4, 5]
        node = TreesAndGraphsQuestions.ArrayToBST(arry)

        self.assertEquals(node.getHeight(), 3)
        self.assertTrue(TreeAndGraphsHelpers.isBST(node))

        arry = [5, 7, 8, 12, 17, 19, 20]
        node = TreesAndGraphsQuestions.ArrayToBST(arry)

        self.assertEquals(node.getHeight(), 3)
        self.assertTrue(TreeAndGraphsHelpers.isBST(node))

        arry = [6, 8, 9, 10, 14, 16]
        node = TreesAndGraphsQuestions.ArrayToBST(arry)

        self.assertEquals(node.getHeight(), 3)
        self.assertTrue(TreeAndGraphsHelpers.isBST(node))

    def test_BSTToDepthList(self):
        arry = [1, 2, 3]
        node = TreesAndGraphsQuestions.ArrayToBST(arry)

        depthList = TreesAndGraphsQuestions.BSTToDepthList(node)

        self.assertEquals(len(depthList), 2)
        self.assertEquals(depthList[0].value.value, 2)
        self.assertEquals(depthList[1].value.value, 1)
        self.assertEquals(node.getHeight(), 2)

    def test_isBalanced(self):
        # Brute force the node creation
        node1 = BSTNode(1)
        node2 = BSTNode(2)
        node3 = BSTNode(3)
        node4 = BSTNode(4)
        node5 = BSTNode(5)
        node6 = BSTNode(6)
        node7 = BSTNode(7)

        node4.left = node2
        node4.right = node6

        node2.left = node1
        node2.right = node3

        node6.left = node5
        node6.right = node7

        self.assertTrue(TreesAndGraphsQuestions.isBalanced(node4))

        node6.left = node4

        node4.right = node5
        node4.left = node2

        node2.left = node1
        node2.right = node3

        self.assertFalse(TreesAndGraphsQuestions.isBalanced(node6))

    def test_nextNode(self):
        node3 = BSTNode(3)
        node5 = BSTNode(5)
        node7 = BSTNode(7)
        node10 = BSTNode(10)
        node12 = BSTNode(12)
        node15 = BSTNode(15)
        node17 = BSTNode(17)
        node20 = BSTNode(20)

        node10.left = node5
        node10.right = node15

        node5.left = node3
        node5.right = node7
        node5.parent = node10

        node15.left = node12
        node15.right = node17
        node15.parent = node10

        node3.parent = node5

        node7.parent = node5

        node12.parent = node15

        node17.right = node20
        node17.parent = node15

        node20.parent = node17

        self.assertEquals(TreesAndGraphsQuestions.nextNode(node3), node5)
        self.assertEquals(TreesAndGraphsQuestions.nextNode(node10), node12)
        self.assertEquals(TreesAndGraphsQuestions.nextNode(node20), None)
        self.assertEquals(TreesAndGraphsQuestions.nextNode(node7), node10)









