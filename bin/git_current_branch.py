#!/home/michael/venv/utilities/bin/python

import sys

import shell


def run():
    cmd = "git branch"
    result = shell.run(cmd)
    values = [elem for elem in result.stdout.split("\n") if elem]
    branch = values[0].replace("*", "").strip()
    sys.stdout.write(branch + "\n")


if __name__ == "__main__":

    run()
