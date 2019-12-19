x = dict(x=1)
y = dict(y=2)
z = dict(x=3)

print(dict(x, **y, **z))
