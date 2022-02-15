#!/bin/csh

cargo build --target i686-pc-windows-msvc --release

# copy over all the rules and then remove a few "extra" files
cp -r ../../MathCAT/Rules addon/globalPlugins/MathCAT
rm -rf addon/globalPlugins/MathCAT/Rules/.tmp.driveupload
rm -f addon/globalPlugins/MathCAT/Rules/Nemeth/unicode.yaml-with-all
rm -rf addon/globalPlugins/MathCAT/Rules/zz

cp ../target/i686-pc-windows-msvc/release/libmathcat_py.dll addon/globalPlugins/MathCAT/libmathcat.pyd
rm mathCAT-*.nvda-addon
scons

