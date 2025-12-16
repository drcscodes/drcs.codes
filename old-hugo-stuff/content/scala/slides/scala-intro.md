% Introduction to Scala
% It's pronounced *skah-lah*, not *scale-uh*.

## Scala History

- First release in 2003
- Designed my Martin Odersky
    - Student of ACM Turing Award winner Niklaus Wirth, creator of Pascal, Modula-2 and Oberon
    - With Philip Wadler, designer of GJ (Generic Java)
    - Chief implementer of Java 5 compiler still used today

Chief design goal: fuse object-oriented and statically-typed functional programming

## Notable Features of Scala

::::{.columns}
::: {.column width="40%" valign="top"}

- Truly object-oriented
    - Everything is an object.  Try `1.equals(1)`
    - No primitive/reference dichotomy
    - No static/instance context dichotomy
- Functional
    - First-class function values
    - Real lambda expressions
    - Immutable data
- Concise, pleasant syntax (~1/3 equivalent Java code)

:::
::: {.column width="40%" valign="top"}

- Many advanced features
    - Rich static typing with type inference
    - By-value parameters
    - Flexible syntax
    - Implicits 
- JVM language with excellent Java interoperability
- "**Sca**lable **La**nguage"
    - REPL, small scripts, million-LOC systems
    - Single machine or clusters
    - Start with simpler features and work up to advanced features
:::
::::

## Running Scala

- Install Java 8+ and Scala for system-wide use using the instructions linked in hw0
- Many ways to run Scala:
    - REPL
    - Command-line scripts
    - Command-line sbt projects
    - IntelliJ (or other IDE) projects
    - IntelliJ (or other IDE) sbt projects
    - IntelliJ (or other IDE) worksheets
    
## The Scala REPL

- Read-Eval-Print-Loop
- Enter an expression, REPL evaluates expression and prints its value
- Great way to become familiar with a language and try out parts of a project

```bash
$ scala
Welcome to Scala 2.12.8 (OpenJDK 64-Bit Server VM, Java 11.0.1).
Type in expressions for evaluation. Or try :help.

scala> 1 + 1
res0: Int = 2

scala> :quit
$
```

## Notable REPL Features

When entering blocks of code, class or function definition, more convenient to use `:paste`

```Scala
scala> :paste
// Entering paste mode (ctrl-D to finish)

def max(x: Int, y: Int): Int =
  if (x > y) x
  else y

// Exiting paste mode, now interpreting.

max: (x: Int, y: Int)Int

scala>
```

Can run a file containing Scala code with `:load`

## Scala Scripts

On Unix, put this at the top of a text file:

```bash
#!/bin/sh
exec scala -savecompiled "$0" "$@"
!#
```

On Windows, put this at the top of a text file ending in `.bat`:

```bash
::#!
@echo off
call scala -savecompiled %0 %*
goto :eof
::!#
```

- `-savecompiled` saves a compiled version of your program with a `.jar` extension so that future execution is faster

- The other two args tell the shell to run the Scala program and pass it the command line args

Run with:

```bash
$ scala myscript.scala
```

## IntelliJ Scala Worksheets

A Scala worksheet is a text file containing Scala code whose name ends in `.sc` (also works in Eclipse).  Run with the play button in upper left corner

![](intellij-scala-worksheet.png){height=70%}

## Command-Line sbt Projects

- Create a directory for your project
- In your project's directory, create a `build.sbt` with minimal contents:

```Scala
ThisBuild / scalaVersion := "2.12.8"
ThisBuild / organization := "edu.gatech.cs2340"

lazy val hello = (project in file("."))
  .settings(
    name := "YOUR NAME HERE"
  )
```

Launch sbt at the command line, which will download some things, create a target directory and a `project` directory with `build.properties` (yes, there's a configuration for the build tool)

```bash
$ sbt
[info] Loading global plugins from /Users/chris/.sbt/1.0/plugins
[info] Loading project definition from /Users/chris/scratch/sample/project
[info] Updating ProjectRef(uri("file:/Users/chris/scratch/sample/project/"), "sample-build")...
[info] Done updating.
[info] Loading settings for project sample from build.sbt ...
[info] Set current project to sample (in build file:/Users/chris/scratch/sample/)
[info] sbt server started at local:///Users/chris/.sbt/1.0/server/2ebfa233db16838ea034/sock
sbt:sample>
```

## sbt Basics

- sbt is interactive.  Use help to list commands
- Common tasks:
    - `compile`
    - `test`
    - `run` -- will find and list all objects with main methods

- Assumes Maven standard source tree structure and its own configuration files:

```bash
├── build.sbt
├── project
│   └── build.properties
└── src
    ├── main
    │   ├── java
    │   └── scala
    └── test
        ├── java
        └── scala
```

## IntelliJ sbt Projects

Can also use IntelliJ's New Project wizard to create a Scala sbt project.
