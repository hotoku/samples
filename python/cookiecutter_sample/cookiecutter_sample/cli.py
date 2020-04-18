"""Console script for cookiecutter_sample."""
import argparse
import sys
from cookiecutter_sample import doit


def main():
    """Console script for cookiecutter_sample."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    doit(args)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
