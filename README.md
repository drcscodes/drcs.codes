# drcs.codes

Hugo source for DrCS.codes web site


```sh
sudo apt-get install python3-dev graphviz libgraphviz-dev pkg-config
sudo apt install pandocfilters pygraphviz
```

Compile one slide:
```sh
pandoc <slide-name>.md -f markdown -t beamer --listings -H beamer-common.tex -F graphviz.py -o <slide-name>.pdf
```



Compile all slides in a directory:
```sh
for file in `ls *.md`; do pandoc -f markdown $file -t beamer --listings -H beamer-common.tex -o `(basename $file .md)`.pdf; done
```
