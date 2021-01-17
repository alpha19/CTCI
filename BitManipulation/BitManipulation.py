class BitHelpers:
    @staticmethod
    def Is32Bit(n: int):
        try:
            bitstring = bin(n)
        except (TypeError, ValueError):
            return False

        if len(bin(n)[2:]) <= 32:
            return True

        return False

"""
Contains methods related to Bit Manipulation Questions from Cracking the Coding Interview
"""
class BitManipulationQuestions:
    """
    This class is basically just a namespace
    """
    @staticmethod
    def Insertion(N: int, M: int, i: int, j: int) -> int:
        """

        :param M:
        :param N:
        :param i:
        :param j:
        :return:
        """
        if not BitHelpers.Is32Bit(M) or not BitHelpers.Is32Bit(N):
            raise ValueError("Not a 32-bit number!!")

        if i < j:
            raise ValueError("i is less than j!!")

        maxBitVal = 31
        if i >  31:
            raise ValueError("i is out of range!")

        topClear = maxBitVal - i
        oneBits = int(1 << 32) - 1

        # Clear unnecessary N bits..
        M = M & (~(oneBits << (i - j + 1)) & oneBits)
        mask =  ~((oneBits >> (maxBitVal - i)) & (oneBits << j))

        return (mask & N) | (M << j)