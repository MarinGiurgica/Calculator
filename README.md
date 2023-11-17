# Calculator

## Introduction

This is a simple calculator application built using Python and Tkinter.

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, division, square, sqrt.
- User-friendly graphical interface using Tkinter.

## Create Standalone Executable

pip install pyinstaller

cd Desktop

pyinstaller --onefile --windowed --icon=icon.ico calc_to_exec.py

"""
!!using command prompt!!

=> --onefile because we only want one executable

=> --windowed because we don`t want a console to be opened

=> icon.ico is our desired icon for the final executable, which must be in the same location as the calc_to_exec.py is, and it must be in an ico/exe format

"""
