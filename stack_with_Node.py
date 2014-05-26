#linked_stack

import os
import glob
import re
import sys
import math
import fnmatch
from operator import itemgetter

class Node (object):
    def __init__(self, value=None):
        self.value = value
        self.next = None

class StackwithNodes(object):
    '''Define the stack with nodes'''
    def __init__(self) :
        self.top = None
    def isEmpty(self):
        return bool (self.top)
    def pop(self):
        node = self.top
        '''If stack is not empty, we make the second node as the top
        and return the value of current Node'''
        if node:
            self.top = node.next
            return node.value
        else:
            raise Exception('stack is empty')

    def push(self, value) :
        node = Node(value)
        node.next  = self.top
        self.top = node

    def size(self):
        node = self.top
        if node : num_nodes = 1
        else:  return 0
        node = node.next
        while node:
            num_nodes += 1
            node = node.next
        return num_nodes

    def peek(self):
        if self.size():
            return self.top.value
        else:
            raise Exception('stack is empty')


def main( ):
    stack = StackwithNodes( )

    stack.push(1)
    stack.push('happy')
    stack.push('Python is soooooo strong')

    print( stack.size( ))
    print( stack.peek( ))
    print( stack.pop( ))
    print( stack.peek( ))

if __name__ == '__main__':
        main( )
