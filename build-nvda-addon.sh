#!/bin/csh
# RUN THIS FILE to build the NVDA addon

rm -rf NVDA-addon/addon/globalPlugins/MathCAT/Rules
cargo build --target i686-pc-windows-msvc --release

cp target/i686-pc-windows-msvc/release/libmathcat_py.dll NVDA-addon/addon/globalPlugins/MathCAT/libmathcat.pyd
cd NVDA-addon
sed 's/^import wx\.xrc/# import wx.xrc/' --in-place "addon/globalPlugins/MathCAT/MathCATgui.py"
rm MathCAT-*.nvda-addon
scons
