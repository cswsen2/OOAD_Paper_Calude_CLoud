---
course: SE2012 - Object Oriented Analysis and Design
lecture_num: 1
aliases: [Java Programming, Java programming]
topics:
  - Java
  - JVM JRE JDK
  - JavaDoc
  - Java classes
  - data types
  - arrays
  - control structures
---

# Java Programming (Introduction to Java)

> **Source**: SE2012 OOAD — Lecture 01 "Introduction to Java" | Prof. Jagath Samarabandu & Mr. Jeewaka Perera

## Overview

This lecture is a brief introduction to **[[Java]]**: understanding the JDK, JVM, and JRE; Java documentation (JavaDoc); and an introduction to Java classes, data types, and control structures, with a comparison to C.

> [!NOTE] On Coding (lecture opening quote)
> *"A program is a building of thought. It is costless to build, it is weightless, and it grows easily under our typing hands. If we are not careful, its size and complexity will grow out of control… The art of programming is the skill of controlling complexity."* — Eloquent JavaScript (Marijn Haverbeke)

## Evolution of Java

- **1991**: Initiated by James Gosling, Mike Sheridan, and Patrick Naughton at Sun Microsystems.
- **Project name**: Originally named **"Oak"** after an oak tree outside Gosling's office, later renamed **"Java"**.
- **1995**: Officially launched as Java 1.0.
- **1996**: Java Development Kit (JDK) 1.0 released.
- **1999**: Java 2 (J2SE) introduced.
- **2004**: Java 5.0 (J2SE 5.0) introduced major updates like generics and metadata.
- **2006**: Java becomes open source under the GNU General Public License.
- **2010**: Oracle acquires Sun Microsystems.

## Java's Philosophy and Design Goals

- **Philosophy**: *"Write Once, Run Anywhere"* (WORA).
- **Design Goals**:
  - **Simplicity** — easy to learn and use.
  - **Object-Oriented** — modular approach to software development.
  - **Platform Independence** — runs on any platform with a [[JVM]].
  - **Security** — built-in security features.
  - **High Performance** — efficient execution.
  - **Robustness** — strong memory management and error handling.

## Java Platform Components

The Java platform has three core components: the **[[JVM]]**, the **[[JRE]]**, and the **[[JDK]]**.

### Java Virtual Machine (JVM)

Executes Java [[bytecode]]. Contains:

- **Bytecode Interpreter** — executes Java bytecode.
- **Just-In-Time (JIT) Compiler** — converts bytecode to native machine code at runtime for improved performance.
- **Garbage Collector** — manages memory by automatically reclaiming unused objects.

> Included in: **JRE and JDK**.

### Java Runtime Environment (JRE)

- **Contains**: the JVM (to run Java applications), **Core Libraries** (essential libraries and classes needed to run applications), and **Runtime Tools** (for monitoring and debugging).
- **Download**: from the Oracle JRE download page — choose the version for your OS, download and install.

### Java Development Kit (JDK)

- **Compiler (javac)** — converts Java source files (`.java`) into [[bytecode]] files (`.class`); essential for developers to compile their code.
- **Java Standard Libraries** — a vast collection of pre-written classes and methods (e.g. `java.lang`, `java.util`, `java.io`, `java.net`).
- **Development Tools** — `javadoc` (generates HTML documentation), `jdb` (command-line debugger), and other tools like `javap` (class-file disassembler) and `jar` (packaging tool).

> [!IMPORTANT] JDK vs. JRE
> - **JDK**: for *development* — includes everything in the JRE **plus** development tools.
> - **JRE**: for *running* Java applications — includes only the JVM and core libraries.

## Java Platforms

| Platform | Purpose |
| -------- | ------- |
| **Java SE** | Standard Edition — core functionality of the Java language (basic types, objects, networking, security, database access, GUI, XML parsing); includes the JVM, development tools, and common class libraries. |
| **Java EE** | Enterprise Edition — built on top of Java SE; API and runtime for large-scale, multi-tiered, scalable, reliable, secure network applications. |
| **Java ME** | Micro Edition — API and small-footprint JVM for small devices like mobile phones; a subset of Java SE. |
| **JavaFX** | For rich internet applications using a lightweight UI API; hardware-accelerated graphics and modern look-and-feel. |

## Setting Up & Running Java

### Setting up the environment (Windows)

- **Temporarily**: `set PATH=%PATH%;C:\Program Files\Java\jdk-11.0.2\bin`
- **Permanently**: This PC → Properties → Advanced system settings → Environment Variables → edit the `Path` system variable → add the JDK `bin` directory.

### Verifying the installation

```bash
java -version      # check the Java version
javac -version     # check the Java compiler version
```

### How compilation and execution work

The developer writes a `.java` file (e.g. `HelloWorld.java`) → the **Java Compiler (javac)** compiles it into [[bytecode]] (`HelloWorld.class`) → the **[[JVM]]** executes the bytecode on the operating system.

```bash
javac FileName.java   # compile the program
java FileName         # run the compiled program
```

## JavaDoc

The `javadoc` tool generates HTML documentation from special comment tags:

| Tag | Describes |
| --- | --------- |
| `@param` | a method parameter |
| `@return` | the return value of a method |
| `@throws` | an exception thrown by a method |
| `@see` | references related information |
| `@since` | the version when the feature was added |
| `@deprecated` | marks a method as deprecated |

## Keywords in Java

> [!NOTE] `true`, `false`, and `null` are **not** keywords — they are *literals* and cannot be used as identifiers.

Java reserved keywords (50): `abstract, assert, boolean, break, byte, case, catch, char, class, const*, continue, default, do, double, else, enum, extends, final, finally, float, for, goto*, if, implements, import, instanceof, int, interface, long, native, new, package, private, protected, public, return, short, static, strictfp, super, switch, synchronized, this, throw, throws, transient, try, void, volatile, while`
(`*` `const`/`goto` are reserved but not used; `assert` added in 1.4, `enum` added in 5.0, `strictfp` added in 1.2.)

## Packages

- **Definition**: A **[[package]]** is a *namespace* that organizes classes and interfaces; it helps avoid class name conflicts and control access.
- **Naming convention**: package names should be all lowercase, e.g. `java.io`, `java.util`.
- **Importing**: use the `import` keyword — `import <<package>>.<<ClassName>>;` — to reuse other classes without reimplementing them.

## Java Classes

A **[[class]]** is a *blueprint for creating objects* (more on [[object|objects]] later). It **defines** attributes (fields/variables) and methods (functions), and can contain **constructors, methods, fields, and nested classes**.

```java
package lecture;

public class Car {
    // <AccessModifier> class ClassName { ... }
    // attributes (fields)
    // methods
    // constructors
    // nested classes
}
```

> [!NOTE] Naming Conventions
> Class names are generally **nouns**, in mixed case with the first letter of each internal word capitalized (**CamelCase**), e.g. `class MyClass { ... }`.

### Main Method

The **entry point** of any Java application — the method the JVM calls to start execution:

```java
public static void main(String[] args) {
    // program logic
}
```

- **public** — accessible from anywhere.
- **static** — belongs to the class, not instances of the class.
- **void** — does not return any value.
- **main** — the name of the method called by the JVM.
- **String[] args** — an array of strings storing command-line arguments.

### Naming .java Files

- The file name must **exactly match** the public class name and have a `.java` extension (e.g. `public class Car` → `Car.java`).
- There can only be **one public class per `.java` file**.
- Any additional classes in the same file should **not** be public.

## Access Modifiers

| Modifier | Accessibility |
| -------- | ------------- |
| **public** | from any other class |
| **protected** | within the same package and subclasses |
| **default** (package-private) | only within the same package |
| **private** | only within the same class |

## Data Types

| Category | Description |
| -------- | ----------- |
| **Primitive** | Basic types provided by the language; simple values. |
| **Non-Primitive** | Complex types created using classes, arrays, or interfaces. |

### Primitive Data Types

| Data Type | Size | Range | Example |
| --------- | ---- | ----- | ------- |
| `byte` | 8-bit | −128 to 127 | `byte b = 10;` |
| `short` | 16-bit | −32,768 to 32,767 | `short s = 1000;` |
| `int` | 32-bit | −2³¹ to 2³¹−1 | `int i = 12345;` |
| `long` | 64-bit | −2⁶³ to 2⁶³−1 | `long l = 123456L;` |
| `float` | 32-bit | ≈ ±3.40282347E+38 (6–7 digits) | `float f = 12.34f;` |
| `double` | 64-bit | ≈ ±1.79769313486231570E+308 (15 digits) | `double d = 123.45d;` |
| `char` | 16-bit | `' '` (0) to `'￿'` (65,535) | `char c = 'A';` |
| `boolean` | 1-bit | `true` or `false` | `boolean flag = true;` |

## Control Structures (Comparison with C)

Java's control structures are similar to C:

- **Selection statements**: `if`, `else if`, `else`; `switch` (Java's `switch` additionally supports **String** types).
- **Loops**: `for`, `while`, `do-while`.

## Handling I/O in Java

### Output (printing)

```java
public class PrintExample {
    public static void main(String[] args) {
        String name = "John";
        int age = 25;
        double salary = 30000.75;

        // Basic print
        System.out.println("Hello, World!");

        // Formatted print
        System.out.printf("Name: %s Age: %d Salary: %.2f\n", name, age, salary);
    }
}
```

| Feature | Java | C |
| ------- | ---- | - |
| Basic Print | `System.out.println("Hello, World!");` | `printf("Hello, World!\n");` |
| Format Print | `System.out.printf("Name: %s Age: %d\n", name, age);` | `printf("Name: %s Age: %d\n", name, age);` |
| Placeholders | `%s` strings, `%d` integers, `%f` floats | `%s` strings, `%d` integers, `%f` floats |

### Input (Scanner)

```java
import java.util.Scanner;

public class InputExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Reading an integer
        System.out.print("Enter a number: ");
        int number = scanner.nextInt();

        // Clearing buffer
        scanner.nextLine();

        // Reading a string
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();

        // Displaying input
        System.out.printf("Name: %s, Number: %d\n", name, number);
    }
}
```

## Arrays

### One-Dimensional Arrays

A one-dimensional array is a *list of variables of the same type, accessed by a common name*. Arrays are **zero-indexed**, use `arrayName.length` to get the size, and elements are accessed with `arrayName[index]`.

```java
public class OneDArrayExample {
    public static void main(String[] args) {
        // Declaration and initialization
        int[] numbers = new int[5];
        numbers[0] = 10;
        numbers[1] = 20;
        numbers[2] = 30;
        numbers[3] = 40;
        numbers[4] = 50;

        // Declaration with initialization
        int[] moreNumbers = {1, 2, 3, 4, 5};

        // Accessing array elements
        for (int i = 0; i < numbers.length; i++) {
            System.out.println("Element at index " + i + ": " + numbers[i]);
        }
    }
}
```

### Two-Dimensional Arrays

Multi-dimensional arrays are *arrays of arrays*; the most common form is the 2D array, thought of as a table with rows and columns. Declaration: `dataType[][] arrayName = new dataType[rows][columns];`

```java
public class MultiDArrayExample {
    public static void main(String[] args) {
        // Declaration and initialization
        int[][] matrix = new int[3][3];
        matrix[0][0] = 1; matrix[0][1] = 2; matrix[0][2] = 3;
        matrix[1][0] = 4; matrix[1][1] = 5; matrix[1][2] = 6;
        matrix[2][0] = 7; matrix[2][1] = 8; matrix[2][2] = 9;

        // Declaration with initialization
        int[][] anotherMatrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        // Accessing array elements
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }
}
```

## In-Class Activities

> [!QUESTION] Activity 1 — Compile & execute
> Write down the steps and commands to compile and execute the following (assume the file is not yet saved):
> ```java
> package lecture01;
>
> public class HelloWorld {
>     public static void main(String[] args) {
>         System.out.println("Hello, World!");
>     }
> }
> ```

> [!QUESTION] Activity 2 — Grading program
> Write a Java program that determines if a student passes or fails based on their score: ≥90 → "Grade A", 80–89 → "Grade B", 70–79 → "Grade C", 60–69 → "Grade D", below 60 → "Fail". Indicate the `.java` filenames and the commands for compiling and running.

> [!QUESTION] Activity 3 — Student marks (2D arrays)
> 5 students each take 3 subjects (Mathematics, Chemistry, Physics). Write a program to let the teacher enter and view the marks of all 5 students. Indicate the `.java` filenames and the commands for compiling and running.

## 📅 Tasks

- [ ] Set up the Java development environment and verify with `java -version` / `javac -version` [due:: 2026-06-26] #p1
- [ ] Complete Activity 1 (HelloWorld compile & execute) [due:: 2026-06-27] #p1
- [ ] Complete Activity 2 (grading program) [due:: 2026-06-28] #p2
- [ ] Complete Activity 3 (student marks with 2D arrays) [due:: 2026-06-30] #p2

## 🧠 Flashcards

What is Java's core philosophy slogan? :: Write Once, Run Anywhere (WORA).

What are the three Java platform components? :: The JVM (Java Virtual Machine), JRE (Java Runtime Environment), and JDK (Java Development Kit).

What are the three components contained in the [[JVM]]? :: The bytecode interpreter, the Just-In-Time (JIT) compiler, and the garbage collector.

What does the JIT compiler do? :: Converts bytecode to native machine code at runtime for improved performance.

What is the difference between the JDK and the JRE? :: The JDK is for development and includes everything in the JRE plus development tools; the JRE only runs Java applications (JVM + core libraries).

What does the javac compiler produce? :: Bytecode (.class) files from Java source (.java) files.

Name the four Java platforms. :: Java SE (Standard), Java EE (Enterprise), Java ME (Micro), and JavaFX.

What does the `@param` JavaDoc tag describe? :: A method parameter.

Are true, false, and null Java keywords? :: No — they are literals and cannot be used as identifiers.

What is a [[package]] in Java? :: A namespace that organizes classes and interfaces, helping avoid name conflicts and control access; named in all lowercase.

What is a [[class]] in Java? :: A blueprint for creating objects that defines attributes (fields) and methods, and can contain constructors, methods, fields, and nested classes.

What is the signature of the Java main method? :: public static void main(String[] args).

In the main method, what does `static` mean? :: The method belongs to the class, not to instances of the class.

What is the rule for naming a .java file? :: The file name must exactly match the public class name; only one public class per file, and additional classes must not be public.

What are the four Java access modifiers, from most to least accessible? :: public (any class), protected (same package + subclasses), default/package-private (same package), private (same class).

What are the two categories of Java data types? :: Primitive (basic language types) and non-primitive (complex types from classes, arrays, or interfaces).

What is the size and range of a Java `int`? :: 32-bit, range −2³¹ to 2³¹−1.

What is the range of a Java `byte`? :: −128 to 127 (8-bit).

What extra type does Java's `switch` support compared to C? :: String types.

Which class is used for console input in Java? :: java.util.Scanner (e.g. new Scanner(System.in)).

How do you get the size of a Java array? :: Using the `length` property: arrayName.length (arrays are zero-indexed).

#flashcards
