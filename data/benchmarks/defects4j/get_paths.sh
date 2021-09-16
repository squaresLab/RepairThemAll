#!bin/bash

defects4j checkout -p "$1" -v "$2"b -w "$1""$2"
cd "$1""$2"
defects4j export -p dir.src.tests  >> paths.data
echo >> paths.data
defects4j export -p dir.src.classes  >> paths.data
echo >> paths.data
defects4j export -p dir.bin.classes  >> paths.data
echo >> paths.data
defects4j export -p dir.bin.tests  >> paths.data
