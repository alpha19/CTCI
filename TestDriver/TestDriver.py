"""
This is the main entry point for Cracking the Coding Interview Work.

This file functions as a basis Test Driver to test the work that
is completed from the book.
"""
import unittest

from ArraysAndStrings.UnitTests_ArraysAndStrings.TestStringQuestions import TestStringQuestions
from LinkedLists.UnitTests_LinkedLists.TestLinkedListQuestions import TestLinkedListQuestions
from StacksAndQueues.UnitTests_StacksAndQueues.UnitTests_Stacks import TestStackQuestions

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringQuestions)

    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestLinkedListQuestions))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestStackQuestions))

    unittest.TextTestRunner(verbosity=2).run(suite)

