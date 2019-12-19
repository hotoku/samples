import argparse


class Command:
    def __init__(self, subparsers):
        self.parser = subparsers.add_parser(self.name,
                                            help=self.__doc__)
        self.register_argument()
        self.parser.set_defaults(handler=self.handler)

    def register_argument(self): pass

    def handler(self, args): pass


class CommandA(Command):
    "command A"
    name = "A"

    def __init__(self, subparsers):
        super(CommandA, self).__init__(subparsers)

    def register_argument(self):
        self.parser.add_argument("-a",  action="store_true")

    def handler(self, args):
        print(f"A: {args.a}")


class CommandB(Command):
    "command B"
    name = "B"

    def __init__(self, subparsers):
        super(CommandB, self).__init__(subparsers)

    def register_argument(self):
        self.parser.add_argument("-b",  action="store_true")

    def handler(self, args):
        print(f"B: {args.b}")


commands = [CommandA, CommandB]

parser = argparse.ArgumentParser(description="sample")
subparsers = parser.add_subparsers()
for c in commands:
    c(subparsers)

args = parser.parse_args()
if hasattr(args, "handler"):
    args.handler(args)
else:
    parser.print_help()
