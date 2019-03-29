"""
compares various methods from LinkedListQuestions
"""
import unittest
from LinkedLists.LinkedListQuestions import *

class TestLinkedListQuestions(unittest.TestCase):
    """ Class for test methods """

    def test_RemoveDuplicates(self):
        """ Test RemoveDuplicates method """
        firstNode = LinkedListQuestions.Node(3)
        firstNode = LinkedListQuestions.Node(5, firstNode)
        firstNode = LinkedListQuestions.Node(4, firstNode)
        firstNode = LinkedListQuestions.Node(5, firstNode)
        firstNode = LinkedListQuestions.Node(2, firstNode)

        secondNode = LinkedListQuestions.Node(3)
        secondNode = LinkedListQuestions.Node(4, secondNode)
        secondNode = LinkedListQuestions.Node(5, secondNode)
        secondNode = LinkedListQuestions.Node(2, secondNode)

        LinkedListQuestions.RemoveDuplicates(firstNode)
        self.assertTrue(LinkedListQuestions.Equals(firstNode, secondNode))

        # TODO: Subsuquent test methods should use a loop to fill out the right
        firstNode = LinkedListQuestions.Node(3)
        for i in range(0,5):
            firstNode = LinkedListQuestions.Node(i, firstNode)

        secondNode = LinkedListQuestions.Node(0)
        for i in range(1,5):
            secondNode = LinkedListQuestions.Node(i, secondNode)

        LinkedListQuestions.RemoveDuplicates(firstNode)
        self.assertTrue(LinkedListQuestions.Equals(firstNode, secondNode))

        firstNode = LinkedListQuestions.Node(6)
        for i in range(0,5):
            if i == 3:
                firstNode = LinkedListQuestions.Node(i, firstNode)
                firstNode = LinkedListQuestions.Node(i, firstNode)

            firstNode = LinkedListQuestions.Node(i, firstNode)

        secondNode = LinkedListQuestions.Node(6)
        for i in range(0,5):
            secondNode = LinkedListQuestions.Node(i, secondNode)

        LinkedListQuestions.RemoveDuplicates(firstNode)
        self.assertTrue(LinkedListQuestions.Equals(firstNode, secondNode))

        firstNode = LinkedListQuestions.Node(0, firstNode)
        firstNode = LinkedListQuestions.Node(6, firstNode)
        firstNode = LinkedListQuestions.Node(4, firstNode)

        for i in range(0,5):
            if i == 3 or i == 1:
                firstNode = LinkedListQuestions.Node(i, firstNode)
                firstNode = LinkedListQuestions.Node(i, firstNode)

            firstNode = LinkedListQuestions.Node(i, firstNode)

        secondNode = LinkedListQuestions.Node(6)
        for i in range(0,5):
            secondNode = LinkedListQuestions.Node(i, secondNode)

        LinkedListQuestions.RemoveDuplicates(firstNode)
        self.assertTrue(LinkedListQuestions.Equals(firstNode, secondNode))

    def test_ReturnKthToLast(self):
        """ Test Return Kth to last method """
        firstNode = LinkedListQuestions.Node(10)
        firstNode = LinkedListQuestions.Node(9, firstNode)
        firstNode = LinkedListQuestions.Node(8, firstNode)
        firstNode = LinkedListQuestions.Node(7, firstNode)
        firstNode = LinkedListQuestions.Node(6, firstNode)
        firstNode = LinkedListQuestions.Node(5, firstNode)
        firstNode = LinkedListQuestions.Node(4, firstNode)
        firstNode = LinkedListQuestions.Node(3, firstNode)
        firstNode = LinkedListQuestions.Node(2, firstNode)
        firstNode = LinkedListQuestions.Node(1, firstNode)

        self.assertEquals(LinkedListQuestions.ReturnKthToLast(firstNode, 1), 10)
        self.assertEquals(LinkedListQuestions.ReturnKthToLast(firstNode, 2), 9)
        self.assertEquals(LinkedListQuestions.ReturnKthToLast(firstNode, 3), 8)
        self.assertEquals(LinkedListQuestions.ReturnKthToLast(firstNode, 4), 7)
        self.assertEquals(LinkedListQuestions.ReturnKthToLast(firstNode, 5), 6)
        self.assertEquals(LinkedListQuestions.ReturnKthToLast(firstNode, 6), 5)
        self.assertEquals(LinkedListQuestions.ReturnKthToLast(firstNode, 7), 4)
        self.assertEquals(LinkedListQuestions.ReturnKthToLast(firstNode, 8), 3)
        self.assertEquals(LinkedListQuestions.ReturnKthToLast(firstNode, 9), 2)
        self.assertEquals(LinkedListQuestions.ReturnKthToLast(firstNode, 10), 1)

        self.assertRaises(BaseException, LinkedListQuestions.ReturnKthToLast, firstNode, 50)
        self.assertRaises(BaseException, LinkedListQuestions.ReturnKthToLast, firstNode, 11)
        self.assertRaises(BaseException, LinkedListQuestions.ReturnKthToLast, firstNode, 0)
        self.assertRaises(BaseException, LinkedListQuestions.ReturnKthToLast, firstNode, -1)
        self.assertRaises(BaseException, LinkedListQuestions.ReturnKthToLast, firstNode, -15)

    def test_DeleteMiddleNode(self):
        """ Test the delete middle node method """
        testNode = LinkedListQuestions.Node(10)
        testNode = LinkedListQuestions.Node(9, testNode)
        testNode = LinkedListQuestions.Node(8, testNode)
        testNode = LinkedListQuestions.Node(7, testNode)
        testNode = LinkedListQuestions.Node(6, testNode)
        # Remove the 6th node!
        removeNode = testNode
        testNode = LinkedListQuestions.Node(5, testNode)
        testNode = LinkedListQuestions.Node(4, testNode)
        testNode = LinkedListQuestions.Node(3, testNode)
        testNode = LinkedListQuestions.Node(2, testNode)
        testNode = LinkedListQuestions.Node(1, testNode)

        # The node to compare to
        compareNode = LinkedListQuestions.Node(10)
        compareNode = LinkedListQuestions.Node(9, compareNode)
        compareNode = LinkedListQuestions.Node(8, compareNode)
        compareNode = LinkedListQuestions.Node(7, compareNode)
        compareNode = LinkedListQuestions.Node(5, compareNode)
        compareNode = LinkedListQuestions.Node(4, compareNode)
        compareNode = LinkedListQuestions.Node(3, compareNode)
        compareNode = LinkedListQuestions.Node(2, compareNode)
        compareNode = LinkedListQuestions.Node(1, compareNode)

        # Remove node and compare to ensure proper node was deleted
        LinkedListQuestions.DeleteMiddleNode(removeNode)
        self.assertTrue(LinkedListQuestions.Equals(testNode, compareNode))

        testNode = LinkedListQuestions.Node(10)
        testNode = LinkedListQuestions.Node(9, testNode)
        testNode = LinkedListQuestions.Node(8, testNode)
        testNode = LinkedListQuestions.Node(7, testNode)
        testNode = LinkedListQuestions.Node(6, testNode)
        testNode = LinkedListQuestions.Node(5, testNode)
        testNode = LinkedListQuestions.Node(4, testNode)
        testNode = LinkedListQuestions.Node(3, testNode)
        # Remove the 3rd node!
        removeNode = testNode
        testNode = LinkedListQuestions.Node(2, testNode)
        testNode = LinkedListQuestions.Node(1, testNode)

        # The node to compare to
        compareNode = LinkedListQuestions.Node(10)
        compareNode = LinkedListQuestions.Node(9, compareNode)
        compareNode = LinkedListQuestions.Node(8, compareNode)
        compareNode = LinkedListQuestions.Node(7, compareNode)
        compareNode = LinkedListQuestions.Node(6, compareNode)
        compareNode = LinkedListQuestions.Node(5, compareNode)
        compareNode = LinkedListQuestions.Node(4, compareNode)
        compareNode = LinkedListQuestions.Node(2, compareNode)
        compareNode = LinkedListQuestions.Node(1, compareNode)

        # Remove node and compare to ensure proper node was deleted
        LinkedListQuestions.DeleteMiddleNode(removeNode)
        self.assertTrue(LinkedListQuestions.Equals(testNode, compareNode))

        testNode = LinkedListQuestions.Node(10)
        testNode = LinkedListQuestions.Node(9, testNode)
        # Remove the 9th node!
        removeNode = testNode
        testNode = LinkedListQuestions.Node(8, testNode)
        testNode = LinkedListQuestions.Node(7, testNode)
        testNode = LinkedListQuestions.Node(6, testNode)
        testNode = LinkedListQuestions.Node(5, testNode)
        testNode = LinkedListQuestions.Node(4, testNode)
        testNode = LinkedListQuestions.Node(3, testNode)
        testNode = LinkedListQuestions.Node(2, testNode)
        testNode = LinkedListQuestions.Node(1, testNode)

        # The node to compare to
        compareNode = LinkedListQuestions.Node(10)
        compareNode = LinkedListQuestions.Node(8, compareNode)
        compareNode = LinkedListQuestions.Node(7, compareNode)
        compareNode = LinkedListQuestions.Node(6, compareNode)
        compareNode = LinkedListQuestions.Node(5, compareNode)
        compareNode = LinkedListQuestions.Node(4, compareNode)
        compareNode = LinkedListQuestions.Node(3, compareNode)
        compareNode = LinkedListQuestions.Node(2, compareNode)
        compareNode = LinkedListQuestions.Node(1, compareNode)

        # Remove node and compare to ensure proper node was deleted
        LinkedListQuestions.DeleteMiddleNode(removeNode)
        self.assertTrue(LinkedListQuestions.Equals(testNode, compareNode))

    def test_PartitionLinkedList(self):
        """ Test the delete middle node method """
        testNode = LinkedListQuestions.Node(1)
        testNode = LinkedListQuestions.Node(2, testNode)
        testNode = LinkedListQuestions.Node(10, testNode)
        testNode = LinkedListQuestions.Node(5, testNode)
        testNode = LinkedListQuestions.Node(8, testNode)
        testNode = LinkedListQuestions.Node(5, testNode)
        testNode = LinkedListQuestions.Node(3, testNode)

        # The node to compare to
        compareNode = LinkedListQuestions.Node(10)
        compareNode = LinkedListQuestions.Node(5, compareNode)
        compareNode = LinkedListQuestions.Node(8, compareNode)
        compareNode = LinkedListQuestions.Node(5, compareNode)
        compareNode = LinkedListQuestions.Node(1, compareNode)
        compareNode = LinkedListQuestions.Node(2, compareNode)
        compareNode = LinkedListQuestions.Node(3, compareNode)

        # Remove node and compare to ensure proper node was deleted
        LinkedListQuestions.PartitionLinkedList(testNode, 5)
        self.assertTrue(LinkedListQuestions.Equals(testNode, compareNode))

    def test_SumLists(self):
        """ Test SumList methods"""
        num1 = LinkedListQuestions.Node(6)
        num1 = LinkedListQuestions.Node(1, num1)
        num1 = LinkedListQuestions.Node(7, num1)

        num2 = LinkedListQuestions.Node(2)
        num2 = LinkedListQuestions.Node(9, num2)
        num2 = LinkedListQuestions.Node(5, num2)

        result = LinkedListQuestions.Node(9)
        result = LinkedListQuestions.Node(1, result)
        result = LinkedListQuestions.Node(2, result)

        self.assertTrue(LinkedListQuestions.Equals(result, LinkedListQuestions.SumLists(num1, num2)))


        num1 = LinkedListQuestions.Node(9)
        num1 = LinkedListQuestions.Node(9, num1)
        num1 = LinkedListQuestions.Node(9, num1)

        num2 = LinkedListQuestions.Node(9)
        num2 = LinkedListQuestions.Node(9, num2)
        num2 = LinkedListQuestions.Node(9, num2)

        result = LinkedListQuestions.Node(1)
        result = LinkedListQuestions.Node(9, result)
        result = LinkedListQuestions.Node(9, result)
        result = LinkedListQuestions.Node(8, result)

        self.assertTrue(LinkedListQuestions.Equals(result, LinkedListQuestions.SumLists(num1, num2)))


        num1 = LinkedListQuestions.Node(6)
        num1 = LinkedListQuestions.Node(1, num1)
        num1 = LinkedListQuestions.Node(7, num1)
        num1 = LinkedListQuestions.Node(7, num1)
        num1 = LinkedListQuestions.Node(7, num1)

        num2 = LinkedListQuestions.Node(2)
        num2 = LinkedListQuestions.Node(9, num2)
        num2 = LinkedListQuestions.Node(5, num2)

        result = LinkedListQuestions.Node(6)
        result = LinkedListQuestions.Node(2, result)
        result = LinkedListQuestions.Node(0, result)
        result = LinkedListQuestions.Node(7, result)
        result = LinkedListQuestions.Node(2, result)

        self.assertTrue(LinkedListQuestions.Equals(result, LinkedListQuestions.SumLists(num1, num2)))


        num1 = LinkedListQuestions.Node(6)
        num1 = LinkedListQuestions.Node(1, num1)
        num1 = LinkedListQuestions.Node(7, num1)

        num2 = LinkedListQuestions.Node(2)
        num2 = LinkedListQuestions.Node(9, num2)
        num2 = LinkedListQuestions.Node(5, num2)
        num2 = LinkedListQuestions.Node(5, num2)
        num2 = LinkedListQuestions.Node(5, num2)

        result = LinkedListQuestions.Node(3)
        result = LinkedListQuestions.Node(0, result)
        result = LinkedListQuestions.Node(1, result)
        result = LinkedListQuestions.Node(7, result)
        result = LinkedListQuestions.Node(2, result)

        self.assertTrue(LinkedListQuestions.Equals(result, LinkedListQuestions.SumLists(num1, num2)))


    def test_IsPalindrome(self):
        """ Test IsPalindrome method """
        result = LinkedListQuestions.Node('a')
        result = LinkedListQuestions.Node('b', result)
        result = LinkedListQuestions.Node('c', result)
        result = LinkedListQuestions.Node('b', result)
        result = LinkedListQuestions.Node('a', result)

        self.assertTrue(LinkedListQuestions.IsPalindrome(result))

        result = LinkedListQuestions.Node('o')
        result = LinkedListQuestions.Node('e', result)
        result = LinkedListQuestions.Node('e', result)
        result = LinkedListQuestions.Node('o', result)

        self.assertTrue(LinkedListQuestions.IsPalindrome(result))

        result = LinkedListQuestions.Node('a')
        result = LinkedListQuestions.Node('b', result)
        result = LinkedListQuestions.Node('c', result)
        result = LinkedListQuestions.Node('e', result)
        result = LinkedListQuestions.Node('a', result)

        self.assertFalse(LinkedListQuestions.IsPalindrome(result))

        result = LinkedListQuestions.Node('o')
        result = LinkedListQuestions.Node('e', result)
        result = LinkedListQuestions.Node('e', result)
        result = LinkedListQuestions.Node('a', result)

        self.assertFalse(LinkedListQuestions.IsPalindrome(result))

        result = LinkedListQuestions.Node('a')
        result = LinkedListQuestions.Node('a', result)
        result = LinkedListQuestions.Node('e', result)
        result = LinkedListQuestions.Node('i', result)
        result = LinkedListQuestions.Node('p', result)
        result = LinkedListQuestions.Node('p', result)
        result = LinkedListQuestions.Node('p', result)
        result = LinkedListQuestions.Node('i', result)
        result = LinkedListQuestions.Node('e', result)
        result = LinkedListQuestions.Node('a', result)
        result = LinkedListQuestions.Node('a', result)

        self.assertTrue(LinkedListQuestions.IsPalindrome(result))

        result = LinkedListQuestions.Node('a')
        result = LinkedListQuestions.Node('b', result)
        result = LinkedListQuestions.Node('b', result)
        result = LinkedListQuestions.Node('t', result)
        result = LinkedListQuestions.Node('e', result)
        result = LinkedListQuestions.Node('e', result)
        result = LinkedListQuestions.Node('t', result)
        result = LinkedListQuestions.Node('b', result)
        result = LinkedListQuestions.Node('b', result)
        result = LinkedListQuestions.Node('a', result)

        self.assertTrue(LinkedListQuestions.IsPalindrome(result))

        result = LinkedListQuestions.Node('e')
        result = LinkedListQuestions.Node('a', result)
        result = LinkedListQuestions.Node('e', result)
        result = LinkedListQuestions.Node('i', result)
        result = LinkedListQuestions.Node('p', result)
        result = LinkedListQuestions.Node('p', result)
        result = LinkedListQuestions.Node('e', result)
        result = LinkedListQuestions.Node('i', result)
        result = LinkedListQuestions.Node('e', result)
        result = LinkedListQuestions.Node('l', result)
        result = LinkedListQuestions.Node('a', result)

        self.assertFalse(LinkedListQuestions.IsPalindrome(result))

        result = LinkedListQuestions.Node('a')
        result = LinkedListQuestions.Node('b', result)
        result = LinkedListQuestions.Node('o', result)
        result = LinkedListQuestions.Node('t', result)
        result = LinkedListQuestions.Node('e', result)
        result = LinkedListQuestions.Node('e', result)
        result = LinkedListQuestions.Node('t', result)
        result = LinkedListQuestions.Node('b', result)
        result = LinkedListQuestions.Node('b', result)
        result = LinkedListQuestions.Node('a', result)

        self.assertFalse(LinkedListQuestions.IsPalindrome(result))

        result = LinkedListQuestions.Node('x')
        result = LinkedListQuestions.Node('x', result)

        self.assertTrue(LinkedListQuestions.IsPalindrome(result))

        result = LinkedListQuestions.Node('t')
        result = LinkedListQuestions.Node('y', result)

        self.assertFalse(LinkedListQuestions.IsPalindrome(result))

        result = LinkedListQuestions.Node('q')

        self.assertTrue(LinkedListQuestions.IsPalindrome(result))

    def test_CheckIntersection(self):
        """ Test CheckIntersection method in LinkedListQuestions """
        intersect1 = LinkedListQuestions.Node(14)
        intersect2 = LinkedListQuestions.Node(15)

        num1 = LinkedListQuestions.Node(6)
        num1 = LinkedListQuestions.Node(1, num1)
        num1 = LinkedListQuestions.Node(7, num1)
        num1 = LinkedListQuestions.Node(7, num1)
        num1 = LinkedListQuestions.Node(20, num1)
        num1 = LinkedListQuestions.Node(63, num1)

        num2 = LinkedListQuestions.Node(2)
        num2 = LinkedListQuestions.Node(9, num2)
        num2 = LinkedListQuestions.Node(5, num2)
        num2 = LinkedListQuestions.Node(5, num2)
        num2 = LinkedListQuestions.Node(5, num2)

        self.assertFalse(LinkedListQuestions.CheckIntersection(num1, num2))

        num1 = LinkedListQuestions.Node(6)
        num1 = LinkedListQuestions.Node(1, num1)
        num1 = LinkedListQuestions.Node(7, num1)
        intersect1.next = num1
        num1 = LinkedListQuestions.Node(7, intersect1)
        num1 = LinkedListQuestions.Node(20, num1)
        num1 = LinkedListQuestions.Node(63, num1)

        num2 = LinkedListQuestions.Node(2)
        num2 = LinkedListQuestions.Node(9, num2)
        num2 = LinkedListQuestions.Node(5, num2)
        num2 = LinkedListQuestions.Node(5, num2)
        num2 = LinkedListQuestions.Node(5, num2)

        self.assertFalse(LinkedListQuestions.CheckIntersection(num1, num2))

        num1 = LinkedListQuestions.Node(6)
        num1 = LinkedListQuestions.Node(1, num1)
        num1 = LinkedListQuestions.Node(7, num1)
        intersect1.next = num1
        num1 = LinkedListQuestions.Node(7, intersect1)
        num1 = LinkedListQuestions.Node(20, num1)
        num1 = LinkedListQuestions.Node(63, num1)

        num2 = LinkedListQuestions.Node(2)
        num2 = LinkedListQuestions.Node(9, num2)
        num2 = LinkedListQuestions.Node(5, num2)
        intersect1.next = num2
        num2 = LinkedListQuestions.Node(5, intersect1)
        num2 = LinkedListQuestions.Node(5, num2)

        self.assertTrue(LinkedListQuestions.CheckIntersection(num1, num2))

        num1 = LinkedListQuestions.Node(6)
        num1 = LinkedListQuestions.Node(1, num1)
        num1 = LinkedListQuestions.Node(7, num1)
        intersect2.next = num1
        num1 = LinkedListQuestions.Node(7, intersect2)
        num1 = LinkedListQuestions.Node(20, num1)
        num1 = LinkedListQuestions.Node(63, num1)

        num2 = LinkedListQuestions.Node(2)
        num2 = LinkedListQuestions.Node(9, num2)
        num2 = LinkedListQuestions.Node(5, num2)
        intersect2.next = num2
        num2 = LinkedListQuestions.Node(5, intersect2)
        num2 = LinkedListQuestions.Node(5, num2)

        self.assertTrue(LinkedListQuestions.CheckIntersection(num1, num2))

        num1 = LinkedListQuestions.Node(6)
        num1 = LinkedListQuestions.Node(1, num1)
        num1 = LinkedListQuestions.Node(7, num1)
        intersect1.next = num1
        num1 = LinkedListQuestions.Node(7, intersect1)
        num1 = LinkedListQuestions.Node(20, num1)
        intersect2.next = num1
        num1 = LinkedListQuestions.Node(63, intersect2)

        num2 = LinkedListQuestions.Node(2)
        num2 = LinkedListQuestions.Node(9, num2)
        num2 = LinkedListQuestions.Node(5, num2)
        intersect1.next = num2
        num2 = LinkedListQuestions.Node(5, intersect1)
        num2 = LinkedListQuestions.Node(5, num2)

        self.assertTrue(LinkedListQuestions.CheckIntersection(num1, num2))

        num1 = LinkedListQuestions.Node(6)
        num1 = LinkedListQuestions.Node(1, num1)
        num1 = LinkedListQuestions.Node(7, num1)
        intersect1.next = num1
        num1 = LinkedListQuestions.Node(7, intersect1)
        num1 = LinkedListQuestions.Node(20, num1)
        intersect2.next = num1
        num1 = LinkedListQuestions.Node(63, intersect2)

        num2 = LinkedListQuestions.Node(2)
        intersect2.next = num2
        num2 = LinkedListQuestions.Node(9, intersect2)
        num2 = LinkedListQuestions.Node(5, num2)
        intersect1.next = num2
        num2 = LinkedListQuestions.Node(5, intersect1)
        num2 = LinkedListQuestions.Node(5, num2)

        self.assertTrue(LinkedListQuestions.CheckIntersection(num1, num2))

        num1 = LinkedListQuestions.Node(6)
        num1 = LinkedListQuestions.Node(1, num1)
        num1 = LinkedListQuestions.Node(7, num1)
        intersect1.next = num1
        num1 = LinkedListQuestions.Node(7, intersect1)
        num1 = LinkedListQuestions.Node(20, num1)
        intersect2.next = num1
        num1 = LinkedListQuestions.Node(63, intersect2)

        num2 = LinkedListQuestions.Node(2)
        num2 = LinkedListQuestions.Node(5, num2)

        self.assertFalse(LinkedListQuestions.CheckIntersection(num1, num2))

        num1 = LinkedListQuestions.Node(6)
        num1 = LinkedListQuestions.Node(1, num1)
        num1 = LinkedListQuestions.Node(7, num1)
        intersect1.next = num1
        num1 = LinkedListQuestions.Node(7, intersect1)
        num1 = LinkedListQuestions.Node(20, num1)
        num1 = LinkedListQuestions.Node(63, num1)

        num2 = LinkedListQuestions.Node(2)
        intersect2.next = num2
        num2 = LinkedListQuestions.Node(9, intersect2)
        num2 = LinkedListQuestions.Node(5, num2)
        num2 = LinkedListQuestions.Node(5, num2)
        num2 = LinkedListQuestions.Node(5, num2)

        self.assertFalse(LinkedListQuestions.CheckIntersection(num1, num2))

        num1 = LinkedListQuestions.Node(6)
        num1 = LinkedListQuestions.Node(1, num1)
        num1 = LinkedListQuestions.Node(7, num1)
        intersect1.next = num1
        num1 = LinkedListQuestions.Node(7, intersect1)
        num1 = LinkedListQuestions.Node(20, num1)
        intersect2.next = num1
        num1 = LinkedListQuestions.Node(63, intersect2)

        num2 = LinkedListQuestions.Node(2)
        num2 = LinkedListQuestions.Node(9, num2)
        num2 = LinkedListQuestions.Node(5, num2)
        num2 = LinkedListQuestions.Node(5, num2)
        num2 = LinkedListQuestions.Node(5, num2)

        self.assertFalse(LinkedListQuestions.CheckIntersection(num1, num2))

    def test_CheckIntersection(self):
        """ Check the FindLoop method in LinkedLists """
        loop = LinkedListQuestions.Node(14)
        node = loop
        node = LinkedListQuestions.Node(7, node)
        node = LinkedListQuestions.Node(20, node)
        node = LinkedListQuestions.Node(46, node)
        node = LinkedListQuestions.Node(63, node)

        # Insert the loop node
        loop.next = node
        node = loop

        node = LinkedListQuestions.Node(40, node)
        node = LinkedListQuestions.Node(98, node)

        self.assertTrue(LinkedListQuestions.IsSameNode(loop, LinkedListQuestions.FindLoop(node)))

        loop = LinkedListQuestions.Node(14)
        node = loop
        node = LinkedListQuestions.Node(7, node)
        node = LinkedListQuestions.Node(63, node)
        node = LinkedListQuestions.Node(20, node)

        # Insert the loop node
        loop.next = node
        node = loop

        node = LinkedListQuestions.Node(46, node)
        node = LinkedListQuestions.Node(63, node)
        node = LinkedListQuestions.Node(63, node)
        node = LinkedListQuestions.Node(40, node)
        node = LinkedListQuestions.Node(98, node)

        self.assertTrue(LinkedListQuestions.IsSameNode(loop, LinkedListQuestions.FindLoop(node)))

        loop = LinkedListQuestions.Node(14)
        node = loop
        node = LinkedListQuestions.Node(7, node)
        node = LinkedListQuestions.Node(63, node)
        node = LinkedListQuestions.Node(20, node)
        node = LinkedListQuestions.Node(46, node)
        node = LinkedListQuestions.Node(63, node)
        node = LinkedListQuestions.Node(63, node)
        node = LinkedListQuestions.Node(40, node)
        node = LinkedListQuestions.Node(98, node)

        # Insert the loop node
        loop.next = node
        node = loop

        self.assertTrue(LinkedListQuestions.IsSameNode(loop, LinkedListQuestions.FindLoop(node)))

