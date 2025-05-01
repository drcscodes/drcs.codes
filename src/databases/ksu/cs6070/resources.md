---
template: course
title: CS 6070 - Resources
---

## General Project Information

- [General Project Description](project.html)
- [Peer Evaluation](peer-eval.html)

## Final Exam Research Paper Ideas

For your research paper, pick one narrow topic and describe what problem(s) it solves, how it works, its tradeoffs vs alternatives, and examples of production databases implementations.  Here are some example topics (feel free to pick your own):

- Column families
- SSTables, LSM-trees
- Database replication schemes
- A particular kind of NoSQL database, like key-value store, document database

References:

- Google Bigtable paper. [https://static.googleusercontent.com/media/research.google.com/en//archive/bigtable-osdi06.pdf](https://static.googleusercontent.com/media/research.google.com/en//archive/bigtable-osdi06.pdf)
- Architecture of Apache Cassandra. [https://cassandra.apache.org/doc/latest/cassandra/architecture/index.html](https://cassandra.apache.org/doc/latest/cassandra/architecture/index.html)
- Kinds of NoSQL database. [https://aws.amazon.com/nosql/#What_are_the_types_of_NoSQL_databases](https://aws.amazon.com/nosql/#What_are_the_types_of_NoSQL_databases)

## Programming Environments

- [Emacs](https://www.gnu.org/software/emacs/) is the most powerful text editor there will ever be.  Its steep learning curve is repaid a thousand-fold over your lifetime.
     - On macOS: `brew install --cask emacs`, which installs [Emacs for Mac OS X](https://emacsformacosx.com/)
    - [Beginners Guide to Emacs](https://www.masteringemacs.org/article/beginners-guide-to-emacs)
    - [Dr. CS's Emacs config](https://github.com/dr-cs/dotfiles) in the `.emacs.d` directory.
- JetBrains [Educational Licenses](https://www.jetbrains.com/community/education/#students/)
    - [DataGrip](https://www.jetbrains.com/datagrip/) is a database IDE.  Probably the easiest choice for this class.
    - [PyCharm](https://www.jetbrains.com/pycharm/) is a good choice for a pythonista, ML/data engineer or data scientist.  You can install the JetBrains [Database Tools plugin](https://plugins.jetbrains.com/plugin/10925-database-tools-and-sql-for-webstorm) to get the functionality of DataGrip.

## MySQL

- [MySQL Guide](mysql.html)
- [Sakila Sample Database](https://dev.mysql.com/doc/sakila/en/)
- [MySQL WorkBench](http://dev.mysql.com/downloads/workbench/)

## Small Learning Databases

- dorms: [dorms.sql](@root/databases/code/dorms.sql)
- pubs: [pubs-schema.sql](@root/databases/code/pubs-schema.sql), [pubs-data.sql](@root/databases/code/pubs-data.sql)

[Relational Algebra Masterclass](@root/databases/exercises/relational-algebra-masterclass.pdf)
