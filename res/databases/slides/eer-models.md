---
title: EER Models
author: CS 6070 Databases
institute: Kennesaw State University
aspectratio: 1610
fontsize: 10pt
colorlinks: yes
urlcolor: blue
header-includes:
- |
  ```{=latex}
  \input{beamer-common}
  \usepackage{framed}
  \usepackage{xcolor}
  \usepackage{tikz,pgfplots}
  \let\oldquote=\quote
  \let\endoldquote=\endquote
  \colorlet{shadecolor}{cyan!15}
  \renewenvironment{quote}{\begin{shaded*}\begin{oldquote}}{\end{oldquote}\end{shaded*}}
  ```
---

## Enahnced Entity-Relationship Models

Enhanced ER models add inheritance to entity types -- superclasses and subclasses. Subclasses inherit all the attributes of their superclass(es).

Subclasses can:

- be *disjoint* or *overlapping*;
- represent *total* or *partial* specialization.

## University Member

Consider this model of a university member:

```{=latex}
\begin{center}
```
![](er-univ-member.pdf)
```{=latex}
\end{center}
```

- Do faculty members have a major?
- Do students have a rank or salary?

## Employee and Student Subclasses

Here we break the UNIV_MEMBER into two subtypes:

```{=latex}
\begin{center}
```
![](eer-employee-student.pdf){height="50%"}
```{=latex}
\end{center}
```

Notice that the subclasses are overlapping, as denoted by the O in the circle under UNIV_MEMBER. That means that an entity can be both a STUDENT and an EMPLOYEE.

But there's more:

- What's that Emp_type attribute?
- Can an emplyee have a salary and a number of hours?

## Faculty and Staff Subclasses

:::: {.columns}
::: {.column width="50%"}

```{=latex}
\begin{center}
```
![](eer-faculty-staff.pdf){height="80%"}
```{=latex}
\end{center}
```

:::
::: {.column width="50%"}

- The subclasses of EMPLOYEE are disjoint (D in the circle) -- an employee is either SALARIED or HOURLY but not both.
- The double line from employee means *total specialization* -- there are no EMPLOYEE instances, only SALARIED or HOURLY.

The process of going from an entity type that has attributes that don't apply to all entity instances to subclasses that are specialized but inherit the common attributes is called *specialization* (top-down).[^fn1]

[^fn1]: We're not quite done, but we'll return to this example.

:::
::::

## Cars and Trucks

Let's consider another model.

```{=latex}
\begin{center}
```
![](er-car-truck.pdf){height="50%"}
```{=latex}
\end{center}
```

Notice the common attributes. We can factor those into a superclass.

## Vehicles

The common attributes are in the superclass and the specialized attributes are in the subclass.


```{=latex}
\begin{center}
```
![](eer-vehicle.pdf){height="60%"}
```{=latex}
\end{center}
```

The process of factoring the common attributes of two or more entity types and creating superclasses to hold the common attributes is called *generalization* (bottom-up).

## Student Employees

Remember our STUDENT - EMPLOYEE hierarchy:

```{=latex}
\begin{center}
```
![](eer-faculty-staff.pdf){height="65%"}
```{=latex}
\end{center}
```

What about STUDENTS who are also HOURLY employees, like TAs and research assistants?

## Multiple Inheritance

Our previous EER models have been inheritance trees -- each subclass had only one superclass. We can create lattices with multiple inheritance:

```{=latex}
\begin{center}
```
![](eer-faculty-staff-student-employee.pdf){height="70%"}
```{=latex}
\end{center}
```

## Fin

Subclassses provide for more granular and precise modeling of entity types. Use sublcasses when:

- you want to represent commonality and differences between different entity types,
- you want to have different subsets of an enity type participate in different relationships (e.g., faculty participate in TEACHES relationships, HOURLY employees don't).
