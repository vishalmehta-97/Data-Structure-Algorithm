'''STACK'''

''' One way is to use it with the array '''
stack=[]  
stack.append("1")
stack.append("2")
stack.append("3")
stack.append("4")
print(stack)
stack.pop()
print(stack)
print(stack[-1])
print('Size-->',len(stack))


''' One way is by Using deque from Collections '''

from collections import deque

stack=deque()
stack.append('1')
stack.append('2')
stack.append('3')
print(stack)
stack.pop()
print(stack)
print(stack[-1])
print('Size',len(stack))

print(('-')*50)

'''QUEUE'''
from collections import deque

queue=deque()

queue.append("1")
queue.append("2")
queue.append("3")
queue.append("4")
print(queue)
queue.popleft()
print(queue)
print("Top->",queue[0])
print('Size',len(queue))


print(('-')*50)

## Another way is to use
from queue import Queue

queue=Queue(maxsize=10)
queue.put("A")
queue.put("B")
queue.put("C")
print(queue.queue)
queue.get()
print(queue.queue)

print("is empty?",queue.empty())
print("Current Size",queue.qsize())
