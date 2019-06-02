#!/home/michael/venv/utilities/bin/python

import shlex
import subprocess as sp

import attr


@attr.s
class ShellResult:
    stdout = attr.ib()
    stderr = attr.ib()

    @classmethod
    def from_subprocess(cls, result):
        values = [
            getattr(result, descriptor).decode("utf-8")
            for descriptor in ["stdout", "stderr"]
        ]
        return cls(*values)


def run(cmd):
    result = sp.run(shlex.split(cmd), stdout=sp.PIPE, stderr=sp.PIPE)
    return ShellResult.from_subprocess(result)
