% Databases
% Data Mastery

## Databases

- Relational
  - MySQL, SQLite, Postgres, Oracle

- Key-value
  - Berkeley-DB, BigTable

- Document
  - XML databases, JSON-oriented databases (like MongoDB)
  
Relational databases bar far the most important

** Relational Databases

- A relational database is a collection of data stored in one or more tables

- A relational database management system (RDBMS) is software that stores and updates a relational database and provides a query and manipulation interface to the data



** Relational Data Model

A *relation schema* $R(A_a, ..., A_n)$ is a relation name $R$ and a list of attributes $A_1, ..., A_n$.

Each attribute $A_i$ is the name of a role played by some domain $D$.

- Example:  $AUTHOR(author\_id, first\_name, last\_name)$

    - $dom(A_1)$ (or $dom(author\_id)$) is integer

A *database schema* is a collection of relation schemas.

- Example: $PUBS$ database has relation schemas $BOOK$, $AUTHOR$, and $PUB$ (for publication, not public house)


## Relations and Databases

A *relation*, or *relation state*, $r(R)$ is a **set** of tuples that conform to a *relation schema* $R$.

- Example: $r(AUTHOR)$ =


    +-----------+------------+-----------+
    | author_id | first_name | last_name |
    +-----------+------------+-----------+
    |         1 | John       | McCarthy  |
    |         4 | Claude     | Shannon   |
    |         5 | Alan       | Turing    |
    |         6 | Alonzo     | Church    |
    +-----------+------------+-----------+


A *database* is a set of relations.

** Tuples

A *tuple* is an **ordered list** of values.

- Example: $t_1 =$ <1, 'John', 'McCarthy'>

Each value in the tuple is that tuple's value for the corresponding attribute of the relation schema.

Example: (these are equivalent notations):

- $t_1[first\_name] =$ 'John' (bracket notation)
- $t_1.first\_name =$ 'John' (object notation)
- $t_1[2] =$ `'John'` (positional notation)

The *degree* or *arity* of a relation schema is the number of attributes it has.

- Example: $AUTHOR$ has degree 3.

** An Example Relation

#+BEGIN_CENTER
[[file:student-relation.png]]
#+END_CENTER

** Attributes and Domains

Each attribute has a name and a *domain*

- The name describes the role played by the attribute

    - Example: the $first\_name$ attribute of the $AUTHOR$ schema plays the role of the first name of an author represented by a tuple in a $r(AUTHOR)$ relation.

- The domain is a set of atomic values that a tuple may have for that attribute.

