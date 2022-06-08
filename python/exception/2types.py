def f(n):
    try:
        assert n > 0, "n <= 0"
        if n == 1:
            raise Exception("n=1")
        else:
            pass
    except (Exception, AssertionError) as e:
        print(type(e), e)


f(0)
f(1)
