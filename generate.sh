#!/bin/bash

# use as: ./generate.sh 02
# where 02 is the notebook id

ipynb_file=$(ls notebooks | grep $1 | head -n1)
stem="${ipynb_file%%.*}"
quarto convert notebooks/$ipynb_file --output qmds/$stem.qmd
quarto render qmds/$stem.qmd -M echo:false --to pdf
mv qmds/$stem.pdf pdfs
