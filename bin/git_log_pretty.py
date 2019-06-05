#!/home/michael/venv/utilities/bin/python

import sys

import attr

import git


@attr.s
class Entry:
    commit_hash = attr.ib()
    message = attr.ib()

    @classmethod
    def from_line(cls, line):
        commit_hash, message = line[:40], line[41:]
        return cls(commit_hash, message)


def run():
    result = git.log()
    raw_entries = [line for line in result.stdout.split("\n")]
    entries = [Entry.from_line(line) for line in raw_entries if line]
    for entry in entries:
        sys.stdout.write(entry.commit_hash + " " + entry.message + "\n")


if __name__ == "__main__":

    run()
