from collections import deque

x = deque()
x.append(1)
print(x)
x.append(2)
x.append(3)
print(x)
x.pop()  # 後ろから捨てられる
print(x)
x.popleft()
print(x)  # 前から捨てられる
print(x[0])
