def child():
    print("start child")
    ret = yield "yield from child"
    print("ret in child:", ret)
    return "return from child"


def parent():
    print("start parent")
    ret = yield from child()
    print("ret in parent:", ret)
    ret = yield "yield from parent"
    print("ret in parent:", ret)


def main():
    print("start main")
    p = parent()
    print("sending to parent 1")
    ret = p.send(None)
    print("ret in main:", ret)
    print("sending to parent 2")
    ret = p.send("sent from main")  # type: ignore
    print("ret in main:", ret)


main()

# start main
# sending to parent 1
# start parent
# start child
# ret in main: yield from child
# sending to parent 2
# ret in child: sent from main
# ret in parent: return from child
# ret in main: yield from parent
