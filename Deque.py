'''
DEQUE:- Deque-Double ended queue
--> Combination of stack and queuue
--> Combination of FIFO and LIFO

Operations:

-->append(X)-insert at rear
-->appendleft(x)-insert at front
[]
append(10) [10]
appendLeft(20) [20,10]
append(30) [20,10,30]
appendLeft(40) [40,20,10,30]
Front[40,20,10,30]Rear
Pop()-Removes from rear
[40,20,10]
PopLeft()-removes from front
[20,10]
deque[0]-Front
deque[-1]-Rear
'''

from collections import deque
dq=deque()
#Insert elements
dq.append(10)
dq.append(20)
dq.appendleft(5)
print(dq)
dq.pop()
dq.popleft()
print(dq)