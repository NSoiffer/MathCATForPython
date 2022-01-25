#!/bin/csh

cargo build --release

# copy over all the rules and then remove a few "extra" files
cp -r ../../MathCAT/Rules addon/globalPlugins/
rm -rf addon/globalPlugins/Rules/.tmp.driveupload
rm -f addon/globalPlugins/Rules/Nemeth/unicode.yaml-with-all
rm -rf addon/globalPlugins/Rules/zz

cp ../target/i686-pc-windows-msvc/release/libmathcat_py.dll addon/globalPlugins/libmathcat.pyd
rm mathCAT-*.nvda-addon
scons

