#!/bin/csh
# RUN THIS FILE to build the NVDA addon

cargo build --target i686-pc-windows-msvc --release

cp target/i686-pc-windows-msvc/release/libmathcat_py.dll NVDA-addon/addon/globalPlugins/MathCAT/libmathcat.pyd
cd NVDA-addon
rm mathCAT-*.nvda-addon
scons

