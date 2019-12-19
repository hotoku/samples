import argparse


class Command:
    def register_subparser(self, subparsers):
        pass

    def handler(self, args):
        pass


class CommandA(Command):
    def register_subparser(self, subparsers):
        parser = subparsers.add_parser("A", help="help of A")
        parser.add_argument("-a",  action="store_true")
        parser.set_defaults(handler=self.handler)

    def handler(self, args):
        print(f"A: {args.a}")


class CommandB(Command):
    def register_subparser(self, subparsers):
        parser = subparsers.add_parser("B", help="help of B")
        parser.add_argument("-b",  action="store_true")
        parser.set_defaults(handler=self.handler)

    def handler(self, args):
        print(f"B: {args.b}")


commands = [CommandA(), CommandB()]

parser = argparse.ArgumentParser(description="sample")
subparsers = parser.add_subparsers()
for c in commands:
    c.register_subparser(subparsers)

args = parser.parse_args()
if hasattr(args, "handler"):
    args.handler(args)
else:
    parser.print_help()
