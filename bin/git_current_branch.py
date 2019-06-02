#!/home/michael/venv/utilities/bin/python

import sys

import shell


def get():
    cmd = "git branch"
    result = shell.run(cmd)
    values = [elem for elem in result.stdout.split("\n") if elem]
    return values[0].replace("*", "").strip()


def run():
    current_branch = get()
    sys.stdout.write(current_branch + "\n")


if __name__ == "__main__":

    run()
