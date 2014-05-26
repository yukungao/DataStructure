#Queue with the following method
'''
enqueue : Insert an item at the back of the queue.
dequeue : Remove an item from the front of the queue.
peek/front : Retrieve an item at the front of the queue without removing it.
empty/size : Check whether the queue is empty or give its size.

'''
class Node( object ):
    def __Init__(self, value):
        self.value = value
        self.next = None
class LinkedQueue( object ):

    def __init__( self ):
        self.front = None
        self.back = None

    def isEmpty( self ):
        return bool(self.front) and bool(self.back)

    def dequeue( self ):
        if self.front:
            value = self.front.value
            self.front = self.front.next
            return value
        raise Exception('Queue  is empty')

    def enqueue(self, value):
        node = Node(value)
        if self.front:
            self.back.next = node
        else:
            self.front = node
        self.back = node
        return True

    def size( self ):
        node = self.front
        if node:
            num_nodes = 1
            node = node.next
            while node:
                num_nodes += 1
                node = node.next
        return num_nodes

    def peek(self):
        return self.front.value

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
