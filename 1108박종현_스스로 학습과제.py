# # deque 라이브러리를 사용하지 않은 경우
# from sys import *
# n = int(stdin.readline())
# deque = []
# for _ in range(n):
#     command = stdin.readline().split()
#     if command[0] == 'push_front':
#         deque.insert(0, command[1])
#     elif command[0] == 'push_back':
#         deque.insert(len(deque), command[1])
#     elif command[0] == 'pop_front':
#         if len(deque) == 0:
#             print(-1)
#         else:
#             print(deque[0])
#             del deque[0]
#     elif command[0] == 'pop_back':
#         if len(deque) == 0:
#             print(-1)
#         else:
#             print(deque[len(deque) - 1])
#             del deque[len(deque) - 1]
#     elif command[0] == 'length':
#         print(len(deque))
#     elif command[0] == 'empty':
#         if len(deque) == 0:
#             print(1)
#         else:
#             print(0)
#     elif command[0] == 'front':
#         if len(deque) == 0:
#             print(-1)
#         else:
#             print(deque[0])
#     elif command[0] == 'back':
#         if len(deque) == 0:
#             print(-1)
#         else:
#             print(deque[len(deque) - 1])

# deque 라이브러리를 사용한 경우

from collections import deque
from sys import *
n = int(stdin.readline())
dq = deque()
for _ in range(n):
    command = stdin.readline().split()
    if command[0] == 'push_front':
        dq.appendleft(command[1])
    elif command[0] == 'push_back':
        dq.append(command[1])
    elif command[0] == 'pop_front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif command[0] == 'pop_back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())
    elif command[0] == 'length':
        print(len(dq))
    elif command[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif command[0] == 'back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[len(dq) - 1])