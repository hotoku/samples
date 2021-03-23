X = type("X", (), dict(
    x=1
))
X.x  # => 1


Y = type("Y", (X,), dict(
    y=10
))
Y.x  # => 1
Y.y  # => 10

x = X()
y = Y()
