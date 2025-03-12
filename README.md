# TimingTests
This repository contains various timing tests I've run comparing C++, Java, and Python.

Each test will have a main directory with the name of the test,
and subdirectories for each language.
Each test will have at least these subdirectories:
- cpp_ref
- java_ref
- python_ref
- tests

These contain unoptimized reference implementations for each language that are known to work,
and some test data.

Every implementation should be fully self-contained,
even if that requires having multiple copies of some
of the same code.
If this becomes too bothersome,
I may relax this later.

The .gitignore file is set to ignore any files ending
in `.output.txt`.
The recommendation for testing
is to use a command line like this:

```
test ..\test\test1.txt test1.output.txt
```
