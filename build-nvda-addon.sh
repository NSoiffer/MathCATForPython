#!/bin/csh
# RUN THIS FILE to build the NVDA addon

rm -rf NVDA-addon/addon/globalPlugins/MathCAT/Rules
# NVDA is currently uses 32 bit python 3.7
# We need to tell PYO3 that
set PYO3_PYTHON_64=c:/Users/neils/AppData/Local/Programs/Python/Python39/python.exe
set PYO3_PYTHON_32=c:/Users/neils/AppData/Local/Programs/Python/Python37-32/python.exe
env PYO3_PYTHON=$PYO3_PYTHON_32 cargo build --target i686-pc-windows-msvc --release
cp target/i686-pc-windows-msvc/release/libmathcat_py.dll NVDA-addon/addon/globalPlugins/MathCAT/libmathcat.pyd
cd NVDA-addon
sed 's/^import wx\.xrc/# import wx.xrc/' --in-place "addon/globalPlugins/MathCAT/MathCATgui.py"
rm MathCAT-*.nvda-addon
scons
