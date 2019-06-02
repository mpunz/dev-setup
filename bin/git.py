#!/home/michael/venv/utilities/bin/python

import sys

import shell


def porcelain():
    cmd = "git status --porcelain"
    result = shell.run(cmd)
    return not bool(result.stdout)


def push(branch, force=True):
    cmd = "git push origin {}".format(branch)
    if force:
        user_input = input("Force push? Press [y] to confirm > ")
        if user_input != "y":
            sys.stdout.write("Did not confirm. Quitting.\n")
            return
        cmd += " --force"
    shell.run(cmd)
