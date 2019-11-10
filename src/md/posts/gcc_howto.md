GCC HOWTOs

![Crane](/images/crane.png){: .img-fluid .img-small }

# GCC How-to Guides
This is a collection of short guides on compiling C programs with GCC, the GNU Compiler Collection. In practice, GNU Make or CMake is used to simplify the build process so users don't have to type out multiple GCC commands. These guides teach which GCC commands to run and in what order. This makes writing and understanding makefiles for C projects much easier later on.

This guide covers:

* [How to compile a simple C program with GCC](#howto-compile-simple-c-program)


## How to compile a simple C program with GCC ## {: #howto-compile-simple-c-program }

Given `hello.c` below:

```c
// hello.c
#include <stdio.h>

int main()
{
	printf("Hello world!\n");
	return 0;
}
```
To compile it from the terminal, run

```bash
$ gcc hello.c
```

A new file named "a.out" is created. To run `a.out`, prepend "./" to "a.out" like so:

```bash
$ ./a.out 
Hello world!
```

The default "a.out" is not a very descriptive name, and we would usually want to give the output file a more descriptive name, such as "hello" in this case . To do that, use `-o` to supply the output file name.

```bash
$ gcc hello.c -o hello
```

Now, we can run `hello` like we run `a.out` by prepending "./" to "hello":

```bash
$ ./hello
Hello world!
```
