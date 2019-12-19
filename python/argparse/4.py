import argparse


parser = argparse.ArgumentParser()
parser.add_argument("vals", nargs="*")


args = parser.parse_args(["a", "b", "c"])
print(args.vals)
