"""
Contains methods related to String Questions from Cracking the Coding Interview
"""
class StringQuestions:
    """
    This class is basically just a namesapce
    """
    def __init__(self):
        """ Constructor does nothing """
        pass

    @staticmethod
    def IsUnique(testStr):
        """
        Test if the passed in string has all unique characters.
        :param testStr: The string to test
        :return: True if all unique characters, False otherwise
        """
        # Loop through all characters to compare
        for i in range(0, len(testStr)):
            for j in range((i+1), len(testStr)):
                # Compare the characters, if equal then string is not unique
                if testStr[i] == testStr[j]:
                    return False

        # We compared all the characters and found no matches
        return True

    @staticmethod
    def IsPermutation(strOne, strTwo):
        """
        Determine whether stings are permutations of each other
        :param strOne: Self explanatory
        :param strTwo: Self explanatory
        :return: True if strings are permuations, False otherwise
        """
        # Character dictionary holds characters as keys and numbers as values
        charDict = {}

        # Strings can't be permutations if they are different sizes
        if len(strOne) != len(strTwo):
            return False

        # Loop over characters in first string and add to map
        for c in strOne:
            try:
                charDict[c] += 1
            except KeyError:
                charDict[c] = 1

        # Loop over characters in second string and decrement from map
        # If a key character is not found, that means the second string has a unique character
        for c in strTwo:
            try:
                charDict[c] -= 1
            except KeyError:
                return False

        # If we haven't returned yet then the strings are the same size and
        # only contain similar characters. Values in map should ALL be zero if
        # the strings contain the same number of each unique character
        for value in charDict.values():
            if value != 0:
                # Strings are not permutations if different number of specific character was found
                return False


        return True

    @staticmethod
    def URLifyString(url, size):
        """
        URLify the passed in string by adding %20 to whitespaces. Assume
        string is long enough to account for increased size. Size is true length of string
        :param url: The string to URLify
        :param size: The true length of the string
        :return: The URLified string
        """
        # First loop through the string searching for whitespace
        urlList = list(url)
        offset = 0
        for index in range(0, (size-1)):
            if urlList[index] is ' ':
                offset += 2

        # With the knowledge of the needed offset, loop backwards through array
        for index in range((size-1), 0, -1):
            # When a space is found
            if urlList[index] is ' ':
                urlList[index + offset] = '0'
                urlList[index + offset - 1] = '2'
                urlList[index + offset - 2] = '%'

                offset -= 2
            else:
                urlList[index + offset] = url[index]

        return "".join(urlList)

    @staticmethod
    def IsPermutatinOfPalindrome(str):
        """
        Determine if string is a permutation of a palindrome. Palindrome does not need
        to consist of dictionary words.
        :param str: The string to test
        :return: The result
        """
        isPalindromePerm = True
        count = 0
        charDict = {}
        # Fill out map which records number of time a character occurs in string
        for c in str:
            if c.isalpha():
                count += 1
                try:
                    charDict[c] += 1
                except KeyError:
                    charDict[c] = 1
            elif c is " ":
                continue
            else:
                raise AttributeError

        foundCenterChar = False
        for value in charDict.values():
            if value % 2 is not 0:
                if count % 2 is not 0:
                    # An odd count is allowed one odd number of characters
                    if foundCenterChar is False:
                        foundCenterChar = True
                    else:
                        isPalindromePerm = False
                        break;
                else:
                    isPalindromePerm = False
                    break;

        return isPalindromePerm

    @staticmethod
    def CheckOneDifferent(str1, str2):
        """
        Check if first string only needs one or zero edits to be equal to string two

        An edit is defined by an addition, removal, or substitution of a character

        :param str1: The string to possibly edit
        :param str2: The string to test against
        :return: The result. True if string one is one edit away, false otherwise
        """
        # Define longer string and shorter string up here. They may be used later
        longerStr = str()
        shorterStr = str()

        # If strings are equal then we are either looking for zero edits or a replacement
        if len(str1) == len(str2):
            foundUnequalChar = False
            count = 0
            while count < len(str1):
                if str1[count] != str2[count]:
                    if foundUnequalChar == False:
                        foundUnequalChar = True
                    else:
                        return False

                count += 1

            # Got through the loop, indicates strings were equal or one replacement from being equla
            return True

        # Check if string one is the larger string
        elif len(str1) == (len(str2) + 1):
            longerStr = str1
            shorterStr = str2
        elif len(str2) == (len(str1) + 1):
            longerStr = str2
            shorterStr = str1
        # String were not equal
        else:
            return False

        # Ok, at this point strings only differ by one character
        offset = 0
        count = 0
        while count < len(shorterStr):
            if shorterStr[count] != longerStr[count+offset]:
                if offset == 0:
                    offset = 1
                else:
                    return False

                continue

            count += 1

        return True

    @staticmethod
    def CompressString(origStr):
        """
        Compresses a string using counts of repeated characters. For example,
        aabcccccaa become a2b1c5a3
        :param origStr: The original non-compressed string
        :return: The compressed string
        """
        occurences = []
        currChar = origStr[0]
        count = 0
        # Create a list that associates number of sequential occurrences of character in origStr
        for c in origStr:
            if c == currChar:
                count += 1
            else:
                occurences.append((currChar,count))
                currChar = c
                count = 1

        # Make sure to add the last run of characters
        occurences.append((currChar,count))

        newStr = ""

        for c,num in occurences:
            newStr += str(c) + str(num)

        if len(newStr) >= len(origStr):
            return origStr

        return newStr

    @staticmethod
    def RotateMatrix(matrix: list, n: int, clockwise: bool):
        """
        Rotate the passed in matrix 90 degrees
        :param matrix: The nxn matrix to rotate
        :param n: Size of the array
        :param clockwise: Determines clockwise or counter-clockwise rotation
        :return: The rotated matrix
        """
        # Contract is that matrix is of nxn size
        # Initialize new matrix to zeros
        rotatedMatrix = [[0 for x in range(n)] for y in range(n)]

        # Rotation entails columns rotating in the rows respectively
        for col in range(0,n):
            for row in range(0,n):
                if clockwise is True:
                    rotatedMatrix[col][n-row-1] = matrix[row][col]
                else:
                    rotatedMatrix[n-1-col][row] = matrix[row][col]

        return rotatedMatrix

    @staticmethod
    def ZeroMatrix(matrix: list, rows: int, columns: int):
        """
        Clears the row and column of any element in the matrix whose
        value is zero.

        :param matrix:
        :param rows:
        :param columns:
        :return:
        """
        # Target rows to clear
        rowsToClear = set()
        columnsToClear = set()

        for col in range(0, columns):
            for row in range(0, rows):
                if matrix[row][col] == 0:
                    rowsToClear.add(row)
                    columnsToClear.add(col)

        for clearRow in rowsToClear:
            StringQuestions._clearRow(matrix, clearRow, columns)

        for clearCol in columnsToClear:
            StringQuestions._clearColumn(matrix, clearCol, rows)

        return matrix

    @staticmethod
    def IsRotation(s1: str, s2: str):
        """
        Determine is string two (s2) is a rotation of string one (s1)
        :param s1: The original string
        :param s2: The string that may be a rotation of s1
        :return: True if s2 is a rotation of s1, False otherwise
        """
        if len(s1) > 0 and (len(s1) == len(s2)):
            # The idea is that a rotation will present a situation where
            # s1 = x+y and s2 = y+x, and so s1s1=x+(y+x)+y will contain y+x (or s2) as a substring
            s1s1 = s1 + s1
            if s2 in s1s1:
                return True

        return False

    @staticmethod
    def _clearRow(matrix: list, row: int, columns: int):
        """
        Clears the row in the matrix
        :param matrix:
        :param row:
        :param columns:
        :return:
        """
        for col in range(0, columns):
            matrix[row][col] = 0

    @staticmethod
    def _clearColumn(matrix: list, col: int, rows: int):
        """
        Clears the column in the matrix
        :param matrix:
        :param col:
        :param rows:
        :return:
        """
        for row in range(0, rows):
            matrix[row][col] = 0




