#!/bin/bash
#before running for the first time, edit python path in PREFERENCES so that the first path is python 3.6

echo starting
cd /usr/bin

ls -ltar python*
alias python='python3.6'

sudo unlink python &&  sudo ln -s python3.6 python
sudo unlink pip &&  sudo ln -s pip-3.6 pip
echo done

echo changing alias
alias python='python3.6'
cd /usr/bin
ls -ltar python*
echo done
