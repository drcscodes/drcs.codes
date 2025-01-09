---
layout: homework
title: Homework 0
---

# Homework 0

## Introduction

This assignment gets you started with the basic tools you will need to complete all of your homework projects.  This project will ensure that you have correctly installed Scala, SBT and IntelliJ. 


## Problem Description

You are a student who needs to install all the tools necessary to get started in CS2340.

## Solution Description

In this assignment you will set up your computer to 

- create and run Scala scripts from the command line,
- create and manage Scala projects from the command-line with SBT, and
- create and manage Scala projects with IntelliJ. 

### Scala Scripts

1. Install Scala for system-wide use on your computer by downloading the appropriate distribution from the bottom of https://www.scala-lang.org/download/

2. Download and install a [programmer's text editor](../../text-editors.html) (you can also use [IntelliJ](../../intellij.html) as a general text editor, but it can be awkward for quick file editing).  In this course we will prmiarily use IntelliJ, but it's important to be comfortable with general-purpose text editors too.

3. Create a directory for your CS2340 coursework somewhere on your hard disk -- we suggest `cs2340`.
    - You can do this on the command line by navigating to the directory you want to contain is the cs2340 folder (using the `cd` command).
        - Create the folder with the command `mkdir cs2340`.
        - Enter the new folder with the command `cd cs2340`.
        - Note: avoid putting spaces in file and directory names, since doing so complicates the use of some command line tools.

4. Create a subdirectory of your `cs2340` directory named `hw0`.

5. On the command line, make sure you are in the `hw0` folder. Enter these commands (remember that '$' is the shell prompt (something like 'C:\cs2340\hw0>' on Windows) -- don't type the shell prompt character(s)):

    ```sh    
    $ scalac -version > hw0-output.txt
    $ scala -version 2>> hw0-output.txt
    ```

    > Please note what is happening here:
    > 
    > `>` redirects the standard output of a program.  `2>` (or `2>>`) redirects `stderr`, which is used for diagnostics (such as version strings).  The first line creates the `hw0-output.txt` file, and the second line (with the extra `>`) adds more text to the file. Here is a [nice discussion](http://www.jstorimer.com/blogs/workingwithcode/7766119-when-to-use-stderr-instead-of-stdout) of the file descriptors `stdin`, `stdout` and `stderr`.
    > 
    > What this means is that `>` (or `2>`) will overwrite the file, so if you go back to repeat the first step, you'll need to repeat all the other steps as well.

6. Open your text editor and create a file in your newly created `hw0` directory named `NimblyBimbly.sh` (on Unix/Linux) or `NimblyBimbly.bat` (on Windows) and enter the following Scala script:

    Unix/Linux: `NimblyBimbly.sh`
    ```Scala
    #!/bin/sh
    exec scala -savecompiled "$0" "$@"
    !#
    
    for (i <- 1 to 9)
      print("\u004D\u0065\u006F\u0077 ")
    println("...")
    println("\u004D\u0065\u006F\u0077 ")
    ```
    
    Windows: `NimblyBimbly.bat`
    ```Scala
    ::#!
    @echo off
    call scala -savecompiled %0 %*
    goto :eof
    ::!#
    
    for (i <- 1 to 9)
      print("\u004D\u0065\u006F\u0077 ")
    println("...")
    println("\u004D\u0065\u006F\u0077 ")
    ```

7. If you're on Unix/Linux, make the script executable by entering `chmod +x NimblyBimbly.sh` on the command line.

8. On the command line, go to the directory containing your newly created script and run it by entering `./NimblyBimbly.sh` on Unix/Linux or `NimblyBimbly.bat` on Windows.  You should see some output on the console.
9. Run the script again and add its output to `hw0-output.txt` by entering

    Unix/Linux:
    ```sh
    $ ./NimblyBimbly.sh >> hw0-output.txt
    ```

    Windows:
    ```sh
    C:\cs2340\hw0> NimblyBimbly.bat >> hw0-output.txt
    ```
    
    Don't forget the the double arrows in `>>`!

9. Examine your `hw0-output.txt` file to ensure that it contains the `scalac` version string, the `scala` version string, and the output of running your `NimblyBimbly` script.


### Command-line SBT Projects

1. Install SBT for your operating system using the instructions linked on the [Getting Started with Scala and SBT on the Command Line page on docs.scala-lang.org](https://docs.scala-lang.org/getting-started-sbt-track/getting-started-with-scala-and-sbt-on-the-command-line.html).

2. In your `hw0` directory, run the following command `sbt new scala/hello-world.g8`. This pulls the ‘hello-world’ template from GitHub, prompts for project template values, and creates a starter SBT project.

3. When prompted, name the application `hello-world`. This will create a project called “hello-world” in a subdirectory named `hello-world`.

4. `cd` to the `hello-world` directory and examine the files and directories created by the `sbt new` command and do the things listed on the [Getting Started with Scala and SBT on the Command Line page on docs.scala-lang.org](https://docs.scala-lang.org/getting-started-sbt-track/getting-started-with-scala-and-sbt-on-the-command-line.html) to get familiar with SBT.

5. Copy the first non-comment, non-blank line from `hello-world/build.sbt` and paste it to the end of your `hw0-output.txt` file.

### IntelliJ SBT Projects

Note: be sure to install the Scala plugin in IntelliJ.

1. Do the steps on the [Building a Scala Project with IntelliJ and SBT page on docs.scala-lang.org](https://docs.scala-lang.org/getting-started-intellij-track/building-a-scala-project-with-intellij-and-sbt.html) with the following modifications:

    - You'll be starting with Step 2 since you already created an SBT project outside of IntelliJ (which is how we'll always do it).
    - In the latest IntelliJ version the menu option to import an existing project is File -> New -> Project from existing sources ...
    - In the File Open dialog find the `build.sbt` file created in the previous section.  Your File Open dialog may look something like this:
        - ![](import-hello-world-build.sbt.png)
    - In the "Import Project from sbt" dialog under "Use sbt shell", check both "for imports" and "for builds".  Your "Import Project from sbt" dialog may look something like this:
        - ![](import-project-from-sbt-dialog.png)

2. You may have noticed that the `scala/hello-world.g8` template creates a project that uses Scala 2.12.7 and SBT 1.2.4.  During the course of a Scala project you may update your Scala version or SBT version.  Here's how to update build settings (like the Scala version) and keep IntelliJ in sync (see also [JetBrain's help page for sbt projects](https://www.jetbrains.com/help/idea/sbt-support.html)).  Do these steps:
   
    - In the sbt shell execute the command `scalaVersion`, which tells you the version of Scala sbt is using to compile and run your project.  The version should be 2.12.7.
    - Open `build.sbt` and update the Scala version (the value of the setting `scalaVersion`) to the most recent stable release (2.12.8 as of January 2019). 
    - Open the `sbt` tool window on the right and click the refresh button in the top left corner.  The SBT shell will open and show the progress of the update.
    
    > Note: You may also want to update the SBT version of an existing project, but to do that you're better off simply updating the SBT version in `project/build.properties`, deleting the `.idea` subdirectory (which contains the IntelliJ project), and re-importing the project from `build.sbt` into IntelliJ as in Step 1 above.

3. After performing the substeps of Step 2 above, in the sbt shell execute the command `scalaVersion` again.  Copy the command's output (which shows the updated value for `scalaVersion`) and paste it to the end of your `hw0-output.txt` file.

### Double-Check your `hw0-output.txt` File

At this point your `hw0-output.txt file should contain

- your `scalac` version string,
- your `scala` version string,
- the output of your `NimblyBimbly` script,
- the first non-comment, non-blank line from `hello-world/build.sbt`, and
- the line from the the output of the sbt shell command `scalaVersion` showing an updated `scalaVersion` for the `hello-world` project.  This line should start with `[info]` and show the most recent stable Scala version.

If your `hw0-output.txt` file is missing any of those elements you should redo all the steps that add content to `hw0-output.txt` in each of the previous sections.


## Turn-in Procedure

Submit your `hw0-output.txt` file on Canvas as an attachment.  When you're ready, double-check that you have submitted and not just saved a draft.

## Verify the Success of Your Submission to Canvas

Practice safe submission! Verify that your HW files were truly submitted correctly, the upload was successful, and that your program runs with no syntax or runtime errors. It is solely your responsibility to turn in your homework and practice this safe submission safeguard.
**NOTE**: Unlike TSquare, Canvas will not send an email indicating that your assignment has been submitted successfully. Follow the steps outlined below to ensure you have submitted correctly.
- After submitting the files to Canvas, return to the Assignment menu option and this homework. It should show the submitted files.
- Download copies of your submitted files from the Canvas Assignment page placing them in a new folder.
- Re-run and test the files you downloaded from Canvas to make sure it's what you expect.
- This procedure helps guard against a few things.

    - It helps ensure that you turn in the correct files.
    - It helps you realize if you omit a file or files. Missing files will not be given any credit, and non-compiling/non-running homework solutions will receive few to zero points. Also recall that late homework will not be accepted regardless of excuse. Treat the due date with respect.  Do not wait until the last minute!
(If you do discover that you omitted a file, submit all of your files again, not just the missing one.)
    - Helps find syntax errors or runtime errors that you may have added after you last tested your code.
