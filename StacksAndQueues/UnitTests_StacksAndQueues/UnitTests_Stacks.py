"""
Tests various  stack classes and methods
"""
import unittest
from StacksAndQueues.Stacks import *

class TestStackQuestions(unittest.TestCase):
    """ Class for unit test methods """

    def test_MultiStack(self):
        """ Test the multi-stack """
        stacks = MultipleStacks()

        stacks.push(4, 5)
        stacks.push(4, 6)
        stacks.push(4, 8)

        for count in range(8):
            stacks.push(1, count)

        stacks.push(3,1)
        stacks.push(3,6)

        self.assertTrue(stacks.peek(3) == 6)
        self.assertTrue(stacks.peek(4) == 8)
        self.assertTrue(stacks.peek(1) == 7)
        self.assertRaises(BaseException, stacks.peek, 2)

        stacks.pop(4)
        stacks.pop(4)

        self.assertTrue(stacks.pop(4) == 5)
        self.assertRaises(BaseException, stacks.pop, 4)

    # TODO: Unit test stack minimum class

    # TODO: Unit test stack of plates


