# drcs.codes

Hugo source for DrCS.codes web site


Compile one slide:
```sh
pandoc -f markdown <slide-name>.md -t beamer --listings -H beamer-common.tex -o <slide-name>.pdf
```



Compile all slides in a directory:
```sh
for file in `ls *.md`; do pandoc -f markdown $file -t beamer --listings -H beamer-common.tex -o `(basename $file .md)`.pdf; done
```
