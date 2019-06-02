#!/bin/bash

DIRBIN=$1

for f in $(ls $DIRBIN | grep -v shell.py)
do
	ln -s $DIRBIN/$f $(echo $DIRBIN/$f | sed 's/\.py//')
done
