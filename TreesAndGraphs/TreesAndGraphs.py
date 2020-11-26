"""
Contains methods related to Trees and Graphs Questions from Cracking the Coding Interview
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class GraphNode:
    def __init__(self, nodeName, adj: list=None):
        self.name = nodeName
        self.visited = False

        if adj is None:
            self.adjacentNodes = []
        else:
            self.adjacentNodes = adj

    def addAdjacentNode(self, node):
        self.adjacentNodes.append(node)

    def setVisited(self):
        self.visited = True

    def clearVisited(self):
        self.visited = False

    def getVisited(self):
        return visited

    def clearAdjacent(self):
        self.adjacentNodes = []

class DirectedGraph:
    """
    Class representation for a graph (directed)
    """
    def __init__(self, nodesInGraph=[]):
        self.nodes = nodesInGraph

    def addNode(self, node):
        """
        Adds a node to a graph
        :param node:
        :return:
        """
        self.nodes.append(node)

    def clearVisited(self):
        """
        Clears flag indicating node has been visited (used during a node search)
        :return:
        """
        for node in self.nodes:
            node.clearVisited()

    def getNodes(self):
        return self.nodes

class TreesAndGraphsQuestions:
    """
    This class is basically just a namespace
    """
    @staticmethod
    def AreNodesConnected(curr: GraphNode, find: GraphNode):
        """
        Determine if the two nodes are connected
        :param curr:
        :param find:
        :return:
        """
        if curr.name == find.name:
            return True

        curr.setVisited(True)
        for next in curr.adjacentNodes:
            if next.getVisited() == False:
                if TreesAndGraphsQuestions.AreNodesConnected(next, find):
                    return True

        return False




    @staticmethod
    def ArrayToBST(arry: list):
        """
        Given an increasing order array with unique interger elements, write
        an algorithm to create a BST with minimal height

        :param arry: The array (increasing order) with unique integer elements
        :return: The BST of minimal possible size
        """

    @staticmethod
    def BSTToDepthList(node: BSTNode, depth: int, arry: list):
        """
        Given a binary tree, design an algorithm which creates a linked list of all
        the nodes at each depth.

        :param node: The current node in the BST (starts with the root node)
        :param depth: The depth the current node is associated with (starts at zero)
        :param arry: The array that contains all the linked lists. Element at index zero is associated with linked list
                     of depth 0 nodes, index one with depth 1 nodes and so on.
        """


