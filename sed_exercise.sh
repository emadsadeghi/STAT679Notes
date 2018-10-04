#!/bin/bash

# echo TG,"1,650",7,100.00% | gsed -E 's,"([0-9]+),([0-9]+)"(+)/\1\t\2\t\3/'
cat tableofSNPs.csv | gsed -E 's/\"([0-9]+),([0-9]+)\"/\1\2/g' | gsed -E 's/\"([0-9]+),([0-9]+),([0-9]+)\"/\1\2\3/g' > new_tableofSNPs.csv


cat new_tableofSNPs.csv | sed -E 's/[^,]//g' | grep -xv ",,," | wc -l



# 's/^(chr[^:]+):([0-9]+)-([0-9]+)/\1\t\2\t\3/'
# echo "chr12:74-431" | gsed -E 's/^(chr[^:]+):([0-9]+)-([0-9]+)/\1\t\2\t\3/'
