"""
Tests various methods from StringQuestions
"""
import unittest
from ArraysAndStrings.StringQuestions import *

class TestStringQuestions(unittest.TestCase):
    """ Class for test methods """

    def test_IsUnique(self):
        """ Test IsUnique method """
        self.assertTrue(StringQuestions.IsUnique("notapedml"))
        self.assertTrue(StringQuestions.IsUnique("asdfghjkl"))

        self.assertFalse(StringQuestions.IsUnique("aa"))
        self.assertFalse(StringQuestions.IsUnique("thisshoulddefinitelyhaveduplicates"))
        self.assertFalse(StringQuestions.IsUnique("aaa"))
        self.assertFalse(StringQuestions.IsUnique("idonbwantbtobabe"))


    def test_IsPermutation(self):
        """ Test IsPermutation method """
        self.assertTrue(StringQuestions.IsPermutation("abee", "baee"))
        self.assertTrue(StringQuestions.IsPermutation("aloha", "aaolh"))
        self.assertTrue(StringQuestions.IsPermutation("fantastic", "fctatisan"))

        self.assertFalse(StringQuestions.IsPermutation("hello", "bad"))
        self.assertFalse(StringQuestions.IsPermutation("monkey", "saturd"))
        self.assertFalse(StringQuestions.IsPermutation("wonderful", "youdlkfgt"))

    def test_URLify(self):
        """ Test URLify method """
        self.assertEquals(StringQuestions.URLifyString("Mr John Smith    ", 13), "Mr%20John%20Smith")
        self.assertEquals(StringQuestions.URLifyString("I am a happy man        ", 16), "I%20am%20a%20happy%20man")

    def test_IsPalindromePermutation(self):
        """ Test IsPalindromePermutation method """
        self.assertTrue(StringQuestions.IsPermutatinOfPalindrome("tact coa"))
        self.assertTrue(StringQuestions.IsPermutatinOfPalindrome("tjjtaaa"))
        self.assertTrue(StringQuestions.IsPermutatinOfPalindrome("apooap"))
        self.assertTrue(StringQuestions.IsPermutatinOfPalindrome("apkkp"))
        self.assertTrue(StringQuestions.IsPermutatinOfPalindrome("ababababooo"))

        self.assertFalse(StringQuestions.IsPermutatinOfPalindrome("tact coaa"))
        self.assertFalse(StringQuestions.IsPermutatinOfPalindrome("aaabbbococ"))
        self.assertFalse(StringQuestions.IsPermutatinOfPalindrome("abdkfjgtlskfdl"))

    def test_CheckOneDifferent(self):
        """ Test CheckOneDifferent method """
        self.assertFalse(StringQuestions.CheckOneDifferent("abbadyui", "abbaetvui"))
        self.assertFalse(StringQuestions.CheckOneDifferent("moreon", "ohmygoodnesss"))
        self.assertFalse(StringQuestions.CheckOneDifferent("akdlf", "akpll"))
        self.assertFalse(StringQuestions.CheckOneDifferent("aboutand", "aboptan"))
        self.assertFalse(StringQuestions.CheckOneDifferent("aboutand", "abotpnd"))
        self.assertFalse(StringQuestions.CheckOneDifferent("ambein", "albeit"))
        self.assertFalse(StringQuestions.CheckOneDifferent("happily", "hoppilp"))
        self.assertFalse(StringQuestions.CheckOneDifferent("happily", "happilydfghdfghdfg"))

        self.assertTrue(StringQuestions.CheckOneDifferent("aboutand", "abotand"))
        self.assertTrue(StringQuestions.CheckOneDifferent("whichiver", "whicheiver"))
        self.assertTrue(StringQuestions.CheckOneDifferent("happily", "hoppily"))
        self.assertTrue(StringQuestions.CheckOneDifferent("boomer", "boomer"))

    def test_CompressString(self):
        """ Test CompressString method """
        self.assertEquals(StringQuestions.CompressString("aabcccccaaa"), "a2b1c5a3")

    def test_RotatedMatrix(self):
        """ Test RotatedMatrix method """
        nineElementMatrix = [[1, 4 ,7], [2, 5, 8], [3, 6, 9]]
        counterNineMatrix = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
        clockNineMatrix   = [[3, 2, 1], [6, 5, 4], [9, 8,7 ]]

        self.assertEquals(StringQuestions.RotateMatrix(nineElementMatrix, 3, False), counterNineMatrix)
        self.assertEquals(StringQuestions.RotateMatrix(nineElementMatrix, 3, True), clockNineMatrix)

        sixteenElementMatrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        counterSixteenMatrix = [[4, 8, 12, 16], [3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13]]
        clockSixteenMatrix   = [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]

        self.assertEquals(StringQuestions.RotateMatrix(sixteenElementMatrix, 4, False), counterSixteenMatrix)
        self.assertEquals(StringQuestions.RotateMatrix(sixteenElementMatrix, 4, True), clockSixteenMatrix)

    def test_ZeroMatrix(self):
        """ Test ZeroMatrix method """
        matrix = [[1, 4 ,7], [2, 5, 8], [3, 6, 9]]
        clearedMatrix = [[1, 4 ,7], [2, 5, 8], [3, 6, 9]]
        self.assertEquals(StringQuestions.ZeroMatrix(matrix, 3, 3), clearedMatrix)

        matrix = [[1, 4 ,7], [2, 0, 8], [3, 6, 9]]
        clearedMatrix = [[1, 0 ,7], [0, 0, 0], [3, 0, 9]]
        self.assertEquals(StringQuestions.ZeroMatrix(matrix, 3, 3), clearedMatrix)

        matrix = [[1, 0 ,7], [2, 5, 8], [3, 6, 9]]
        clearedMatrix = [[0, 0 ,0], [2, 0, 8], [3, 0, 9]]

        self.assertEquals(StringQuestions.ZeroMatrix(matrix, 3, 3), clearedMatrix)

        matrix = [[1, 4 ,7], [0, 5, 8], [3, 6, 9], [3, 0, 9]]
        clearedMatrix = [[0, 0 ,7], [0, 0, 0], [0, 0, 9], [0, 0, 0]]

        self.assertEquals(StringQuestions.ZeroMatrix(matrix, 4, 3), clearedMatrix)

        matrix = [[1, 1 ,0], [1, 1, 1], [1, 1, 0]]
        clearedMatrix = [[0, 0 ,0], [1, 1, 0], [0, 0, 0]]

        self.assertEquals(StringQuestions.ZeroMatrix(matrix, 3, 3), clearedMatrix)

        matrix = [[0, 1 ,1], [1, 1, 1], [0, 1, 1]]
        clearedMatrix = [[0, 0 ,0], [0, 1, 1], [0, 0, 0]]

        self.assertEquals(StringQuestions.ZeroMatrix(matrix, 3, 3), clearedMatrix)

        matrix = [[0, 0, 1], [1, 1, 1], [0, 1, 1]]
        clearedMatrix = [[0, 0 ,0], [0, 0, 1], [0, 0, 0]]

        self.assertEquals(StringQuestions.ZeroMatrix(matrix, 3, 3), clearedMatrix)

    def test_IsRotation(self):
        """ Test IsRoatation method """
        s1 = "erbottlewat"
        s2 = "waterbottle"
        self.assertTrue(StringQuestions.IsRotation(s1,s2))

        s1 = "hunkdory"
        s2 = "doryhunk"
        self.assertTrue(StringQuestions.IsRotation(s1,s2))

        s1 = "hellolord"
        s2 = "ordhellol"
        self.assertTrue(StringQuestions.IsRotation(s1,s2))

        s1 = "afksadf"
        s2 = "asd"
        self.assertFalse(StringQuestions.IsRotation(s1,s2))

        s1 = "helloburt"
        s2 = "butrhello"
        self.assertFalse(StringQuestions.IsRotation(s1,s2))