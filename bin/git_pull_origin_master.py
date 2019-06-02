#!/home/michael/venv/utilities/bin/python

import sys

import git


def run():
    result = git.pull_origin_master()
    if result.stdout:
        sys.stdout.write(result.stdout)
    if result.stderr:
        sys.stderr.write(result.stderr)


if __name__ == "__main__":

    run()
