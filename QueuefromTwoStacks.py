#Queue with the following method
'''
enqueue : Insert an item at the back of the queue.
dequeue : Remove an item from the front of the queue.
peek/front : Retrieve an item at the front of the queue without removing it.
empty/size : Check whether the queue is empty or give its size.

One improvement compared with OneListQueue is that this one avoid inefficient insert(0,item)
method in OneListQueue.py
'''

import os
import glob
import re
import sys
import math
import fnmatch
from operator import itemgetter

class My_Queue( object ):
    ''' the class for a queue'''
    def __init__(self):
        self.in_stack = [ ]
        self.out_stack = [ ]

    def isEmpty(self):
        return ( (self.in_stack == [ ])  and (self.out_stack == [ ]) )


    def enqueue(self, item):
        '''Notice that the insert method is inefficient in Python'''
        self.in_stack.append(item)

    def dequeue(self):
        if self.out_stack:
            return self.out_stack.pop()
        while(self.in_stack):
            self.out_stack.append( self.in_stack.pop( ) )
        if not self.out_stack:
            raise Exception('Queue is Empty')
        return self.out_stack.pop( )

    def size(self):
        return len(self.in_stack)+len(self.out_stack)

    def peek(self):
        if  self.out_stack:
            '''The index method is really powerful'''
            return self.out_stack[-1]
        while(self.in_stack):
            self.out_stack.append( self.in_stack.pop( ) )
        if  self.out_stack:
            return self.out_stack[ -1 ]
        else:
            return None

def main( ):
    queue = My_Queue( )
    queue.enqueue('one')
    queue.enqueue('two')
    queue.enqueue('three')
    print "expect 3 return " + str(queue.size( ))
    print "expect one return "+ str(queue.peek( ))
    print "expect one return " + str(queue.dequeue( ))
    print "expect two return " + str(queue.peek( ))

if __name__ == '__main__':
    main( )
