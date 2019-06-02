#!/home/michael/venv/utilities/bin/python

import argparse
import sys

import git
import git_current_branch


def run(force):
    current_branch = git_current_branch.get()
    if current_branch == "master":
        sys.stdout.write("Current branch is `master`. This is not allowed. Quitting....\n")
        return

    result = git.push(current_branch, force)
    if result.stdout:
        sys.stdout.write(result.stdout)
    if result.stderr:
        sys.stdout.write(result.stderr)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    run(args.force)
