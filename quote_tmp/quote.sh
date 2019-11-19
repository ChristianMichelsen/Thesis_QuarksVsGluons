#!/bin/bash

# new fortunes every hour
if [ ! -f ./tmp/fortune-$1.tex ] || test "`find ./tmp/fortune-$1.tex -mmin +60`"
then
    fortune | sed -e 's/-- .*//g' | sed '/^\s*$/d' > ./tmp/fortune-$1.tex
fi