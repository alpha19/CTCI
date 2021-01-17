"""
compares various methods from BitManipulationQuestions
"""
import unittest
from BitManipulation.BitManipulation import *

class TestBitManipulationQuestions(unittest.TestCase):
    """ Class for test methods """

    def test_Insertion(self):
        """ Test Insertion method """
        N = int("10000000000", 2)
        M = int("10011", 2)
        res = int("10001001100", 2)

        self.assertEquals(BitManipulationQuestions.Insertion(N, M, 6, 2), res)