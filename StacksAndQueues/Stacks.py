"""
Contains methods and classes related to Stack and Queue Questions from Cracking the Coding Interview
"""

class MultipleStacks:
    """
    Class to represent multiple stacks. Default is five stacks but this
    value is arbitrary and an be changed without breaking any functionality.

    TODO: Make the stacks sizes resizable so that they can grow to fit demand.
    Also just making a comment to test pushes out and stuff.

    """
    NUM_STACKS = 5

    def __init__(self, default_size=10):
        self.size = default_size
        self.stacks = [None] * MultipleStacks.NUM_STACKS * self.size
        self.offsets = [-1] * MultipleStacks.NUM_STACKS

    def _getIndex(self, stack_num):
        """
        Retrieves the index of the top of the stack denoted by the stack number

        :param stackNum: The stack requested
        :return: The index corresponding to the top
        """
        return (self.size * stack_num) + self.offsets[stack_num]

    def isEmpty(self, stack_num):
        return self.offsets[stack_num] < 0

    def isFull(self, stack_num):
        return (self.offsets[stack_num] + 1) >= self.size

    def push(self, stack_num, item):
        if self.isFull(stack_num):
            raise Exception("STACK " + str(stack_num) + " IS FULL!")

        self.offsets[stack_num] += 1
        self.stacks[self._getIndex(stack_num)] = item

    def pop(self, stack_num):
        if self.isEmpty(stack_num):
            raise Exception("STACK " + str(stack_num) + " IS EMPTY!")

        item = self.stacks[self._getIndex(stack_num)]

        self.stacks[self._getIndex(stack_num)] = None
        self.offsets[stack_num] -= 1

        return item

    def peek(self, stack_num):
        if self.isEmpty(stack_num):
            raise Exception("STACK " + str(stack_num) + " IS EMPTY!")

        return self.stacks[self._getIndex(stack_num)]

class StackMin:
    """
    Class that implements a stack while also keeping track of minimum
    element in the stack.
    """
    class StackNode:
        """
        A node. Data structure used to implement the stack
        """
        def __init__(self, val, minVal, next=None):
            self.val = val
            self.min = minVal
            self.next = next

    self.top = None

    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, val):
        # No elements? Then just push to top node
        if self.top is None:
            self.top = StackMin.StackNode(val, val)
        # If current min is less than new value then retain minimum
        elif self.top.min <= val:
            self.top = StackMin.StackNode(val, self.top.min, self.top)
        else:
            self.top = StackMin.StackNode(val, val, self.top)

    def pop(self):
        if self.isEmpty():
            raise BaseException("NO ELEMENTS IN STACK!!")

        tempVal = self.top.val
        self.top = self.top.next

        return tempVal

    def min(self):
        if self.isEmpty():
            raise BaseException("NO ELEMENTS IN STACK!!")

        return self.top.min

class StackOfPlates:
    """
    Implementation of a stack that will create a new sub-stack once the
    defined threshold value is reached. Implementation behavior should be
    abstracted to the user (who just see this as a normal stack).

    Note: Useful to think about this implementation as similar to a stack of plates.
          Once the plates are stacked high enough, the a new sub-stack is created.
    """
    def __init__(self, threshold=10):
        self.threshold = threshold
        self.num_sub_stacks = 0
        self.offset = -1
        self.sub_stacks = []

    def __is_empty(self):
        return (self.num_sub_stacks == 0 and self.offset < 0)

    def push(self, val):
        # First need to increment the offset to ensure data isn't overwritten
        self.offset += 1

        # Check if threshold is exceeded. If so, create new stack and enter list
        # Also check if offset is zero. This handles the special case where there are NO elements
        if self.offset >= self.threshold or self.offset == 0:
            # Create a new stack
            newStack = [None] * self.threshold

            self.sub_stacks.append(newStack)
            self.offset = 0
            self.num_sub_stacks += 1

        # Add the element
        self.sub_stacks[self.num_sub_stacks - 1][self.offset] = val

    def pop(self):
        # Check if overall stack is empty. If so, throw exception
        if self.__is_empty():
            raise Exception("EMPTY STACK!!!")

        # Remove the element, erase value in stack, then decrement offset
        val = self.sub_stacks[self.num_sub_stacks - 1][self.offset]

        self.sub_stacks[self.num_sub_stacks - 1][self.offset] = None
        self.offset -= 1

        # Check if the current sub-stack is now empty. Update accordingly
        if self.offset < 0:
            # Remove last stack (which is now empty
            del self.sub_stacks[-1]
            self.num_sub_stacks -= 1

            # If
            if self.num_sub_stacks > 0:
                self.offset = self.threshold - 1
