"""
Contains methods related to Linked List Questions from Cracking the Coding Interview
"""
class LinkedListQuestions:
    """
    This class is basically just a namespace
    """
    def __init__(self):
        """ Constructor does nothing """
        pass

    class Node:
        def __init__(self, data=0, next=None):
            self.data = data
            self.next = next

    @staticmethod
    def IsSameNode(node1: Node, node2: Node):
        """
        Determines if nodes are same (based on reference)

        :param node1: The first node
        :param node2: The second node
        :return: True is nodes are identical, false otherwise
        """
        return id(node1) == id(node2)

    @staticmethod
    def Equals(node1: Node, node2: Node):
        """
        Determines if the linked lists denoted by node1 and node2 are equal.
        Equality is specified by the same elements in the same order

        :param node1: The first node
        :param node2: The second node
        :return: True if Linked Lists are equal, False otherwise
        """
        # Technically if both nodes are null they are the same
        if node1 is None and node2 is None:
            return True

        if node1 is None or node2 is None:
            return False

        while True:
            if node1.data != node2.data:
                return False

            if node1.next is None or node2.next is None:
                if node1.next is not None or node2.next is not None:
                    return False

                return True

            node1 = node1.next
            node2 = node2.next

        return True

    @staticmethod
    def RemoveDuplicates(head: Node):
        """
        Removes any duplicate data elements from a linked list.

        :param head: The start of the linked list (the head node)
        :return: Do not return anything
        """
        p1 = head

        while p1 is not None and p1.next is not None:
            p2 = p1
            while p2.next is not None:
                if p1.data == p2.next.data:
                    p2.next = p2.next.next
                    continue

                p2 = p2.next

            p1 = p1.next

    @staticmethod
    def ReturnKthToLast(head: Node, k: int):
        """
        Return the kth to last element in a singly linked list

        :param head: The start of the linked list (the head node)
        :param k: The kth to last element to return
        :return: The kth to last element
        """

        if head is None:
            raise BaseException("Head is NULL!")
        if k <= 0:
            raise BaseException("k cannot be zero or negative. 0 to last element makes no sense.")

        # Set the lead pointer
        lead = head

        for i in range(0, k):
            if lead is None:
                raise BaseException(str(k) + "th to last element does not exist!")

            lead = lead.next

        while lead is not None:
            head = head.next
            lead = lead.next

        return head.data

    @staticmethod
    def DeleteMiddleNode(middle: Node):
        """
        Deletes the passed in middle node from singly linked list.
        Note: The passed in middle node shall not be the first or last element in linked list

        :param middle: The middle node (does not have to be in the direct middle
        :return:
        """
        if middle is None:
            raise Exception("Empty element!")

        if middle.next is None:
            raise Exception("OMG that was the last element!")

        middle.data = middle.next.data
        middle.next = middle.next.next

    @staticmethod
    def PartitionLinkedList(head: Node, partitionVal):
        """
        Partitions a linked list around a value. Anything less than the partition value
        goes before any value more than or equal to the partition value. Other than these
        two groups (e.g. less than partition and more than partition groups) order doesn't matter

        :param head: The linked list to partition
        :param partitionVal: The partition value
        :return: The partitioned linked list
        """
        if head is None:
            raise Exception("Empty linked list!")

        lessThanHead = None
        lessThanCur = None
        moreThanHead = None
        moreThanCur = None

        while head is not None:
            if head.data < partitionVal:
                # Check to see if head has been set yet
                if lessThanHead is None:
                    lessThanHead = head
                    lessThanCur = head
                else:
                    lessThanCur.next = head
                    lessThanCur = lessThanCur.next
            else:
                # Check to see if head has been set yet
                if moreThanHead is None:
                    moreThanHead = head
                    moreThanCur = head
                else:
                    moreThanCur.next = head
                    moreThanCur = moreThanCur.next

            head = head.next

        lessThanCur.next = moreThanHead
        moreThanCur.next = None

        return lessThanHead

    @staticmethod
    def SumLists(head1: Node, head2: Node):
        """
        Add two numbers represented as linked lists. Head pointer points to the 1's digits, then 10's
        and so on.

        :param head1: The first number
        :param head2: The second number
        :return: Head pointer to added linked list
        """
        if head1 is None and head2 is None:
            raise Exception("Empty linked lists!")
        # Return the non-empty pointer if one linked list is empty
        if head1 is None:
            return head2
        if head2 is None:
            return head1

        carryOver = 0
        # The result head will point to the sum that is calculated
        resultHead = head1
        # Now we have something to work with
        while head1 is not None:
            value = int()
            if head2 is not None:
                value = (head1.data + head2.data + carryOver)
            else:
                value = head1.data + carryOver

            head1.data = value % 10
            carryOver = int(value / 10)

            if head2 is not None:
                head2 = head2.next

            # If the first linked list runs out of digits but second linked list still
            # has a few, then put the rest of the digits in the first linked list
            # NOTE: Will still need to deal with carry over
            if head2 is not None and head1.next is None:
                head1.next = head2
                head2 = None

            # Create a new digit if end of numbers are reached and carry over bit is set
            if head1.next is None and carryOver > 0:
                head1.next = LinkedListQuestions.Node(carryOver)
                carryOver = 0


            head1 = head1.next

        return resultHead

    @staticmethod
    def IsPalindrome(head: Node):
        """
        Determines if the word represented by the passed in list of characters is a palindrome

        :param head: The beginning of the word linked list
        :return: True if linked list is a palindrom, False otherwise
        """
        if head is None:
            raise Exception("EMPTY LIST!!!")

        # A single character word is a palindrome according to my definition
        if head.next is None:
            return True

        while head is not None and head.next is not None:
            comparison = head
            # Move to the end of the word (linked list)
            while comparison.next.next is not None:
                comparison = comparison.next

            # If the compared elements are unequal then we do NOT have a palindrome.
            if head.data != comparison.next.data:
                return False

            comparison.next = None
            head = head.next

        return True

    @staticmethod
    def CheckIntersection(node1: Node, node2: Node):
        """
        Checks whether passed in linked lists intersect (by reference). Intersection
        is denoted by linked lists containing a shared element by reference.

        :param node1: The first node
        :param node2: The second node
        :return: True if linked list intersect, False otherwise
        """
        if node1 is None or node2 is None:
            raise Exception("EMPTY LISTS!!!")

        intersectDict = {}

        while node1 is not None:
            intersectDict[id(node1)] = True
            node1 = node1.next

        while node2 is not None:
            if intersectDict.get(id(node2), False) == True:
                return True

            node2 = node2.next

        return False

    @staticmethod
    def FindLoop(head: Node):
        """
        Find the node at the beginning of the circular loop in a linked list

        Example:

        Input: A -> B -> C -> -> D -> E -> C
        Output: C

        :param head: The beginning of the linked list
        :return: The node that is the starting point of the circular loop
        """
        if head is None:
            raise Exception("Linked list is empty!")

        refDict = {}
        while head is not None:
            if id(head) in refDict:
                # We found the duplicate!
                return head

            refDict[id(head)] = True
            head = head.next

        return None

