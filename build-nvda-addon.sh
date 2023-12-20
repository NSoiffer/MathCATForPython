#!/bin/csh
# RUN THIS FILE to build the NVDA addon

rm -rf addon/globalPlugins/MathCAT/Rules
# NVDA currently uses 32 bit python 3.7
# We need to tell PYO3 that
set PYO3_PYTHON_64=c:/Users/neils/AppData/Local/Programs/Python/Python39
set PYO3_PYTHON_32=c:/Users/neils/AppData/Local/Programs/Python/Python37-32
env PYO3_PYTHON=$PYO3_PYTHON_32/python.exe cargo build --target i686-pc-windows-msvc --release
cp target/i686-pc-windows-msvc/release/libmathcat_py.dll addon/globalPlugins/MathCAT/libmathcat.pyd
sed 's/^import wx\.xrc/# import wx.xrc/' --in-place "addon/globalPlugins/MathCAT/MathCATgui.py"
rm MathCAT-*.nvda-addon

# use "pip install SCons" to add scons to the python env
$PYO3_PYTHON_32/Scripts/scons
