"""
Contains methods related to Trees and Graphs Questions from Cracking the Coding Interview
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def getHeight(self) -> int:
        if self.left == None and self.right == None:
            return 1

        leftH = rightH = 0
        if self.left is not None:
            leftH = self.left.getHeight()
        if self.right is not None:
            rightH = self.right.getHeight()

        if leftH > rightH:
            return leftH + 1

        return rightH + 1


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
        return self.visited

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

class TreeAndGraphsHelpers:
    @staticmethod
    def isBST(node: GraphNode) -> bool:
        if node is None:
            return False
        if node.left is None and node.right is None:
            return True

        isLeftBST = isRightBST = True
        if node.left is not None:
            if node.value < node.left.value:
                return False
            isLeftBST = TreeAndGraphsHelpers.isBST(node.left)
        if node.right is not None:
            if node.value >= node.right.value:
                return False
            isRightBST = TreeAndGraphsHelpers.isBST(node.right)

        return isRightBST and isLeftBST


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

        curr.setVisited()
        for next in curr.adjacentNodes:
            if next.getVisited() == False:
                if TreesAndGraphsQuestions.AreNodesConnected(next, find):
                    return True

        return False


    @staticmethod
    def ArrayToBSTRecurse(arry: list, left: int, right: int) -> BSTNode:
        """
        Helper for ArrayToBST method. This recurses down and builds the BST
        :param arry:
        :param left:
        :param right:
        :return: BSTNode the current root node
        """
        if left == right:
            return BSTNode(arry[left])
        elif left > right:
            return None

        center = int((right - left) / 2)
        root = BSTNode(arry[center])
        root.left = TreesAndGraphsQuestions.ArrayToBSTRecurse(arry, left, center - 1)
        root.right = TreesAndGraphsQuestions.ArrayToBSTRecurse(arry, center + 1, right)

        return root

    @staticmethod
    def ArrayToBST(arry: list):
        """
        Given an increasing order array with unique integer elements, write
        an algorithm to create a BST with minimal height

        :param arry: The array (increasing order) with unique integer elements
        :return: The BST of minimal possible size
        """
        if arry is None:
            return None

        return TreesAndGraphsQuestions.ArrayToBSTRecurse(arry, 0, len(arry) -  1)

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


