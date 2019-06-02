#!/home/michael/venv/utilities/bin/python

import argparse
import sys

import git


def run(branch):
    result = git.checkout_new_branch(branch)
    if result.stdout:
        sys.stdout.write(result.stdout)
    if result.stderr:
        sys.stderr.write(result.stderr)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("branch", help="the name of the new branch")
    args = parser.parse_args()

    run(args.branch)
