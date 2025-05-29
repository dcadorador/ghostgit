#!/bin/bash

# Install tkinter for Python 3
brew install python-tk@3.13

# Create a symbolic link for tkinter
ln -s /opt/homebrew/opt/python-tk@3.13/lib/python3.13/site-packages/_tkinter.cpython-313-darwin.so /opt/homebrew/opt/python@3.13/Frameworks/Python.framework/Versions/3.13/lib/python3.13/lib-dynload/_tkinter.cpython-313-darwin.so
