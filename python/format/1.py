d0 = dict(
    x=1,
    y="abc"
)

d1 = dict(
    x=2,
    y="def"
)

print("{0[x]}, {0[y]}".format(d0, d1))
print("{1[x]}, {1[y]}".format(d0, d1))
