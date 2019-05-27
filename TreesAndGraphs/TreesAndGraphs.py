"""
Contains methods related to Trees and Graphs Questions from Cracking the Coding Interview
"""

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
        curr.setVisited()
        if curr.name == find.name:
            return True

        for node in curr.adjacentNodes:
            if node.visited is False and TreesAndGraphsQuestions.AreNodesConnected(node, find):
                return True

        return False
