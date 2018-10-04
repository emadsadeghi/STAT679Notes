#!/bin/bash


# write a one-liner using sed to fix the problem: 
# change every value in the "Minimum" column to eliminate
#     the commas inside the numbers and
#     the quotes around the numbers.
cat tableofSNPs.csv | gsed -E 's/\"([0-9]+),([0-9]+)\"/\1\2/g' | gsed -E 's/\"([0-9]+),([0-9]+),([0-9]+)\"/\1\2\3/g' > new_tableofSNPs.csv

# To check that your edited csv file is correct, 
# write another one-liner using sed to make sure that every row 
# has exactly 3 commas (because 4 columns).
cat new_tableofSNPs.csv | gsed -E 's/[^,]//g' | grep -xv ",,," | wc -l
