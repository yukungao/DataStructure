#Queue with the following method
'''
enqueue : Insert an item at the back of the queue.
dequeue : Remove an item from the front of the queue.
peek/front : Retrieve an item at the front of the queue without removing it.
empty/size : Check whether the queue is empty or give its size.

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
        self.items = [ ]

    def isEmpty(self):
        return self.items == [ ]

    def enqueue(self, item):
        '''Notice that the insert method is inefficient in Python'''
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.isEmpty( ):
            '''The index method is really powerful'''
            return self.items[-1]
        else:
            raise Exception('Queue is empty')

def main( ):
    queue = My_Queue( )
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print queue.size( )
    print queue.peek( )
    print queue.dequeue( )
    print queue.peek( )

if __name__ == '__main__':
    main( )
