#!/bin/sh
exec scala -savecompiled "$0" "$@"
!#

qs(args.map(_.toInt)).foreach(x => print(s"$x "))
println()

def qs(xs: Array[Int]): Array[Int] =
  if (xs.length <= 1) xs
  else qs(xs.filter(_ < xs(xs.length / 2))) ++ xs.filter(_ == xs(xs.length / 2)) ++ qs(xs.filter(_ > xs(xs.length / 2)))
