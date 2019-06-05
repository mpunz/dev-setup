#!/home/michael/venv/utilities/bin/python

import sys

import shell


def checkout(branch):
    cmd = "git checkout {}".format(branch)
    return shell.run(cmd)


def checkout_new_branch(branch):
    cmd = "git checkout -b {}".format(branch)
    return shell.run(cmd)


def checkout_master():
    return checkout("master")


def log():
    cmd = "git log --pretty=oneline"
    return shell.run(cmd)


def porcelain():
    cmd = "git status --porcelain"
    result = shell.run(cmd)
    return not bool(result.stdout)


def pull_origin(branch):
    cmd = "git pull origin {}".format(branch)
    return shell.run(cmd)


def pull_origin_master():
    return pull_origin("master")


def push(branch, force=True):
    cmd = "git push origin {}".format(branch)
    if force:
        user_input = input("Force push? Press [y] to confirm > ")
        if user_input != "y":
            sys.stdout.write("Did not confirm. Quitting.\n")
            return
        cmd += " --force"
    return shell.run(cmd)
