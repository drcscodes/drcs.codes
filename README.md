# drcs.codes

Hugo source for DrCS.codes web site

```sh
sudo apt-get install python3-dev graphviz libgraphviz-dev pkg-config
sudo apt install pandocfilters pygraphviz
```

```sh
pip3 install pandoc-imagine
```

Compile one slide:
```sh
pandoc --filter pandoc-imagine -f markdown -t beamer --listings -H beamer-common.tex <slide-name>.md -o <slide-name>.pdf
```

Compile all slides in a directory:
```sh
for file in `ls *.md`; do pandoc --filter pandoc-imagine -f markdown -t beamer --listings -H beamer-common.tex $file -o `(basename $file .md)`.pdf; done
```
