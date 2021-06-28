"""
Contains methods related to Trees and Graphs Questions from Cracking the Coding Interview
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

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

    @staticmethod
    def BFSToList(node: GraphNode):
        """
        Return the BFS path for a directed graph
        A circular cycle is an Exception!
        :param node:
        :return: A list showing the BFS path
        """
        if node is None or len(node) == 0:
            return []

        queue = []
        result = []

        queue.append(node)

        while len(queue) > 0:
            depthLength = len(queue)

            for _ in range(depthLength):
                curr = queue.pop(0)
                result.append(curr)
                for n in node.adjacentNodes:
                    if n.getVisited() == False:
                        n.setVisited()
                        queue.append(n)
        return result



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

        center = int((right + left) / 2)
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
    def BSTToDepthList(node: BSTNode) -> list():
        """
        Given a binary tree, design an algorithm which creates a linked list of all
        the nodes at each depth.

        :param node: The current node in the BST (starts with the root node)
        :return List: The linked list array of BST nodes at each depth
        """
        if node is None:
            return []

        def addNode(node: BSTNode) -> None:
            nonlocal depth, depthList

            newNode = LinkedListNode(node)
            if depth == len(depthList):
                depthList.extend([None])
                depthList[depth] = newNode
            else:
                currNode = depthList[depth]
                while currNode.next is not None:
                    currNode = currNode.next
                currNode.next = newNode

        depthList = []
        depth = 0

        addNode(node)
        prevNodes = depthList[depth]

        while len(depthList) > depth:
            prevNodes = depthList[depth]
            depth += 1
            while prevNodes is not None:
                currNode = prevNodes.value
                if currNode.left is not None:
                    addNode(currNode.left)
                if currNode.right is not None:
                    addNode(currNode.right)

                prevNodes = prevNodes.next


        return depthList

    @staticmethod
    def getHeight(node: BSTNode) -> int:
        """
        Get the height of a binary search tree
        :param node: the BST node
        :return: The height
        """
        if node == None:
            return 0

        leftH = TreesAndGraphsQuestions.getHeight(node.left)
        rightH = TreesAndGraphsQuestions.getHeight(node.right)

        return (leftH if leftH > rightH else rightH) + 1

    @staticmethod
    def isBalanced(node: BSTNode) -> bool:
        """
        Determine if a BST is balanced or not
        :param node: the binary search tree node
        :return: True if balanced, False otherwise
        """
        if node is None:
            raise Exception("An empty BST node was provided")

        leftH = TreesAndGraphsQuestions.getHeight(node.left)
        rightH = TreesAndGraphsQuestions.getHeight(node.right)

        return False if abs(leftH - rightH) > 1 else True

    @staticmethod
    def nextNode(node: BSTNode) -> BSTNode:
        if node is None:
            return node

        if node.right is not None:
            node = node.right
            while node.left != None:
                node = node.left
        else:
            while node.parent is not None and node.parent.right is node:
                node = node.parent
            node = node.parent
        return node

    @staticmethod
    def buildNode(projects, dependencies):
        """
        Return a list of build order from a list of projects and their dependencies

        :param projects:
        :param dependencies:
        :return:
        """
        nodeMap = {}
        result = []
        for val in projects:
            nodeMap[val] = (GraphNode(val), True)

        for d in dependencies:
            curr = nodeMap[d[0]][0]
            curr.adjacentNodes.append(nodeMap[d[1]][0])
            nodeMap[d[1]][1] = False

        for val in nodeMap.values():
            if val[1]:
                bfsList = TreeAndGraphsHelpers.BFSToList(val[0])
                for node in bfsList:
                    result.append(node.value)

        return result






